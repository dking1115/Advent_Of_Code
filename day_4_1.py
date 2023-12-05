total=0
with open("day_4_input.txt","r") as file:
    
    for line in file:
        card_total=0
        sp=line.split(":")
        sp_2=sp[1].split("|")
        win_st=sp_2[0].split(" ")
        win_int=[]
        for i in win_st:
            try: 
                win_int.append(int(i))
            except:
                pass
        check_st=sp_2[1].split(" ")
        check_int=[]
        for i in check_st:
            try: 
                check_int.append(int(i))
            except:
                pass
        #print(win_int)
        for i in check_int:
            win=False
            for j in win_int:
                #print(f" {i}, {j} {win}")
                if i==j:
                    win=True
            if win:
                card_total+=1
        points=0
        if card_total>0:
            points=1
        if card_total>1:
            points=points*(2**(card_total-1))
        total+=points
    print(total)