import pandas as pd  # Library for data manipulation and analysis
import json  # Library for working with JSON data
from pymongo import MongoClient  # MongoDB client for database operations
from bson.objectid import ObjectId  # BSON ObjectId for unique identifiers in MongoDB
import numpy as np  # Library for numerical operations

def convert_to_serializable(data):
    """Recursively convert non-serializable data types to serializable types."""
    if isinstance(data, list):
        # If data is a list, convert each element recursively
        return [convert_to_serializable(item) for item in data]
    elif isinstance(data, dict):
        # If data is a dictionary, convert each key-value pair recursively
        return {key: convert_to_serializable(value) for key, value in data.items()}
    elif isinstance(data, ObjectId):
        # Convert MongoDB ObjectId to string for JSON compatibility
        return str(data)
    elif isinstance(data, pd._libs.tslibs.timestamps.Timestamp):
        # Convert pandas Timestamp to string
        return str(data)
    elif isinstance(data, np.int64):
        # Convert numpy int64 to native Python int
        return int(data)
    elif isinstance(data, np.bool_):
        # Convert numpy bool_ to native Python bool
        return bool(data)
    return data  # Return data as is if no conversion is needed

# Load CSV files into pandas DataFrames
companies_df = pd.read_csv('mp2-data/companies.csv')  # Companies data
industries_df = pd.read_csv('mp2-data/industry_info.csv')  # Industry info data
jobs_df = pd.read_csv('mp2-data/jobs.csv')  # Jobs data
employment_df = pd.read_csv('mp2-data/employment_details.csv')  # Employment details
education_skills_df = pd.read_csv('mp2-data/education_and_skills.csv')  # Education & skills

# 1. Prepare Companies Data
companies = []  # Initialize an empty list to store company documents
for _, row in companies_df.iterrows():
    # Create a dictionary for each company with its relevant attributes
    company = {
        "_id": ObjectId(),  # Unique identifier for MongoDB
        "company_id": int(row['id']),
        "name": row['name'],
        "size": row['size'],
        "type": row['type'],
        "location": row['location'],
        "website": row['website'],
        "description": row['description'],
        "hr_contact": row['hr_contact']
    }
    companies.append(company)  # Add company to the list

# Save companies data to a JSON file
with open('companies.json', 'w') as f:
    json.dump(convert_to_serializable(companies), f, indent=4)

# 2. Prepare Industries Data
industries = []  # Initialize an empty list to store industry documents
for _, row in industries_df.iterrows():
    # Create a dictionary for each industry with its relevant attributes
    industry = {
        "_id": ObjectId(),  # Unique identifier for MongoDB
        "industry_id": int(row['id']),
        "industry_name": row['industry_name'],
        "growth_rate": row['growth_rate'],
        "industry_skills": row['industry_skills'].split(', '),  # Convert string to list
        "top_companies": row['top_companies'].split(', '),  # Convert string to list
        "trends": row['trends'].split(', ')  # Convert string to list
    }
    industries.append(industry)  # Add industry to the list

# Save industries data to a JSON file
with open('industries.json', 'w') as f:
    json.dump(convert_to_serializable(industries), f, indent=4)

# 3. Prepare Jobs Data with Embedded Employment and Education Details
jobs = []  # Initialize an empty list to store job documents
for _, job_row in jobs_df.iterrows():
    # Fetch matching employment details for the job
    employment_row = employment_df[employment_df['id'] == job_row['id']]
    employment_row = employment_row.iloc[0] if not employment_row.empty else None

    # Fetch matching education and skills details for the job
    education_row = education_skills_df[education_skills_df['job_id'] == job_row['id']]
    education_row = education_row.iloc[0] if not education_row.empty else None

    # Create a dictionary for each job with its attributes and embedded details
    job = {
        "_id": ObjectId(),  # Unique identifier for MongoDB
        "job_id": int(job_row['id']),
        "title": job_row['title'],
        "description": job_row['description'],
        "years_of_experience": job_row['years_of_experience'],
        "detailed_description": job_row['detailed_description'],
        "responsibilities": job_row['responsibilities'],
        "requirements": job_row['requirements'],
        "employment_details": {
            "employment_type": employment_row['employment_type'] if employment_row is not None else None,
            "average_salary": employment_row['average_salary'] if employment_row is not None else None,
            "benefits": employment_row['benefits'].split(', ') if employment_row is not None else [],
            "remote": bool(employment_row['remote']) if employment_row is not None else False,
            "job_posting_url": employment_row['job_posting_url'] if employment_row is not None else None,
            "posting_date": str(employment_row['posting_date']) if employment_row is not None else None,
            "closing_date": str(employment_row['closing_date']) if employment_row is not None else None
        },
        "education_and_skills": {
            "required_education": education_row['required_education'] if education_row is not None else None,
            "preferred_skills": education_row['preferred_skills'].split(', ') if education_row is not None else []
        }
    }
    jobs.append(job)  # Add job to the list

# Save jobs data to a JSON file
with open('jobs.json', 'w') as f:
    json.dump(convert_to_serializable(jobs), f, indent=4)

# Print success message after generating all JSON files
print("JSON files generated successfully!")
