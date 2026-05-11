# Insurance Claims Analysis Using SQL

## Project Overview

This project focuses on analyzing insurance claim data using SQL to identify customer claim patterns based on:

- Age groups
- Vehicle type
- Vehicle age
- Region
- Gender

The analysis helps understand which customer segments have higher insurance claim rates and provides insights useful for risk assessment and business decision-making.

---

## Dataset Information

The dataset used is `insurance_claims`.

### Initial Exploration

```sql
-- TOP 10 ROWS OF THE TABLE
SELECT * FROM insurance_claims LIMIT 10;

-- TOTAL NUMBER OF ROWS
SELECT COUNT(*) FROM insurance_claims;
