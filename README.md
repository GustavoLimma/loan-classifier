# 🏦 Project: Loan Approval Classification

This project aims to develop a machine learning model to predict loan approval based on historical data.

---

## ✨ Overview

Using the dataset [loan.csv](https://github.com/josenalde/machinelearning/blob/main/src/dataset/loan.csv) – created by **Professor Josenalde Oliveira** ([GitHub profile](https://github.com/josenalde)) – the model will perform **binary classification** to predict loan approval based on features like income, marital status, number of dependents, and more.

---

## 🚀 Technologies Used

- **Main Language:** Python
- **Libraries:**
  - pandas, numpy, scikit-learn
  - matplotlib and seaborn (for visualization)
- **Web Framework:**
  - Flask (for the web application)
- **Tools:**
  - Jupyter Notebook (for initial development and experiments)

---

## 🎨 Project Steps

1. **Preprocessing:**
   - Remove irrelevant columns: `loan_id`, `coapplicantincome`, `loan_amount_term`, `credit_history`, `property_area`.
   - Fill missing values:
     - `dependents`, `self_employed`, `married`, `gender` – fill with the column's mode.
   - Convert the `dependents` feature to numeric (convert "3+" to 3).
   - Encode categorical features using **LabelEncoder** or **OneHotEncoder**, depending on the case.
   - Standardize numerical features using `StandardScaler`.

2. **Modeling:**
   - Create 5 pipelines with:
     - Grid Search and cross-validation.
     - 5 different classification algorithms.
     - Evaluation with `classification_report` and AUC of the ROC curve.
   - Select the best-performing final model.
   - Save the final pipeline containing only the `best_estimator_` (for use in production).

3. **Web Application:**
   - Create a form for the user to input data:
     - Gender, dependents, marital status, self-employed status, income, education, and loan amount.
   - Display the loan analysis result: **Loan approved?** (yes/no).
   - If the model supports `predict_proba()`, also display the **probability of the majority class**.

---

## 🔧 How to Run the Project

**Requirements:**
- Python 3.8+
- Virtual environment (optional, but recommended)

**Steps:**

```bash
# Clone the repository
git clone https://github.com/your-username/repository-name.git

# Navigate to the project folder
cd repository-name

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # on Linux/macOS
venv\Scripts\activate     # on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app (Flask)
python app.py  # or equivalent command
````

---

## 🚧 Project Status and Contributors

> **In development** – we are finalizing the pipeline, testing, and the web interface.

**Contributors:**

* [@GustavoLimma](https://github.com/GustavoLimma) – lead developer

---

## 📜 License

This project is licensed under the [MIT](LICENSE) license.

---

## 📬 Contact

If you have suggestions, questions, or want to collaborate, reach out:

* [gustavo69gls@email.com](gustavo69gls@email.com)

---

✨ **Thank you for checking out the project!** ✨
