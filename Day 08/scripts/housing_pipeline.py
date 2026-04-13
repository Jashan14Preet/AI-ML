from sklearn.datasets import fetch_california_housing
import pandas as pd
# 1. Load the dataset
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseVal'] = data.target # This is our 'y' (Price in$100,000s)
print("Dataset Overview:")
print(df.head())
print("\nBasic Statistics:")
print(df.describe())


