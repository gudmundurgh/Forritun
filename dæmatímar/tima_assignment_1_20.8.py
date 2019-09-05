secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
# 60 sec í mín
# 3600 sec in hour
# minutes =
# seconds =
# hours = 
hours = secs_int // 3600
#sec used in hours
used_secs_in_hours = hours * 3600
#sec  
secs_left_for_minutes = secs_int - used_secs_in_hours
# minutes =
minutes = secs_left_for_minutes // 60
#sec left
seconds = secs_int % 60
print(hours,":",minutes,":",seconds) # do not change this line


