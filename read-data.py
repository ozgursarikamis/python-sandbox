from pyspark.sql import SparkSession

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
PLSQL_JAR = os.getenv("PLSQL_JAR")

# Initialize Spark session with the JDBC driver
spark = SparkSession.builder \
    .appName("PostgreSQL_Spark") \
    .config("spark.jars", PLSQL_JAR) \
    .getOrCreate()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Define PostgreSQL connection properties
properties = {
    "user": DB_USER,
    "password": DB_PASSWORD,
    "driver": "org.postgresql.Driver"
}

# JDBC URL format for PostgreSQL
jdbc_url = f"jdbc:postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Read data from PostgreSQL table into a Spark DataFrame
df = spark.read.jdbc(url=jdbc_url, table='"public"."Organisations"', properties=properties)

df.show()  # Display data

df.printSchema()
