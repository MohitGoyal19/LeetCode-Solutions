-- Table: Trips

-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | id          | int      |
-- | client_id   | int      |
-- | driver_id   | int      |
-- | city_id     | int      |
-- | status      | enum     |
-- | request_at  | date     |     
-- +-------------+----------+
-- id is the primary key for this table.
-- The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
-- Status is an ENUM type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
 

-- Table: Users

-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | users_id    | int      |
-- | banned      | enum     |
-- | role        | enum     |
-- +-------------+----------+
-- users_id is the primary key for this table.
-- The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
-- banned is an ENUM type of ('Yes', 'No').
 

-- The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

-- Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

SELECT
	[trips].[request_at] AS [Day],
	ROUND(CONVERT(FLOAT, SUM(CASE WHEN [trips].[status] LIKE '%cancelled%' THEN 1 ELSE 0 END))/COUNT(*), 2) AS [Cancellation Rate]
FROM
	[trips]
INNER JOIN
	[users] [client_details]
ON
	[trips].[client_id] = [client_details].[users_id]
INNER JOIN
	[users] [driver_details]
ON
	[trips].[driver_id] = [driver_details].[users_id]
WHERE
	[client_details].[banned] = 'No'
		AND
	[driver_details].[banned] = 'No'
		AND
	[trips].[request_at] BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY
	[trips].[request_at];