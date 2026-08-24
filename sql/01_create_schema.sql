-- Create the lab schema
CREATE SCHEMA IF NOT EXISTS lab;

-- Drop table if it exists so the script is rerunnable
DROP TABLE IF EXISTS lab.customers;

-- Create the table based on our profile and contract
CREATE TABLE lab.customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    city VARCHAR(100),
    signup_date DATE NOT NULL,
    customer_segment VARCHAR(50) NOT NULL,
    
    -- CHECK constraint to ensure customer_id format is correct
    CONSTRAINT ck_customer_id_format CHECK (customer_id LIKE 'C%')
);