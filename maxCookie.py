def countCookieOccurance(cookie, counter):
  if cookie not in counter:
    counter[cookie] = 1
  else:
    counter[cookie] += 1

def findMaxCookies(counter):
  max_value = max(counter.values())
 
  keys_with_max_val = [key for key,val in counter.items() if val == max_value]

  print ("\n".join(keys_with_max_val))