College Visit Microservice

This microservice is an API with get, post, and update functionality. It is hosted on port 5000.
The API is to a MongoDB database where college visits are tracked.
* Get data = http://127.0.0.1:5000/get-visits
* Post data = http://127.0.0.1:5000/add-visit
* Update data = http://127.0.0.1:5000/update-visit

How to make a request:
The main program calls each API individually by sending a request. 
For the post and update APIs a JSON body with data is passed to the API through the request. 
The json data could come from an html form as implemented in the test program.
The main program must install and import "requests" before it can be used. 
* Example: requests.post('http://127.0.0.1:5000/add-visit', json=data)

How receive data: 
The response for the post and update APIs is a successful (201) or unsuccesful (401) status message that is sent back to the main program. 
The response for the get API is the requested data.
For the post and update APIs, the response is recieved by defining "response" as the request and checking the status code
* Example: response = requests.post('http://127.0.0.1:5000/add-visit', json=data), if response.status_code == 201:, response.json()

For the get API, the response can be received by rendering the template of the frontend page you would like to displaay the data on and passing render_template the response.
The main program must have render_template imported from flask
* Example: response = requests.get('http://127.0.0.1:5000/get-visits'), return render_template('index.html', response=response)
