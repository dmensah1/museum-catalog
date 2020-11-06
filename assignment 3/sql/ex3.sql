-- Insert #1
INSERT INTO Visitor (firstName,lastName, email, password, numVisits, museumsVisited)
VALUES ('Demir', 'Mensah', 'demirmensah@hotmail.com', '1234', 2, "AGO, MOMA");


-- Insert #2
INSERT INTO Visitor (firstName,lastName, email, password, numVisits)
VALUES ('Aaron', 'Rodgers', 'test@hotmail.com', '999', 5),
('Jimmy', 'Garrapollo', '49ers@gmail.com', '1278', 3),
('Lebron', 'James', 'test12@hotmail.com', '12345', 12);


-- Insert #3
SELECT lastName, email, password, numVisits
INTO @lName, @email, @pass, @numVis
FROM (
	SELECT lastName, email
	FROM Visitor 
    WHERE visitorNo = 1) as mergeIn
CROSS JOIN
(
	SELECT password, numVisits
	FROM Visitor 
    WHERE visitorNo = 2) as mergeTo;
INSERT INTO Visitor (firstName, lastName, email, password, numVisits, museumsVisited)
Values('Ben', @lname, @email, @pass, @numVis, 'Halifax Museum');
SELECT * FROM Visitor;