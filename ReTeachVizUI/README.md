# ReTeach Final Project

**Author**: Ananya, Susheel, Yuhao, Tianhao (Team Butterfly)

## Overview
Welcome to the ReTeach Project – an innovative venture aimed at revolutionizing the way educational feedback is processed and utilized. As a co-founder of an education startup, our goal is to develop a groundbreaking automated teacher feedback product named \ReTeach.\ This tool is designed to listen to teachers in the classroom and provide insightful feedback, making the educational process more efficient and effective.


## Objectives
Our primary aim is to devise a user-friendly interface that:,

**Facilitates Rapid Labeling**: Minimizes manual effort by reducing the need for excessive clicking and manual data entry.

**Intelligent Label Prediction**: Incorporates a model that provides preliminary label suggestions for each statement, easing the review process.

**Interactive Querying**: Allows users to pose questions to the data, yielding quick and relevant answers.

**Iterative Learning**: An advanced feature where the platform \learns\ from ongoing user interaction, enhancing its prediction accuracy over time.

## Implementation
We are committed to delivering an in-house solution that is both maintainable and extensible. The project will be developed using Jupyter notebooks, accompanied by an app.py file for the user interface, and a requirements.txt file detailing the necessary packages.

## Key Components:
Modular Design and Software Development Principles: Adherence to software engineering standards, ensuring code reuse, clarity, and effective documentation.
AI-Assisted Labeling: Utilization of advanced language models like OpenAI's GPT and Huggingface's transformers for initial data labeling.
Interactive Data Querying: Empowering users to inquire about data directly through the model, promoting a deeper understanding of the data.
In-the-Loop Labeling: A dynamic feature where the model adapts and improves its predictions based on user corrections and feedback.

## User Interface:
The user interface, crucial for accessibility and ease of use, will be developed using tools like Streamlit or Gradio. It will consist of:

**Overview Page**: An informative section about the project, its purpose, and the team behind it.

**AI-Assisted Labeling Page**: A functional area for uploading transcripts, viewing model-suggested labels, and downloading the modified data.

**Ask the Dataset Page**: A query interface for posing questions and receiving model-generated responses.

**AI-Assisted Analysis (In-loop) Page**: An interactive section for real-time label correction and model training.

## How to use it

1. Initialize docker container, make sure docker desktop is installed and configured correctly. Note that docker might take a while to initialize, please be patient.

2. Run streamlit, the command is very simple: **streamlit run app.py**
    - If you are using VSCode, but facing issue where you can't open the streamlit page, please check your VSCode settings:
        - Make sure **Remote: Auto Forward Ports Source** is set to **process**
        - Make sure to enable **Remote: Auto Forward Ports**

3. Follow the instructions on each streamlit page, enjoy!
    - Please use dataset in **/data** folder for testing functionalities.
    - For **Ask Dataset** page, make sure to have a OpenAI API key in hand, because that is required for GPT to reply to questions.
    - Since our implementation involves training and predicting using a BERT model, the streamlit application might seem sluggish (especially for the in-loop labeling part due to training). This is completely normal, and doesn't mean something is wrong with the program.




