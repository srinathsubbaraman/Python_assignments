'''
Name 	:time.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question: If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
'''

start =6+52/60.0
easy_pace =((8+15/60.0)/60.0)*2
tempo_pace =((7+12/60.0)/60.0)*3
total_run =easy_pace+tempo_pace
breakfast_hr=start+total_run
break_min=(breakfast_hr-int(breakfast_hr))*60
print "break fast time is",int(breakfast_hr),':',int(break_min)