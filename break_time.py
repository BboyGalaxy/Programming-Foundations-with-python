import webbrowser
import time

total_breaks = 3
count = 0

print "This program started at " + time.ctime()
while(count < total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=CTFtOOh47oo")
	count += 1
