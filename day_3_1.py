import re
symbol_list=["*","%","/","$","@","&","-","+","#","="]
li=[]
num_list=[]
lines=[]
total=0
with open("day_3_input.txt","r") as file:
    for line in file:
        #print(line)
        line ="."+line+"."
        s_line=[]
        #symbols=re.search("%",line)
        nums=re.finditer(r'[0-9]*',line)
        """for num in nums:
             print(num.string[num.span()[0]:num.span()[1]])
        """
        lines.append(line)
            
        for symbol in symbol_list:
            symbols=re.search(f"\{symbol}",line)
            symbols=[m.start() for m in re.finditer(f"\{symbol}",line)]
            for s in symbols:
                s_line.append(s)
        #print(s_line)
        li.append(s_line)
        num_list.append(nums)
    
    for i,num_line in enumerate(num_list):
        for num_obj in num_line:
            #print(num_obj)
            try:
                num=int(num_obj.string[num_obj.span()[0]:num_obj.span()[1]])
                good=False
                this_line=lines[i][num_obj.span()[0]-1:num_obj.span()[1]+1]
                above=lines[i-1][num_obj.span()[0]-1:num_obj.span()[1]+1]
                below=lines[i+1][num_obj.span()[0]-1:num_obj.span()[1]+1]
                
                for symbol in symbol_list:
                        if symbol in this_line or symbol in above or symbol in below:
                            good=True
                if good != True:
                    print(above)
                    print(this_line)
                    print(below)
                    print(f"{num}, {good}")   
                if good:
                    total+=num
            except:
                pass
    #print(li)
print(total)