# SELECT salary as SecondHighestSalary 
# from Employee
# WHERE salary < (SELECT MAX(salary) FROM Employee)
# order by salary Desc
# Limit 1
# null not handled

SELECT IFNULL(
    (SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1),
    NULL
) AS SecondHighestSalary