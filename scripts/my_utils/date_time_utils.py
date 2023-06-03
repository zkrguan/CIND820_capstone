from datetime import datetime

def convert_to_time_of_day(date_format:str,date_string:str):
    date_object = datetime.strptime(date_string,date_format)
    hour = date_object.hour
    if hour>= 0 and hour <6:
        return "dawn"
    elif 6 <= hour < 12:
        return "morning"
    elif 12<= hour <18:
        return "afternoon"
    else: 
        return "evening"


__all__ = ['convert_to_time_of_day']