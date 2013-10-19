from flask import Flask, Response, render_template
import requests

app = Flask(__name__)

@app.route('/message')
def twil():
	return Response(render_template('twilio_response.twml'), mimetype='text/xml')

@app.route('/')
def home():
	return "hey how's it going"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
