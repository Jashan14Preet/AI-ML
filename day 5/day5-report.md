# Day 5 Report: Linear Regression & First Prediction

---

## Setup Status

My development environment is fully operational.

* Python is installed and running correctly
* Jupyter Notebook is working smoothly
* Required libraries like `pandas`, `scikit-learn`, and `matplotlib` are installed
* VS Code / Notebook environment is properly configured

---

## Task Inventory

* Created a sample dataset (Hours vs Score) using pandas
* Separated features (`X`) and target (`y`)
* Performed train-test split (80% training, 20% testing)
* Initialized and trained the Linear Regression model using `model.fit()`
* Generated predictions on test data using `model.predict()`
* Evaluated model performance using Mean Squared Error (MSE) and R² score
* Predicted output for a new unseen value (11 hours)
* Visualized the dataset and regression line using matplotlib
* Wrote reflection on impact of training with less data

---

## Debugging Log

###  Bug 1: NameError - 'X' is not defined

**Error:**
NameError: name 'X' is not defined

**Cause:**
The plotting cell was executed before defining `X` and `y`.

**Solution:**
Re-ran the cell where `X` and `y` were defined before executing the plotting code. Also ensured to run all cells in sequence using "Run All".

---

### Bug 2: Model not fitted error (predict before fit)

**Error:**
Model was used for prediction before calling `model.fit()`

**Cause:**
Attempted to use `model.predict()` without training the model first.

**Solution:**
Ensured that `model.fit(X_train, y_train)` is executed before making predictions.

---

## Key Insights

* Splitting data into training and testing sets is essential to evaluate real model performance
* Linear Regression works by finding the best-fit line that represents the relationship between input and output
* More training data improves model accuracy and generalization
* Small datasets can lead to poor predictions and unreliable models
* Visualization helps in clearly understanding how well the model fits the data
* Evaluation metrics like R² score and MSE are important to judge model performance


