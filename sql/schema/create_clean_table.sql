CREATE TABLE insurance_claims (
    claim_id SERIAL PRIMARY KEY,
    policy_id VARCHAR NOT NULL,
    customer_id VARCHAR NOT NULL,
    age INT NOT NULL,
    gender VARCHAR NOT NULL,
    region VARCHAR NOT NULL,
    poolicy_type VARCHAR NOT NULL,
    premium DECIMAL(10, 2) NOT NULL,
    claim_amount DECIMAL(10, 2) NOT NULL,
    claim_date DATE NOT NULL,
    accident_type VARCHAR NOT NULL,
    vehicle_age INT NOT NULL,
    has_previous_claim BOOLEAN NOT NULL,
    claim_status VARCHAR NOT NULL,
    hospital_visits INT NOT NULL,
    settlement_amount FLOAT NOT NULL,
    fraud_flag BOOLEAN NOT NULL,
    description TEXT, 
)


psql -U postgres -d insurance_db -f sql/schema/create_clean_table.sql