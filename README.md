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

## Experiment Design

The cohort analysis suggests that users stop buying after the first few months.
The hypothesis is that an offer at the start of period 3 helps users buy again.
Eligible users first purchased in period 0 and also purchased in period 2.
I only keep users whose full period-3 month ended before the last observed month.
The test splits users 50/50 into control (no offer) and treatment (offer), with a fixed seed.
The primary metric is period-3 buyers divided by eligible users.
The guardrail is period-3 revenue per eligible user after a 10% treatment discount cost.
Baseline: 25.49% (26 of 102 eligible users). Only 51 users are available per group.
A 5 percentage point lift needs 1264 users per group at 5% significance and 80% power, two-sided.
This dataset is too small; a real test would need more eligible users and complete follow-up.
SIMULATED result: lift 19.61 points, p = 0.0265, 95% interval [2.25, 35.53] points.
SIMULATED revenue per user after cost: control 126.76, treatment 235.92.
SIMULATED decision: SHIP. Ship only with a positive significant lift and no guardrail drop.
SIMULATED detection over 1,000 tests: 5.50%, compared with the 80% target.
Limits: Faker data, an assumed lift and treatment spend, one offer and one window; no real offer was sent.
Run [03_experiment_design.ipynb](03_experiment_design.ipynb) from the repo root after installing `requirements.txt`.
