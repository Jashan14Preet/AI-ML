### **Day 6 Report: Logistic Regression & Classification Metrics**

---

### Technical Summary

Today, I worked with **Logistic Regression**, a fundamental classification algorithm used to predict binary outcomes (0 or 1). I learned how the **Sigmoid function** converts numerical outputs into probabilities between 0 and 1.

Additionally, I explored model evaluation techniques such as the **Confusion Matrix** and **Classification Report**, which include metrics like Precision, Recall, and F1-score. These tools help in understanding model performance beyond simple accuracy.

---

### The "Bug" Log

**Error Faced:**
`NameError: name 'importance' is not defined`

**Cause:**
The variable `importance` was mistakenly written inside a comment, so it was never actually defined in the code.

**Fix:**
I separated the assignment from the comment and correctly defined the variable:

```python
importance = clf.coef_[0]
```

**Learning:**
Even small syntax mistakes like commenting out important code can lead to errors. Careful code structure and debugging are essential.

---

### Conceptual Reflection

**Question:** In a cancer detection AI, which is more dangerous: a False Positive or a False Negative? Why?

**Answer:**
A **False Negative** is more dangerous because it predicts that a patient does not have cancer when they actually do. This can delay diagnosis and treatment, allowing the disease to progress and potentially become life-threatening.

In contrast, a **False Positive** may cause stress and lead to additional testing, but it can usually be corrected. Therefore, False Negatives pose a much greater risk to patient safety.

---

### Conclusion

This session helped me understand the shift from regression to classification and the importance of evaluating models using detailed metrics. I also learned how to interpret model predictions and identify errors effectively.
