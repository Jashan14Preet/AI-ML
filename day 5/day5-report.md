Technical Summary

Today, I worked on Linear Regression, building a model to predict exam scores based on hours studied.

I learned and implemented:

Train/Test Split
Used scikit-learn’s train_test_split to separate training and testing data (80/20)
Model Training
Implemented LinearRegression to learn the relationship between Hours and Score
Prediction
Generated predictions for unseen data (e.g., 11 hours)
Evaluation
Calculated Mean Squared Error (MSE) and R² Score to measure model performance
Visualization
Used Matplotlib to plot actual points and the regression line

The most important concept I mastered today was how to evaluate a model’s performance using metrics and visualizations.

The "Bug" Log
Warning: X does not have valid feature names

Message:

UserWarning: X does not have valid feature names

Cause:
Predicted using a plain list ([[11]]) instead of a DataFrame with column names.

Fix Applied:

new_data = pd.DataFrame([[11]], columns=['Hours'])
prediction = model.predict(new_data)
Conceptual Reflection
What happens if we train the model on only 2 rows instead of 8?
The model may overfit the 2 points and fail to learn the real trend.
Predictions become unreliable and can be misleading.
More data allows the model to generalize better and make accurate predictions.

Lesson: Linear Regression requires enough data points to capture the underlying relationship effectively.