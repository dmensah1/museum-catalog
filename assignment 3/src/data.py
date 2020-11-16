import time
import random
import string
import datetime
import mysql.connector

fullNames = []
emails = []
passwords = []
musCapacity = [300, 400, 600, 800, 1000, 1250, 1500, 1750, 2000, 2500, 3000, 3500]

themes = []
countries = ["China", "USA", "Canada", "France", "England", "Roman", "Egyptian", "Greek", "Japanese", "Brazil", "Thailand", "Germany"]
timePeriods = ["90's", "80s", "40s", "50s", "60s", "70s", "00s", "19th Century", "18th Century", "Medieval", "17th Century", "16th Century", "15th Century"]
descriptions = ["Nice", "Very Cool", "Awesome", "Extravagant", "Fancy", "Delicate", "Fabulous", "Beautiful", "Heavy", "Chunky", "Antique", "Light", "Brisk", "Sharp", "Cool", "Elegant", "Excellent", "Very cool looking.", "Dope"]
locations = []
museumNames = []
artifactNames = []
expositionNames = ["Modern Day Sports", "Ancient Sports", "European Art", "Modern Day Art", "World War 2", "World War 1", "Mammals", "Games", "Ancient History", "Evolution", "Survival", "Automobiles", "Ancient Navigation", "Hobbies & Crafts", "Medieval Times"]
admissionPrices = [10, 15, 20, 25, 30, 40]


# id fields to hold results of one relation to enter into others who use field as FK
curatorNo = []
museumNo = []
visitorNo = []
artifactNoID = []
artifactNameID = []
artifactThemeID = []
artifactCountryID = []
artifactTimeID = []
expoNameID = []

# arrays holding rows of relations to push onto db
visitors = []
curators = []
museums = []
expositions = []
expoDetails = []
artifacts = []
artifactDetails = []
artifactThemes = []
artifactCountries = []
artifactTimes = []
admissionTickets = []
favoriteDetails = []

# arrays to hold formatted dates going into the db
startDates = []
endDates = []
datesAdded = []
datesRemoved = []
admissionDates = []


# Initialize intermediate variables for data generation
def randomIndex(start, size):
    return random.randint(start, size-1)

def initializeNames():
    fnames = []
    lnames = []

    # Fill fnames array with male names
    with open("assignment 3/src/BoyNames.txt", 'r') as file:
        line = file.readline()
        line = file.readline()  # to skip header
        while line:
            line = line.strip()
            if line != '':
                fnames.append(line)
            line = file.readline()

    # Adding girl names
    with open('assignment 3/src/GirlNames.txt', 'r') as file:
        line = file.readline()
        line = file.readline()
        while line:
            line = line.strip()
            if line != '':
                fnames.append(line)
            line = file.readline()

    # Fill lnames with common last names
    with open('assignment 3/src/LastNames.txt', 'r') as file:
        line = file.readline()
        line = file.readline()
        while line:
            line = line.strip().lower().capitalize()
            if line != '':
                lnames.append(line)
            line = file.readline()

    # Randomly connect first and last names
    while len(lnames) > 0:
        first = fnames.pop(randomIndex(0, len(fnames)))
        last = lnames.pop(randomIndex(0, len(lnames)))
        fullNames.append(first + " " + last)

def initializeEmails():
	clients = ['@gmail.com', '@hotmail.com', '@yahoo.com']

	for name in fullNames:
		nameSplit = name.split()
		emailAddr = nameSplit[0] + '.' + nameSplit[1] + str(randomIndex(1, 9999)) + clients[randomIndex(0,len(clients))] 
		emails.append(emailAddr)

def initializePasswords(limit, stringLength = 10):
    characters = string.ascii_letters + string.digits
    while len(passwords) < limit:
        _password =  ''.join(random.choice(characters) for i in range(stringLength))
        passwords.append(_password)

def initializeThemes():
    with open('assignment 3/src/Themes.txt', 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line != '':
                themes.append(line)
                line = file.readline()

def initializeLocations():
    with open('assignment 3/src/Locations.txt', 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line != '':
                locations.append(line)
                line = file.readline()

def initializeMuseums():
    with open('assignment 3/src/MuseumNames.txt', 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line != '':
                museumNames.append(line)
                line = file.readline()

def initializeArtifactNames():
    with open('assignment 3/src/ArtifactNames.txt', 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line != '':
                artifactNames.append(line)
                line = file.readline()

def initializeStartDates(limit):
    i = 0
    while i < limit:
        startDates.append(getRandomDate("2015-1-1", "2016-1-1"))
        i += 1 

def initializeEndDates(limit):
    i = 0
    while i < limit:
        endDates.append(getRandomDate("2019-1-1", "2021-1-1"))
        i += 1 

def getRandomDate(startDate, endDate):
    randomGenerator = random.random()
    dateFormat = '%Y-%m-%d'


    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

def initializeDatesAdded(limit):
    i = 0
    while i < limit:
        datesAdded.append(getRandomDate("2017-1-1", "2018-9-1"))
        i += 1 

def initializeDatesRemoved(limit):
    i = 0
    while i < limit:
        datesRemoved.append(getRandomDate("2020-1-1", "2021-12-1"))
        i += 1 

def initializeAdmissionDates(limit):
    i = 0
    while i < limit:
        admissionDates.append(getRandomDate("2016-1-1", "2021-1-1"))
        i += 1 


#  Functions below are to build data for inserting into database
def buildVisitors(limit):
    initializeNames()
    initializeEmails()
    initializePasswords(limit)

    while len(visitors) < limit:
        nameIndex = randomIndex(0, len(fullNames))
        visitor = [fullNames.pop(nameIndex), emails.pop(nameIndex), passwords.pop(randomIndex(0, len(passwords)))]
        if len(fullNames) <= 0:
            initializeNames()
            initializeEmails()
        if visitor not in visitors:
            visitors.append(visitor)

def buildCurators(limit):
    initializeNames()
    initializeThemes()
    initializeLocations()

    while len(curators) < limit:
        nameIndex = randomIndex(0, len(fullNames))
        locationIndex = randomIndex(0, len(locations))
        themeIndex = randomIndex(0, len(themes))
        curator = [fullNames.pop(nameIndex), locations.pop(locationIndex), themes.pop(themeIndex)]
        if len(fullNames) <= 0:
            initializeNames()
        if len(themes) <= 0:
            initializeThemes()
        if len(locations) <= 0:
            initializeLocations()
        if curator not in curators:
            curators.append(curator)

def buildMuseums(limit):
    initializeMuseums()
    initializeLocations()

    while len(museums) < limit:
        museumIndex = randomIndex(0, len(museumNames))
        locationIndex = randomIndex(0, len(locations))
        capacityIndex = randomIndex(0, 11)
        museum = [museumNames.pop(museumIndex), locations.pop(locationIndex), musCapacity[capacityIndex]]

        if len(museums) <= 0:
            initializeMuseums()
        if len(locations) <= 0:
            initializeLocations()
        if museum not in museums:
            museums.append(museum)

def buildArtifactDetails(limit):
    initializeArtifactNames()

    while len(artifactDetails) < limit:
        artifactIndex = randomIndex(0, len(artifactNames))
        artifactDetail = [artifactNames.pop(artifactIndex)]
        
        if len(artifactNames) <= 0:
           initializeArtifactNames()
        if artifactDetail not in artifactDetails:
            artifactDetails.append(artifactDetail)

def buildArtifactThemes(limit):
    #limit should be same as that of artifactDetails
    initializeThemes()
    print(len(artifactNameID))

    i = 0
    while i < limit:
        themeIndex = randomIndex(0, len(themes))
        
        artifactTheme = [artifactNameID[i], themes.pop(themeIndex)]
        i += 1

        if len(themes) <= 0:
            initializeThemes()
        if artifactTheme not in artifactThemes:
            artifactThemes.append(artifactTheme)
        if(len(artifactNameID) == 0):
            break

def buildArtifactCountry(limit):
    i = 0

    while i < limit:
        countryIndex = randomIndex(0, len(countries))

        artifactCountry = [artifactNameID[i], countries[countryIndex]]
        i += 1

        if artifactCountry not in artifactCountries:
            artifactCountries.append(artifactCountry)
        if(len(artifactNameID) == 0):
            break

def buildArtifactTimePeriod(limit):
    i = 0

    while i < limit:
        timeIndex = randomIndex(0, len(timePeriods))

        artifactTime = [artifactNameID[i], timePeriods[timeIndex]]
        i += 1

        if artifactTime not in artifactTimes:
            artifactTimes.append(artifactTime)
        if(len(artifactNameID) == 0):
            break

def buildArtifact(limit):
    i = 0

    while i < limit:
        descIndex = randomIndex(0, len(descriptions))
        
        artifact = [artifactNameID[i], descriptions[descIndex], artifactCountryID[i], artifactThemeID[i], artifactTimeID[i]]
        i += 1

        if artifact not in artifacts:
            artifacts.append(artifact)

def buildExpositions(limit):
    initializeStartDates(limit)
    initializeEndDates(limit)

    i = 0
    while i < limit:
        descIndex = randomIndex(0, len(descriptions))
        expoIdx = randomIndex(0, len(expositionNames))
        musIdx = randomIndex(0, len(museumNo))
        curIdx = randomIndex(0, len(curatorNo))

        exposition = [expositionNames.pop(expoIdx), descriptions[descIndex], startDates[i], endDates[i], museumNo[musIdx], curatorNo[curIdx]]
        i += 1

        if exposition not in expositions:
            expositions.append(exposition)

def buildExpositionDetails(limit):
    initializeDatesAdded(limit)
    initializeDatesRemoved(limit)
    i = 0

    while i < limit:
        artIdx = randomIndex(0, len(artifactNoID))

        expoDetail = [datesAdded[i], datesRemoved[i], expoNameID[i], artifactNoID[artIdx]]
        i += 1

        if expoDetail not in expoDetails:
            expoDetails.append(expoDetail)

def buildAdmissionTickets(limit):
    initializeAdmissionDates(limit)
    i = 0

    while i < limit:
        dateIdx = randomIndex(0, len(admissionDates))
        priceIdx = randomIndex(0, len(admissionPrices))
        visitorIdx = randomIndex(0, len(visitorNo))
        musIdx = randomIndex(0, len(museumNo))

        ticket = [admissionDates[dateIdx], admissionPrices[priceIdx], museumNo[musIdx], visitorNo[visitorIdx]]
        i += 1

        if ticket not in admissionTickets:
            admissionTickets.append(ticket)

def buildFavoriteDetails(limit):
    initializeStartDates(limit)
    i = 0

    while i < limit:
        visitorIdx = randomIndex(0, len(visitorNo))
        artIdx = randomIndex(0, len(artifactNameID))

        favorite = [startDates[i], visitorNo[visitorIdx], artifactNameID[artIdx]]
        i += 1

        if favorite not in favoriteDetails:
            favoriteDetails.append(favorite)


# connecting to the mysql db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Demirmensah12@",
    database="museum"
)
mycursor = mydb.cursor()

# Calling builds and pushing data into database in lines below
buildMuseums(20)
buildCurators(3000)
buildVisitors(3000)
buildArtifactDetails(150)


for artifact in artifactDetails:
    sql = "INSERT INTO ArtifactDetails (name) VALUES (%s)"
    mycursor.execute(sql, artifact)
    mydb.commit()

sql_query = "select name from artifactdetails"
mycursor.execute(sql_query)
records = mycursor.fetchall()
for row in records:
    artifactNameID.append(row[0])


buildArtifactThemes(150)
for artifactTheme in artifactThemes:
    sql = "INSERT INTO Theme (artifactName, artifactTheme) VALUES (%s, %s)"
    mycursor.execute(sql, artifactTheme)
    mydb.commit()

sql_query2 = "select artifactName from Theme"
mycursor.execute(sql_query2)
records2 = mycursor.fetchall()
for row in records2:
    artifactThemeID.append(row[0])


buildArtifactCountry(150)
for country in artifactCountries:
    sql = "INSERT INTO Country (artifactName, artifactCountry) VALUES (%s, %s)"
    mycursor.execute(sql, country)
    mydb.commit()

sql_query3 = "select artifactName from Country"
mycursor.execute(sql_query3)
records3 = mycursor.fetchall()
for row in records3:
    artifactCountryID.append(row[0])


buildArtifactTimePeriod(150)
for artTime in artifactTimes:
    sql = "INSERT INTO Time (artifactName, timePeriod) VALUES (%s, %s)"
    mycursor.execute(sql, artTime)
    mydb.commit()

sql_query4 = "select artifactName from time"
mycursor.execute(sql_query4)
records4 = mycursor.fetchall()
for row in records4:
    artifactTimeID.append(row[0])

buildArtifact(150)
for artifact in artifacts:
    sql = "INSERT INTO Artifact (name, description, country, theme, timePeriod) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, artifact)
    mydb.commit()
    mycursor.execute("select artifactNo from artifact ORDER BY artifactNo DESC LIMIT 1")
    myresult = mycursor.fetchall()
    artifactNoID.append(myresult[0][0])

for visitor in visitors:
    sql = "INSERT INTO Visitor (name, email, password) VALUES (%s, %s, %s)"
    mycursor.execute(sql, visitor)
    mydb.commit()
    mycursor.execute("select visitorNo from visitor ORDER BY visitorNo DESC LIMIT 1")
    myresult = mycursor.fetchall()
    visitorNo.append(myresult[0][0])

for museum in museums:
    sql = "INSERT INTO Museum (name, location, capacity) VALUES (%s, %s, %s)"
    mycursor.execute(sql, museum)
    mydb.commit()
    mycursor.execute("select museumNo from museum ORDER BY museumNo DESC LIMIT 1")
    myresult = mycursor.fetchall()
    museumNo.append(myresult[0][0])

for curator in curators:
    sql  = "INSERT INTO Curator (name, location, theme) VALUES (%s, %s, %s)"
    mycursor.execute(sql, curator)
    mydb.commit()
    mycursor.execute("select curatorNo from curator ORDER BY curatorNo DESC LIMIT 1")
    myresult = mycursor.fetchall()
    curatorNo.append(myresult[0][0])
    

buildExpositions(12)
for exposition in expositions:
    sql = "INSERT INTO Exposition (name, description, startDate, endDate, museumNo, curatorNo) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, exposition)
    mydb.commit()

sql_query8 = "select name from exposition"
mycursor.execute(sql_query8)
records8 = mycursor.fetchall()
for row in records8:
    expoNameID.append(row[0])

buildExpositionDetails(12)
for detail in expoDetails:
    sql = "INSERT INTO ExpositionDetails (dateAdded, dateRemoved, expoName, artifactNo) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, detail)
    mydb.commit()

buildAdmissionTickets(150)
for ticket in admissionTickets:
    sql = "INSERT INTO AdmissionTicket (date, admissionPrice, museumNo, visitorNo) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, ticket)
    mydb.commit()

buildFavoriteDetails(200)
for detail in favoriteDetails:
    sql = "INSERT INTO FavoriteDetails (dateAdded, visitorNo, artifactName) VALUES (%s, %s, %s)"
    mycursor.execute(sql, detail)
    mydb.commit()