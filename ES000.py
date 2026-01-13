from datetime import datetime, timedelta
from time import sleep

start_time = datetime.now()
now_time = datetime.now()
cont = 0
while(now_time <start_time + timedelta(minutes=1)):
    cont = cont + 1
    print(f"{cont}: Hello from the ISS")
    sleep(1)
    now_time = datetime.now()