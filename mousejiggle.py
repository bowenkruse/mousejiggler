import os
import time
import argparse
import pyautogui

def timer(minutes_awake):
    counter = 0
    time_start = time.strftime('%d-%b-%Y_%H-%M-%S', time.localtime())
    print(time_start)
    while counter < minutes_awake:
        time.sleep(5)
        pyautogui.click(button='right')
        counter = counter + 1
    time_end = time.strftime('%d-%b-%Y_%H-%M-%S', time.localtime())
    print(time_end)

    file = open("timelogs.txt", "w")
    file.write('Start at {}\n'.format(time_start))
    file.write('End at {}\n'.format(time_end))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", help="Enter time in minutes")
    args = parser.parse_args()
    if args.time:
        timer(int(args.time))
