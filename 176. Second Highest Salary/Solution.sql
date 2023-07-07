-- Table: Employee

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key column for this table.
-- Each row of this table contains information about the salary of an employee.
 

-- Find the second highest salary from the Employee table. If there is no second highest salary, return null.

WITH [Ranked_Salaries] AS (
	SELECT 
		[salary], 
		DENSE_RANK () OVER (ORDER BY [salary] DESC) AS [rank]
	FROM 
		[employee]
)

SELECT 
	MAX([salary]) AS [SecondHighestSalary]
FROM [Ranked_Salaries]
WHERE [rank] = 2