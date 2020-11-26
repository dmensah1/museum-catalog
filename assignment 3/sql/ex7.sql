CREATE VIEW artifactsByTimePeriods 
AS SELECT a.artifactNo, a.name, tp.timePeriod
FROM artifact a
JOIN time tp on tp.artifactName = a.name
ORDER BY timePeriod;

SELECT * 
FROM artifactsbytimeperiods;

INSERT INTO artifactsbytimeperiods
VALUES('999', 'Piano', '17th Century');