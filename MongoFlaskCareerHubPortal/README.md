# CareerHub API

This project provides a complete backend solution for the CareerHub platform, built using **Flask**, **MongoDB**, and **Docker**. It includes APIs to manage companies, industries, and job listings with various CRUD operations.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Schema Design](#schema-design)
- [Reasoning for Collections](#reasoning-for-collections)
- [Setup Instructions](#setup-instructions)
- [Example Usage with Postman](#example-usage-with-postman)
- [Generative AI Usage](#generative-ai-usage)

---

## Project Overview

This project provides:
1. **Management of companies, industries, and jobs**: Create, read, update, and delete job postings and retrieve relevant data from MongoDB.
2. **MongoDB for data storage**: Three collections for companies, industries, and jobs ensure efficient data separation.
3. **Flask API routes**: Eight API routes to interact with the backend, including query and CRUD operations.

---

## Project Structure

MongoFlaskCareerHubPortal/
│
├── careerhub-app.py         # Converts CSV to JSON and loads data into MongoDB
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Docker configuration
├── mp2-data/                # CSV data files
└── README.md                # Project documentation


## Schema Design

### **1. Companies Collection**
Stores company information such as name, size, and location.

{
  "_id": ObjectId,
  "company_id": Number,
  "name": String,
  "size": String,
  "type": String,
  "location": String,
  "website": String,
  "description": String,
  "hr_contact": String
}

### **2. Industries Collection**
Stores industry-level information, including required skills and trends.

{
  "_id": ObjectId,
  "industry_id": Number,
  "industry_name": String,
  "growth_rate": Float,
  "industry_skills": [String],
  "top_companies": [String],
  "trends": [String]
}

### **3. Jobs Collection**
Stores job listings along wiht employment and education details.

{
  "_id": ObjectId,
  "job_id": Number,
  "title": String,
  "description": String,
  "industry": String,
  "average_salary": Number,
  "location": String,
  "employment_details": {...},
  "education_and_skills": {...}
}

---

## Reasoning for Collections

### **1. Separation of Concerns**
- **Companies:** The companies collection stores specific company details, which makes it easy to manage and retrieve company-related data independently.

- **Industries:** Industry information is centralized in the industries collection, allowing us to track trends, skills, and top companies per industry without redundancy.

- **Jobs:** Each job listing is stored with embedded employment and education details, keeping all job-related information together.

### **2. Reducing Redundancy**
- If multiple jobs belong to the same company, we only need to store the company details once in the companies collection. Similarly, industry information is maintained separately to avoid duplicating industry-specific data in each job listing.

### **3. Query Efficiency**
- With this schema, we can efficiently query jobs based on:
    - **Industry:** By including the industry attribute in the jobs collection, we can filter jobs by industry directly.
    - **Salary Range:** Querying jobs by salary range becomes easier since the average_salary is directly available in the jobs collection.
    - **Experience Level:** Jobs can be queried based on years_of_experience without needing to join with other collections.

### **4. Flexibility for Expansion**
- If the application expands, it’s easy to add more attributes to each collection without impacting other parts of the schema. For example, we could add new fields to industries (like certifications required) without changing the job or company data structures.

### **5. Optimized for MongoDB Queries**
- Embedding employment and education details inside the jobs collection reduces the need for joins, making read operations faster and more efficient in MongoDB.

---

## Setup Instructions
- Ensure Docker, Visual Studio Code, and Postman are installed before proceeding to the setup.

1. Clone the Repository
    - In gitbash, enter the command: git clone https://github.com/ananim30j/ProjectsPortfolio.git
    - cd MongoFlaskCareerHubPortal
    - Make sure this is cloned in a directory where this folder is mounted in Docker
        - If not, you need to mount it in Docker
2. Modify docker-compose.yml
    - Under 'volumes', change the path on the left side of the ':' to the directory of the parent folder of where your docker-compose.yml resides
    - Keep a note of this directory as you will need to refer to it frequently (referred to "the project directory" in upcoming steps)
3. Install Dependencies
    - Open a terminal on your machine and cd into the project directory
    - Enter the command: pip install -r requirements.txt
        - Downloads all necessary components to run the code
4. Start Docker Container
    - Open Docker Desktop on your machine
    - In the same terminal as step 3, enter: docker compose up
        - Starts docker container
5. Transform CSV to JSON
    - Open a second terminal and cd into the project directory
    - Enter the command: python careerhub-app.py
        - Runs the code to take the 5 .csv files and transform them into the 3 collections, structured in JSON format
    - Verify it was successful by looking for a message "JSON files generated successfully!" in the terminal
        - Can look in the project directory as well
6. Import Data into MongoDB
    - In the second terminal, enter the command: docker exec -it careerhub-mongo sh
        - Opens the mongo shell to import the collections that were just created
    - Once you see '#', run the following 3 import statements 1 at a time
        - mongoimport --db careerhub --collection companies --file /ds5760/mongo/companies.json --jsonArray
        - mongoimport --db careerhub --collection industries --file /ds5760/mongo/industries.json --jsonArray
        - mongoimport --db careerhub --collection jobs --file /ds5760/mongo/jobs.json --jsonArray
    - You should see a message each time saying "100 document(s) imported successfully"
7. Run Flask App
    - Open a third terminal and cd into the project directory
    - Enter the command: python app.py
        - The Flask app will be accessible at http://localhost:5000/
8. Use Postman to Test Functionality
    - Use Postman to view the outputs of various queries
    - For POST, PUT, and DELETE, you need to input a request:
        - Insert it in: Body > raw > JSON

---

## Example Usage with Postman
1. Homepage
    - GET http://localhost:5000/
    - Returns a welcome message for the user
2. Create a Job Post
    - POST http://localhost:5000/create/jobPost
    - Sample Request Body:
        {
            "title": "Data Scientist",
            "industry": "Technology",
            "description": "Analyze data",
            "average_salary": 120000,
            "location": "Remote"
        }
    - Creates a job post based on what user inputs with various details
    - Requires title and industry as inputs
    - Auto increments job_id if not provided
    - "Job post created successfully!" message shown
    - Provides internal server error (500) if failed to create job post
3. View Job Details
    - GET http://localhost:5000/search_by_job_id/<job_id>
        - <job_id> is replaced with a valid value (1-100, or any others that have been created by the user)
        - Ex: GET http://localhost:5000/search_by_job_id/1
    - Allows user to search a job by its id
    - "Job details updated successfully" message shown
    - If job not found, 404 error displayed 
4. Update Job Details
    - PUT http://localhost:5000/update_by_job_title
    - Sample Request Body:
        {
            "title": "Data Scientist",
            "description": "This role requires technical and business acumen.",
            "average_salary": 130000,
            "location": "Remote"
        }
    - Allows users to input a job title they wish to update
        - Searches for job in database and displays current details if found
        - Gives option to modify fields and updates MongoDB collection
    - Requires job title
        - Error 400 otherwise
    - If job not found, error 404 displayed
5. Remove Job Listing
    - DELETE http://localhost:5000/delete_by_job_title
    - Sample Request Body:
        {
            "title": "Data Scientist",
            "confirm": true
        }
    - Allows users to delete a job title
        - Error 400 otherwise
    - Must have "confirm": true in the request body to delete
        - If user enters just the title, they are prompted "Send the same DELETE request with 'confirm': true to confirm deletion."
    - "Job '{title}' deleted successfully" message shown
    - If job not found, error 404 displayed
6. Salary Range Query
    - GET http://localhost:5000/query_salary_range?min_salary=<num1>&max_salary=<num2>
        <num1> and <num2> replaced with desired parameters
        - Ex: GET http://localhost:5000/query_salary_range?min_salary=100000&max_salary=120000
    - Queries jobs based on given salary range
        - Displays job details
    - If invalid range, error 400 displayed
7. Job Experience Level Query
    - GET http://localhost:5000/query_experience_level?experience_level=<Experience Level>
        - <Experience Level> replaced with valid value (Entry Level, Mid Level, Senior Level)
        - Ex: GET http://localhost:5000/query_experience_level?experience_level=Entry Level
    - Levels based on years of experience
        - Entry: 0-2
        - Mid: 3-5
        - Senior: 6+
    - Returns information about jobs based on experience level
    - Error 400 displayed if user enters an invalid value
8. Top Companies in Industry
    - GET http://localhost:5000/top_companies?industry=<Industry Name>
        - <Industry Name> replaced with a valid value ('Consulting', 'Healthcare', 'Finance', etc.)
            - Can check industry_info.csv for all possible values
        - Ex: GET http://localhost:5000/top_companies?industry=Consulting
    - Returns top companies in given industry
    - Error 404 displayed if no companies found in specified industry
        - Handles both invalid user entry and no data available based on criteria
9. Stop Docker Container
    - After you are finished testing, navigate to the project directory in the terminal
    - Enter the command: docker compose down
    - This will stop the docker container, and you can close everything
        - Verify it is no longer running in Docker Desktop
    
---

## Generative AI Usage

The use of generative AI aided in developing and enhancing this project. Below is a detailed breakdown of how AI contributed to various aspects of the project:

### AI Contributions:
- **Project Structure & Architecture**:
  - AI helped in brainstorming how to combine and separate the data into various collections
  
- **Data Transformation**:
  - AI assisted in troubleshooting errors when trying to convert CSV files into JSON format
    - Helped create function to convert non-serializable data types to serializable types

- **Error Handling & Validation**:
  - AI ensured robust error handling, validating inputs like job titles and salary ranges to return informative error messages in the API responses
  - AI Also guided through developing the logic to confirm deletion of jobs before executing the removal

- **Generative AI for Code Refactoring**:
  - AI suggested improvements to the code structure, ensuring readability and maintainability
  - For example, optimizing the query logic for industry-based job listings and adding dynamic job ID assignment using MongoDB’s `find_one` with sorting