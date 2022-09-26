#this should be a executeable python script that checks for temp and writes it to "txt.txt" every 20 seconds
#if program doesnt compile make sure and go over the errors and find if the parentheses are not in the wrong spot
a=1
def temptest():
	while(a==1):
		import time
		import os

		def checktemp():
			cputmp = os.popen("vcgencmd measure_temp").readline()
			return checktemp
                        print(checktemp)
		def timer():
			timed = os.popen("date").readline()
			return timer
                        print(timer)

		outputt = (checktemp() + "@" timer() )

		print(outputt)

		text_file = open("home/pi/Documets/txt.txt" "a")

		text_file.write("\n")

		text_file.write(outputt)
		#does outputt need a ""

		text_file.close()

		sleep(20)

temptest()
