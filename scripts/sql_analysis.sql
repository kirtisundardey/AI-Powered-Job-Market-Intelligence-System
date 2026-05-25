-- 1. Show All Data
SELECT * FROM jobs;

-- 2. Total Jobs
SELECT COUNT(*) FROM jobs;

-- 3. Average Salary
SELECT AVG(salary_avg) FROM jobs;

-- 4. Top Hiring Cities
SELECT
	Job_City,
	COUNT(*) AS total_jobs
FROM jobs
GROUP BY Job_City
ORDER BY total_jobs DESC;

-- 5. Highest Paying Roles
SELECT
	Job_Title_Sim,
    AVG(Salary_Avg) AS avg_salary
FROM jobs
GROUP BY Job_Title_Sim
ORDER BY avg_salary DESC;

-- 6. Most Demanded Skills
SELECT
	SUM(Python) AS python_jobs,
	SUM(SQL) AS sql_jobs,
    SUM(AWS) AS aws_jobs,
    SUM(Spark) AS spark_jobs
FROM jobs;