import datetime
import requests

now = datetime.datetime.now()

with open('time.txt', 'a') as f:
        f.write(str(now))
        f.write('\n')