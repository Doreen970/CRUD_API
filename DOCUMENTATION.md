# MY Flask API DOCUMENTATION

# Available Endpoints
# Retrieve User
**Objective:** Get user data by name or id
**HTTP method:** GET
**Path:** /api/user_id
**Query Parameter:**
name (string, required): User's name
user_id (integer, required): Userr's id
**Responses:**
**200:** Successful Response (Content: JSON)
**404:** Validation Error (Content: HTTPValidationError JSON object)

# Add User
**Objective:** Establish a new user
**HTTP Method:** POST
**Path:** /api
**Request Body:** PersonCreate JSON object (Required)
This can only be done on postman not on your browser
**Responses:**
**201:** Successful Response (Content: Person JSON object)
**404:**  Validation Error (Content: HTTPValidationError JSON object)

# Remove User
**Objective:** Remove a user by name
**HTTP Method:** DELETE
**Path:** /api/user_id
**Query Parameter:**
name (string, required): User's name
**Responses:**
**204:** Successful Response (Content: JSON)
**404:** Validation Error (Content: HTTPValidationError JSON object)

# Modify User
**Objective:** Adjust user information by name
**HTTP Method:** PUT
**Path:** /api/user_id
**Query Parameter:**
name (string, required): Name of the user to update
**Request Body:** PersonCreate JSON object (Required)
**Responses:**
**200:** Successful Response (Content: Person JSON object)
**404:** Validation Error (Content: HTTPValidationError JSON object)

# Data Structures
**Person**
**Attributes:**
name (string, required): User's name
id (integer): User ID

**Create_Person**
**Attributes:**
name (string, required): User's name

---
This guide gives details about the accessible API endpoints, their functions, expected request/response structures, and data organization.


