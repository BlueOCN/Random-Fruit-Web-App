# Import Flask to enable creating the REST API web service
from flask import Flask  

# Import random library to generate random fruit selections
import random   

# Create a Flask application instance called app
app = Flask(__name__)

# List of fruits that will be used for random selection
fruits = ["apple", "banana", "orange"]  

# Route decorator to tell Flask what URL path triggers this function
@app.route("/fruit")

# Function that will execute for the /fruit route 
def get_fruit():

    # Select random fruit from list of fruits
    fruit = random.choice(fruits)  

    # Return the randomly selected fruit text back to the client
    return fruit 

# Check if running as standalone script  
if __name__ == "__main__":

    # Launch built-in Flask development web server on localhost
    app.run(host="127.0.0.1", port=8080, debug=True)