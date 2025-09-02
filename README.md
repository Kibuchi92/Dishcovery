# Dishcovery

Dishcovery is a recipe recommender web application built with **Flask** and integrated with the **OpenRouter API (OpenAI models)**. The app allows users to input ingredients and receive recipe suggestions dynamically. It uses MySQL for database storage and was deployed successfully on **PythonAnywhere**.

---

## Features

* Ingredient-based recipe recommendation
* Flask backend with API endpoints
* MySQL integration
* OpenRouter AI integration for generating recipes
* Deployment-ready with `gunicorn` and `requirements.txt`

---

## Tech Stack

* **Python 3.13**
* **Flask**
* **MySQL**
* **Gunicorn** (for production server)
* **OpenRouter API (OpenAI models)**
* **PythonAnywhere** (hosting)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/dishcovery.git
cd dishcovery
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```bash
OPENROUTER_API_KEY=your_api_key_here
DB_HOST=your_db_host
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
```

Or (for testing) hardcode your API key inside `app.py`:

```python
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key="sk-your_api_key")
```

### 5. Run locally

```bash
python src/app.py
```

---

## Deployment on PythonAnywhere

1. Zip the project folder (excluding `venv`).
2. Upload it to PythonAnywhere.
3. Create a virtual environment on PythonAnywhere and install requirements:

   ```bash
   mkvirtualenv recipe-env --python=python3.13
   pip install -r requirements.txt
   ```
4. Edit the WSGI file to point to your Flask app.
5. Set environment variables in **PythonAnywhere Web settings**.
6. Reload the web app.

Logs can be checked under:

```bash
/var/log/yourusername.pythonanywhere.com.error.log
/var/log/yourusername.pythonanywhere.com.server.log
```

---

## Appendix: Essential Prompts

Below is a curated list of **essential prompts** (under 100) that guided the project from initialization to deployment.

### Project Initialization & Setup

1. How do I deploy my flask app to vercel is it free?
2. What are the steps to deploy to render?
3. Is it possible to upload it directly without first pushing to github?
4. Do I first need to activate venv before I can install gunicorn?
5. After running this pip freeze > requirements.txt do I need to first push to github so that the requirements.txt is in the git repo?
6. Why are they asking me to add a card after I click deploy I thought it was the free tier?
7. It seems like heroku would be my best bet then.
8. I want a platform that does not initially require a credit card.
9. Is python anywhere free to use?
10. I found an app called pella.app.

### Project Structure & Code

11. How do I first create a zip for the recipe recommender folder?
12. Do I need to zip everything including the venv files?
13. Do they have a place to check logs or errors?
14. Shouldn’t I set the environment variables in a .env file?
15. Since its a dummy project can I just hard code it in the app.py?

### GitHub Integration

16. How do I log into a different github account on vs code?
17. How do I push this project to github?
18. I’ve successfully pushed to my github account and created a render account how do I now deploy to render?

### Debugging & Errors

19. Traceback error: ModuleNotFoundError: No module named 'mysql'.
20. Tail: cannot open 'identicalSawfish.pythonanywhere.com.error.log'.
21. Error running WSGI application: The api\_key client option must be set.

### PythonAnywhere Deployment

22. Ok I’ve created a PythonAnywhere account.
23. How do I check logs on PythonAnywhere?
24. How do I configure environment variables on PythonAnywhere?
25. Should I set environment variables in .env or in PythonAnywhere settings?
26. Where do I check for errors in my deployed app?
27. How do I reload the app after fixing errors?
28. How do I confirm the API key is being read?

### Progression Toward Success

29. Walkthrough on setting up virtualenv on PythonAnywhere.
30. How do I point WSGI to my app.py?
31. How do I run migrations for MySQL?
32. How do I connect Flask to the MySQL database in production?
33. Do I need to add gunicorn for PythonAnywhere?
34. How to zip and upload without venv?
35. How to test the Flask app before deploying?
36. Where to update the web tab configuration in PythonAnywhere?
37. How do I check if my Flask routes are working?
38. How do I restart the server after updating app.py?
39. Should I remove debug=True in production?
40. How to verify database connectivity on PythonAnywhere?

---

## License

This project is licensed under the MIT License.

