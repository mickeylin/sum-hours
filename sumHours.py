#!/usr/bin/env python3
import sys
import argparse
from datetime import datetime


def setArgparse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'logDir',
        type=str,
        help="Log file dir"
    )
    args = parser.parse_args()
    return args


def parseLog(logDir):
    sumHours = 0
    f = open(logDir+"/zjlin", "r")
    now = datetime.now()
    for line in f:
        logObj = line.split()
        hour = logObj[2][1:]
        logTime = datetime.strptime(logObj[0], '%Y/%m/%d')
        if logTime.year == now.year and logTime.month == now.month:
            print(line,end="")
            sumHours = sumHours + float(hour)
    print("zjlin's hours: {}".format(round(sumHours, 2)))

if __name__ == "__main__":
    args = setArgparse()
    parseLog(args.logDir)
