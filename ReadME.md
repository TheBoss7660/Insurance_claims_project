# Insurance_claims_project

import pandas as pd
import numpy as np

def clean_insurance_data(file_path):
    """
    Automated data cleaning pipeline for insurance datasets.
    Input: file_path - path to CSV or Excel file
    Output: cleaned pandas DataFrame
    """
    # 1️⃣ Load the dataset
    df = pd.read_csv(file_path)  # or pd.read_excel(file_path)

    # 2️⃣ Handle categorical columns
    cat_cols = ['gender', 'region', 'policy_type', 'accident_type', 'claim_status', 'fraud_flag', 'has_previous_claims']
    for col in cat_cols:
        df[col] = df[col].astype(str).str.strip().str.lower()
        # Fill missing values
        if col == 'gender':
            df[col] = df[col].replace({'nan': 'other'}).fillna('other')
        else:
            df[col] = df[col].replace({'nan': 'unknown'}).fillna('unknown')

    # 3️⃣ Handle numeric columns
    num_cols = ['age', 'premium', 'claim_amount', 'vehicle_age', 'hospital_visits', 'settlement_amount']
    for col in num_cols:
        # Replace negative values where not allowed
        if col in ['claim_amount', 'settlement_amount', 'age', 'vehicle_age', 'hospital_visits']:
            df[col] = df[col].apply(lambda x: np.nan if x < 0 else x)
        # Fill missing values with median
        df[col] = df[col].fillna(df[col].median())
        # Optional: handle outliers using IQR
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df[col] = df[col].clip(lower=lower, upper=upper)

    # 4️⃣ Handle date column
    df['claim_date'] = pd.to_datetime(df['claim_date'], errors='coerce')
    # Optional: fill missing dates with a default date or leave as NaT
    # df['claim_date'] = df['claim_date'].fillna(pd.Timestamp('1900-01-01'))

    # 5️⃣ Apply business logic for settlement amount
    df['settlement_amount'] = df.apply(
        lambda row: row['settlement_amount'] if row['claim_status'] == 'settled' else 0,
        axis=1
    )

    # 6️⃣ Ensure proper datatypes
    df['age'] = df['age'].astype(int)
    df['hospital_visits'] = df['hospital_visits'].astype(int)
    df['premium'] = df['premium'].astype(float)
    df['claim_amount'] = df['claim_amount'].astype(float)
    df['vehicle_age'] = df['vehicle_age'].astype(float)
    df['settlement_amount'] = df['settlement_amount'].astype(float)

    # 7️⃣ Return cleaned DataFrame
    return df