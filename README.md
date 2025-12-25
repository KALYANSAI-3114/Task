# 📦 Shipment AI Query System — Screening Task

This project was developed as part of the **AI Engineer Screening Assignment**.  
The goal was to load shipment data, store it in a database, and build a system that can answer **natural language queries** about the data.

---

## 🛠 Tools & Technologies Used

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python Flask |
| NLP | spaCy (Rule-based Intent Extraction) |
| Database | MySQL |
| Data Source | Excel → Cleaned to CSV |

---

## 🚀 Project Approach

1. **Data Understanding & Preprocessing**
   - Explored dataset, identified missing values and inconsistent formats
   - Cleaned and formatted data for smooth ingestion
   - Exported cleaned version as `final_shipping_data.csv`

2. **Database Setup**
   - Imported CSV into MySQL using Table Data Import Wizard
   - Table name: `final_shipping_data`

3. **Backend Development (Flask)**
   - Created API `/query` to process English questions
   - Implemented **NLP module** to extract intent (count, total cost, group analysis, date range, top-N queries)
   - Created SQL Builder to dynamically convert NLP output → SQL queries
   - Used MySQL connector for DB communication

4. **Frontend UI**
   - Simple clean interface built with HTML + CSS + JS
   - User enters query → frontend sends request to Flask
   - Response is displayed in human-readable format


---

## ▶ How to Run the Project

### Step 1 — Clone the Repository

```bash
git clone https://github.com/KALYANSAI-3114/Task.git
```

### Step 2 — Navigate to Backend Folder

```bash
cd Task/backend
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run the Application

```bash
python app.py
```

### Step 5 — Open Browser

```
http://127.0.0.1:5000
```

Enter queries in plain English.

---

## 🧠 Example Queries You Can Ask

```
How many shipments were created this month?
Show total shipment cost for the current month.
Provide a cost analysis of shipments grouped by status.
List the top 5 most expensive shipments.
Show shipments created in the last 7 days.
Top 10 costly shipments.
UPS shipments last week.
Group shipments by carrier.
```

---

## 📊 Output Format

The system returns:

| Intent | Output |
|---|---|
| Count | "📦 Shipments count: X" |
| Sum | "💰 Total shipment cost: Y" |
| Group Analysis | Table-like JSON summary |
| Top / Expensive List | Sorted shipment rows |
| Unknown Queries | Returns all data or safe fallback |

---

