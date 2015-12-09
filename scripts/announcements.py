#!/usr/bin/python
# This script generates the config.yml file for the Announcer plugin. It is run
# whenever the announcements_config.json file is modified.
# Author: Alvin Lin (alvin.lin.dev@gmail.com)

import json
import os
import sys
import yaml

ANNOUNCEMENTS_TEMPLATE = {
  "deluxechat_placeholders": False,
  "announcer_enabled": True,
  "announcer_random": True,
  "announce_interval": 120,
  "sound": {
    "enabled": False,
    "sound_name": "NOTE_PLING",
    "volume": 10,
    "pitch": 1
  }
}

ANNOUNCEMENTS_CONFIG_FILENAME = "announcements_config.json"

def get_announcements_config():
  """
  Gets the configurations of the script assuming the script's announcement.json is
  in the same directory as this script.
  """
  announcements = None
  announcements_filepath = "%s/%s" % (
    os.path.dirname(os.path.realpath(sys.argv[0])),
    ANNOUNCEMENTS_CONFIG_FILENAME)
  try:
    with open(announcements_filepath) as announcement_file:
      announcements = json.loads(announcement_file.read())
    test = (announcements["output_file"], announcements["prefix"],
            announcements["announcements"])
  except:
    raise ValueError("Invalid config.json!")
  return announcements

def generate_announcements_yaml(prefix, announcements):
  """
  Generates and returns announcements config.yml file.
  """
  announcement_tags = map(lambda s: "announcement%s" % s, range(len(announcements)))
  announcement_dict = {}
  for i in range(len(announcements)):
    announcement = json.dumps({
      "text": "%s%s" % (prefix, announcements[i])
    })
    announcement_dict[announcement_tags[i]] = [announcement]

  config_file = ANNOUNCEMENTS_TEMPLATE
  config_file["interval_announcement_list"] = announcement_tags
  config_file["announcements"] = announcement_dict
  return yaml.dump(config_file, default_flow_style=False)

def main():
  """
  Main function that takes the generated config.yml file and writes it as well as
  printing it.
  """
  announcements_config = get_announcements_config()
  announcements_yaml = generate_announcements_yaml(
    announcements_config["prefix"], announcements_config["announcements"])
  with open(announcements_config["output_file"], "w") as announcements_output:
    announcements_output.write(announcements_yaml)
  print "Wrote %s" % announcements_config["output_file"]

if __name__ == "__main__":
  main()
