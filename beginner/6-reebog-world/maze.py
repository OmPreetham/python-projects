while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
            move()
    elif wall_on_right():
        turn_left()