from replit import db
from time import sleep
from keep_alive import keep_alive
from tweet import tweet

# db["DAYS"] = 156


caption = "Days Until Khedira’s Contract Ends\n\n{}"

DAYS = db["DAYS"]


keep_alive()

while True:
  try:
    tweet(caption.format(DAYS))
    DAYS = DAYS - 1
    db["DAYS"] = DAYS
    if(DAYS == 0) : break
    sleep(86400)
  except:
    print('error')