# Google Calendar Parsing 
This repo contains the code to parse an ICS file. One can use the calendar data from gmail to create a csv file which will have the following structure:


| name | begin | end | duration |
|------|-------|-----|----------|
| Name of event | DD-MM-YYYY H:M:S  |DD-MM-YYYY H:M:S  | seconds  | 

## How to use the code?

1. Download/clone the repo
2. Use requirements.txt to install the dependencies 
3. Download the ICS file from your [gmail account](https://support.google.com/calendar/answer/37111?hl=en) 
4. Now use the `parser.py` file
   - In your terminal cd to `app/src`
   - Run `python parser.py`
   - Now give the path to the ICS file you downloaded in 3
   - And give the path where you want to save the csv file
   - You will see a file named `calendar.csv` at the path entered above