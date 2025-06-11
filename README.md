# **Bank App Reviews Analysis**
🚀 **Analyzing User Sentiment & App Performance for Ethiopian Banks**

## **Project Overview**
 This project collects and analyzes  to **enhance customer retention and satisfaction** from **Google Play Store reviews** from three banking apps to identify:
- **User sentiment** (positive, neutral, negative)
- **Common themes** (UI, speed, transaction issues)
- **Pain points** and **satisfaction drivers**
- **Actionable recommendations** for better customer experience

## **Key Features**
✅ **Scrape** user reviews from Google Play Store  
✅ **Perform Sentiment Analysis** with NLP models  
✅ **Extract Themes & Keywords** (e.g., login issues, slow transfers)  
✅ **Store Cleaned Data** in **Oracle Database**  
✅ **Visualize Insights** using `Matplotlib`, `Seaborn`  `wordcloud`
✅ **Deliver Actionable Reports** to improve banking apps  
---

## **Installation & Setup**
### **Prerequisites**
- Python `>= 3.9`
- Git & GitHub
- Oracle Database (or PostgreSQL fallback)
- Virtual Environment (recommended)

### **Clone the Repository**
```bash
git clone https://github.com/your-username/bank-app-reviews.git
cd bank-app-reviews
```

### **Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Configure Database Connection**
Update your **config/settings.yaml** file with Oracle **username, password, host**.

---

## **Usage**
### **1️⃣ Scrape Google Play Store Reviews**
Run the scraper to collect data:
```bash
python src/scraper.py
```

### **2️⃣ Preprocess & Clean Data**
```bash
python src/preprocess.py
```

### **3️⃣ Perform Sentiment & Theme Analysis**
```bash
python src/sentiment.py
python src/thematic_analysis.py
```

### **4️⃣ Store Processed Data in Oracle**
```bash
python src/database.py
```

### **5️⃣ Generate Visualizations & Reports**
```bash
python src/visualize.py
```

---

## **Project Structure**
```
bank-app-reviews/
│── data/               # Raw & cleaned datasets
│── src/                # Python scripts for analysis
│── notebooks/          # Jupyter notebooks
│── reports/            # Insights & recommendations
│── config/             # Database & settings
│── tests/              # Unit tests
│── .github/            # CI/CD workflows
│── .gitignore          # Ignored files
│── README.md           # Documentation
│── requirements.txt    # Dependencies
```

---

## **Contributing**
1️⃣ **Fork this repo**  
2️⃣ **Create a branch** (`git checkout -b feature-new`)  
3️⃣ **Commit changes** (`git commit -m "Added new feature"`)  
4️⃣ **Push to GitHub** (`git push origin feature-new`)  
5️⃣ **Create a Pull Request!** 🚀  

---

## **License**
📜 **MIT License** - Free to use & modify!

---
