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