-- Check nulls
SELECT COUNT (*) FROM insurance_claims
WHERE claim_amount IS NULL;

-- Check for negative claim amounts
SELECT COUNT (*) FROM insurance_claims
WHERE claim_amount < 0;

-- Check for future claim dates
SELECT COUNT (*) FROM insurance_claims
WHERE claim_date > CURRENT_DATE;

-- Check for duplicate claim IDs
SELECT claim_id, COUNT (*)
FROM insurance_claims 
GROUP BY claim_id
HAVING COUNT(*) > 1;