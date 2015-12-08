#!/usr/bin/python
# This script handles the backing up of the Minecraft worlds and is scheduled
# to run as a cronjob.
# Author: Alvin Lin (alvin.lin.dev@gmail.com)

import datetime
import json
import os
import zipfile

def get_config():
  config = None
  with open('config.json') as config_file:
    config = json.loads(config_file.read())
  return config

def list_files_all(path):
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
  today = datetime.datetime.today()
  return today.strftime(worldname + "_%m-%d-%Y_%H-%M-%S.zip")

def main():
  config = get_config()
  for world in config['worlds']:
    full_backup_path = '%s/%s' % (config['backups_folder'],
                                  get_backup_name(world))
    with zipfile.ZipFile(full_backup_path, 'w') as newzip:
      full_world_path = '%s/%s' % (config['server_folder'], world)
      for filename in list_files_all(full_world_path):
        newzip.write(filename, filename[len(config['server_folder']) + 1:])

if __name__ == '__main__':
  main()
