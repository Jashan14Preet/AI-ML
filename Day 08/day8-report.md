# Day 8 Report: The Regression Modeling Protocol

---

## Technical Summary

Today, I worked on building a complete **Machine Learning Regression Pipeline** using the California Housing dataset.

I successfully:

- Fetched and loaded the dataset using `fetch_california_housing()`
- Converted it into a structured **Pandas DataFrame**
- Split the data into **training and testing sets (80:20)**
- Applied **StandardScaler** to ensure all features are on the same scale
- Trained a **Linear Regression model**
- Evaluated the model using:
  - **Mean Absolute Error (MAE)** in actual dollar value
  - **R² Score** to measure model performance
- Generated a **Residual Plot** to visually analyze prediction errors

The most important concept I understood today was **Residual Analysis**, which helps identify whether a linear model is suitable for the dataset.

---

## The "Bug" Log

### Error 1: None appearing before evaluation

**Error Message:**  
`None` printed before evaluation results

**Cause:**  
An unnecessary `None` statement was present in the code.

**Fix Applied:**

Removed the extra `None` line, which resolved the issue.

---

## Conceptual Reflection

### What does a patterned residual plot indicate?

If the residual plot shows a clear pattern such as a U-shape instead of random scattered points, it indicates that the relationship between the input features and the target variable is non-linear. 

This means the Linear Regression model is not able to properly capture the underlying pattern in the data, since it assumes a straight-line relationship. 

As a result, the model systematically overestimates and underestimates values in different regions, leading to visible patterns in the residuals. This suggests that a more suitable approach would be to use non-linear models or introduce polynomial features to better fit the data.
