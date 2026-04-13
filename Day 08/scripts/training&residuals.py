from sklearn.metrics import mean_absolute_error, r2_score
# 3. Train
model = LinearRegression()
model.fit(X_train_scaled, y_train)
# 4. Predict
predictions = model.predict(X_test_scaled)
# 5. Evaluate

None
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"Mean Absolute Error: ${mae * 100000:.2f}")
print(f"R-Squared Score: {r2:.2f}")