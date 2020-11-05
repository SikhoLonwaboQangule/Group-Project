def check_slot(day, start_time):
    #request if a slot is available to be volunteered by a volunteer
    #return true or false
    pass


def already_booked(day, start_time):
    #tells user its booked and can't book that slot
    pass


def book_slot(day, start_time):
    #books the slot
    pass


def get_date():
    #gets date and time from the user to book the session
    return day, start_time


def main():
    #runs the program
    day, start_time = get_date
    if check_slot(day,start_time):
        book_slot(day, start_time)
    else:
        already_booked(day, start_time)