import time
import datetime
import subprocess

def wait_and_run():
    while True:
        now = datetime.datetime.now()
        if now.hour == 6 and now.minute == 0:
            print("🕕 Đang thu thập dữ liệu...")
            subprocess.run(["python", "alonhadat.py", "ha-noi", "nha"])
            time.sleep(86400)  # đợi 24h
        else:
            time.sleep(30)  # kiểm tra mỗi 30s

if __name__ == "__main__":
    wait_and_run()
