import re
colors=["red","green","blue"]
maxes=[12,13,14]
sum=0
psum=0
with open("day_2_input.txt","r") as file:
    game_objs=[]
    for q,line in enumerate(file):
        id=int(line.split("Game ")[1].split(":")[0])
        line=line.split(":")[1]
        games=line.split(";")
        game_obj={"id":id,"possible":True}
        for color in colors:
            game_obj[color]=0
        for j,round in enumerate(games):
            splits=round.split(",")
            for split in splits:
                num=re.findall("[0-9]*",split)
                #print(num)
                for color in colors:
                    #print(f"{color} {split}")
                    if split.find(color)!=-1:
                        split_color=color
                print(f"{split}, {split_color}, {max(num)}")
                game_obj[split_color]=max(int(max(num)),game_obj[split_color])
        game_objs.append(game_obj)
        for w,color in enumerate(colors):
            if game_obj[color]>maxes[w]:
                game_obj["possible"]=False
        if game_obj["possible"]:
            sum+=id
            print(sum)
        print(game_obj)
        power=game_obj["red"]*game_obj["green"]*game_obj["blue"]
        psum+=power
    print(sum)
    print(psum)
            
