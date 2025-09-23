# 📺 Netflix Data Cleaning Project

## 🎯 Objective
This project focuses on cleaning and preprocessing the [Netflix Movies and TV Shows dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows) using Python and Pandas. The goal is to transform raw, inconsistent data into a clean, structured format suitable for analysis, visualization, or machine learning workflows.

---

## 🛠 Tools & Technologies
- Python 3.x
- Pandas
- Matplotlib & Seaborn
- Jupyter Notebook / VS Code

---

## 📂 Project Structure
netflix-data-cleaning/ ├── data/                  # Raw dataset │   └── netflix_titles.csv ├── cleaned_data/          # Final cleaned dataset │   └── netflix_cleaned.csv ├── images/                # Visualizations │   └── missing_values_heatmap.png │   └── type_distribution.png ├── notebooks/             # Jupyter notebook (optional) │   └── netflix_cleaning.ipynb ├── netflix_cleaning.py    # Python script ├── requirements.txt       # Dependencies └── README.md              # Project documentation


---

## 🧹 Cleaning Steps
- Filled missing values in director and cast with "Unknown"
- Dropped rows missing country, date_added, or rating
- Removed duplicate entries
- Standardized text fields (type, rating)
- Converted date_added to datetime format
- Renamed columns to snake_case for consistency

---

## 📊 Visualizations

### 🔥 Missing Values Heatmap
![Missing Values Heatmap](images/missing_values_heatmap.png)

### 🎬 Type Distribution (Movies vs TV Shows)
![Type Distribution](images/type_distribution.png)

You can generate these using:

```python
# Missing values heatmap
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Values Heatmap")
plt.savefig("./images/missing_values_heatmap.png")

# Type distribution
sns.countplot(data=df, x='type')
plt.title("Type Distribution")
plt.savefig("./images/type_distribution.png")


---

🚀 How to Run

1. Clone the repository:git clone https://github.com/YOUR_USERNAME/netflix-data-cleaning.git
cd netflix-data-cleaning

2. Install dependencies:pip install -r requirements.txt

3. Run the script:python netflix_cleaning.py

4. Or launch the notebook:jupyter notebook notebooks/netflix_cleaning.ipynb
