# 🏦 Bank Statement Importer

A user-friendly Streamlit web application to import, clean, and process bank statements from CSV and Excel formats. Perfect for accountants, analysts, and finance professionals who need a quick and interactive way to clean and analyse bank statement data.

---

## ✨ Features

- 📥 Upload CSV or Excel bank statements
- 🧹 Automatically cleans dates, amounts, and other essential columns
- 📊 Displays a clean preview of the data
- 🔄 Allows downloading of cleaned data as CSV
- 🖥️ Easy to run with Streamlit (no need for command line)

---

## 📂 Folder Structure

bank-statement-importer/
- app.py # Streamlit frontend
- parser.py # Script logic to clean the data
- requirements.txt # Python dependencies
- README.md # This file
- sample_data/
- zenith_sample.csv # Example CSV file

---

## 🚀 How It Works

1. **Upload** a CSV or Excel file with your bank statement.
2. The script **cleans** the data:
   - Normalises column names
   - Converts dates and amounts to correct formats
3. **Preview** the cleaned data in a table.
4. Optionally, **download** the cleaned data as a CSV file.

---

## 📊 Sample Output

After uploading your bank statement, the cleaned data will be displayed like this:

| Date       | Description        | Amount  | Balance |
|------------|--------------------|---------|---------|
| 2024-12-01 | Transfer from GTB  | 5000    | 15000   |
| 2024-12-02 | POS Purchase       | -2000   | 13000   |
| 2024-12-03 | ATM Withdrawal     | -5000   | 8000    |

---

## 🧪 Requirements

### 📌 Prerequisites

Make sure you have Python installed, then install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

To start the web app, run:

```bash
streamlit run app.py
```
## 📁 Sample CSV File (zenith_sample.csv)

- Date,Description,Amount,Balance
- 2024-12-01,Transfer from GTB,5000,15000
- 2024-12-02,POS Purchase,-2000,13000
- 2024-12-03,ATM Withdrawal,-5000,8000

---

## 📄 License
This project is licensed under the MIT License.

---

## 👨🏾‍💻 Author

Olawale Iwarere Jr.  
Finance + AI Enthusiast | Accountant | Python Developer  
GitHub: [@iwasoffice](https://github.com/iwasoffice)  
Twitter & TikTok: [@iwas_official](https://twitter.com/iwas_official) | IG: [@iwas_official](https://www.instagram.com/iwas_official)  
Quora: [Olawale Iwarere Jr.](https://www.quora.com/profile/Olawale-Iwarere-Jr)

_“Finance made smarter. Automation made simpler.”_



