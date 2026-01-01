CREATE DATABASE hr_project;
USE hr_project;

/* Create dept table */
CREATE TABLE departments (
    department_id INT,
    department_name VARCHAR(50)
);

SHOW TABLES;

/* Create employees table */
CREATE TABLE employees (
    employee_id INT,
    employee_name VARCHAR(50),
    department_id INT,
    joining_date DATE,
    status VARCHAR(20)
);

INSERT INTO departments VALUES
(10, 'HR'),
(20, 'IT'),
(30, 'Finance');

SELECT * FROM departments;
DELETE FROM departments;
TRUNCATE TABLE departments;

/* Insert into departments */
INSERT INTO departments VALUES
(10, 'HR'),
(20, 'IT'),
(30, 'Finance');

SELECT * FROM departments;

/* Insert into employees */
INSERT INTO employees VALUES
(1, 'Anita', 10, '2021-01-10', 'Active'),
(2, 'Rohit', 20, '2020-03-15', 'Active'),
(3, 'Sneha', 10, '2022-06-01', 'Active'),
(4, 'Vikas', 30, '2019-11-20', 'Resigned'),
(5, 'Pooja', 20, '2023-02-12', 'Active');

SELECT * FROM employees;
SELECT * FROM departments;

/* Find resigned employees */
SELECT * FROM employees
WHERE status = 'Resigned';

/* Remove resigned employees*/
DELETE FROM employees
WHERE status = 'Resigned';

/* Which employee works in which department? */
SELECT 
    e.employee_name,
    d.department_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;

















