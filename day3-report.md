# Day 3 Report

## Setup Status
All required tools are successfully installed and operational.  
- VS Code is configured for Python development  
- Python is installed and running correctly  
- NumPy and Pandas libraries are installed  
- Jupyter Notebook is working properly  
- Git is initialized and connected to GitHub  

---

## Task Inventory
- Created project folder structure (datasets, scripts, notebooks)
- Implemented Python fundamentals in `basics.py`
- Used loops and functions for data processing
- Performed array operations using NumPy
- Reshaped data into a 2×2 matrix
- Applied vectorization to scale data
- Created `data.csv` dataset
- Loaded and analyzed dataset using Pandas
- Generated statistical summary using `describe()`
- Calculated average score using column operations
- Created Jupyter Notebook and documented vectorization concept
- Organized files and prepared project for GitHub submission

---

## Debugging Log

**1. Error: IndentationError in basics.py**  
- Cause: Incorrect indentation inside the `for` loop  
- Solution: Fixed indentation to properly align the print statement inside the loop  
- Cause: Incorrect indentation inside the `analyse_numbers(numbers)` function 
- Solution: Fixed indentation to properly align the min_val ,max_val ,avg_val and return statement

**2. Error: FileNotFoundError in Pandas**  
- Cause: Incorrect file path while loading CSV file  
- Solution: Updated path to correct location (`AI-ML\datasets\data.csv`) using relative path   

---

## Key Insights

The biggest insight for me today was understanding **Vectorization**. I was astonised to learn that instead of using loops to process each data element, NumPy allows operations to be applied to entire datasets at once, making the computations faster and more efficient.

I also understood how Python, NumPy, and Pandas work together as a complete data processing pipeline—Python being the **Logic Engine** handles logic, NumPy being the **Mathematical Powerhouse**performs fast numerical operations , and Pandas being the **The Data Librarian** simplifies data analysis.

---

## Conclusion

This task helped me transition from basic coding to handling and analyzing data efficiently. I gained practical experience in structuring data workflows and documenting my work in a professional manner.