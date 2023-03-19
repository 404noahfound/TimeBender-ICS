import re
from datetime import datetime, timedelta
from icalendar import Calendar, Event


def read_schedule_from_txt(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    schedule = []
    date_line = data[0].strip()
    date = datetime.strptime(date_line.split(': ')[1], '%B %d, %Y (%A)')

    for line in data[2:]:
        time_range, description = line.strip().split(': ', 1)
        start_time, end_time = time_range.split(' - ')
        schedule.append({
            'start_time': start_time,
            'end_time': end_time,
            'description': description
        })

    return date, schedule


def generate_ics_file(date, schedule):
    cal = Calendar()
    cal.add('prodid', '-//Schedule to ICS converter//example.com//')
    cal.add('version', '2.0')

    for event_data in schedule:
        start_datetime = datetime.strptime(event_data['start_time'], '%H:%M')
        end_datetime = datetime.strptime(event_data['end_time'], '%H:%M')
        start_datetime = date + \
            timedelta(hours=start_datetime.hour, minutes=start_datetime.minute)
        end_datetime = date + \
            timedelta(hours=end_datetime.hour, minutes=end_datetime.minute)

        event = Event()
        event.add('summary', event_data['description'])
        event.add('dtstart', start_datetime)
        event.add('dtend', end_datetime)
        cal.add_component(event)

    output_file = f"{date.strftime('%Y-%m-%d')}_schedule.ics"
    with open(output_file, 'wb') as f:
        f.write(cal.to_ical())

    print(f"Conversion successful! Output file: {output_file}")


if __name__ == '__main__':
    input_file = 'schedule.txt'  # Replace with your text file containing the schedule

    date, schedule = read_schedule_from_txt(input_file)
    generate_ics_file(date, schedule)
