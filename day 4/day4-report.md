# Day 4 Report: The Pre-processing Protocol

---

## Technical Summary

Today, I worked on **Data Preprocessing**, which is a crucial step in building Machine Learning models.

I learned and implemented:

- **Data Cleaning using Pandas**
  - Handling missing values using **Data Imputation**
- **Feature Scaling using Scikit-learn**
  - Used **MinMaxScaler** to normalize data between 0 and 1
- **Data Visualization**
  - Used **Seaborn and Matplotlib** to generate correlation heatmaps

The most important concept I mastered today was **Data Imputation**, where missing values are replaced using statistical methods instead of removing data.

---

## The "Bug" Log

### Error 1: FileNotFoundError

**Error Message:**  
FileNotFoundError: No such file or directory: 'data.csv'

**Cause:**  
The script was trying to read `data.csv` from the current working directory, but the file was actually located inside a nested folder (`Day4/datasets/`).

**Fix Applied:**

df = pd.read_csv(r"Day4\datasets\data.csv")


### Error 2: SyntaxWarning (invalid escape sequence '\d')

**Cause:**  
The backslash (`\`) in the file path was interpreted as an escape sequence.

**Fix Applied:**

df = pd.read_csv(r"Day4\datasets\data.csv")


### Error 3: KeyError: 'Age'

**Cause:**  
The column name contained an extra space (e.g., ' Age' instead of 'Age'), so Python could not match it exactly.

**Fix Applied:**

Removed leading/trailing spaces and resolved the issue.

---

## Conceptual Reflection

### Why is it better to fill a missing age with the mean rather than just putting 0?
Replacing the age values that were missing with a value of 0 is inaccurate because there will never be any age of zero in this particular dataset. This will make data inaccurate and could have negative consequences for the learning process of the model.

Mean imputation ensures that we replace the missing values with an estimate of an actual number based on available numbers.

Hence, mean imputation is more appropriate than simply putting 0.