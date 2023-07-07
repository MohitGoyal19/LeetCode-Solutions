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

IF EXISTS (
	SELECT
		[salary]
	FROM
		[employee]
	GROUP BY [salary]
	ORDER BY 
		[salary] DESC
	OFFSET 1 ROWS FETCH NEXT 1 ROW ONLY)
	BEGIN
		SELECT
			[salary] AS [SecondHighestSalary]
		FROM
			[employee]
		GROUP BY [salary]   
		ORDER BY 
			[SecondHighestSalary] DESC
		OFFSET 1 ROWS FETCH NEXT 1 ROW ONLY
	END
ELSE
	SELECT
		NULL AS [SecondHighestSalary]
	