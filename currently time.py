import os
import datetime
import time
while True:
    now = datetime.datetime.now()
    current_time = datetime.datetime.now().strftime("%I : %M :%S %p")
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("Date Of day is: ", now.strftime("%d/%m/%Y"))
    print("Current time : ", current_time)
    time.sleep(1)
