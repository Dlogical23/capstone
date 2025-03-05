# capstone
capstone project files and research

# Brainstorm Your Project Ideas For your initial project ideas, you’ll want to: 
● Include a short blurb for each of your ideas. 
○ The blurb should, at a high level, describe the problem and the data you’ll be using to solve it. At this point, there’s no need to talk about specific methods and techniques. 
● Post your idea (title and blurb) on the community and solicit feedback from both mentors and other students. Pick one idea to work on based on the feedback you get. Discuss the idea with your mentor to ensure they’re on board. Please note: The goal of a project is NOT to do something novel — it’s to demonstrate your competence as a machine learning engineer. It’s perfectly acceptable to work on a dataset that’s been worked on before and even answer a question that’s been answered before, as long as the work is your own. Examples For Inspiration Here are a few ideas to spark inspiration for your capstone project. Many of these ideas come from natural language processing or computer vision, since they’re two of the hottest fields in AI. Your project doesn’t need to be in one of these specializations. 
● Inventory tracking and compliance using object recognition: A company wants to automatically track inventory in its warehouses using a camera with an object recognition algorithm. A similar model could be used in a home application, such as a smart fridge which recognizes what’s placed in it. 
● Language translation: Also called machine translation, this technique uses AI to translate one human language to another, in text or speech. You can work between the two formats like speech-to-text transcription or text-to-speech generation. 
● QAsystemsandchatbots: Increasingly, companies are using automated chatbots to address their customer service workloads. These bots produce human-like responses to questions and are getting better every day. 
● Text summarization: Imagine an application that can digest the daily news and produce a coherent summary tailored to a user. You can apply summarization to different domains, such as an application that can automatically produce a personalized summary for a student who’s trying to research a large amount of material.
● Fraud/spam detection: Detect “bad” transactions or items in a dataset. This could take the form of detecting fraudulent credit card transactions, fake news on social media, spam in email, doctored images or video, or abusive behavior on Twitter. Depending on the problem, you can use a variety of techniques, ranging from “traditional” machine learning to the latest in deep learning. Former Capstone Project This is a project by one of our alumni, Siri Surab. She used the Quora Duplicate Questions dataset from Kaggle, and applied NLP techniques from both “old-school” Machine Learning as well as Deep Learning to identify duplicate questions on Quora. 
● Ideation 
● BlogPost 
● GitHub repository We don’t expect you to understand all of these techniques at the beginning of the course, but we’ve presented this here as an example of what your final project will look like. You’ll go much deeper into this specific project in a later unit on NLP. Plan For Your Project Based On Your Focus Area In total, you would spend ~120 hours on your project, including studying for some advanced topics if you choose to. 

In the last resource, you just learned about four areas of focus. Be aware that each of these focuses would influence how you spend time on each of the milestone steps of your capstone project. 
1.) Think about which area that you want to focus on based on your strengths and what you want to showcase for your future employers. 

# KMeans Classification Model with FastAPI

This repository contains code for training a KMeans classification model and serving it via a FastAPI-based REST API. The API allows users to send input features and receive cluster predictions.


2.) Here is a potential plan for you. It contains a breakdown of suggested time allocation for each main part based on your focus, and some areas where you need to budget extra time. This is only a reference, please discuss concrete details with your mentors. Don’t feel that you need to commit to this plan. Your plan may likely change as you proceed through the course. 

Data Collection & Processing Models

Prototype & Scaling Deployment/ Engineering Architecture 

Step 1-5 
Step 6-9 
Step 10-12 
Data-focused 50%-60% 

You may spend extra time on data collection, clean, and processing. And if you need to process real-time data, you will need to build ETL infrastructure. 
20-30% 20-30% 
Model-focused 25% 50% 
You will try different models and make ensemble models to enhance performance. If you are developing DL models, please budget extra time. 
25% If you are short on time, feel free to leverage existing deployment methods like Algorithmia. 
Architecture-focused 30-40% You can shine by building automation in the data pipeline to support analysis at scale. 
20~30% 
40% You can build automation to train/test data or design your own engineering architecture. We suggest this focus for students with a strong SW engineer background. 
Product-focused 30% 20% 50% You might spend extra time on developing the appUI/UX and streaming data. Project Submission Steps 1. Write a description of your three capstone project ideas. Your ideas can be broad and high-level. The descriptions should address the problem and identify the data you’ll use to solve it. You do not need to talk about specific methods and techniques. 

● Write at least 3 to 4 sentences explaining your idea and identifying the data you’d use to solve it. 
    2. Submit a Google Doc link to the submission box. 
  ● Remember to enable sharing permissions to “comment.” 
  ● Please do not submit .pdfs, .ppts, or markdowns. 
    3. Review your ideas and your tentative decision for your focus area with your mentor during your next call. 
    4. Post your idea (including a title and description) to your student community to receive peer feedback.

KMeans Classification Model with FastAPI
    
# *Disclaimer - These processes were assisted by ChatGPT, and will reflect in screen captures.

This repository contains code for training a KMeans classification model and serving it via a FastAPI-based REST API. The API allows users to send input features and receive cluster predictions.

# Table of Contents
1. Overview
2. Repository Structure
3. Classification : A Through Look Inside
4. Prerequisites
5. Installation
6. Training the KMeans Model
7. Running the FastAPI Server
8. API Endpoints
9. Maintenance
10. Contributing
11. License
12. Acknowledgements

# Overview
# Repository Structure
    kmeans-fastapi/
    ├── app.py                  # FastAPI server code
    ├── train_model.py          # Script to train and save the KMeans model
    ├── kmeans_model.pk1        # Trained KMeans model (generated by train_model.py)
    ├── requirements.txt        # Python dependencies
    ├── README.md               # This file
    └── data/                   # Directory for training data (if applicable)
    
This project demonstrates how to:
Train a KMeans clustering model using scikit-learn.
Save the trained model using joblib.
Serve the model via a FastAPI REST API.
Make predictions by sending input features to the API.


# Classification: A Through Look Inside
Classification models are a fundamental part of machine learning, used to categorize data into predefined classes or clusters. Below is a breakdown of different classification models, followed by a detailed explanation of KMeans clustering, its methodology, and advantages.

# Types of Classification Models

# 1. Supervised Classification Models
These models require labeled data (input features and corresponding output labels) to learn the relationship between inputs and outputs.
a. Logistic Regression
Description: A linear model used for binary or multi-class classification.
Methodology: Uses a logistic function to model the probability of a class.
Advantages:
Simple and interpretable.
Works well for linearly separable data.
b. Decision Trees
Description: A tree-like model that splits data based on feature values.
Methodology: Recursively splits the data into subsets based on feature thresholds.
Advantages:
Easy to visualize and interpret.
Handles both numerical and categorical data.
c. Random Forest
Description: An ensemble of decision trees.
Methodology: Combines multiple decision trees to reduce overfitting.
Advantages:
Robust and accurate.
Handles high-dimensional data well.
d. Support Vector Machines (SVM)
Description: A model that finds the optimal hyperplane to separate classes.
Methodology: Maximizes the margin between classes using support vectors.
Advantages:
Effective in high-dimensional spaces.
Works well with small datasets.
e. Neural Networks
Description: A model inspired by the human brain, consisting of layers of neurons.
Methodology: Learns complex patterns through backpropagation and gradient descent.
Advantages:
Highly flexible and powerful.
Can model non-linear relationships.

# 2. Unsupervised Classification Models
These models do not require labeled data and are used to find patterns or groupings in data.
a. KMeans Clustering
Description: A clustering algorithm that partitions data into k clusters.
Methodology: Iteratively assigns data points to the nearest cluster centroid and updates the centroids.
Advantages:
Simple and efficient.
Works well for large datasets.
b. Hierarchical Clustering
Description: A clustering algorithm that builds a hierarchy of clusters.
Methodology: Agglomerative (bottom-up) or divisive (top-down) approaches.
Advantages:
No need to specify the number of clusters.
Provides a dendrogram for visualization.
c. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
Description: A clustering algorithm that groups data based on density.
Methodology: Identifies core points, border points, and noise.
Advantages:
Handles noise and outliers well.
Does not require specifying the number of clusters.

# KMeans Clustering: Methodology and Advantages
# What is KMeans?
KMeans is an unsupervised learning algorithm used to partition data into k clusters, where each data point belongs to the cluster with the nearest mean (centroid).

# Methodology
Initialization:
Choose the number of clusters (k).
Randomly initialize k cluster centroids.
# Assignment:
Assign each data point to the nearest centroid based on a distance metric (usually Euclidean distance).
Update:
Recalculate the centroids as the mean of all data points assigned to each cluster.
Iteration:
Repeat the assignment and update steps until convergence (when centroids no longer change significantly).

# Advantages of KMeans
Simplicity:
Easy to understand and implement.
Requires only a few parameters (k and distance metric).
Efficiency:
Computationally efficient, especially for large datasets.
Scales well with the number of data points.
Interpretability:
Provides clear cluster assignments and centroids.
Useful for exploratory data analysis.
Versatility:
Can be applied to a wide range of data types (numerical, categorical with preprocessing).

# Limitations of KMeans
Choice of k:
Requires the number of clusters (k) to be specified in advance.
Choosing an inappropriate k can lead to poor results.
Sensitivity to Initialization:
The algorithm can converge to local minima depending on the initial centroids.
Assumes Spherical Clusters:
Works best when clusters are spherical and evenly sized.
Struggles with irregularly shaped clusters.
Outliers:
Sensitive to outliers, which can skew the centroids.

# When to Use KMeans
When you have a large dataset and need a quick clustering solution.
When the data has clear, spherical clusters.
For exploratory data analysis or as a preprocessing step for other algorithms.

# Example Use Cases
Customer Segmentation:
Group customers based on purchasing behavior.
Image Compression:
Reduce the number of colors in an image by clustering pixel values.
Document Clustering:
Group similar documents together for topic modeling.

# Comparison with Other Clustering Algorithms
Algorithm
Strengths
Weaknesses
KMeans
Simple, efficient, scalable
Requires k, sensitive to initialization
Hierarchical
No need for k, visual dendrogram
Computationally expensive
DBSCAN
Handles noise, no need for k
Struggles with varying densities

# Now, take a walk into the forest(pun intended)...

# Prerequisites
Before running the code, ensure you have the following installed:
Python 3.7 or higher
pip (Python package manager)
Installation
Clone the repository:

# Installation
Clone the repository:

    git clone https://github.com/your-username/kmeans-fastapi.git
    cd kmeans-fastapi

Install the required Python packages:

    pip install -r requirements.txt

# Training the KMeans Model
To train the KMeans model:

Ensure your training data is available in the data/ directory (or modify the script to load your data).
Run the training script:

# python train_model.py

This script will:
Load the training data.
Train a KMeans model using scikit-learn.
Save the trained model to kmeans_model.pk1.
Running the FastAPI Server
To start the FastAPI server:
Ensure the trained model (kmeans_model.pk1) is in the root directory.
Run the server:

    python app.py

The server will start at http://127.0.0.1:8000.

# *A quick aside to say along this process(at this point in particular) is where I struggled and learned the most. I gained a great deal of knowledge about FastAPI and API keys. Docker images and containers became home. Python and the CMD window became engrained in me. Moving on…

# API Endpoints
1. Root Endpoint
URL: GET /
Description: Check if the API is running.
Response:

    {
    "message": "API is running!"
    }

3. Prediction Endpoint
URL: POST /predict/
Description: Predict the cluster label for given input features.
Request Body:

    [1, 3, 5, 7]

Response:
    {
      "cluster_label": 1
    }

Maintenance
Updating the Model
Retrain the model using train_model.py.
Replace the existing kmeans_model.pk1 file with the new model.
Monitoring the API
Use tools like Postman or curl to test the API endpoints.
Check the server logs for errors or issues.
Dependency Management
Update requirements.txt if new dependencies are added:

    pip freeze > requirements.txt

Contributing
Contributions are welcome! Please follow these steps:
Fork the repository.
Create a new branch for your feature or bugfix.
Submit a pull request with a detailed description of your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments
scikit-learn for the KMeans implementation.
FastAPI for the REST API framework.
joblib for model serialization.
FastAPI and family(uvicorn, gunicorn…etc.) for local hosting magic
Docker for imaging and containerization
Python for the language coding environments
And many more “unnecessary” exploratory tools!(Looking at you AWS…)

# This README.md provides a clear and structured guide for users to understand, use, and contribute to my repository. I look forward to test the concepts here more. I’ve undertaken building a food website orderflow chatbot from end-to-end and have most of that project completed. See you soon!

