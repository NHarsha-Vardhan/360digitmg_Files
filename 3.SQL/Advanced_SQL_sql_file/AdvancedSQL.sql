-- Create a database named AdvancedSQL
CREATE DATABASE AdvancedSQL;

-- Set it as default database
USE AdvancedSQL;

-- Create IndianCelebrities table
CREATE TABLE IndianCelebrities (
    CelebrityID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    DepartmentID INT,
    ManagerID INT,  -- Manager ID for hierarchical relationship
    Salary DECIMAL(10, 2)
);

-- Sample data for IndianCelebrities
INSERT INTO IndianCelebrities (CelebrityID, Name, Age, Gender, DepartmentID, ManagerID, Salary)
VALUES 
(1, 'Akshay Kumar', 54, 'Male', 1, 14, 5000000.00),
(2, 'Virat Kohli', 33, 'Male', 2, 8, 8000000.00),
(3, 'Narendra Modi', 71, 'Male', 3, NULL, 10000000.00),
(4, 'Deepika Padukone', 35, 'Female', 1, 14, 7000000.00),
(5, 'PV Sindhu', 26, 'Female', 2, 8, 6000000.00),
(6, 'Rahul Gandhi', 51, 'Male', 3, 3, 9000000.00),
(7, 'Shah Rukh Khan', 55, 'Male', 1, 14, 7500000.00),
(8, 'MS Dhoni', 40, 'Male', 2, NULL, 8500000.00),
(9, 'Amitabh Bachchan', 79, 'Male', 1, 14, 10000000.00),
(10, 'Sania Mirza', 35, 'Female', 2, 8, 6500000.00),
(11, 'Sachin Tendulkar', 48, 'Male', 2, 8, 9000000.00),
(12, 'Priyanka Chopra', 39, 'Female', 1, 14, 8000000.00),
(13, 'Rahul Dravid', 49, 'Male', 2, 8, 7500000.00),
(14, 'Rajinikanth', 70, 'Male', 1, NULL, 12000000.00),
(15, 'Arvind Kejriwal', 53, 'Male', 3, 3, 8000000.00);

-- Create Departments table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

-- Sample data for Departments
INSERT INTO Departments (DepartmentID, DepartmentName)
VALUES 
(1, 'Acting'),
(2, 'Sports'),
(3, 'Politics');

-- Joins:

-- Inner Join:
-- Query: Retrieve the name of the celebrity along with their department name for all celebrities who have a department assigned.

SELECT ic.Name AS CelebrityName, d.DepartmentName
FROM IndianCelebrities ic
INNER JOIN Departments d ON ic.DepartmentID = d.DepartmentID;

-- Left Join:
-- Query: Retrieve the name of all celebrities and their department names, including those celebrities who don't have a department assigned.

SELECT ic.Name AS CelebrityName, d.DepartmentName
FROM IndianCelebrities ic
LEFT JOIN Departments d ON ic.DepartmentID = d.DepartmentID;

-- Right Join:
-- Query: Retrieve the name of all departments and the names of celebrities who belong to those departments, including departments with no celebrities assigned.

SELECT ic.Name AS CelebrityName, d.DepartmentName
FROM IndianCelebrities ic
RIGHT JOIN Departments d ON ic.DepartmentID = d.DepartmentID;

-- Outer Join:
-- Query: Retrieve all celebrities and their departments, including those without a department and all departments with or without assigned celebrities.

SELECT ic.Name AS CelebrityName, d.DepartmentName
FROM IndianCelebrities ic
FULL OUTER JOIN Departments d ON ic.DepartmentID = d.DepartmentID;

-- Cross Join:
-- Query: Retrieve all possible combinations of celebrities and departments.

SELECT ic.Name AS CelebrityName, d.DepartmentName
FROM IndianCelebrities ic
CROSS JOIN Departments d;

-- Self Join:
-- Query: Retrieve pairs of celebrities where one is the manager of the other.

SELECT m.Name AS ManagerName, e.Name AS EmployeeName
FROM IndianCelebrities m
INNER JOIN IndianCelebrities e ON m.CelebrityID = e.ManagerID;

-- Subqueries:

-- Subquery in SELECT:
-- Query: Retrieve the name of the celebrity and the total number of departments.

SELECT ic.Name AS CelebrityName, (SELECT COUNT(*) FROM Departments) AS TotalDepartments
FROM IndianCelebrities ic;

-- Subquery in FROM:
-- Query: Retrieve the name of all celebrities who belong to the department with the highest ID.

SELECT ic.Name AS CelebrityName
FROM (SELECT * FROM IndianCelebrities WHERE DepartmentID = (SELECT MAX(DepartmentID) FROM Departments)) ic;

-- Subquery in WHERE:
-- Query: Retrieve the name of all celebrities whose salary is higher than the average salary of all celebrities.

SELECT ic.Name AS CelebrityName
FROM IndianCelebrities ic
WHERE ic.Salary >  (SELECT AVG(Salary) FROM IndianCelebrities);

-- Subquery in INSERT:
-- Query: Insert a new celebrity record with a salary equal to the average salary of all celebrities.

INSERT INTO IndianCelebrities (CelebrityID, Name, Age, Gender, DepartmentID, ManagerID, Salary)
SELECT 
    16, -- Desired CelebrityID
    'Ravi Kumar', -- Desired Name
    30, -- Desired Age
    'Male', -- Desired Gender
    1, -- Desired DepartmentID
    14, -- Desired ManagerID
    AVG(Salary) -- Average salary of all celebrities
FROM IndianCelebrities;

-- Subquery in UPDATE:
-- Query: Update the salary of all celebrities to be 10% higher than the average salary of all celebrities.
SET SQL_SAFE_UPDATES = 0;
UPDATE IndianCelebrities ic
JOIN (
    SELECT AVG(Salary) * 1.1 AS new_salary
    FROM IndianCelebrities
) AS subquery ON 1=1
SET ic.Salary = subquery.new_salary;

-- CTE:

-- Normal CTE:
-- Query: Retrieve the name of the celebrity along with their department name using a CTE.

WITH CelebrityInfo AS (
    SELECT ic.Name AS CelebrityName, d.DepartmentName
    FROM IndianCelebrities ic
    JOIN Departments d ON ic.DepartmentID = d.DepartmentID
)
SELECT * FROM CelebrityInfo;


-- Recursive CTE:
-- Query: Retrieve the hierarchical structure of politicians and their parties.

WITH Recursive PoliticianCTE AS (
    SELECT 
        CelebrityID,
        Name,
		ManagerID,
        0 AS Level
    FROM 
        IndianCelebrities
    WHERE 
        ManagerID IS NULL

    UNION ALL

    SELECT 
        c.CelebrityID,
        c.Name,
        c.ManagerID,
        pc.Level + 1
    FROM 
        IndianCelebrities c
    INNER JOIN 
        PoliticianCTE pc ON c.ManagerID = pc.CelebrityID
)
SELECT * FROM PoliticianCTE;

-- Window Functions:

-- Sum:
-- Query: Calculate the total salary for each category of celebrities.

SELECT 
    DepartmentID,
    SUM(Salary) OVER(PARTITION BY DepartmentID) AS TotalSalary
FROM IndianCelebrities;

-- Avg:
-- Query: Calculate the average age of celebrities.

SELECT 
    AVG(Age) OVER() AS AverageAge
FROM IndianCelebrities;

-- Row_number:
-- Query: Assign a row number to each celebrity ordered by their age.

SELECT 
    Name,
    Age,
    ROW_NUMBER() OVER(ORDER BY Age) AS RowNumber
FROM IndianCelebrities;

-- Rank:
-- Query: Determine the rank of celebrities based on their salary.

SELECT 
    Name,
    Salary,
    DepartmentID,
    RANK() OVER(ORDER BY Salary ) AS SalaryRank
FROM IndianCelebrities;

-- Dense_rank:
-- Query: Determine the dense rank of celebrities based on their salary.

SELECT 
    Name,
    Salary,
    DENSE_RANK() OVER(ORDER BY Salary DESC) AS DenseSalaryRank
FROM IndianCelebrities;

-- Percent_rank:
-- Query: Determine the percentile rank of celebrities based on their age.

SELECT 
    Name,
    Age,
    PERCENT_RANK() OVER(ORDER BY Age) AS AgePercentileRank
FROM IndianCelebrities;

-- Ntile:
-- Query: Divide celebrities into quartiles based on their salary.

SELECT 
    Name,
    Salary,
    NTILE(4) OVER(ORDER BY Salary) AS SalaryQuartile
FROM IndianCelebrities;

-- First_value:
-- Query: Retrieve the first celebrity in terms of age.

SELECT 
    Name,
    Age,
    FIRST_VALUE(Name) OVER(ORDER BY Age) AS FirstCelebrity
FROM IndianCelebrities;

-- Last_value:
-- Query: Retrieve the last celebrity in terms of age.

SELECT 
    Name,
    Age,
    LAST_VALUE(Name) OVER(ORDER BY Age ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS LastCelebrity
FROM IndianCelebrities;

-- Lead:
-- Query: Retrieve the name of the next celebrity in terms of salary.

SELECT 
    Name,
    Salary,
    LEAD(Name) OVER(ORDER BY Salary) AS NextCelebrity
FROM IndianCelebrities;

-- Lag:
-- Query: Retrieve the name of the previous celebrity in terms of salary.

SELECT 
    Name,
    Salary,
    LAG(Name) OVER(ORDER BY Salary) AS PreviousCelebrity
FROM IndianCelebrities;
































