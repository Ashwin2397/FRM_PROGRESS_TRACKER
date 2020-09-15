for i in range(2,5):
    file_name="book"+str(i)+"_intensity.txt"
    with open(file_name,"r") as ip:
        redundant_count=0
        for line in ip:
            if "REDUNDANT" in line:
                redundant_count+=1

    with open(file_name,"a+") as ip:
        ip.write("REDUNDANT: "+str(redundant_count))
        
