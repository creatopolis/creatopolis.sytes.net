#!/usr/bin/python
# Web portal for Minecraft server. Displays upstate, players, and useful
# information.
# Author: Alvin Lin (alvin.lin.dev@gmail.com)

from mcstatus import MinecraftServer
from flask import Flask
from flask import redirect, render_template, request, send_file
from werkzeug.contrib.fixers import ProxyFix

import json
import os
import sys

app = Flask(__name__)

root_app_path = os.path.dirname(os.path.realpath(__name__))

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/resourcepack")
def resource_pack():
  return send_file("%s%s" % (root_app_path, "/resourcepack/ModernHD1.8.8.zip"),
                   as_attachment=True,
                   attachment_filename="ModernHD1.8.8.zip")

@app.route("/ticket", methods=["GET", "POST"])
def ticket():
  if request.method == "GET":
    return render_template("ticket.html")
  else:
    print request.form.get("ticket", "")
    with open("tickets.log", "a") as tickets:
      tickets.write(request.form.get("ticket", ""))
    return redirect("/")

@app.route("/check_upstate")
def check_upstate():
  data = {}

  # If the app has been started in debug mode, return dummy data.
  if app.debug:
    data["online"] = True
    data["players_online"] = ["testname1", "testname2"]
    data["players_max"] = 20
    data["version"] = "CraftBukkit 1.8.8"
    data["plugins"] = ["WorldEdit", "WorldGuard"]
    return json.dumps(data)

  # Otherwise, an actual server query should be made.
  server = MinecraftServer("localhost", 25565)
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
