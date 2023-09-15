# Person REST API

This project introduces a REST API for overseeing "person" resources, which involves the creation, retrieval, modification, and deletion of individual records. Crafted using Flask API, this API seamlessly interfaces with diverse databases. It dynamically adapts to user-provided input, such as a person's name, allowing for versatile operations.

# Key Features
**CRUD operations:** API allows users to Create, Read, Update, and Delete person resources.
**Secure Database Interaction:** All interactions with the database are designed to safeguard against common vulnerabilities like SQL injections.
**Dynamic Parameter Handling:** The API processes operations based on user-supplied parameters, such as a person's name.
**Comprehensive Documentation:** A detailed documentation file outlines request/response formats, setup instructions, and sample API usage.

# Initiating the program
**Prerequisites**
Python (3.7+)
Flask(This should be installed)

# Set-Up Process
1. Clone the GitHub repository to your local machine: 
2. Change directory and get inside the directory of the cloned repository
3. Create and activate a virtual environment
4. Install flask

# Application Flow
**Run Application:**
python yourfilename.py

# Create a new Person
To introduce a new person, initiate a POST request to /api with a JSON payload containing the person's name.
you can do this using postman
# Viewing Person details
To acquire details of a person by name, initiate a GET request to /api/user_id with the name query parameter.
# Adjusting Person Details
To modify a person's details by name, dispatch a PUT request to /api/user_id with the name query parameter and a JSON payload containing the updated information.
# Deleting a Person
To erase a person by name, send a DELETE request to /api/user_id with the name query parameter.

# Verification
To verify the API, you can employ tools like Postman or write scripts in Python utilizing the requests library. Ensure you test each CRUD operation.
