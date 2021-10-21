import csv


from maxCookie import countCookieOccurance

def readCSV(fileName, timeStamp, counter):
  with open(fileName, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row['timestamp'].split('T')[0] == timeStamp:
        countCookieOccurance(row['cookie'], counter)
