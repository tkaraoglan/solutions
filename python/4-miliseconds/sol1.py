def convert(millisecond):
    hour_in_milisecond = 60*60*100
    hours = millisecond // hour_in_milisecond
    millisecond_left = millisecond % hour_in_milisecond
    minute_in_millisecond = 60*1000
    minutes = millisecond_left // minute_in_millisecond
    millisecond_left %= minute_in_millisecond
    seconds = millisecond_left//1000

    return f"{hours} hour/s"*(hours!=0) + f"{minutes} minute/s"*(minutes!=0) + f" {seconds} second/s"*(seconds!=0) or f" just {millisecond} millisecond/s"