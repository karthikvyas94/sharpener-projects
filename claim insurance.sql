-- TOP 10 ROWS OF THE TABLE
SELECT * FROM insurance_claims LIMIT 10;


-- ROWS OF THE TABLE
SELECT COUNT(*) FROM INSURAnCE_CLAIMS;


-- ADDING AGE GROUP COLUMN TO THE TABLE
ALTER TABLE insurance_claims ADD COLUMN age_group VARCHAR(10);


-- UPDATING AGE-GROUP COLUMN WITH AGE-GROUPS
UPDATE insurance_claims
SET age_group =
CASE
    WHEN age BETWEEN 18 AND 25 THEN '18-25'
    WHEN age BETWEEN 26 AND 35 THEN '26-35'
    WHEN age BETWEEN 36 AND 45 THEN '36-45'
    WHEN age BETWEEN 46 AND 55 THEN '46-55'
    WHEN age BETWEEN 56 AND 65 THEN '56-65'
    WHEN age > 65 THEN '65+'
END;


-- NO.OF CUSTOMERS IN EACH AGE GROUP
SELECT age_group, COUNT(*) AS customer_count FROM insurance_claims
GROUP BY age_group
ORDER BY customer_count desc;

-- CLAIM FREQUENCY BY AGE GROUP
SELECT age_group,round(AVG(claim_flag)*100,2) AS claim_rate FROM insurance_claims
GROUP BY age_group
ORDER BY claim_rate desc;


-- CLAIM RATE BY VEHICLE GROUP
SELECT vehicle_type,ROUND(AVG(claim_flag) * 100, 2) AS claim_rate FROM insurance_claims
GROUP BY vehicle_type
ORDER BY claim_rate desc ;


-- CLAIM RATE BY REGION
SELECT region,round(AVG(claim_flag)*100,2) AS claim_rate FROM insurance_claims
GROUP BY region
ORDER BY claim_rate desc;


-- CLAIM RATE BY VEHICLE-AGE
SELECT vehicle_age, round(AVG(claim_flag)*100,2) AS claim_rate FROM insurance_claims
GROUP BY vehicle_age
ORDER BY claim_rate desc;


-- CLAIM RATE BY GENDER
SELECT gender,AVG(claim_flag) AS value FROM insurance_claims
GROUP BY gender
ORDER BY gender;


