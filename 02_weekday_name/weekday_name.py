def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days_dict = {'Sunday':1, 'Monday':2, 'Tuesday':3, 'Wednesday':4,'Thursday':5, 'Friday':6, 'Saturday':7}

    if day_of_week in days_dict:
        return days_dict[day_of_week]
    else:
        return None


weekday_name(1)