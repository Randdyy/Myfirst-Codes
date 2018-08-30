import datetime
while True:
    user_input=str(input("input on to begin")).lower().strip()
    if user_input == "on":
        start_time = datetime.datetime.now()
        break
    else :
        print("only on to start")
        continue

while True:
    user_off = str(input("input off to stop")).lower().strip()
    if user_off == "off":
        end_time=datetime.datetime.now()
        break
    else:
        print("only off to stop")
        continue
final_time = (end_time-start_time).seconds
print(final_time)
        
