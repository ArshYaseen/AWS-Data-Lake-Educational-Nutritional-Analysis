from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, count
import matplotlib.pyplot as plt
import boto3
from botocore.exceptions import NoCredentialsError

# Initialize Spark session
spark = SparkSession.builder.appName("UniversityCrimeAnalysis").getOrCreate()

# Load datasets from S3
university_df = spark.read.csv("s3://university-crime-analysis/World_University_Ranking.csv", header=True, inferSchema=True)
crime_df = spark.read.csv("s3://university-crime-analysis/US_Crime_Rates_by_County.csv", header=True, inferSchema=True)

# Display schemas for clarity
print("University Dataset Schema:")
university_df.printSchema()
print("Crime Dataset Schema:")
crime_df.printSchema()

# Data Cleaning
# Handle missing values and rename columns for clarity
university_df = university_df.na.fill({'score': 0}).withColumnRenamed("institution", "University_Name").withColumnRenamed("country", "University_Country")
crime_df = crime_df.dropna().withColumnRenamed("county_name", "County")

# --- Crime Dataset Analysis ---
# Ensure 'population' is treated as a numeric type (integer or long)
crime_df = crime_df.withColumn("population", col("population").cast("long"))

# Extract 'state' from the 'county_name' column (assuming it's the U.S. state abbreviation)
crime_df = crime_df.withColumn("state", col("County").substr(-2, 2))  # Extract state from county name

# Aggregate crime data by state (average crime rate, total population)
crime_by_state = crime_df.groupBy("state").agg(
    avg("crime_rate_per_100000").alias("avg_crime_rate"),
    sum("population").alias("total_population")
)

# Show aggregated crime data by state
print("Crime Data Aggregated by State:")
crime_by_state.show()

# Save aggregated crime data to S3
crime_by_state.write.csv("s3://university-crime-analysis/Processed_Crime_Data.csv", header=True)

# --- University Dataset Analysis ---
# Aggregate university scores by country
university_by_country = university_df.groupBy("University_Country").agg(
    avg("score").alias("avg_score"),
    count("University_Name").alias("university_count")
)

# Show aggregated university data by country
print("University Data Aggregated by Country:")
university_by_country.show()

# Save aggregated university data to S3
university_by_country.write.csv("s3://university-crime-analysis/Processed_University_Data.csv", header=True)

# --- Insights ---
# Example: Filter top states with highest crime rates
top_crime_states = crime_by_state.sort("avg_crime_rate", ascending=False).limit(5)
print("Top 5 States with Highest Crime Rates:")
top_crime_states.show()

# Example: Filter top countries with highest university scores
top_university_countries = university_by_country.sort("avg_score", ascending=False).limit(5)
print("Top 5 Countries with Highest University Scores:")
top_university_countries.show()

# --- Visualization ---
# Collect data to Pandas DataFrame for visualization
top_crime_states_pd = top_crime_states.toPandas()
top_university_countries_pd = top_university_countries.toPandas()

# Crime Rate by State - Save as PNG locally
plt.figure(figsize=(10, 6))
plt.bar(top_crime_states_pd['state'], top_crime_states_pd['avg_crime_rate'], color='red')
plt.title("Top 5 States with Highest Crime Rates")
plt.xlabel("State")
plt.ylabel("Average Crime Rate per 100,000")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/tmp/top_crime_states.png")  # Save the plot as a PNG file locally
plt.close()

# University Score by Country - Save as PNG locally
plt.figure(figsize=(10, 6))
plt.bar(top_university_countries_pd['University_Country'], top_university_countries_pd['avg_score'], color='blue')
plt.title("Top 5 Countries with Highest University Scores")
plt.xlabel("Country")
plt.ylabel("Average University Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/tmp/top_university_scores.png")  # Save the plot as a PNG file locally
plt.close()

# --- Upload to S3 ---
# Initialize S3 client using boto3
s3_client = boto3.client('s3')

# Define the S3 bucket
bucket_name = 'university-crime-analysis'

# Upload the images to S3
try:
    s3_client.upload_file('/tmp/top_crime_states.png', bucket_name, 'visualizations/top_crime_states.png')
    s3_client.upload_file('/tmp/top_university_scores.png', bucket_name, 'visualizations/top_university_scores.png')
    print("Visualization images successfully uploaded to S3.")
except FileNotFoundError:
    print("The file was not found.")
except NoCredentialsError:
    print("Credentials not available.")
except Exception as e:
    print(f"Error uploading to S3: {str(e)}")

# Stop Spark session
spark.stop()

print("Processing and Visualization completed successfully!")
