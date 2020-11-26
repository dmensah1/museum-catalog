USE `museum` ;

-- visitors for november
SELECT a.date, v.name, m.name
FROM visitor v
JOIN admissionticket a on a.visitorNo = v.visitorNo
JOIN museum m on m.museumNo = a.museumNo
WHERE a.date >= DATE('2020-11-01') AND a.date <= DATE('2020-11-30');


-- Most Popular museums
SELECT m.name, COUNT(DISTINCT a.visitorNo) AS numberOfVisits, m.location
FROM admissionticket a
JOIN museum m on m.museumNo = a.museumNo
GROUP BY m.museumNo
HAVING COUNT(DISTINCT a.visitorNo)>=10;


-- Rank museums genearting over $200 by revenue
SELECT ad.museumNo, m.name, SUM(admissionPrice) AS revenue
FROM admissionticket ad
JOIN museum m on m.museumNo = ad.museumNo
GROUP BY museumNo
HAVING SUM(admissionPrice) > 200
ORDER BY revenue DESC;


-- Return exhibitions with an endDate after that of 'Modern Day Art' exhibition
SELECT name, museumNo, startDate, endDate
FROM exposition
WHERE endDate > 
(SELECT endDate
FROM exposition
WHERE name = 'Modern Day Art');


-- Find the name of curators (if they exist) who are in charge of expositions with start dates before Jan 01 2016
SELECT name
FROM curator
WHERE EXISTS 
(SELECT curatorNo 
	FROM Exposition 
	WHERE curator.curatorNo = Exposition.curatorNo AND startDate < '2016-01-01');

-- Visitor's who have first names beginning with A and last names ending with z
SELECT name
FROM visitor
WHERE name LIKE 'A%z';