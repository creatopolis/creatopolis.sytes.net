#!/usr/bin/python
# This script handles the backing up of the Minecraft worlds and is scheduled
# to run through the Essentials plugin.
# Author: Alvin Lin (alvin.lin.dev@gmail.com)

import datetime
import json
import os
import sys
import zipfile

CONFIG_FILENAME = "backup_config.json"

def get_config():
  """
  Gets the configurations of the script assuming the script"s config.json is
  in the same directory as this script.
  """
  config = None
  config_filepath = "%s/%s" % (os.path.dirname(os.path.realpath(sys.argv[0])),
                               CONFIG_FILENAME)
  try:
    with open(config_filepath) as config_file:
      config = json.loads(config_file.read())
    test = (config["worlds"], config["server_folder"], config["backups_folder"])
  except:
    raise ValueError("Invalid config.json!")
  return config

def list_files_all(path):
  """
  Given a path, this function recursively goes lists the directory"s contents.
  """
  files = []
  for name in os.listdir(path):
    pathname = os.path.join(path, name)
    if os.path.isfile(pathname):
      files.append(os.path.abspath(pathname))
    else:
      subfiles = list_files_all(pathname)
      for subfile in subfiles:
        files.append(os.path.abspath(subfile))
  return files

def get_backup_name(worldname):
  """
  This function generates the name of the backup given the name of the world for
  which the backup is being created.
  """
  today = datetime.datetime.today()
  return today.strftime(worldname + "_backup_%m-%d-%Y_%H-%M-%S.zip")

def main():
  """
  Main function, reads the config and makes backups of the specified folders.
  """
  config = get_config()
  for world in config["worlds"]:
    backup_name = get_backup_name(world)
    full_backup_path = "%s/%s" % (config["backups_folder"], backup_name)
    with zipfile.ZipFile(full_backup_path, "w") as newzip:
      full_world_path = "%s/%s" % (config["server_folder"], world)
      for filename in list_files_all(full_world_path):
        newzip.write(filename, filename[len(config["server_folder"]) + 1:])
    print "Successfully made %s" % backup_name

if __name__ == "__main__":
  main()
