# Tic Tac Toe Game
An implementation of Tic Tac Toe using minimax algorithm to determine computer's moves. This project is designed using React, Redux (frontend) and Flask/Python (backend).

To create your own game and set up React-Redux-Flask, follow these instructions:
[Setting up React & Redux](./client/README.md)
[Setting up Flask](./server/README.md)

## Build and run instructions
#### Frontend
Set up `SERVER_URL='0.0.0.0'` with your IP address at the top of the file `client/js/actions/game.jsx`
```sh
$ cd client
$ npm install
$ npm run watch
```

#### Backend
Set up `SERVER_URL='0.0.0.0'` with your IP address at the top of the file `server/server.py`

###For Linux and Mac
```sh
$ virtualenv env
$ source venv/bin/activate
$ pip install flask flask-cors
$ python server.py
```

###For Windows
```sh
$ virtualenv env
$ .\env\Scripts\activate
$ pip install flask flask-cors
$ python server.py
```