with open("day_5_input.txt","r") as file:
    lines=[]
    for line in file:
        lines.append(line)
    sts=["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]
    nums=[0]*len(sts)
    for i,line in enumerate(lines):
        for q,st in enumerate(sts):
            if st in line:
                nums[q]=i+1
    #print(nums)
    init_seeds=lines[0].split(":")[1].split(" ")

    #print(init_seeds)
    init_seeds_ints=[int(q) for q in init_seeds if q !=""]
    new_init_seeds_ints=[]
    """for i in range(0,len(init_seeds_ints),2):
        for q in range(init_seeds_ints[i],init_seeds_ints[i]+init_seeds_ints[i+1]):
            new_init_seeds_ints.append(q)"""
    seed_ranges=[]
    for i in range(0,len(init_seeds_ints),2):
        t=[init_seeds_ints[i],init_seeds_ints[i+1]]
        seed_ranges.append(t)
    #print(f"length of new seeds {len(new_init_seeds_ints)}")
    seed_soil=[]
    for i in range(nums[0],nums[1]-2):
        #print(i)
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        seed_soil.append(int_vals)
    #print(f"Seed_soil:{seed_soil}")
    soil_fert=[]
    for i in range(nums[1],nums[2]-2):
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        soil_fert.append(int_vals)
    #print(f"soil_fert:{soil_fert}")
    fert_water=[]
    for i in range(nums[2],nums[3]-2):
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        fert_water.append(int_vals)
    
    water_light=[]
    for i in range(nums[3],nums[4]-2):
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        water_light.append(int_vals)
    
    light_temp=[]
    for i in range(nums[4],nums[5]-2):
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        light_temp.append(int_vals)
    
    temp_hum=[]
    for i in range(nums[5],nums[6]-2):
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        temp_hum.append(int_vals)
    
    hum_location=[]
    #print(f"from {nums[6]} to {len(lines)}")
    for i in range(nums[6],len(lines)):
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        hum_location.append(int_vals)
    
    #print(f"hum_location{hum_location}")

    rules=[seed_soil,soil_fert,fert_water,water_light,light_temp,temp_hum,hum_location]
    for rule in rules:
        for i in rule:
            out_start=i[0]
            in_start=i[1]
            length=i[2]
            i[0]=in_start
            i[1]=out_start

    def in_range(num):
        for i in seed_ranges:
            if num>=i[0] and num<i[0]+i[1]:
                return True
        return False

    def check(inp,arr):
        out=None
        for i in arr:
            if inp>=i[1] and inp<=i[1]+i[2]-1:
                out=(inp-i[1])+i[0]
                break
        if not out:
            out=inp
        #print(f"Input: {inp}, Output: {out}")
        return out
    done=False
    #i=0
    i=6310000
    while True:
        num=i
        if done:
            break
        print(i)
        for q in range(len(rules)-1,-1,-1):
            #print(q)
            
            num=check(num,rules[q])
            #print(f"q:{q}, num:{num}")
        #print(f"Checking range:{num}")
        if in_range(num):
            print(f"Done:{i}")
            done=True
        i+=1
        #print(f"num:{num}")
    #print(water_light)