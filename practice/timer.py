import time


while(True):
    #these update every second
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    seconds = time.localtime().tm_sec

    print(f"\r{hour}:{minute}:{seconds}", end = '', flush = True)
    
    time.sleep(1)

    

