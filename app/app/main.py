from app import app
app.debug = True

if __name__ == "__main__":
    print "Running webserver!"
    app.run(host='0.0.0.0', port = 8085)
