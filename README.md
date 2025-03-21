# 🛠️ Data Cleaning App Python

The Data Cleaning App is a Python-based application built for fast and efficient dataset cleaning. It seamlessly handles duplicates, missing values, and data inconsistencies, delivering a cleaned output in seconds. Designed for ease of use and high performance, it has been rigorously tested across various datasets to ensure accuracy and smooth execution.

Capable of processing thousands of rows, the application efficiently removes duplicates while keeping a backup, fills missing numeric values with column averages, and eliminates rows with missing non-numeric values. This makes it a powerful tool for data preprocessing, streamlining workflows in data analysis.

## Example of Execution

![image Alt](https://github.com/lekhakasinadhuni07/Data-Cleaning-App-Python/blob/6d73d63551b887982ce5914daab1177a682c91b9/Screenshot%20(57).png)

## Expected output:
Duplicate records saved as: `walmart_data_duplicates.csv`

Cleaned data saved as: `walmart_data_Clean_data.csv`

## Objectives
The primary goals of this project are to:

✅ **Load and clean datasets** in **CSV** and **Excel** formats.  

✅ **Identify and remove duplicate records**, keeping a backup for reference.

✅ **Handle missing values**:  
   - **Numeric columns** → Replace missing values with the column’s mean.  
   - **Non-numeric columns** → Remove rows containing missing values.

✅ **Save the cleaned dataset** and provide access to both cleaned data and duplicate records.  

## 🔧 Technologies Used  
- **Python**  
- **Pandas**  
- **NumPy**  
- **OpenPyXL** (for Excel files)
- **Xlrd**
- **OS library**

## Step-by-Step Process
1️⃣ **Input & File Verification**

- The application prompts the user to enter the dataset path and name.
- It verifies the file format, ensuring it is either CSV or Excel.

2️⃣ **Duplicate Detection & Removal**

- Scans the dataset for duplicate records.
- Saves duplicates as {dataset_name}_duplicates.csv before removal.
- Cleans the main dataset by eliminating duplicate rows.

3️⃣ **Handling Missing Values**

- Identifies missing values in the dataset.
- Numeric columns (integer/float): Missing values are replaced with the column’s mean.
- Non-numeric columns: Rows with missing values are removed.

4️⃣ **Exporting Clean Data**

- Saves the cleaned dataset as {dataset_name}_Clean_data.csv.
- Displays a confirmation message upon successful cleaning.

5️⃣ **Testing & Performance Optimization**

- Successfully tested on 5+ datasets with over 10,000 rows each.
- Consistently cleaned datasets within seconds without errors.
- Validated in Jupyter Notebook for seamless integration with data science workflows.

## Key Features
✅ **Fast & Efficient:** Cleans large datasets (10k+ rows) in seconds.

✅ **Duplicate Backup:** Stores removed duplicates separately.

✅ **Smart Missing Value Handling:** Fills numeric values with the mean and removes non-numeric missing rows.

✅ **User-Friendly:** Step-by-step prompts for smooth execution.

✅ **Supports Multiple Formats:** Compatible with CSV and Excel files.

## How to Use
- Run the application in a Python environment.
- Enter the dataset path and name when prompted.
- The application automatically processes and saves the cleaned dataset.


