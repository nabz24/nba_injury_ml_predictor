# NBA Injury Risk Predictor ( MSDS 434 Final Project)

This repository contains the codebase for a machine learning-powered Flask application deployed to Google Cloud Run. It predicts injury risk for NBA players based on workload metrics. It used google bigquery ml features for predictions as well as python ml packages.


---

## Screencast Videos

1. [Functional Specification + Dataset](https://your-link-1)
2. [BigQuery ML Model Creation](https://your-link-2)
3. [Step 3: Construct a Functional Specification](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=401dda96-e905-4abc-8783-b2c500eafdaa&start=0)
4. [Step 4: Perform a Data Ingest](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d1c92949-cc1b-4d66-b7bb-b2cc00f08329&start=0)
5. [Step 5: Create a Demonstration of the packages BigQuery ML](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=c87cad64-efcd-48e9-bcfd-b2d20115a83b&start=0)
6. [Step 6: Implement a Predictive Model with GCP Big Query AutoML](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=03eb1736-2076-4cc0-8e04-b2d901298de2&start=0)
7. [Step 7: Construct a Demonstration of Containerized Microservice Application](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3eaeefce-39db-42a4-9a90-b2e00119baa4&start=0)
8. [Step 8: Implement Containerized Application](https://your-link-8)
9. [Step 9: Implement Performance Monitoring Application](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9dc7b7b9-03be-463a-933c-b2ee0184c785&start=0)
10. [Step 10: Implement a Production Environment](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7ddbedb7-a562-42c7-a53f-b2f501146e44&start=0)

---
## Written Posts
1.Step 1: Identify the Problem
For my final project, I am interested in building a cloud-native analytics application focused on predicting injury risk for professional athletes. I plan to develop an application that uses player workload data such as minutes played, number of tackles, or recent injuries, to predict the likelihood of a player getting injured in their next game. As a huge sports enthusiast, I chose a sports related project because it aligns with my interests. Since I’ve been working in tech, I hope this project will serve as a bridge into the sports industry, while also allowing me to gain hands-on experience building a machine learning cloud application that can help teams anticipate injuries and better manage player workloads.
Question I want to explore are: Given an athlete’s recent workload history, how likely are they to sustain an injury in the near future? Do performance metrics influence injury risk? Are there specific workload patterns that lead to higher injury rates?
I plan to use publicly available sports data from sources like Kaggle or Google BigQuery's public datasets. For machine learning I will use BigQueryML. The model will be deployed via Google App Engine, with a REST API to serve injury risk predictions. I plan to implement monitoring and alerting using Stackdriver.
