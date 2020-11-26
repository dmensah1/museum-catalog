USE `museum` ;

-- create View for user favorites
CREATE VIEW visitorFavorites
AS SELECT f.dateAdded, f.artifactName, v.name
FROM favoritedetails f
JOIN visitor v on v.visitorNo = f.visitorNo;

SELECT *
FROM visitorFavorites
WHERE dateAdded >= DATE('2015-12-20');

DROP VIEW visitorFavorites;


-- create view for curator's expositions
CREATE VIEW curatorExpositions
AS SELECT c.name as curatorName, e.name as expositionName, e.description, e.startDate, e.endDate
FROM curator c
JOIN exposition e on c.curatorNo = e.curatorNo;

SELECT *
FROM curatorExpositions;

DROP VIEW curatorExpositions;


-- create view for artifacts
CREATE VIEW artifactsByTimePeriods 
AS SELECT a.artifactNo, a.name, tp.timePeriod
FROM artifact a
JOIN time tp on tp.artifactName = a.name
ORDER BY timePeriod;

SELECT * 
FROM artifactsbytimeperiods;

INSERT INTO artifactsbytimeperiods
VALUES('999', 'Piano', '17th Century');