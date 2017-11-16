import time
print("What is your name; ")
name = input()
hour = time.localtime().tm_hour
if hour < 14:
	print("Good morning", name)
else:
	print("Good afternoon", name)
wait = 3
time.sleep(wait)
answer = 42
print("The Answer is...", answer)
