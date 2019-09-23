-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

SELECT CITY 
FROM STATION
WHERE CITY REGEXP '^[aeiou]';


-- https://www.tutorialspoint.com/mysql/mysql-regexps.htm 