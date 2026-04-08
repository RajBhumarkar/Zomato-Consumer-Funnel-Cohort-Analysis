# Zomato Consumer Funnel & Cohort Analysis

## Project Summary
In this project, I analyzed the consumer journey across the core Zomato app funnel: **App Open → Search → Restaurant Viewed → Add to Cart → Order Placed → Payment**. 

The primary objective was to identify drop-off points and calculate conversion rates segmented by city and acquisition channel. Additionally, I built retention cohorts based on the acquisition month, channel, and city to understand long-term user behavior. 

*Note: The dataset used for this analysis was simulated using the Python Faker library.*

## Key Findings
* **Acquisition vs. Conversion:** While Google Ads drives a significant volume of top-of-funnel users (28% of total traffic), it only converts at 13.4%. In contrast, Organic traffic shows a much stronger conversion rate at 30.9%.
* **Geographic Friction:** Pune exhibits the highest drop-off rate at the checkout stage. Based on the data, this friction is likely driven by price shock from unexpected delivery or platform charges added at the final step.
* **Long-Term Retention:** Quality of acquisition matters more than volume. Organic users proved to be significantly more loyal, retaining at 2x the rate of Google Ads users by Month 3.

## Funnel Overview

![Funnel Chart](https://github.com/RajBhumarkar/Zomato-Consumer-Funnel-Cohort-Analysis/blob/main/output%2FConversion_rate_by_funnel_stage.png)

## Cohort Retention

![Cohort Heatmap](https://github.com/RajBhumarkar/Zomato-Consumer-Funnel-Cohort-Analysis/blob/main/output%2Fcohort_by_acquisition_month.png)

## Tech Stack
* **Languages:** Python, SQL
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn, Plotly
* **Data Generation:** Faker
