
import os
import time
from datetime import datetime

s=int(input("Enter Hour For Shutdown :"))
m=int(input("Enter Minute of Hour For Shutdown :"))

print("⏳ Waiting for scheduled shutdown...")

while True:
    now = datetime.now()
    if now.hour == s and now.minute == m:
        print("Time matched! Shutting down now...")
        os.system("shutdown /s /t 0") 
        break
    time.sleep(10) 
