from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def getVisits():
    response = requests.get('http://127.0.0.1:5000/get-visits')
    return render_template('index.html', response=response) #visits=response.json

@app.route('/add-visit', methods=['POST'])
def addVisit():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        location = request.form['location']
        visitDate = request.form['visitDate']
        contacts = request.form['contacts']
        rating = request.form['rating']
        notes = request.form['notes']
    
        data = {'email': email, 'name':name, 'location':location, 'visitDate': visitDate, 'contacts':contacts, 'rating':rating, 'notes':notes}

        response = requests.post('http://127.0.0.1:5000/add-visit', json=data)
        if response.status_code == 201:
            return response.json()

@app.route('/update-visit', methods=['POST'])
def updateVisit():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        element = request.form['element']
        updateValue= request.form['updateValue']
        #data = {element: updateValue}
    
        data = {'key': key, 'value': value, 'element': element, 'updateValue': updateValue}

        response = requests.post('http://127.0.0.1:5000/update-visit', json=data)
        if response.status_code == 201:
            return response.json()



    


if __name__ == "__main__":
    app.run(debug=True, port=5010)
