# Pattern Assignment Backend

This project is a backend for the given technical assignment. It is built using FastAPI.

### Technologies Used:
- FastAPI
- PyMongo(MongoDB)
- OpenAI model using APIs

### API Workflow:
- API request received then first thing checked in route match in src.api.api.py
- Route takes API to controller product_controller.py where AUTH is checked i.e. if the API KEY or Access Token received in API header is valid.
- Controller also checks the schema ProductReviewData where we have only 1 property i.e. asi_number (ASIN Number)
- Controllers routes request to service where the following sequence of events are happening:
  - Make Request to Amazon Rainforest using ASIN Number
  - Receive API response from Amazon Rainforest and dump into MongoDB
  - Calls OPENAI API Service & summarises the reviews
  - Prepare the final response to be returned
  - Return the API response

This project is a microservice that provides REST APIs. The service makes sure the following principles are followed:
- Modularity
- Security
- Data Availability

### What can be improved?
- The product reviews can be read from MongoDB collection instead of Amazon Rainforest as the vendor API is taking time in returning us the response.
- We can create "Celery" background service which keeps on pulling the data from Amazon Rainforest API and "UPSERT" in our MongoDB database. Then we can create all our API where source of data would be just MongoDB
- We can keep the API Access Token & OPENAPI API KEY on AWS Secrete Manager and access it from there instead of hard coding in the codebase

### To setup project on your local

In the project directory, you can run:

#### `pip install -r requirements.txt`

#### `uvicorn src.main:app`

Or 

In Pycharm - Edit configurations as follows:
- Set Scipt to main.py
- Set Working directory to main directory "pattern_assignment_backend"

Go to your browser and checks the Swagger UI on http://localhost:8000/docs

### About Swagger UI:
 This is FastAPI's built in UI where you can see all your Project details which includes:
 - API Endpoints
 - Request Payload of APIs
 - Response details of API if you run APIs from this UI

Some Screenshots:

##### Data pulled from Amazon Rainforest saved to MongoDB:

![alt text](https://github.com/dipakrathod258/pattern_assignment_backend/blob/main/src/assets/documentation_images/amazon_rainforest_api_data_pulled.png?raw=true)


##### Product Review Summarised using OPENAI is saved to MongoDB:

![alt text](https://github.com/dipakrathod258/pattern_assignment_backend/blob/main/src/assets/documentation_images/product_review_summary_saved_to_mongo.png?raw=true)

