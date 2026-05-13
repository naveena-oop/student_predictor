import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Sample dataset
data = {
    'attendance': [90,85,60,70,95,40,55,80,75,50,
                   88,92,45,65,78,30,95,72,68,85],
    'study_hours': [5,4,2,3,6,1,2,4,3,2,
                    5,6,1,2,4,1,7,3,2,5],
    'prev_score':  [80,75,45,55,90,30,40,70,65,42,
                    82,88,35,50,72,25,92,60,55,78],
    'result':      [1,1,0,0,1,0,0,1,1,0,
                    1,1,0,0,1,0,1,1,0,1]
    # 1 = Pass, 0 = Fail
}

df = pd.DataFrame(data)

X = df[['attendance', 'study_hours', 'prev_score']]
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, preds) * 100:.2f}%")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as model.pkl ✅")