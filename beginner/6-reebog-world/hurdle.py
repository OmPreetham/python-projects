def jump():
    turn_right()
    move()
    turn_right()
    move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        jump()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
    