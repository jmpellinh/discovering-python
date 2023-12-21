weight = 1
total_weight = 0
count_weight = 0
while weight > 0:
    weight = float(input ("please input your weight, or 0 to stop: "))
    total_weight += weight
    if weight > 0:
        count_weight += 1

average_weight = total_weight/count_weight
print ("Your average weight is:", average_weight)
    
        
