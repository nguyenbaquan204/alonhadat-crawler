import time
import datetime
from alonhadat import collect_data  

def main_loop():
    while True:
        now = datetime.datetime.now()  
        print(f"Thời gian hiện tại: {now.strftime('%H:%M:%S')}")
        if now.hour == 23 and now.minute == 21 and now.second == 0:
            print("Đến giờ tra cứu")
            collect_data()  
            print("Tra cứu hoàn tất.\n")
        time.sleep(1)

if __name__ == "__main__":
    main_loop()
