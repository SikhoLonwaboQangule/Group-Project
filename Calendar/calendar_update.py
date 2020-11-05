def check_day():
    #function to check if each day is updated handled through a request to the 
    #api do this for each day as 1 we will store it as seperate days and 2 less 
    #data will need to be updated as if only 1 day is out of date 1 day gets 
    #updated 3 easy to expand the system to handle more less then 7 days if we 
    #store each day in its own unique file
    pass


def get_update(day_list):
    #takes a list of days that need to be updated if non it does nothing
    #changes each day with the new data that it gets from a request from the api
    #returns a variable to the main to return to calendar viewer so it knows its 
    #updated
    while day_list:
        current_day = day_list[0]
        day_list.remover(day_list[0])
        #reqeust the current days data and then loop again
    return True


def controller():
    #directs all the functions in the program to do there job accordinly
    day_list = check_day()
    updated = get_update(day_list)
    return updated
