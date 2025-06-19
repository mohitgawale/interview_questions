# Data Processing Pipeline

## What Does This Code Do?

This code creates a **data processing pipeline** using **Apache Spark** (a tool for handling large amounts of data) to:

- **Extract**: Read data from database tables.
- **Transform**: Combine and clean the data using a SQL query.
- **Load**: Save the processed data into a new table in a database.

The pipeline is **reusable and flexible**, so it can work with different databases and data processing tasks.

It’s split into two files:

- `Commons/DataProcessor.py`: Contains the main logic for reading, transforming, and saving data.
- `Jobs/etl_job.py`: Sets up and runs the pipeline with specific settings.

---

## 📁 File Breakdown

### 1. `Commons/DataProcessor.py`

This file has a class called `DataProcessor` that does the heavy lifting of the pipeline.  
It’s like a **toolbox** with functions to handle different steps of data processing.

#### Key Functions:

##### `create_spark_session(app_name)`

- Starts a Spark session (like launching a data app).
- Sets up a connection to a database using a JDBC driver.
- Returns the Spark session for other steps.

##### `process_data_pipeline(...)`

This function runs the **full ETL pipeline**:

- Reads data from source tables.
- Runs a SQL query to transform the data (e.g., joining tables, filtering rows).
- Repartitions data into smaller chunks for faster processing.
- Saves the transformed data into a target table in the database.
- Optionally removes duplicate rows.
- Logs messages for tracking and debugging.

##### `_read_source_data(...)`

- Reads data from multiple source tables using JDBC.
- Creates temporary views (virtual tables) for SQL queries.

##### `_write_to_database(...)`

- Writes the final data to a target table.
- Uses batching to avoid overloading the database.

##### `_deduplicate_table(...)`

- Removes duplicate records if needed.
- Uses a SQL query and a partition column to keep unique rows.

#### Why It’s Useful

- Organized into **reusable functions** for easy use in different projects.
- Built-in **logging and error handling**.
- Highly **configurable** (e.g., batch size, partition columns).

---

### 2. `Jobs/etl_job.py`

This file is the **entry point**. It sets up example configs and **runs the pipeline**.

#### Key Parts:

##### `PipelineRunner` Class

- Sets up the pipeline with environment info (e.g., dev/prod), username, password, and app name.
- Creates a Spark session and runs the pipeline using `DataProcessor`.
- Ensures the Spark session is always closed properly.

##### `run_pipeline()` Method

- Calls the `process_data_pipeline()` function with the provided settings.
- Handles execution flow and logs issues.

##### `main()` Function

- Reads input parameters from the command line (like environment, username, and password).
- Sets up an example pipeline with:
  - **Two source tables**: `student` and `batches`
  - **SQL query** to join the tables and filter only active students
  - **Target table**: `student_batch_details`
  - Configs for batch size and partitioning
- Starts the pipeline using `PipelineRunner`

#### Example Settings

- **Source Tables**:
  - `student`: Contains student details (e.g., ID, name, status)
  - `batches`: Contains batch details (e.g., ID, status, update time)

- **SQL Query**: Joins student and batch tables, filters out inactive students

- **Target Table**: Stores the final result in `student_batch_details` in the `target_db`

---
