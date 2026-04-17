# Day 11 Report: Ensemble Learning & Model Stability

---

## Technical Summary

Today, I explored how to improve model performance and stability using **ensemble learning** with a Random Forest model.

- Implemented a Random Forest model using multiple decision trees  
- Learned how combining models reduces variance using Bagging  
- Compared performance with previous single-model approaches  
- Generated a **Feature Importance plot** to identify key predictors  
- Evaluated model performance using the **R² score**  

---

## Conceptual Reflection

As the number of trees in a Random Forest increases, the model becomes more stable and accurate initially because averaging multiple trees reduces variance. However, this improvement does not continue indefinitely.

After a certain point, adding more trees results in very small gains in accuracy while significantly increasing training time. This demonstrates diminishing returns, where higher computational cost does not lead to meaningful performance improvement.

This highlights the importance of balancing model complexity and efficiency rather than simply increasing the number of trees.

---

## Key Takeaway

Combining multiple models leads to better stability and performance, but optimal results come from balancing accuracy with computational efficiency rather than maximizing complexity.