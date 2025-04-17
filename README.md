# COM745 Big Data & Infrastructure: Educational Attainment & Nutritional Quality Analysis on AWS

## Project Overview

This repository contains the work submitted for Coursework 2 of the Big Data & Infrastructure module (COM745) at Ulster University (MSc Internet of Things/Computer Science). The project involves building and utilizing a data lake environment on Amazon Web Services (AWS) to analyze the relationship between educational attainment and nutritional quality using publicly available datasets.

The primary goal was to demonstrate practical skills in identifying, ingesting, processing, analyzing, and visualizing big data using cloud-based data lake technologies, fulfilling the requirements outlined in the coursework specification.

**Module:** Big Data & Infrastructure (COM745)
**Institution:** Ulster University
**Assessment:** Coursework 2 (75% of module mark)
**Technology Focus:** AWS Data Lake Services

---

## 1. Problem Definition & Dataset Selection

### 1.1. Problem Focus

The project aimed to investigate potential correlations and insights related to **[Your Specific Problem Focus - e.g., the impact of school meal nutritional quality on student performance, regional disparities in nutrition and educational outcomes, trends over time, etc.]**. This involved exploring publicly available data sources to identify relevant datasets that could support such analysis.

### 1.2. Dataset Identification and Justification

Several public data repositories were explored, including Kaggle, data.gov.uk, data.gov, etc. The following datasets were selected for this analysis:

*   **Dataset 1:** `[Dataset Name 1]`
    *   **Source:** `[e.g., Kaggle, data.gov.uk, specific URL]`
    *   **Description:** `[Briefly describe the data - e.g., UK school exam results per region 2015-2020]`
    *   **Justification:** `[Why was this dataset chosen? e.g., Relevance to educational attainment, data quality, geographical coverage, temporal range]`
*   **Dataset 2:** `[Dataset Name 2]`
    *   **Source:** `[e.g., WHO nutritional data, specific government food survey]`
    *   **Description:** `[Briefly describe the data - e.g., National dietary survey data for children aged 5-15]`
    *   **Justification:** `[Why was this dataset chosen? e.g., Relevance to nutritional quality, compatibility with Dataset 1 for potential joins/comparisons]`
*   **[Add more datasets if applicable]**

The selection process focused on datasets that offered sufficient granularity, quality, and potential for integration to address the defined problem focus.

---

## 2. Technical Solution: AWS Data Lake Architecture

### 2.1. Chosen Technology: AWS

Amazon Web Services (AWS) was selected as the platform for building the data lake solution.

*   **Rationale:** `[Explain why AWS was chosen. e.g., Scalability, pay-as-you-go pricing suitable for academic projects, breadth of managed services reducing infrastructure overhead, prior experience, alignment with module content covering cloud data platforms like EMR/Azure Data Lakes].` Comparison with alternatives like `[Mention Hadoop on-premise or Azure Data Lake if discussed]` was considered, favouring AWS for `[mention specific advantages for your project, e.g., ease of setup for EMR, integration with S3]`.

### 2.2. Architecture Overview

The solution implemented the following AWS services:

*   **Storage:** `[e.g., Amazon S3]` - Used as the central storage repository for raw and processed data, forming the core of the data lake.
*   **Data Catalog:** `[e.g., AWS Glue Data Catalog]` - Used to crawl S3 data and create a metadata catalog, making data discoverable and queryable.
*   **Processing/ETL:** `[e.g., AWS Glue ETL, Amazon EMR with Spark/Hive, AWS Lambda]` - Used for data ingestion, cleaning, transformation, integration, and analysis. `[Briefly mention the main processing steps/scripts]`.
*   **Querying:** `[e.g., Amazon Athena]` - Used for ad-hoc SQL-based querying directly on data stored in S3.
*   **Visualization:** `[e.g., Amazon QuickSight, or mention if using external tools like Tableau/PowerBI connecting to Athena/S3, or libraries like Matplotlib/Seaborn if analysis was done in EMR/Python]` - Used to create dashboards and visualizations from the processed data.
*   **[Add any other services used, e.g., IAM for security, CloudFormation/Terraform for infrastructure if used]**

*[Optional: You could embed or link to a simple architecture diagram if you have one.]*

### 2.3. Scalability

The chosen AWS services (particularly S3, EMR/Glue, Athena) are inherently scalable, allowing the solution to handle larger datasets or more complex analyses with appropriate configuration adjustments, aligning with the principles of big data infrastructure.

---

## 3. Data Analysis and Insights

### 3.1. Analysis Performed

The integrated datasets were analyzed to derive meaningful information related to the problem focus. Key analysis steps included:

*   `[e.g., Data cleaning and preprocessing]`
*   `[e.g., Merging/joining datasets based on common keys like region or time]`
*   `[e.g., Calculating key metrics - average scores, nutritional indices]`
*   `[e.g., Performing correlation analysis between nutritional factors and educational outcomes]`
*   `[e.g., Trend analysis over time or across regions]`
*   `[e.g., Statistical comparisons]`

### 3.2. Key Insights Obtained

The analysis yielded the following insights:

*   **Insight 1:** `[Describe a key finding. e.g., A weak positive correlation was observed between X nutritional metric and Y educational score in region Z.]`
*   **Insight 2:** `[Describe another key finding. e.g., Analysis revealed significant regional disparities in access to nutritious school meals.]`
*   **Insight 3:** `[Describe another key finding. e.g., Visualization showed a trend of improving/declining... ]`

*[Refer to the specific tables/graphs produced if possible or describe them.]*

---

## 4. Demonstration Video Overview

*(This section adapts Slide 13's requirement)*

As part of the original coursework submission, a 5-minute demonstration video was created (embedded within a presentation). The video showcased the functionality of the implemented solution, including:

*   `[e.g., Navigating the AWS console to show key services used (S3 buckets, Glue catalog, EMR cluster status)]`
*   `[e.g., Demonstrating a sample data processing job execution (running a Glue job or Spark script)]`
*   `[e.g., Showing how Amazon Athena was used to query the processed data]`
*   `[e.g., Walking through the key visualizations/dashboards created (in QuickSight or other tools)]`
*   `[e.g., Highlighting how the visualizations presented the key insights derived from the data]`

*[If you have uploaded the video somewhere accessible (e.g., YouTube as unlisted), you could optionally link it here. Otherwise, this description suffices.]*

---

## 5. Conclusion and Reflection

This project successfully demonstrated the application of big data principles and cloud infrastructure (AWS) to analyze real-world datasets concerning educational attainment and nutritional quality.

*   **Key Learnings:** `[e.g., Practical experience with AWS data services, challenges in data cleaning/integration from disparate sources, importance of clear visualization for communicating findings].`
*   **Limitations/Challenges:** `[e.g., Data availability/quality issues, assumptions made during analysis, time constraints].`
*   **Potential Future Work:** `[e.g., Incorporating more diverse datasets, applying machine learning models for predictive analysis, exploring real-time data streams if available].`

---

## 6. References

*(This mirrors Slide 15)*

*   [1] `[Reference for Dataset 1 - e.g., Kaggle Dataset Link or Gov Data page]`
*   [2] `[Reference for Dataset 2]`
*   [3] `[Reference for any specific techniques or tools used, if applicable]`
*   [4] Ulster University Student Guide: https://www.ulster.ac.uk/connect/guide
*   [5] COM745 Module Specification / Coursework Brief

---

*Disclaimer: This project was completed as part of a university coursework assignment. While functional, it may not represent a production-ready system.*
