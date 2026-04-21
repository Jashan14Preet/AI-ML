import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'User1_Age': [21,25,30,22,27,24,28,26,23,29,31,20,22,27,35,33,26,28,24,30],
    'User2_Age': [23,26,29,24,28,25,27,29,22,30,32,21,23,26,34,32,25,27,23,31],
    'Interest_Similarity': [0.8,0.6,0.9,0.4,0.7,0.5,0.85,0.65,0.9,0.3,0.8,0.7,0.6,0.75,0.4,0.5,0.88,0.77,0.66,0.55],
    'Distance_km': [2,10,1,15,5,8,3,7,2,20,4,6,9,3,18,12,2,4,6,10],
    'Compatibility': [1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,1,1,0,0]
}

df = pd.DataFrame(data)

X = df.drop('Compatibility', axis=1)
y = df['Compatibility']

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_poly, y, test_size=0.3, random_state=42
)

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

print("\nModel Used:", model)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - User Compatibility")
plt.xlabel("Predicted")
plt.ylabel("Actual")


print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nFeature Importance:\n")

feature_names = poly.get_feature_names_out(X.columns)
importances = model.feature_importances_

feat_imp = pd.Series(importances, index=feature_names)
print(feat_imp.sort_values(ascending=False))

sample = [[22, 24, 0.85, 3]]

sample_poly = poly.transform(sample)
prediction = model.predict(sample_poly)

print("\nCustom Prediction:")
print("Compatible" if prediction[0] == 1 else "Not Compatible")

plt.show()
plt.close()