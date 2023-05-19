#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename, 'r')
  text = f.read()
 # print text
  extract = []
  match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
  if not match:
    print("MATCH ERROR")
    sys.exit(0)
  year = match.group()
  extract.append(year)
#  print extract

  name = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
 # print name
  name_data = {}
  for name_rank in name:
   # if name_rank[1] not in name_data:
    #  name_data[name_rank[1]] = name_rank[0]
    #if name_rank[2] not in name_data:
    #  name_data[name_rank[2]] = name_rank[0]
    (rank, name1, name2) = name_rank
    if name1 not in name_data:
      name_data[name1] = rank
    if name2 not in name_data:
      name_data[name2] = rank

  name_list = sorted(name_data.keys())
 # print name_list
  for names in name_list:
    extract.append(names + " " + name_data[names])
  return extract


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    result = extract_names(filename)
    list_summary = '\n'. join(result)
  if summary:
    f2 = open(filename + '.summary' , 'w')
    f2.write(list_summary + '\n')
    f2.close()
  else:
    print list_summary
  
if __name__ == '__main__':
  main()
