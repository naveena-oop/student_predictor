# 🎓 Student Performance Predictor

A Machine Learning web app that predicts whether a student will **Pass or Fail** based on attendance, study hours, and previous exam scores.

---

## 🎯 What It Does

- Takes 3 inputs — Attendance (%), Study Hours, Previous Exam Score
- Predicts **Pass ✅ or Fail ❌** instantly using a trained ML model
- Clean and interactive web interface

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| ML Model | scikit-learn (Random Forest) |
| Backend | Flask |
| Frontend | HTML, CSS |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
student_predictor/
│
├── app.py              # Flask web server
├── model.py            # ML model training
├── model.pkl           # Saved trained model
└── templates/
        └── index.html  # Frontend UI
```

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/naveena-oop/student_predictor.git
cd student_predictor
pip install pandas scikit-learn flask
python model.py
python app.py
```
Open browser → `http://127.0.0.1:5000`

---

## 🧠 Model Details

- Algorithm: Random Forest Classifier
- Features: Attendance %, Study Hours, Previous Score
- Target: Pass (1) or Fail (0)
- Accuracy: 75%

---

## 👩‍💻 Author

**Naveena Jammigumpula**
3rd Year B.Tech CSIT — KL University, Hyderabad
