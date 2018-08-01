from time import sleep
seconds = 0
miliseconds = 0

while 0 != currentY:
    time.sleep(0.001)
    miliseconds = miliseconds + 1
    if miliseconds = 1000:
        seconds = seconds + 1
        miliseconds = 0
    print(seconds, "seconds and", miliseconds, "miliseconds")
