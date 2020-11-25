USE `museum` ;

-- insert new favourite
INSERT INTO favoritedetails
SELECT current_date(), v.visitorNo, 'Ancient Clothes'
FROM visitor v
WHERE v.name = 'Aitana Savage';

-- see artifacts
SELECT f.*, v.name, v.email
FROM favoritedetails f
JOIN visitor v on v.visitorNo = f.visitorNo
WHERE v.visitorNo = 75;

-- delete favoriteDetails that were added before beginning of February 2015
DELETE FROM favoritedetails
WHERE dateAdded < '2015-2-01';
