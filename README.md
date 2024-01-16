# Chatterbox Lab

## Learning Goals

- Create an API with Flask for a React frontend application.

## Introduction

So far, we've seen how to build a Flask API and perform various CRUD actions
using SQLAlchemy. In this lab, you'll work on creating an API in Flask once more
— but this time, you'll also have code for a React frontend application, so you
can get a taste of full-stack development!

This project is separated into two applications:

- A React frontend, in the `client` directory.
- A Flask backend, in the `server` directory.

All of the features for the React frontend are built out, and we have a simple
`json-server` API that you can run to see what the completed version of the app
will look like. Your main goal with this lab is to build out a Flask API server
to replace `json-server`, so most of your coding will be done in the backend.

---

## Frontend Setup

Let's take a quick tour of what we have so far.

To get started, `cd` into the `client` directory. Then run:

```console
$ npm install
$ npm run server
```

This will install the React project dependencies, and run a demo API server
using `json-server`. Next, run this in a new terminal:

```console
$ npm start
```

NOTE: If you get an error message about "Error: digital envelope
routines::unsupported", type the following in your terminal:
`export NODE_OPTIONS=--openssl-legacy-provider`, then try starting the client
again.

Then visit [http://localhost:3000](http://localhost:3000) in the browser and
interact with the demo application to get a sense of its features.

Here's a demo of the what the React app should look like when using
`json-server` as the API:

![Chatterbox screenshot
1](https://curriculum-content.s3.amazonaws.com/python/chatterbox_screenshot_1.png "A screenshot of the chatterbox app in dark mode. The header is a purple bar
with 'Chatterbox' in white text. White messages are displayed below their
associated usernames on a black background beneath the header. There is a space
to enter new messages below this black box.")

![Chatterbox screenshot
2](https://curriculum-content.s3.amazonaws.com/python/chatterbox-screenshot_2.png "A screenshot of the chatterbox app in light mode. The header is a pink bar with
'Chatterbox' in black text. Black messages are displayed below their associated
usernames on a white background beneath the header. There is a space to enter
new messages below this black box. A message by user 'Duane' is in the process
of being edited.")

Take a look at the components provided in the `client` directory. Explore the
code and pay special attention to where the React application is interacting
with `json-server`. Where are the `fetch` requests being written? What routes
are needed to handle these requests? What HTTP verbs? What data is being sent in
the body of the requests?

Once you've familiarized yourself yourself with the code, turn off `json-server`
with `control + c` in the terminal where we ran `npm run server` (you can keep
the React application running, though). Next, let's see what we have in the
backend.

---

## Backend Setup

In another terminal, run `pipenv install; pipenv shell` to install the
dependencies and enter your virtual environment, then `cd` into the `server`
directory to start running your Python code.

```console
pipenv install  && pipenv shell
cd server
```

In this directory, you're given a bare-bones template for a Flask API
application. It should look familiar to other Flask labs you've seen and has all
the code set up so you can focus on building out your model and API routes.

Note the database has not been created, nor have any migrations been performed.

You'll be responsible for:

- Implementing the `Message` model and performing migrations.
- Setting up the necessary routes to handle requests.
- Performing CRUD actions with SQLAlchemy.
- Sending the

```

### Routes

Build out the following routes to handle the necessary CRUD actions:

- `GET /messages`: returns an array of all messages as JSON, ordered by
  `created_at` in ascending order.
- `POST /messages`: creates a new message with a `body` and `username` from
  params, and returns the newly created post as JSON.
- `PATCH /messages/<int:id>`: updates the `body` of the message using params,
  and returns the updated message as JSON.
- `DELETE /messages/<int:id>`: deletes the message from the database.

---

## Resources

- [Flask - Pallets](https://flask.palletsprojects.com/en/2.2.x/)
- [Cross-Origin Resource Sharing - Mozilla][cors mdn]
- [Flask-CORS][flask-cors]
- [flask.json.jsonify Example Code - Full Stack Python](https://www.fullstackpython.com/flask-json-jsonify-examples.html)
- [SQLAlchemy-serializer - PyPI](https://pypi.org/project/SQLAlchemy-serializer/)

[cors mdn]: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
[flask-cors]: https://flask-cors.readthedocs.io/en/latest/
