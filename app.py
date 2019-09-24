from flask import Flask, render_template, jsonify, request
import requests 

app = Flask(__name__)


@app.route("/pokemon/<query>")
def pokemon(query):
	#Placeholder allows user to either add id or name
	place_holder = "https://pokeapi.co/api/v2/pokemon/" + query
	r = requests.get(place_holder) #gets information from the API
	if(query.isdigit()): #determines whether query is an digit 
		return 'The pokemon with id %s is %s' % (query,r.json()["name"])# returns the corresponding Pokemon from the id
	else:
		return '%s has id %s' % (query,r.json()["id"]) #returns the corresponding id from Pokemon name. 
	

if __name__ == '__main__':
   app.run(debug=True) #runs
