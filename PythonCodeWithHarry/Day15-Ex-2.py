# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.
import time
c_hour = time.localtime().tm_hour

NowTime = time.strftime('%I:%M:%S.%p')
if  5 <= c_hour < 12:
 print("Good Morning",NowTime) 
elif  12 <= c_hour < 17:
  print("Good AfterNooN",NowTime) 
elif 17 <= c_hour < 21:
 print("Good Evening",NowTime)   
else:
    print("Good Night!", NowTime) 