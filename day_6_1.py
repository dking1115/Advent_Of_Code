with open("day_6_input.txt","r") as file:
    lines=[]
    for i in file:  
        lines.append(i)
    times_split=lines[0].split(" ")
    times=[]
    for time in times_split:
        try:
            time_int=int(time)
            times.append(time_int)
        except:
            pass
    dists_split=lines[1].split(" ")
    dists=[]
    for time in dists_split:
        try:
            time_int=int(time)
            dists.append(time_int)
        except:
            pass
    
    print(dists)
    total=1
    for time,dist in zip(times,dists):
        wins=0
        for i in range(time):
            speed=i
            d=speed*(time-i)
            if d>dist:
                wins+=1
        total*=wins
    print(total)
        