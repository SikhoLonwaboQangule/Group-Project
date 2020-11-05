import calendar_update as check

def check_calendar():
    #function to check the calendar is up to date before passing it on to the 
    #rest of the functions in the program makes use of calendar update to check 
    #and update the current calendar
    checked = False
    while 1:
        if checked:
            convert()
            break
        else:
            checked = check.controller()


def convert():
    #takes the calendar in its request format and converst it into readbale text
    #for the user before passing it on to the printer to display or store the 
    #data
    for days in calendar:
        #convert here
    display(converted_calendar)


def display(converted_calendar):
    #gets the converted data and presents it to the user in the way we decide later
    #for now in place of a groupd decision lets just print it out into terminal
    pass