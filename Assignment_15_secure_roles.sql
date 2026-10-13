-- Create Database
CREATE DATABASE company_database;

-- Connect to Database
USE company_database;

-- Create Users
CREATE USER 'diego'@'localhost'
IDENTIFIED BY 'EmployeePass123!';

CREATE USER 'adminuser'@'localhost'
IDENTIFIED BY 'AdminPass123!';

-- Create Roles
CREATE ROLE 'employee_role';
CREATE ROLE 'admin_role';

-- Grant Permissions to Roles
GRANT SELECT
ON company_database.*
TO 'employee_role';

GRANT SELECT, INSERT, UPDATE, DELETE
ON company_database.*
TO 'admin_role';

-- Assign Roles to Users
GRANT 'employee_role'
TO 'diego'@'localhost';

GRANT 'admin_role'
TO 'adminuser'@'localhost';

-- Set Roles as Default
SET DEFAULT ROLE 'employee_role'
TO 'diego'@'localhost';

SET DEFAULT ROLE 'admin_role'
TO 'adminuser'@'localhost';
