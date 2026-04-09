from sklearn.model_selection import train_test_split
import pandas as pd

# Sample Dataset: Hours Studied vs Exam Score
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score': [35, 40, 55, 60, 68, 72, 81, 88, 92, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Hours']]   # 2D (important for sklearn)
y = df['Score']     # 1D

# Split into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Output
print(f"Training items: {len(X_train)} | Testing items: {len(X_test)}")

print("\nX_train:\n", X_train)
print("\nX_test:\n", X_test)
print("\ny_train:\n", y_train)
print("\ny_test:\n", y_test)