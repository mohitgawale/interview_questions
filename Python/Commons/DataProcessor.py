import logging
from pyspark.sql import SparkSession

class DataProcessor:
    @staticmethod
    def create_spark_session(app_name="GenericApp"):
        """
        Initialize a Spark session with basic configuration.

        Args:
            app_name (str): Name of the Spark application. Defaults to 'GenericApp'.

        Returns:
            SparkSession: Configured Spark session.
        """
        logger = logging.getLogger(__name__)
        full_app_name = f"data_job_{app_name}"
        logger.info(f"Starting Spark session: {full_app_name}")
        spark = SparkSession.builder \
            .appName(full_app_name) \
            .config("spark.jars.packages", "com.example.jdbc:driver:1.0.0") \
            .getOrCreate()
        return spark

    @staticmethod
    def process_data_pipeline(
        spark,
        source_configs,
        db_credentials,
        db_config,
        sql_query,
        target_table,
        target_schema,
        batch_size=1000,
        repartition_count=5,
        repartition_cols=None,
        dedup_query=None,
        partition_col=None
    ):
        """
        Process data through a pipeline: read, transform, write, and deduplicate.

        Args:
            spark (SparkSession): Spark session.
            source_configs (list): List of source table configurations.
            db_credentials (dict): Database credentials (username, password).
            db_config (dict): Database connection details (host, port).
            sql_query (str): SQL query for data transformation.
            target_table (str): Name of the target table.
            target_schema (str): Name of the target schema.
            batch_size (int): Batch size for writing data.
            repartition_count (int): Number of partitions for repartitioning.
            repartition_cols (list): Columns to repartition by.
            dedup_query (str): Query to identify duplicates.
            partition_col (str): Column for partitioning during deduplication.
        """
        logger = logging.getLogger(__name__)
        try:
            logger.info("Reading source data...")
            DataProcessor._read_source_data(
                spark,
                source_configs,
                db_credentials,
                db_config
            )

            logger.info(f"Executing SQL transformation: {sql_query}")
            result_df = spark.sql(sql_query)

            logger.info("Repartitioning data...")
            repartition_cols = repartition_cols or []
            if repartition_cols:
                result_df = result_df.repartition(repartition_count, *repartition_cols)
            else:
                result_df = result_df.repartition(repartition_count)

            logger.info("Writing data to target...")
            DataProcessor._write_to_database(
                result_df,
                db_config,
                db_credentials,
                target_table,
                target_schema,
                batch_size
            )

            logger.info("Removing duplicates...")
            DataProcessor._deduplicate_table(
                spark,
                db_config,
                db_credentials,
                target_schema,
                target_table,
                dedup_query,
                partition_col
            )

            logger.info("Data pipeline completed.")
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            raise

    @staticmethod
    def _read_source_data(spark, source_configs, db_credentials, db_config):
        """
        Read data from source tables and create temporary views.

        Args:
            spark (SparkSession): Spark session.
            source_configs (list): Source table configurations.
            db_credentials (dict): Database credentials.
            db_config (dict): Database connection details.
        """
        logger = logging.getLogger(__name__)
        for config in source_configs:
            query = config["query"]
            table_name = config["table_name"]
            logger.info(f"Reading data for table: {table_name}")

            df = spark.read \
                .format("jdbc") \
                .option("url", f"jdbc:database://{db_config['host']}:{db_config['port']}/db") \
                .option("query", query) \
                .option("user", db_credentials["username"]) \
                .option("password", db_credentials["password"]) \
                .option("driver", "com.example.jdbc.Driver") \
                .load()

            view_name = f"view_{table_name}"
            df.createOrReplaceTempView(view_name)
            logger.info(f"Created view: {view_name}")

    @staticmethod
    def _write_to_database(df, db_config, db_credentials, table_name, schema_name, batch_size):
        """
        Write data to the target database.

        Args:
            df (DataFrame): Spark DataFrame to write.
            db_config (dict): Database connection details.
            db_credentials (dict): Database credentials.
            table_name (str): Target table name.
            schema_name (str): Target schema name.
            batch_size (int): Batch size for writing.
        """
        logger = logging.getLogger(__name__)
        full_table = f"{schema_name}.{table_name}"
        logger.info(f"Writing to {full_table}")

        df.write \
            .format("jdbc") \
            .option("url", f"jdbc:database://{db_config['host']}:{db_config['port']}/{schema_name}") \
            .option("dbtable", table_name) \
            .option("user", db_credentials["username"]) \
            .option("password", db_credentials["password"]) \
            .option("driver", "com.example.jdbc.Driver") \
            .option("batchsize", batch_size) \
            .mode("append") \
            .save()

        logger.info(f"Write completed for {full_table}")

    @staticmethod
    def _deduplicate_table(spark, db_config, db_credentials, schema_name, table_name, dedup_query, partition_col):
        """
        Remove duplicates from the target table.

        Args:
            spark (SparkSession): Spark session.
            db_config (dict): Database connection details.
            db_credentials (dict): Database credentials.
            schema_name (str): Schema name.
            table_name (str): Table name.
            dedup_query (str): Query to identify duplicates.
            partition_col (str): Column for partitioning.
        """
        logger = logging.getLogger(__name__)
        full_table = f"{schema_name}.{table_name}"

        if not dedup_query or not partition_col:
            logger.info(f"No deduplication required for {full_table}")
            return

        logger.info(f"Deduplicating {full_table} using query: {dedup_query}")
        # Simulate deduplication logic
        spark.read \
            .format("jdbc") \
            .option("url", f"jdbc:database://{db_config['host']}:{db_config['port']}/{schema_name}") \
            .option("query", dedup_query) \
            .option("user", db_credentials["username"]) \
            .option("password", db_credentials["password"]) \
            .option("driver", "com.example.jdbc.Driver") \
            .load() \
            .write \
            .format("jdbc") \
            .option("url", f"jdbc:database://{db_config['host']}:{db_config['port']}/{schema_name}") \
            .option("dbtable", table_name) \
            .option("user", db_credentials["username"]) \
            .option("password", db_credentials["password"]) \
            .option("driver", "com.example.jdbc.Driver") \
            .mode("overwrite") \
            .save()

        logger.info(f"Deduplication completed for {full_table}")
