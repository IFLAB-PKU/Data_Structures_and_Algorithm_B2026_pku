def move_plate(num_plate, tower1, tower2, tower3): 
    # move the num_plate plates from tower1 to tower2
    if num_plate == 2:
        print(f"1:{tower1}->{tower3}")
        print(f"2:{tower1}->{tower2}")
        print(f"1:{tower3}->{tower2}")
        return
    
    if num_plate == 1:
        print(f"1:{tower1}->{tower2}")
        return
    
    # 1->3
    move_plate(num_plate-1, tower1, tower3, tower2)
    # 1->2
    print(f"{num_plate}:{tower1}->{tower2}")
    # 3->2
    move_plate(num_plate-1, tower3, tower2, tower1)
    return


num_plate, tower1, tower2, tower3 = input().split()
num_plate = int(num_plate)
move_plate(num_plate, tower1, tower3, tower2)