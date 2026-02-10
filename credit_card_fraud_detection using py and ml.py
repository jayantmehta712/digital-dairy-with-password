# credit_card_fraud_detection.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from imblearn.over_sampling import RandomOverSampler  # need imbalanced-learn package
import pickle
import warnings

warnings.filterwarnings("ignore")


def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    df = df.copy()
    # If dataset has irrelevant columns (e.g. transaction ID), drop them if needed
    # Example dataset: features V1–V28 (after PCA), plus 'Time' and 'Amount', and target 'Class'
    # Assume target column is named 'Class'

    # Separate features and target
    X = df.drop(['Class'], axis=1)
    y = df['Class']

    # Because the dataset is often highly imbalanced (fraud << normal), we apply over-sampling
    ros = RandomOverSampler(random_state=42)
    X_res, y_res = ros.fit_resample(X, y)

    # Feature scaling (important especially if some features have different scales, e.g. 'Amount')
    scaler = StandardScaler()
    X_res_scaled = scaler.fit_transform(X_res)

    return X_res_scaled, y_res, scaler

def train
