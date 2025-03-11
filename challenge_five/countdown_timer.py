import time

def countdown_timer(seconds):

    while seconds > 0:
        mins,secs = divmod(seconds,60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -=1

number = int(input("Enter the seconds to onn countdown: "))
countdown_timer(number)        