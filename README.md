# myCalculators
About My Calculators App with a simple Python script to calculate monthly loan payments, interest and installment.

🧠 Case Study: Building Mortgage Calculator Application in Python<br/>

🧩 The Project structure:  (Latest update)<br/>
    📁 my-apps                              ← This is the folder I'll turn into a GitHub repo<br/>
        └── myCalculators/<br/>
            ├── static/<br/>
            │   ├── favicon.ico<br/>
            │   └── styles.css              ← My custom CSS<br/>
            ├── templates/<br/>
            │   ├── home.html               ← Welcome page<br/>
            │   └── mortgage.html<br/>
            ├── __init__.py<br/>
            ├── basic_calculator.py<br/>
            ├── financial_calculator.py<br/>
            ├── mortgage_calculator.py<br/>
            ├── app.py                      ← Main Flask application file<br/>
            ├── main.py<br/>
            ├── .gitignore                  ← (optional, but recommended)<br/>
            ├── LICENSE<br/>
            ├── README.md                   ← (optional, to explain the project)<br/>
            └── requirements.txt<br/>

This project helped me learn how to build and structure a Python application. The app consists of multiple calculator classes:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 BasicCalculator()     - Handles basic arithmetic operations<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 FinancialCalculator() - Inherits from BasicCalculator, and adds financial calculation features<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 MortgageCalculator()  - Inherits from FinancialCalculator, performs mortgage-related calculations<br/>
<br/>
🚀 Deployment<br/>
I created this project as a learning exercise and deployed it online.<br/>

To publish the app on GitHub:

    cd path/to/myCalculators
    git init
    git remote add origin https://github.com/yourusername/myCalculators.git
    git add .
    git commit -m "Initial commit for myCalculators Flask app"
    git push -u origin main

Deployed it to online platforms:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 Railway.app – Deployment failed due to the platform's trial limitations.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 Render.com – Successfully deployed ⇒ https://mycalculators.onrender.com<br/>

    Render.com : Create a free account.
    New ➝ Web Service ➝ Connect GitHub repo.
    Set build and start command:
        Build Command: pip install -r requirements.txt
        Start Command: python app.py
    Set environment to Python 3.

<hr>

📚 What I’ve Learned<br/>
I start learning Python on my own with the goal of returning to an IT career. I used online resources, e-learning courses, tutorials, and study plans, while sharpening my problem solving skills through LeetCode challenges.<br/>
<br/>
Key lessons from this project:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 Understanding inheritance in Python, and using 'super()' to avoid code duplication.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 Handling financial accuracy and avoid rounding issues from redundant calculations.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 Export results to Excel using 'pandas'.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 Build a Flask Web UI, simple web interface with input fields.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 Creating a CLI (Command-Line Interface) tool using 'argparse'.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;🔹 Deploying a Flask Web App locally and on hosting platforms (e.g., Render.com).<br/>
<br/>
This project represents my journey in rebuilding my IT skills, starting from the fundamentals and moving into applications.
