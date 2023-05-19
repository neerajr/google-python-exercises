#!/usr/bin/python`:
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(directory):
  specfiles = []
  files = os.listdir(directory)
  for fil in files:
    match = re.search(r'__(\w+)__' , fil)
    if match:
      specfiles.append(os.path.abspath(os.path.join(directory, fil)))
 # print specfiles
  return specfiles

def copy_to(paths, dir1):
  if not os.path.exists(dir1):
    os.mkdir(dir1)
  for path in paths:
    fil = os.path.basename(path)
    shutil.copy(path, os.path.join(dir1, fil))


def zip_to(paths,zippath):
  zipcomand = 'zip -j ' + zippath + ' ' .join(paths)
  print 'Im going to do' +zipcomand
  

  (status, output) = commands.getstatusoutput(zipcomand) 
  if status:
    sys.stderr.write(output)
    sys.exit(1)







def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  for directory in args:
    paths.extend(get_special_paths(directory))

  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    print '\n'.join(paths)

  
if __name__ == "__main__":
  main()
