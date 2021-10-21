#!/usr/bin/env python

# Import the library
import argparse
import os.path

from maxCookie import findMaxCookies
from searchCookie import readCSV

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type=argparse.FileType('r'))
  parser.add_argument('-d', action='store')

  args = parser.parse_args()
  fileName, timeStamp = str(args.file.name), str(args.d)
  counter = {}
  file_exists = os.path.exists(fileName)

  if file_exists:
    readCSV(fileName, timeStamp, counter)
    if len(counter) > 0:
      findMaxCookies(counter)
    else:
      print("No cookie found")
  else:
    print ("File not found")




main()