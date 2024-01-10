In the Reebort World challenges given in this module:

 Hurdle 4: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
 
 and 
 
 Maze: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


 My python code solution was: 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
while not at_goal():
    if front_is_clear():
        move()
        turn_right()
    else:
        turn_left