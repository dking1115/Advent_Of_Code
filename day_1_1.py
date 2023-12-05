sums=[]
total=0
with open("day_1_input.txt","r") as file:
    for line in file:
        x=[]
        for ch in line:
            try:
                i=int(ch)
                x.append(i)
            except:
                pass
        print(x)
        sum=x[0]*10+x[-1]
        sums.append(sum)
        total+=sum
print(sums)
print(total)