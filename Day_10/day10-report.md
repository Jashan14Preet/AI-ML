# Day 10 Report: Non-Linear Models & Overfitting

---

##  Technical Summary

Today, I explored how to model **non-linear relationships** in data using two different approaches: **Polynomial Regression** and **Decision Tree Regression**.

- Learned how to transform linear models into **curvy models** using `PolynomialFeatures`
- Implemented a **DecisionTreeRegressor** to understand step-based predictions
- Visualized the difference between **smooth curves vs step-like functions**
- Explored the concept of **overfitting** by changing the `max_depth` of the decision tree
- Compared model performance using the **R² score**

---

##  The "Bug" Log

While plotting multiple Decision Tree models with different depths, all prediction lines appeared in the same color, making it impossible to distinguish between them.

To fix this, I assigned **different colors dynamically** using a list and mapped each depth to a unique color using the `zip()` function. This improved the visualization and made comparison clear.

---

##  Conceptual Reflection

A jittery model that perfectly fits every training point is a sign of overfitting, not true learning. It memorizes noise and small fluctuations instead of capturing the real pattern in the data. While it achieves very high accuracy on training data, it becomes unreliable for real-world use because new data will always differ.

In contrast, a smooth curvy model focuses on the overall relationship between input and output. By ignoring minor variations and noise, it generalizes better to unseen data and provides more reliable predictions.

This can be explained by the bias-variance tradeoff: very complex models have low bias but high variance, making them sensitive to small changes. Simpler models maintain a better balance, which is why a smooth model is more effective than a jittery one for future predictions.

---

##  Key Takeaway

Not all high-accuracy models are good models. A model that generalizes well on unseen data is more valuable than one that simply memorizes training data.