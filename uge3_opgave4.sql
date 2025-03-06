SHOW DATABASES;
USE northwind;
SHOW TABLES;

#2
SELECT ProductName, UnitPrice 
FROM products
ORDER BY UnitPrice DESC;

#3
SELECT * 
FROM customers
WHERE Country IN ('UK', 'Spain')
ORDER BY Country;

#4
SELECT ProductName, 
       UnitPrice, 
       CAST(REPLACE(UnitPrice, '.', '') AS DECIMAL(10,2)) AS CleanedPrice
FROM products
WHERE UnitsInStock > 100
HAVING CleanedPrice >= 25
ORDER BY UnitPrice;


#5
SELECT DISTINCT ShipCountry
FROM orders
ORDER BY ShipCountry;

#6
SELECT *
FROM orders
WHERE OrderDate BETWEEN '1996-10-01' AND '1996-10-31';

#7
SELECT *
FROM orders
WHERE ShipRegion IS NULL
AND ShipCountry = 'Germany'
AND Freight >= 100
AND EmployeeID = 1
AND OrderDate LIKE '%1996%';

#8
SELECT *
FROM orders
WHERE ShippedDate > RequiredDate;

#9
SELECT *
FROM orders
WHERE ShipCountry = 'Canada'
AND OrderDate BETWEEN '1997-01-01' AND '1997-04-30';

#10
SELECT * 
FROM orders
WHERE EmployeeID IN (2, 5, 8)
AND ShipRegion <> ''
AND ShipVia IN (1, 3)
ORDER BY EmployeeID ASC, ShipVia ASC;

#11 Der er ikke nogen kolonne der hedder ReportsTo
SELECT * 
FROM employees
WHERE Region <> '' 
AND YEAR(BirthDate) <= 1960;














