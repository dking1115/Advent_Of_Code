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
    print(nums)
    init_seeds=lines[0].split(":")[1].split(" ")
    #print(init_seeds)
    init_seeds_ints=[int(q) for q in init_seeds if q !=""]
    seed_soil=[]
    for i in range(nums[0],nums[1]-2):
        print(i)
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        seed_soil.append(int_vals)
    print(f"Seed_soil:{seed_soil}")
    soil_fert=[]
    for i in range(nums[1],nums[2]-2):
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        soil_fert.append(int_vals)
    print(f"soil_fert:{soil_fert}")
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
    print(f"from {nums[6]} to {len(lines)}")
    for i in range(nums[6],len(lines)):
        line=lines[i]
        vals=line.split(" ")
        int_vals=[int(q) for q in vals]
        #print(int_vals)
        hum_location.append(int_vals)
    
    print(f"hum_location{hum_location}")



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
    print(water_light)
    locations=[]
    for seed in init_seeds_ints:
        print(f"Seed:{seed}")
        soil=check(seed,seed_soil)
        print(f"Soil:{soil}")
        fert=check(soil,soil_fert)
        print(f"Fert:{fert}")
        water=check(fert,fert_water)
        print(f"Water:{water}")
        light=check(water,water_light)
        print(f"Light:{light}")
        temp=check(light,light_temp)
        print(f"Temp:{temp}")
        hum=check(temp,temp_hum)
        print(f"Hum:{hum}")
        location=check(hum,hum_location)
        print(f"Location:{location}")
        locations.append(location)
    
    print(min(locations))