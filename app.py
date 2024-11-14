from flask import Flask, jsonify, request
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

@app.route('/add-visit', methods=['POST'])
def addVisit():
    visitData = request.get_json()
    email = visitData.get('email')
    name = visitData.get('name')
    location = visitData.get('location')
    visitDate = visitData.get('visitDate')
    contacts = visitData.get('contacts')
    rating = visitData.get('rating')
    notes = visitData.get('notes')

    visit = {
        'Email': email,
        'Name': name,
        'Location': location,
        'VisitDate': visitDate,
        'Contacts': contacts, 
        'Rating': rating,
        'Notes': notes
    }

    CollegeVisits.insert_one(visit)
    return jsonify({'message': f'Visit added successfully.'}), 201

@app.route('/get-visits', methods = ['GET'])
def getVisits():
    allVisits = CollegeVisits.find()
    output = {}
    i = 0
    for visit in allVisits:
        output[i] = visit
        output[i].pop('_id')
        i += 1
    return output #"200, GET Request Successful "

@app.route('/update-visit', methods = ['POST'])
def updateVisit():
    visitUpdateData = request.get_json() #{"key": "Name", "value": "Hogwarts", "element": "Contacts", "updateValue": "HarryPotter,HermioneGranger"}
    key = visitUpdateData.get('key')
    value = visitUpdateData.get('value')
    element = visitUpdateData.get('element')
    updateValue = visitUpdateData.get('updateValue')
    visit = {key: value}
    updateElement = {element: updateValue}
    CollegeVisits.update_one(visit, {'$set': updateElement})
    return jsonify({'message': f'Visit updated successfully.'}), 201

if __name__ == "__main__":
    app.run(debug=True)