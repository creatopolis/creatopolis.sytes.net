#!/usr/bin/python
# Web portal for Minecraft server. Displays upstate, players, and useful
# information.
# Author: Alvin Lin (alvin.lin.dev@gmail.com)

from flask import Flask
from flask import redirect, render_template
from werkzeug.contrib.fixers import ProxyFix

from mcstatus import MinecraftServer

import json
import sys

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/check_upstate")
def check_upstate():
  server = MinecraftServer("localhost", 25565)

  data = {}
  try:
    query = server.query()
    data["online"] = True
    data["players_online"] = query.players.names
    data["players_max"] = query.players.max
    data["version"] = query.software.brand
    data["plugins"] = query.software.plugins
  except:
    data["online"] = False

  return json.dumps(data)

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
  app.debug = "--debug" in sys.argv
  app.run()
