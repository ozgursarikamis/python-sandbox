from pyspark.sql import SparkSession
from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# CREATE AN ENGINE:
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

try:
    with engine.connect() as connection:
        print('connection was successful')
except Exception as e:
    print(f"connection failed: {e}")

# spark = SparkSession.builder.appName("example").getOrCreate()

# data = [("John", 25),("Jane", 20), ("Mike", 20)]

# df = spark.createDataFrame(data, ["name", "age"])
# df.show()

# spark.stop()