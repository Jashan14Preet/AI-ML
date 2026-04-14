# Day 9 Report: The Hyperparameter Optimization Protocol

---

## Technical Summary

Today, I focused on improving machine learning model performance through **Hyperparameter Tuning** using Grid Search and Cross-Validation.

I successfully:

- Reused the **California Housing dataset** from the previous task
- Applied **StandardScaler** to normalize feature values
- Implemented a **Ridge Regression model** for regularized learning
- Defined a **hyperparameter grid** to test multiple values of `alpha`
- Used **GridSearchCV** to automatically find the best parameter combination
- Applied **5-fold Cross-Validation (cv=5)** to ensure reliable and unbiased results
- Identified the **optimal alpha value** for the Ridge model
- Evaluated the model using **R² Score**
- Compared the performance of:
  - A **default Ridge model**
  - An **optimized Ridge model using GridSearchCV**

The key concept I understood today was **Cross-Validation**, which ensures that model performance is consistent and not dependent on a single random train-test split.

---

## The "Bug" Log

### Error 1: Inconsistent Results Across Runs

**Error Message:**  
Different "Best Alpha" and R² scores were observed every time the script was executed.

**Cause:**  
The `train_test_split()` function was used without setting a `random_state`, leading to different data splits on each run.

**Fix Applied:**

Added a fixed random state for reproducibility:


train_test_split(X, y, test_size=0.2, random_state=42)

---

## Conceptual Reflection

**Why is it better to use a wide range of values first in Grid Search?**

Using a wide range of values such as [0.1, 1, 10, 100] allows us to explore the overall behavior of the model across different scales of the hyperparameter. It helps identify the general region where the model performs best.

If we start with small increments like [1.1, 1.2, 1.3], we risk missing better values that lie far outside this narrow range. A wide search prevents getting stuck in a local optimum and provides a broader understanding of how the hyperparameter affects model performance.

Once the optimal range is identified, we can perform a more fine-grained search within that region for further improvement.
