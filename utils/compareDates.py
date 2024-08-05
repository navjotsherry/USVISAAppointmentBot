import datetime
from config import current_appointment

def compareDates(first_available_date):
    print("Current Appointment: ", current_appointment)
    print("First Available Appointment: ", first_available_date)

    if current_appointment == None:
        print("Current Appointment is not available")
        return
    
    if first_available_date == None:
        print("First Available Appointment is not available")
        return

    formatted_current_appointment = datetime.strptime(current_appointment, '%d %B, %Y')
    formatted_first_available_date = datetime.strptime(first_available_date, '%Y-%m-%d')

    if formatted_current_appointment < formatted_first_available_date:
        print("New Appointment is not available")   
    else:
        print("New Appointment is available on: ", first_available_date)

