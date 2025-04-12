import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

full_df = pd.read_csv("Alia-clustered.csv", header=0)

#create x and y
X = full_df[['temp', 'cloudcover', 'windspeed', 'precip'] + [col for col in full_df.columns if col.startswith('icon_')]]
y = full_df['cluster']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

#do an ensemble
pipelines = {
    "Random Forest": Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(class_weight="balanced", random_state=42))
    ]),
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced", multi_class="multinomial", solver="lbfgs"))
    ]),
    "GaussianNB": Pipeline([
        ("scaler", StandardScaler()),
        ("clf", GaussianNB())
    ])
}

best_model = None
best_score = 0

for name, pipe in pipelines.items():
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {acc:.4f}")

    if acc > best_score:
        best_score = acc
        best_model = pipe
        best_name = name

print(f"\nBest model: {best_name} with accuracy: {best_score:.2%}")

proba = best_model.predict_proba(X_test)
top3 = np.argsort(proba, axis=1)[:, -3:]

correct = sum(y_test.iloc[i] in top3[i] for i in range(len(y_test)))
print(f"Top-3 Accuracy: {correct / len(y_test):.2%}")
