# NBA Injury Risk Predictor ( MSDS 434 Final Project)

This repository contains the codebase for a machine learning-powered Flask application deployed to Google Cloud Run. It predicts injury risk for NBA players based on workload metrics. It used google bigquery ml features for predictions as well as python ml packages.


---

## Screencast Videos

1. [Step 3: Construct a Functional Specification](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=401dda96-e905-4abc-8783-b2c500eafdaa&start=0)
2. [Step 4: Perform a Data Ingest](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d1c92949-cc1b-4d66-b7bb-b2cc00f08329&start=0)
3. [Step 5: Create a Demonstration of the packages BigQuery ML](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=c87cad64-efcd-48e9-bcfd-b2d20115a83b&start=0)
4. [Step 6: Implement a Predictive Model with GCP Big Query AutoML](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=03eb1736-2076-4cc0-8e04-b2d901298de2&start=0)
5. [Step 7: Construct a Demonstration of Containerized Microservice Application](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3eaeefce-39db-42a4-9a90-b2e00119baa4&start=0)
6. [Step 9: Implement Performance Monitoring Application](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9dc7b7b9-03be-463a-933c-b2ee0184c785&start=0)
7. [Step 10: Implement a Production Environment](https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7ddbedb7-a562-42c7-a53f-b2f501146e44&start=0)

---
## Written Posts
<b>Step 1: Identify the Problem</b> <br>
For my final project, I am interested in building a cloud-native analytics application focused on predicting injury risk for professional athletes. I plan to develop an application that uses player workload data such as minutes played, number of tackles, or recent injuries, to predict the likelihood of a player getting injured in their next game. As a huge sports enthusiast, I chose a sports related project because it aligns with my interests. Since I’ve been working in tech, I hope this project will serve as a bridge into the sports industry, while also allowing me to gain hands-on experience building a machine learning cloud application that can help teams anticipate injuries and better manage player workloads.
Question I want to explore are: Given an athlete’s recent workload history, how likely are they to sustain an injury in the near future? Do performance metrics influence injury risk? Are there specific workload patterns that lead to higher injury rates?
I plan to use publicly available sports data from sources like Kaggle or Google BigQuery's public datasets. For machine learning I will use BigQueryML. The model will be deployed via Google App Engine, with a REST API to serve injury risk predictions. I plan to implement monitoring and alerting using Stackdriver.
<br>
<br>
<b>Step 2: Identify the Data Set</b><br>
For my final project, I plan to use publicly available NBA datasets to build an application that predicts injury risk for professional NBA athletes based on workload metrics. The primary dataset I’ll be using is the NBA Database available on Kaggle, which includes detailed game-by-game player statistics such as minutes played, field goals attempted, rebounds, fouls, and play-by-play data. The dataset is in SQLite format, and I’ll extract and query data directly from the database to support my analysis.

NBA DatabaseLinks to an external site.

GitHub will be a central tool in managing the development of this application. I’ll use it to track changes to my code. Most importantly, GitHub will enable automated continuous integration and deployment to Google App Engine. This setup will ensure that updates to the main branch are automatically deployed, helping me maintain code and easily deploy my updates.
<br>

<b>Step 8: Implement Containerized Application</b> <br>
For my final project, I would build on my containerized REST API by introducing a second microservice running RabbitMQ as a message broker. This would allow me to implement a publish/subscribe model within my application. Instead of having clients send POST requests directly to the API to process player workload data, the API would be configured to publish a message to a RabbitMQ queue.

A separate consumer microservice, running in its own container, would subscribe to this queue and handle the injury prediction task by applying a machine learning model to analyze the data and return predictions through an API response. This architecture allows the API to remain lightweight and responsive by offloading the more intensive machine learning tasks to a separate service.

It also improves scalability as RabbitMQ manages the message flow and prevents the API from becoming a bottleneck when handling a large volume of requests. By using RabbitMQ as its own microservice, I can decouple data ingestion from data processing, making the easier to maintain and more scalable.

This setup also allows me to add more consumer microservices in the future, each dedicated to different machine learning models or analytics tasks, without needing to modify the core API or the RabbitMQ service.
