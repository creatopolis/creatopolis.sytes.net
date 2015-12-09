# Web application
from flask import Flask
from flask import redirect, render_template
from werkzeug.contrib.fixers import ProxyFix

import sys

app = Flask(__name__)
 
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/*")
def catchall():
  return redirect("/")
 
app.wsgi_app = ProxyFix(app.wsgi_app)
 
if __name__ == "__main__":
  app.debug = "--debug" in sys.argv
  app.run()
