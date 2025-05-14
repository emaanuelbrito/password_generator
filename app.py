from flask import Flask, render_template, request
import logging

from helpers import generate_password

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    if request.method == "POST":
        logging.debug(f"Form data: {request.form}")
        try:
            length = int(request.form["passwordLength"])
            include_numbers = "include_numbers" in request.form
            include_uppercase = "include_uppercase" in request.form
            include_lowercase = "include_lowercase" in request.form
            include_special = "include_special" in request.form

            # Generate the password
            password = generate_password(length, include_numbers, include_uppercase, include_lowercase, include_special)

            return render_template("index.html", password=password)
        except Exception as e:
            logging.error(f"Error processing form data: {e}")
            return "Bad Request", 400
