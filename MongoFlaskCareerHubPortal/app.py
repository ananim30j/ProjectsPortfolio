from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

# Initialize Flask app
app = Flask(__name__)

# Initialize MongoDB client and collections
client = MongoClient('mongodb://localhost:27017/')
# Database: careerhub
db = client['careerhub']

# Collections for storing jobs, companies, and industries
jobs_collection = db['jobs']
companies_collection = db['companies']
industries_collection = db['industries']

# 1. Homepage route
# GET http://localhost:5000/
# Returns a simple welcome message in JSON format.
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the CareerHub API!"})

# 2. Create a Job Post
# POST http://localhost:5000/create/jobPost
# Sample Request Body:
# {
#   "title": "Data Scientist",
#   "industry": "Technology",
#   "description": "Analyze data",
#   "average_salary": 120000,
#   "location": "Remote"
# }
# Insert in Body > raw > JSON
@app.route('/create/jobPost', methods=['POST'])
def create_job_post():
    try:
        data = request.json
        required_fields = ['title', 'industry']

        # Validate input to ensure required fields are present
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Auto-increment job_id (if not provided)
        last_job = jobs_collection.find_one(sort=[("job_id", -1)])
        new_job_id = (last_job["job_id"] + 1) if last_job else 1
        # Prepare the job document
        job = {
            "job_id": data.get('job_id', new_job_id),
            "title": data['title'],
            "description": data.get('description', ''),
            "industry": data['industry'],
            "average_salary": data.get('average_salary', 0),
            "location": data.get('location', 'Not specified')
        }

        # Insert into MongoDB
        jobs_collection.insert_one(job)

        return jsonify({
            "message": "Job post created successfully!",
            "job_id": job["job_id"]
        }), 201

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# 3. View Job Details by Job ID
# GET http://localhost:5000/search_by_job_id/<job_id>
# Example: http://localhost:5000/search_by_job_id/1
@app.route('/search_by_job_id/<int:job_id>', methods=['GET'])
def view_job_details(job_id):
    """Search job details by job_id (integer)."""
    # Ensure job is found by its ID
    job = jobs_collection.find_one({"job_id": job_id})

    if not job:
        return jsonify({"error": "Job not found"}), 404

    # Convert ObjectId to string for JSON response
    job['_id'] = str(job['_id'])
    return jsonify(job), 200

# 4. Update Job Details by Job Title
# PUT http://localhost:5000/update_by_job_title
# Sample Request Body:
# {
#   "title": "Data Scientist",
#   "description": "This role requires technical and business acumen.",
#   "average_salary": 130000,
#   "location": "Remote"
# }
# Insert in Body > raw > JSON
@app.route('/update_by_job_title', methods=['PUT'])
def update_job_details():
    data = request.json
    title = data.get('title', '').strip()

    if not title:
        return jsonify({"error": "Job title is required"}), 400

    # Search for job by title (case-insensitive)
    job = jobs_collection.find_one({"title": {"$regex": f"^{title}$", "$options": "i"}})

    if not job:
        return jsonify({"error": "Job not found"}), 404
    # Prepare update data
    update_data = {
        "description": data.get('description', job.get('description', '')),
        "average_salary": data.get('average_salary', job.get('average_salary', 0)),
        "location": data.get('location', job.get('location', 'Not specified')),
        "job_id": data.get('job_id', job['job_id'])  # Ensure job_id remains consistent
    }

    # Update the job in MongoDB
    jobs_collection.update_one({"_id": job['_id']}, {"$set": update_data})
    return jsonify({"message": "Job details updated successfully"}), 200

# 5. Remove Job Listing by Job Title
# DELETE http://localhost:5000/delete_by_job_title
# Sample Request Body:
# {
#   "title": "Data Scientist",
#   "confirm": true
# }
# Insert in Body > raw > JSON
@app.route('/delete_by_job_title', methods=['DELETE'])
def delete_job():
    data = request.json
    title = data.get('title', '').strip()
    confirm = data.get('confirm', False)  # Check for confirmation flag

    if not title:
        return jsonify({"error": "Job title is required"}), 400

    # Find the job (case-insensitive)
    job = jobs_collection.find_one({"title": {"$regex": f"^{title}$", "$options": "i"}})

    if not job:
        return jsonify({"error": "Job not found"}), 404

    if not confirm:
        # Ask for confirmation before deletion
        job['_id'] = str(job['_id'])  # Convert ObjectId to string for JSON response
        return jsonify({
            "job_details": job,
            "message": "Send the same DELETE request with 'confirm': true to confirm deletion."
        }), 200

    # Proceed with deletion if confirmed
    jobs_collection.delete_one({"_id": job['_id']})
    return jsonify({"message": f"Job '{title}' deleted successfully"}), 200


# 6. Query Jobs by Salary Range
# GET http://localhost:5000/query_salary_range?min_salary=<num1>&max_salary=<num2>
# Ex: GET http://localhost:5000/query_salary_range?min_salary=100000&max_salary=120000
# Modify the minimum & maximum endpoints if desired
@app.route('/query_salary_range', methods=['GET'])
def query_salary_range():
    try:
        min_salary = int(request.args.get('min_salary', 0))
        max_salary = int(request.args.get('max_salary', float('inf')))
    except ValueError:
        return jsonify({"error": "Invalid salary values"}), 400

    jobs = list(jobs_collection.find({"average_salary": {"$gte": min_salary, "$lte": max_salary}}))
    for job in jobs:
        job['_id'] = str(job['_id'])

    return jsonify(jobs), 200

# 7. Query Jobs by Experience Level
# GET http://localhost:5000/query_experience_level?experience_level=<Experience Level>
# Replace <Experience Level> with a valid value ('Entry Level', 'Mid Level', 'Senior Level')
@app.route('/query_experience_level', methods=['GET'])
def query_experience_level():
    experience_level = request.args.get('experience_level', '').strip().title()

    if experience_level not in ['Entry Level', 'Mid Level', 'Senior Level']:
        return jsonify({"error": "Invalid experience level"}), 400

    # Map experience levels to year ranges
    if experience_level == 'Entry Level':
        query = {"years_of_experience": {"$lte": 2}}
    elif experience_level == 'Mid Level':
        query = {"years_of_experience": {"$gte": 3, "$lte": 5}}
    else:  # Senior Level
        query = {"years_of_experience": {"$gte": 6}}

    jobs = list(jobs_collection.find(query))

    for job in jobs:
        job['_id'] = str(job['_id'])

    return jsonify(jobs), 200

# 8. Fetch Top Companies in an Industry
# GET http://localhost:5000/top_companies?industry=<Industry Name>
# Replace <Industry Name> with a valid value ('Consulting', 'Healthcare', 'Finance', etc.)
@app.route('/top_companies', methods=['GET'])
def top_companies():
    industry_name = request.args.get('industry', '').strip().title()

    if not industry_name:
        return jsonify({"error": "Industry parameter is required"}), 400

    # Query the industries collection for the given industry_name
    industry = industries_collection.find_one(
        {"industry_name": {"$regex": f"^{industry_name}$", "$options": "i"}}
    )

    if not industry:
        return jsonify({"error": f"No companies found for industry '{industry_name}'"}), 404

    # Extract top companies from the matched industry
    top_companies = industry.get("top_companies", [])

    if not top_companies:
        return jsonify({"error": f"No top companies listed for industry '{industry_name}'"}), 404

    # Prepare the response with company names
    response = [{"company": company} for company in top_companies]

    return jsonify(response), 200

# Run the Flask app
# Can use Postman to verify if functionality is working
# Use given URLs & Sample Request Body to test
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
