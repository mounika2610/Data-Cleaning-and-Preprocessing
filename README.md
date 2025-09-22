# Data Cleaning – Task 1

**Dataset:** Netflix Movies & TV Shows (Kaggle)  
**Original file:** `netflix_titles.csv`  
**Cleaned file:** `netflix_cleaned.csv`  

---

## 🧰 Tools & Environment

- Python 3.x  
- Pandas  
- NumPy  
- Jupyter Notebook  

---

## 🔍 Data Cleaning Steps

1. **Load Data**  
   Read the original dataset with Pandas.

2. **Inspect Basic Info**  
   Checked data types, summary statistics, missing values, duplicates.

3. **Handle Missing Values**  
   - Dropped rows where the **title** was missing (title is essential).  
   - Filled missing values in **director** and **country** with `"Unknown"`.

4. **Remove Duplicates**  
   Removed full duplicate records to avoid redundancy.

5. **Standardize Text Columns**  
   - Trimmed whitespace from string fields.  
   - Converted `type` column to lowercase.  
   - Replaced variants of “United States” with `"USA"` in the `country` column.

6. **Convert Date Formats**  
   Transformed `date_added` to a datetime format (error coercion for invalid/missing values).

7. **Rename Columns**  
   Converted column names to **snake_case** (lowercase + underscores) and removed leading/trailing spaces.

8. **Check & Fix Data Types**  
   Ensured that numerical columns are of numeric type, date columns are datetime, etc.

---

## ✅ Outputs

- `netflix_cleaned.csv` — the cleaned version of the dataset  
- `task1_data_cleaning.ipynb` — notebook with full code (cleaning steps + comments)

---

## 📝 How to Run

1. Clone or download this repository.  
2. Ensure `netflix_titles.csv` is in the same folder as the notebook.  
3. Install dependencies if needed:  
   ```bash
   pip install pandas numpy
   ```  
4. Open `task1_data_cleaning.ipynb` in Jupyter.  
5. Run all cells in sequence.  
6. The cleaned dataset will be saved as `netflix_cleaned.csv`.

---

## 🧐 Notes & Observations

- Some records had missing **date_added**, causing conversion issues — those are marked as `NaT` via `pd.to_datetime(..., errors='coerce')`.  
- There are entries with missing or ambiguous `director` or `country`, which are set to `"Unknown"` to avoid dropping too much data.  
- Outlier detection was not deeply addressed here — focus was more on structural cleanliness. You may extend in future.

---

## 📂 Repository Structure

```
.
├── netflix_titles.csv
├── netflix_cleaned.csv
├── task1_data_cleaning.ipynb
└── README.md
```
