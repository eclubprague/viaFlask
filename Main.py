from Server import flask

if __name__ == '__main__':  # Main method
    flask.run(port=8088, debug=False, threaded=True, host="127.0.0.1")  # Starts server
