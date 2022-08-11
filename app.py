from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    rv = "Hello, World!" + \
         "\nSee\nhttps://chrisnoring.gitbooks.io/road-to-azure/content/deployment/python-web-app-deploy.html\n"
    return rv
