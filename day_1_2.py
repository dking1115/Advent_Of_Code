sums=[]
total=0
nums={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
with open("day_1_input.txt","r") as file:
    for line in file:
        x=[]
        print(line)
        digits=[None]*len(line)
        for key in nums.keys():
            #line=line.replace(key,str(nums[key]))
            pos=-1
            start=0
            poss=[]
            for i in range(10):
                if pos!=-1:
                    start=pos+len(key)
                pos=line.find(key,start,-1)
                if pos!=-1:
                    digits[pos]=nums[key]
        for q,ch in enumerate(line):
            i=digits[q]
            if i:
                x.append(i)
            try:
                i=int(ch)
                x.append(i)
            except:
                pass
        print(x)
        sum=x[0]*10+x[-1]
        print(sum)
        sums.append(sum)
        total+=sum
#print(sums)
print(total)