# churn_prediction.py

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import warnings
warnings.filterwarnings('ignore')


def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df, target_col='Churn'):
    df = df.copy()
    # optional: drop columns not useful for prediction
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)

    # Label-encode categorical columns
    for col in df.select_dtypes(include=['object']).columns:
        if col != target_col:
            df[col] = LabelEncoder().fit_transform(df[col].astype(str))

    # Encode target if it's object
    if df[target_col].dtype == 'object':
        df[target_col] = LabelEncoder().fit_transform(df[target_col].astype(str))

    # Handle missing values (simple approach)
    df = df.fillna(0)

    # Split features and target
    X = df.drop([target_col], axis=1)
    y = df[target_col]

    # Feature scaling (optional, but helps some models)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns.tolist()


def train_models(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    trained_models = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_proba = None
        if hasattr(model, "predict_proba"):
            y_proba = model.predict_proba(X_test)[:, 1]

        print(f"\n--- {name} ---")
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        if y_proba is not None:
            print("ROC-AUC:", roc_auc_score(y_test, y_proba))

        trained_models[name] = model

    return trained_models


def save_model(model, scaler, filename_model='churn_model.pkl', filename_scaler='scaler.pkl'):
    with open(filename_model, 'wb') as f:
        pickle.dump(model, f)
    with open(filename_scaler, 'wb') as f:
        pickle.dump(scaler, f)


def load_model_and_scaler(model_path='churn_model.pkl', scaler_path='scaler.pkl'):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler


def predict_new(model, scaler, input_dict, feature_list):
    """
    input_dict: dict with {feature_name: value}
    feature_list: list of features (in same order as training X columns)
    """
    x = [ input_dict.get(f, 0) for f in feature_list ]
    x = np.array(x).reshape(1, -1)
    x_scaled = scaler.transform(x)
    pred = model.predict(x_scaled)[0]
    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(x_scaled)[0,1]
    return pred, proba


if __name__ == '__main__':
    # Example usage:
    df = load_data('customer_churn_data.csv')    # ▸ replace with your data file
    X, y, scaler, feature_list = preprocess_data(df, target_col='Churn')
    models = train_models(X, y)
    # Save the best model — e.g. RandomForest
    save_model(models['RandomForest'], scaler)

    # Example: predict for a new customer
    model, scaler = load_model_and_scaler()
    new_customer = {
        # fill values for all features, e.g.:
        # 'Gender': 'Male',
        # 'Age': 35,
        # 'Tenure': 5,
        # 'Balance': 50000,
        # ...
    }
    pred, prob = predict_new(model, scaler, new_customer, feature_list)
    print("Prediction (1 = churn, 0 = stay):", pred, "Probability:", prob)
