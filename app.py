import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template, request, redirect, url_for
from threading import Lock
from decimal import Decimal, getcontext, ROUND_HALF_EVEN
from mortgage_calculator import MortgageCalculator

# Set precision and rounding for financial accuracy
getcontext().prec = 28
getcontext().rounding = ROUND_HALF_EVEN

# === 1. Configuration ===
# app = Flask(__name__)
app = Flask(__name__, template_folder="templates", static_folder="static")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "log.txt")

HOME_FORM = "home.html"
MORTGAGE_FORM = "mortgage.html"


# Route 1: Home --------------------------------------------------------------------------------------------------------
@app.route("/")
def home():
    # return "Welcome to Calculator App!"
    return render_template(HOME_FORM)


# Route 2: Mortgage Calculator -----------------------------------------------------------------------------------------
@app.route("/mortgage", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            loan_amount = Decimal(request.form["loan_amount"])
            annual_interest_rate = Decimal(request.form["annual_interest_rate"])
            years = Decimal(request.form["years"])

            mortgage = MortgageCalculator(loan_amount, annual_interest_rate, years)
            monthly_payment = mortgage.calculate_monthly_payment()
            total_payment = monthly_payment * mortgage.num_months
            total_interest = total_payment - loan_amount

            result = {
                "monthly_payment": monthly_payment,
                "total_payment": total_payment,
                "total_interest": total_interest
            }

            return render_template(MORTGAGE_FORM, result=result)

        except ValueError:
            return render_template(MORTGAGE_FORM, result=None)

    return render_template(MORTGAGE_FORM, result=None)

"""
Setting debug=True tells Flask to:
    - Auto-reload on any file change (HTML, CSS, Python)
    - Show helpful error messages
"""
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
