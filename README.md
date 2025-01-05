# Pharma Sales Data Processing

## Project Overview

This project is designed to process and transform pharmaceutical sales data. It includes various scripts for data cleaning, anomaly detection, and loading data into a PostgreSQL database. Additionally, it supports uploading data to Google Cloud Storage.

## Setup

1. Clone the repository to your local machine.
2. Ensure you have Python installed along with the necessary libraries. You can install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Data Cleaning and Transformation**: Use `scripts/data_cleaning_transformation.py` to clean and transform the sales data.
- **Anomaly Detection**: Run `scripts/anomaly_detection.py` to detect anomalies in the sales data.
- **Load to PostgreSQL**: Use `scripts/load_to_postgresql.py` to load the processed data into a PostgreSQL database.
- **Upload to Google Cloud Storage**: Execute `scripts/upload_to_gcs.py` to upload data files to Google Cloud Storage.
- **Airflow DAG**: The `scripts/airflow_dag.py` script can be used to automate the workflow using Apache Airflow.

## Data

The `csv` directory contains sample sales data files, including daily, hourly, weekly, and monthly sales data.

## License

This project is licensed under the MIT License.
