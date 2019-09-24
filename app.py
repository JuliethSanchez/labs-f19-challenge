from flask import Flask, render_template, jsonify, request
import requests 

app = Flask(__name__)


@app.route("/pokemon/<query>")
def pokemon(query):
	place_holder = "https://pokeapi.co/api/v2/pokemon/" + query
	r = requests.get(place_holder)
	if(query.isdigit()):
		return 'The pokemon with id %s is %s' % (query,r.json()["name"])
	else:
		return '%s has id %s' % (query,r.json()["id"])
	

if __name__ == '__main__':
   app.run(debug=True)
