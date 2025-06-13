import logging
import argparse
import sys
from pyspark.sql import SparkSession
from commons.DataProcessor import DataProcessor

class PipelineRunner:
    def __init__(self, environment, username, password, app_name="DataProcessor"):
        """
        Initialize the pipeline runner with configuration details.

        Args:
            environment (str): Execution environment (e.g., dev, prod).
            username (str): Database username.
            password (str): Database password.
            app_name (str, optional): Spark application name. Defaults to 'DataProcessor'.
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

        self.environment = environment
        self.username = username
        self.password = password
        self.app_name = app_name

        self.logger.info("Loading database configuration...")
        self.db_config = {"host": "localhost", "port": 9000}  # Dummy config
        self.spark = DataProcessor.create_spark_session(self.app_name)

    def run_pipeline(self, source_configs, sql_query, target_table, target_schema, batch_size, repartition_count, repartition_cols):
        """
        Execute the data processing pipeline.

        Args:
            source_configs (list): List of source table configurations.
            sql_query (str): SQL query for data transformation.
            target_table (str): Name of the target table.
            target_schema (str): Name of the target schema.
            batch_size (int): Batch size for writing data.
            repartition_count (int): Number of partitions for repartitioning.
            repartition_cols (list): Columns to repartition by.
        """
        try:
            DataProcessor.process_data_pipeline(
                spark=self.spark,
                source_configs=source_configs,
                db_credentials={"username": self.username, "password": self.password},
                db_config=self.db_config,
                sql_query=sql_query,
                target_table=target_table,
                target_schema=target_schema,
                batch_size=batch_size,
                repartition_count=repartition_count,
                repartition_cols=repartition_cols
            )
        except Exception as e:
            self.logger.error(f"Pipeline execution failed: {e}")
            raise
        finally:
            self.spark.stop()
            self.logger.info("Spark session terminated.")

def main():
    """
    Main entry point for the data processing application.
    """
    parser = argparse.ArgumentParser(description="Generic Data Processing Pipeline")
    parser.add_argument("--environment", type=str, required=True, help="Environment)")
    parser.add_argument("--username", type=str, required=True, help="Database username")
    parser.add_argument("--password", type=str, required=True, help="Database password")
    args = parser.parse_args()

    source_configs = [
        {
            "table_name": "source_db.table_one",
            "query": "SELECT * FROM source_db.student",
            "partition_column": "id",
            "num_partitions": 4
        },
        {
            "table_name": "source_db.table_two",
            "query": "SELECT * FROM source_db.batches",
            "partition_column": "key",
            "num_partitions": 8
        }
    ]

    sql_query = """
        SELECT 
            a.id AS record_id,
            a.name,
            a.created_at,
            b.status,
            b.updated_at
        FROM source_db_student a
        LEFT JOIN source_db_batches b
        ON a.id = b.id
        WHERE a.status != 'inactive'
    """

    target_schema = "target_db"
    target_table = "student_batch_details"
    batch_size = 1000
    repartition_count = 10
    repartition_cols = ["record_id"]

    try:
        runner = PipelineRunner(
            environment=args.environment,
            username=args.username,
            password=args.password,
            app_name=target_table
        )

        runner.run_pipeline(
            source_configs=source_configs,
            sql_query=sql_query,
            target_table=target_table,
            target_schema=target_schema,
            batch_size=batch_size,
            repartition_count=repartition_count,
            repartition_cols=repartition_cols
        )

    except Exception as e:
        logging.error(f"Application failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
