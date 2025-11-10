def breakdown_time(seconds):

    if type(seconds) != int or seconds < 0:
        return -1
    if seconds == 0:
        return {}
    
    time_dict = {}
    
    hours = seconds // 3600 
    if hours > 0:
        time_dict[3600] = hours
    seconds = seconds % 3600
    
    minutes = seconds // 60
    if minutes > 0:
        time_dict[60]= minutes
    seconds = seconds % 60
    
    if seconds > 0:
        time_dict[1] = seconds
        
    return time_dict