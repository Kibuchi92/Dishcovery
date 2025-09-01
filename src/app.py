import mysql.connector
from flask import Flask, jsonify, render_template, request, json
from dotenv import load_dotenv
from openai import OpenAI
import os
import re

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

app = Flask(__name__)

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=OPENROUTER_API_KEY)


def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/landing")
def landing():
    return """
    <div id='landing'>
    
        <h1>Welcome to Dishcovery</h1>
        <h4>Discover dishes with your ingredients</h4>
        <p>Dishcovery helps you turn everyday ingredients into delicious meals. You simply enter what you have in your kitchen, and we’ll suggest quick, simple recipes tailored to your ingredients, no extra shopping needed.</p>
        <button hx-get='/recipe-prompt' hx-target='#main-content' hx-swap='innerHTML' id="start-btn" class="btn">
            Get Some Recipes
        </button>
        
    </div>
    """


@app.route("/recipe-prompt")
def recipe_prompt():
    return """
    <div id='recipe-section'>
    <h1>✨ Recipe Finder</h1>
        <form hx-post='/prompt' hx-target='#response' hx-swap='innerHTML'>
            <label for='prompt'>Enter your ingredients (comma-separated):</label><br>
            <input type='text' id='prompt' name='prompt' required><br>
            <input type='submit' value='Get Recipes' id="start-btn" class="btn" hx-on:click="document.getElementById('cooking-message').classList.remove('hidden');">
        </form>
        <div id='response'>
        <p id="cooking-message" class="cooking hidden">Cooking up some magic...</p>
        </div>
    </div>
    """


@app.route("/prompt", methods=["POST"])
def ai():
    user_input = request.form.get("prompt")
    user_input = (
        "Suggest 3 simple recipes with these ingredients: "
        + user_input
        + ". Format the response as HTML in the following the following format: "
        "<h3>Try these out😋</h3> <h4>title</h4> <ul><li>ingredient1</li><li>ingredient2</li></ul> <p>instructions<p>"
    )

    if not user_input:
        return jsonify({"error": "No prompt provided"}), 400

    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
        messages=[{"role": "user", "content": user_input}],
    )

    response_text = completion.choices[0].message.content
    return response_text


if __name__ == "__main__":
    app.run(debug=True)
