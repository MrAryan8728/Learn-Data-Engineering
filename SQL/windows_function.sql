-- 178.Rank Scores Leetcode

SELECT score, DENSE_RANK() OVER(ORDER BY score DESC) as `rank`
FROM Scores
ORDER BY score DESC;

-- 185.Department top three salaries

SELECT 
Department, Employee, Salary
FROM
(
    SELECT
        Department, Employee, Salary,
        DENSE_RANK() OVER (PARTITION BY Department ORDER BY salary DESC) as rnk
    FROM (
        SELECT
        d.name AS Department, e.name as Employee, e.salary as Salary
        FROM employee e
        JOIN department d
        ON e.departmentId = d.id
    ) tmp
) tmp2
WHERE rnk <= 3;