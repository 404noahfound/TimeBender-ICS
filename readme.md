# TimeBender-ICS

This project allows you to convert a plain text schedule into an ICS file that can be imported into various calendar applications such as Google Calendar or Apple Calendar.

## Input Format

The input should be a plain text file with the following format:

1. The first line should contain the date and day of the week in the format `Date: Month DD, YYYY (Day)`.
2. The second line should be empty.
3. The remaining lines should contain the events in the format `HH:MM - HH:MM: Event description`.

### Sample Input

Date: March 19, 2023 (Sunday)

09:00 - 09:30: Wake up and morning routine
09:30 - 09:50: Have breakfast
09:50 - 10:50: 1-hour gym session at home
10:50 - 11:20: Shower and get dressed
12:00 - 13:15: Cook and have lunch
13:15 - 14:15: MIT open course Finance Theory I (https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/introduction-and-course-overview/)
14:15 - 18:15: Free time (play games, hobbies, etc.)
18:15 - 19:30: Cook and have dinner
19:30 - 20:30: Call family
20:30 - 22:15: Wind down and prepare for bedtime
22:15 - 23:15: Shower and brush teeth
23:15 - 23:30: Relaxation or self-care activity

## Usage

1. Create a plain text file with your schedule following the input format described above.
2. Run the Python script `schedule_to_ics.py` with the text file as input.
3. The script will generate an ICS file with the same date as in the input file.

For example, if your input file is named `schedule.txt`, you can run the script as follows:

`python schedule_to_ics.py schedule.txt`

The script will generate an ICS file named `YYYY-MM-DD_schedule.ics`, which can be imported into your preferred calendar application.


Please note that you will need to install the icalendar package for this script to work. You can install it using pip:

pip install icalendar