from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # Add article to string which will be displayed
    rv = "Hello, World!" + \
         "\nSee\nhttps://chrisnoring.gitbooks.io/road-to-azure/content/deployment/python-web-app-deploy.html\n"
    return rv
