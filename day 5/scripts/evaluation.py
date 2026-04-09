# -------------------------------
# IMPORT LIBRARIES
# -------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------------
# 1. CREATE DATASET
# -------------------------------
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score': [35, 40, 55, 60, 68, 72, 81, 88, 92, 95]
}

df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Hours']]
y = df['Score']

# -------------------------------
# 2. TRAIN / TEST SPLIT
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training items: {len(X_train)} | Testing items: {len(X_test)}")

# -------------------------------
# 3. TRAIN MODEL
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# 4. PREDICT
# -------------------------------
predictions = model.predict(X_test)

print("\nPredictions:", predictions)
print("Actual:", y_test.values)

# -------------------------------
# 5. EVALUATION
# -------------------------------
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"\nMean Squared Error: {mse:.2f}")
print(f"R-Squared Score: {r2:.2f}")

# -------------------------------
# 6. NEW PREDICTION (FIXED WARNING)
# -------------------------------
new_data = pd.DataFrame([[11]], columns=['Hours'])
new_prediction = model.predict(new_data)

print(f"\nPrediction for 11 hours: {new_prediction[0]:.2f}")

# -------------------------------
# 7. VISUALIZATION
# -------------------------------
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')

plt.title("Hours vs Score: AI Prediction Line")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.legend()

plt.show()