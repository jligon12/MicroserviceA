from flask import Flask, jsonify
from flask_cors import CORS
import pymongo

#MongoDB connection 
connection_url = 'mongodb+srv://ligonj:MicroA@microservicea.ublsl.mongodb.net/'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)

#Database
db = client.get_database("MicroserviceA")
#Collection
CollegeVisits = db.CollegeVisits

# This guide uses GET here instead of POST? https://www.geeksforgeeks.org/make-python-api-to-access-mongo-atlas-database/
@app.route('/insert-one/<email>/<name>/<location>/<visitDate>/<contacts>/<rating>/<notes>/', methods=['GET'])
def addCollegeVisit(email, name, location, visitDate, contacts, rating, notes):
    visit = {
        'Email': email,
        'Name': name,
        'Location': location,
        'VisitDate': visitDate,
        'Contacts': contacts, 
        'Rating': rating,
        'Notes': notes
    }
    addedVisit = CollegeVisits.insert_one(visit)
    return "201, POST Request Successful" #is there where I would write the status code?

@app.route('/find/', methods = ['GET'])
def getVisits():
    allVisits = CollegeVisits.find()
    output = {}
    i = 0
    for visit in allVisits:
        output[i] = visit
        output[i].pop('_id')
        i += 1
    return "200, GET Request Successful "

@app.route('/update/<key>/<value>/<element>/<updateValue>/', methods = ['GET'])
def update(key, value, element, updateValue):
    visit = {key: value}
    updateElement = {element: updateValue}
    updateVisit = CollegeVisits.update_one(visit, {'$set': updateElement})
    if updateVisit.acknowledged:
        return "201, Update Successful"
    else:
        return "Update Unsuccessful"

if __name__ == "__main__":
    app.run(debug=True)