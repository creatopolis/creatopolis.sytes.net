#!/usr/bin/python
# This script handles the backing up of the Minecraft worlds and is scheduled
# to run through the Essentials plugin.
# Author: Alvin Lin (alvin.lin.dev@gmail.com)

import datetime
import json
import os
import re
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
    test = (config["folders"], config["server_folder"],
            config["backups_folder"], config["ignore_files"],
            config["keep_time"])
  except:
    raise ValueError("Invalid config.json!")
  return config

def list_files_all(path, ignore_files=[]):
  """
  Given a path, this function recursively goes lists the directory's contents,
  ignoring all specified file extensions.
  """
  files = []
  for name in os.listdir(path):
    pathname = os.path.join(path, name)
    if os.path.isfile(pathname):
      if pathname.split(".")[-1] not in ignore_files:
        files.append(os.path.abspath(pathname))
    else:
      subfiles = list_files_all(pathname)
      for subfile in subfiles:
        files.append(os.path.abspath(subfile))
  return files

def get_backup_name(foldername):
  """
  This function generates the name of the backup given the name of the folder
  for which the backup is being created.
  """
  today = datetime.datetime.today()
  return today.strftime(foldername + "_backup_%m-%d-%Y_%H-%M-%S.zip")

def should_remove_backup(backup_name, keep_time):
  """
  This function returns true if the backup with the given name should be deleted
  given the amount of time that backups are kept for in days.
  """
  try:
    backup_dateparse = re.search("([0-9]{2})-([0-9]{2})-([0-9]{4})",
                                 backup_name)
    today = datetime.date.today()
    backup_date = datetime.date(int(backup_dateparse.group(3)),
                                int(backup_dateparse.group(1)),
                                int(backup_dateparse.group(2)))
    return (today - backup_date).days > keep_time
  except:
    return False

def main():
  """
  Main function, reads the config and makes backups of the specified folders.
  Checks and removes backups that are too old.
  """
  config = get_config()
  for f in list_files_all(config["backups_folder"], config["ignore_files"]):
    if should_remove_backup(f, config["keep_time"]):
      print "Removing %s" % f
      os.remove(f)
      
  for folder in config["folders"]:
    backup_name = get_backup_name(folder)
    full_backup_name = "%s/%s" % (config["backups_folder"], backup_name)
    with zipfile.ZipFile(full_backup_name, "w") as newzip:
      full_folder_path = "%s/%s" % (config["server_folder"], folder)
      for filename in list_files_all(full_folder_path):
        newzip.write(filename, filename[len(config["server_folder"]) + 1:])
    print "Successfully made %s" % backup_name

if __name__ == "__main__":
  main()
