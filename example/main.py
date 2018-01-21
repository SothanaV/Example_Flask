from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello():
	return("Hello")

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/chat')
def chat():
	return render_template('chat.html')

@socketio.on('c2s')
def message(message):
	emit('s2c',message, broadcast=True)
	print(message)