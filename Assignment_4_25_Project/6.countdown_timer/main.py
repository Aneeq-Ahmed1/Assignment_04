import time

def countdown_timer(seconds):

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_format, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    seconds = int(input("Enter the time in seconds: "))
    countdown_timer(seconds)

