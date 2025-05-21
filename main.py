"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Case Study: Building Calculator Software in Python
    🔹 BasicCalculator()     - Basic arithmetic operations
    🔹 FinancialCalculator() - Inherits from BasicCalculator + Method for financial calculation
    🔹 MortgageCalculator()  - Inherits from FinancialCalculator
    I also learned about types of inheritance.
# ----------------------------------------------------------------------------------------------------------------------
🧩 The Project structure:
    📁 my-apps                              ← This is the folder I'll turn into a GitHub repo
        ├── myCalculators/
        │   ├── static/
        │   │   ├── favicon.ico
        │   │   └── styles.css              ← My custom CSS
        │   ├── templates/
        │   │   ├── home.html               ← Welcome page
        │   │   └── mortgage.html
        │   ├── __init__.py
        │   ├── basic_calculator.py
        │   ├── financial_calculator.py
        │   ├── mortgage_calculator.py
        │   ├── app.py
        │   └── main.py                     ← We are here!
        ├── requirements.txt
        ├── .gitignore                      ← (optional, but recommended)
        ├── LICENSE
        └── README.md                       ← (optional, to explain the project)

    When trying to run main.py from inside the myCalculators/ folder directly like this:
        -bash--------------------------------------------------------------------------------
        | cd my-apps\myCalculators                                                          |
        | python main.py                                                                    |
        -------------------------------------------------------------------------------------
    This causes Python to treat myCalculators as just a folder, not as a module package
    — so the import from myCalculators.financial_calculator import FinancialCalculator fails,
    because from the perspective of Python, there is no parent folder to look for myCalculators.

Solution 1: Run from the parent directory
    Go one level above myCalculators and run:
        -bash--------------------------------------------------------------------------------
        | cd ..                 # Go to the parent directory of myCalculators               |
        | python -m myCalculators.main                                                      |
        -------------------------------------------------------------------------------------
    Explanation:
    🔹 -m myCalculators.main tells Python: “run this as a module from the package”
    🔹 Now, Python will recognize myCalculators as a package

Solution 2: Modify sys.path inside main.py (quick hack) ⇐ I use this method to fix the problem.
    Add this at the top of main.py:
        -python------------------------------------------------------------------------------
        | import sys                                                                        |
        | import os                                                                         |
        | sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))   |
        -------------------------------------------------------------------------------------
    Then I can run main.py directly:
        -bash--------------------------------------------------------------------------------
        | cd my-apps\myCalculators                                                          |
        | python main.py                                                                    |
        -------------------------------------------------------------------------------------
    But this is more of a workaround and not ideal for production code.

Solution 3: Restructure for Scripts (alternative)
    Move main.py outside the package folder:
    📁 my-apps
        ├── myCalculators/
        │   ├── static/
        │   │   ├── favicon.ico
        │   │   └── styles.css
        │   ├── templates/
        │   │   ├── home.html
        │   │   └── mortgage.html
        │   ├── __init__.py
        │   ├── basic_calculator.py
        │   ├── financial_calculator.py
        │   ├── mortgage_calculator.py
        │   └── app.py
        ├── main.py                         ← Move file main.py here!
        ├── requirements.txt
        ├── .gitignore
        ├── LICENSE
        └── README.md
    Then in main.py do (use Absolute import):
        -python------------------------------------------------------------------------------
        | from myCalculators.financial_calculator import FinancialCalculator               |
        | from myCalculators.mortgage_calculator import MortgageCalculator                 |
        -------------------------------------------------------------------------------------
    Run it from the root:
        -bash--------------------------------------------------------------------------------
        | python main.py                                                                    |
        -------------------------------------------------------------------------------------

Summary:
    -----------------------------------------------------------------------------------------
    | Solution  | Method                            | When to Use                           |
    -----------------------------------------------------------------------------------------
    |     1     | python -m myCalculators.main      | Best for packages                     |
    |     2     | Add sys.path.append(...)          | Quick and dirty script testing        |
    |     3     | Move main.py outside              | Clean separation of code & entry      |
    -----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
🎯 Relative import VS Absolute import:
    - When you run main.py, it runs in the context of the myCalculators package.
    - So, any file inside the same package should use relative imports (. or ..) to access siblings.
    
    How to run it:
    Since this is a package, make sure you run the entry point from outside the package like this:
        -bash--------------------------------------------------------------------------------
        | cd path/to/parent/of/myCalculators                                                |
        | python -m myCalculators.main                                                      |
        -------------------------------------------------------------------------------------

🔥 Don't run mortgage_calculator.py directly.
    Instead, always run main.py as the module entry point (python -m myCalculators.main), which allows relative imports inside your package to work correctly.
    (Later on, I've tried Command-Line Interface (CLI) Tool for mortgage_calculator.py which need to run the file directly.)

Summary:
    -------------------------------------------------------------------------------------------------------------------------
    | What You Want                                     | How to Do It                                                      |
    -------------------------------------------------------------------------------------------------------------------------
    | Import between files inside same folder/package   | Use relative imports like from .file import Class                 |
    | Run the app                                       | Run via python -m myCalculators.main from the parent directory   |
    | Avoid sys.path hacking                            | Yes, when using proper package structure                          |
    -------------------------------------------------------------------------------------------------------------------------
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the financial_calculator / mortgage_calculator module in the myCalculators package, using Absolute import.
from myCalculators.financial_calculator import FinancialCalculator
from myCalculators.mortgage_calculator import MortgageCalculator

# Example run : financial_calculator module
financial = FinancialCalculator()
monthly_interest = financial.monthly_interest(0.06)
print("Monthly Interest:", monthly_interest)

# Example run : mortgage_calculator module
# -EX1-----------------------------------------------------------
# | Loan Amount:          300,000                               |
# | Annual Interest Rate: 5%                                    |
# | Loan Term:            30 years                              |
# |                                                             |
# | Monthly Payment     ≈ $1,610.46                             |
# | Total Payment       = $1,610.46 × 360 months = $579,765.60  |
# | Total Interest      = $579,765.60 − $300,000 = $279,765.60  |
# ---------------------------------------------------------------
mortgage_ex1 = MortgageCalculator(loan_amount=300000, annual_interest_rate=0.05, years=30)
print("\n[✨Example✨ 1] -----------------------------------------------------------------")
print("\t", f"Monthly Payment: ${mortgage_ex1.calculate_monthly_payment():.2f}")    # $1610.46
print("\t", f"Total Payment:   ${mortgage_ex1.total_payment():.2f}")                # $579765.60
print("\t", f"Total Interest:  ${mortgage_ex1.total_interest():.2f}")               # $279765.60
mortgage_ex1.export_to_excel()

# -EX2-----------------------------------------------------------
# | Loan Amount:          100,000                               |
# | Annual Interest Rate: 3.5%                                  |
# | Loan Term:            15 years                              |
# |                                                             |
# | Monthly Payment     ≈ $714.88                               |
# | Total Payment       = $714.88 × 180 months = $128,678.40    |
# | Total Interest      = $128,678.40 − $100,000 = $28,678.40   |
# ---------------------------------------------------------------
mortgage_ex2 = MortgageCalculator(loan_amount=100000, annual_interest_rate=0.035, years=15)
print("\n[✨Example✨ 2] -----------------------------------------------------------------")
print("\t", f"Monthly Payment: ${mortgage_ex2.calculate_monthly_payment():.2f}")    # $714.88
print("\t", f"Total Payment:   ${mortgage_ex2.total_payment():.2f}")                # $128678.40
print("\t", f"Total Interest:  ${mortgage_ex2.total_interest():.2f}")               # $28678.40
mortgage_ex2.export_to_excel()