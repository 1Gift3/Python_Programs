# To run this code
# uvicorn filename:app --reload
# Then visit : http://127.0.0.1:8000/docs for the Swagger UI
# I can POST to /submit_score and GET from /results

# Questions
# HTTPException allows me to throw HTTP errors like 400 for bad input
# Basemodel from pydantic is used to define and validate the shape of incoming data
# Line 10 input model using pydantic defines the expected input
# - When i post a json FASTAPI will first validate data
# - convert it into a python object for you
# - and Automatically show the schema in the /docs Swagger ui
# Line 30 - is a POST Route submitting a score
# - The route /submit_score accepts a JSON payload.
# - uses your convert_to_grade() function to get the grade.
# - If there's an invalid score, it returns a 400 error.
# - Otherwise, it adds the result (name, score, grade) to the in-memory list.
# - Then it returns the result as JSON.

# WHAT
# This FastAPI app takes in student test scores through an API, converts the scores to letter grades, stores the results, and provides a way to view all the submitted student grades.

# The code builds a basic backend API for a student grading platform

# Doing only two main things
# 1. First it acccepts student scores and converts by sending a students  name test score from 0.0 to 1.0
# API validates the input
# - converts the score to a grade (abcd etc)
# - Then returns a JSON response with name,score, and grade
# Secondly it lets me view all submitted results
# - using second endpoint /results
# - allowing me to call it anytime to see a list of all students, their scores and grades
# Summary 
# The API is built using FastAPI 
# It uses Pydantic for input validation (ScoreInput)
# The score is stored in a list (acting like a temporary database)
# There's error handling for invalid scores (e.g., scores over 1.0)

# Improve
# 🧾 Store data in MongoDB instead of memory
# 🛡️ Add JWT authentication so only teachers can see all scores

