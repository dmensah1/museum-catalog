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