# Web application
from flask import Flask
from flask import redirect, render_template
from werkzeug.contrib.fixers import ProxyFix

import json
import nmap
import sys

app = Flask(__name__)
 
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/check_upstate")
def check_upstate():
  scanner = nmap.PortScanner()
  result = scanner.scan('localhost', '25565')
  return json.dumps(result)

@app.route("/*")
def catchall():
  return redirect("/")
 
app.wsgi_app = ProxyFix(app.wsgi_app)
 
if __name__ == "__main__":
  app.debug = "--debug" in sys.argv
  app.run()
