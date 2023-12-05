import re
symbol_list=["*","%","/","$","@","&","-","+","#","="]
li=[]
num_list=[]
lines=[]
total=0

with open("day_3_input.txt","r") as file:

    for i,line in enumerate(file):
        line=".."+line+".."
        lines.append(line)
    for i,line in enumerate(lines):
        asts=re.finditer("\*",line)
        for ast in asts:
            this_line=lines[i][ast.span()[0]-1:ast.span()[1]+1]
            above=lines[i-1][ast.span()[0]-1:ast.span()[1]+1]
            below=lines[i+1][ast.span()[0]-1:ast.span()[1]+1]
            print(above)
            print(this_line)
            print(below)
            st=above+below+this_line
            a=re.search("[0-9]",above)
            t=re.search("[0-9]",this_line)
            b=re.search("[0-9]",below)
            if  a or t or b:
                print("True")
                ra=[]
                if a:
                    new_above=lines[i-1][ast.span()[0]-2:ast.span()[1]+2]
                    for y in re.finditer("[0-9]*",new_above):
                        if y.group()!="":
                            ra.append(int(y.group()))
                if t:
                    new_this_line=lines[i][ast.span()[0]-2:ast.span()[1]+2]
                    for y in re.finditer("[0-9]*",new_this_line):
                        if y.group()!="":
                            ra.append(int(y.group()))
                if b:
                    new_below=lines[i+1][ast.span()[0]-2:ast.span()[1]+2]
                    for y in re.finditer("[0-9]*",new_below):
                        if y.group()!="":
                            ra.append(int(y.group()))
                if len(ra)>1:
                    print(f"ra: {ra[0]}, {ra[1]}")
                    num=ra[0]*ra[1]
                    print(f"num={num}")
                    total+=num


print(total)