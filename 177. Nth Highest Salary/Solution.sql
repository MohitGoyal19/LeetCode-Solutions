-- Table: Employee

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key column for this table.
-- Each row of this table contains information about the salary of an employee.
 

-- Find the nth highest salary from the Employee table. If there is no nth highest salary, return null.


CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
	RETURN (
		SELECT
			MAX(salary)
		FROM
			(SELECT
				[salary],
				DENSE_RANK() OVER(ORDER BY salary DESC) AS [ranked]
			FROM
				[employee]) [ranked_salaries]
		WHERE [ranked] = @N
	);
END