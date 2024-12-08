
game_state = {"seventy_chickens": False, "chicken_key": False, 
              "comedy_club_new": True, "comedian_alive": True, "lifeforce": True, "comedian_dying": False, "gushers": False, 
              "kissing_cousins": True, "cousins_distracted": False, "sex_key": False, "big_naturals": False, "dildo": False, 
              "fat_hitler": True, "hitler_new": True, "nanny_new": True, 
              "racist": True, "n_word_new": True, "hallway_new": True, "sex_doll": False, "congress_new": True,
              "tummyache": False, "flames": True}


print("Dungeon Escape: Feel the Wet")
print("Feel the wet dungeon suck fest: party in your pants?")
input("Press Enter")
print("Yeah that's right, bitch. You do what you're told.")
input()

#start parameters
origin = ["You wake up in a dungeon."]

origin_description = ["To your left and right are two hallways. Behind you are two locked doors. In the center of the room is a screaming pit of fire."]
final_origin_description = ["To your left and right are two hallways. Behind you are two locked doors. In the center of the room is a screaming pit of fire. You have a tummyache from all the gushers."]

choices = ["What would you like to do?", "1. Go left", "2. Go right", "3. Stare into pit", "4. Jump into pit"]
choices2 = ["What would you like to do?", "1. Go left", "2. Go right", "3. Stare into pit", "4. Jump into pit", "5. Puke", "6. Puke into flame pit"]

go_back = ["You find yourself in a dungeon."]

#start game
def start(a, b=[], c=[]):

    for item in a:
        print(item)
    
    if b:
        input()
        for item in b:
            print(item)
        
    if c:
        input()
        for item in c:
            print(item)
    
    start_choice = input(">")

    if start_choice in ["1","go left"]:
        chicken_room(chicken_room_origin, chicken_room_key, chicken_room_choices)
    elif start_choice in ["1","go left"] and game_state["chicken_key"] == True:
        chicken_room(chicken_room_origin, chicken_room_new_choices)
    elif start_choice in ["2","go right"]:
        costco()
    elif start_choice in ["3", "stare into pit"]:
        print("You see something glimmer in the flames.")
        start("")
    elif start_choice in ["4", "jump into pit"]:
        dead("You burn to death.")
    elif start_choice in ["5", "puke"] and game_state["tummyache"] == True:
        dead("You puke on the floor. You'll die in this dungeon.")
    elif start_choice in ["6", "puke into flame pit", "puke into flames"] and game_state["tummyache"] == True:
        print("You puke into the flame pit, putting out the fire. The puke fumes burn off your eyebrows.")
        game_state["flames"] = False
        input()
        print("At the bottom of the pit is a small key.")
        input()
        print("You take the key.")
        input()
        exit_dungeon()
    elif start_choice == "look around":
        start(origin_description)
    
    elif start_choice == "choices":
        start(choices)
    else:
        print("Nothing happens.")
        start("")

def exit_dungeon():
    print("Exit dungeon.")
    input()
    print("Congratulations! You escaped the dungeon.")
    dead("You find yourself in the MAGA apocalypse. A pipe bomb goes off and you die.")

#what happens when you die
def dead(a):
    print(a, "Great job!")

    dead_choice = input(">")

    if dead_choice in ["exit", "exit game", "quit", "quit game"]:
        exit(0)
    else:
        start(origin)

#chicken room

#chicken room parameters
chicken_room_origin = ["You find yourself in a chicken coop where chicken people are roosting."]
chicken_room_key = ["They have a shiny key carved from a chicken bone."]
chicken_room_again = ["You find yourself in a chicken coop where chicken people are roosting."]
chicken_room_choices = ["What would you like to do?", "1. Attack", "2. Talk", "3. Ask about key", "4. Go back"]
chicken_room_new_choices = ["What would you like to do?", "1. Attack", "2. Talk", "3. Go back"]

def chicken_room(a=[], b=[], c=[]):

    for item in a:
        print(item)

    if b:
        input()
        for item in b:
            print(item)

    if c:
        input()
        for item in c:
            print(item)
        if game_state["seventy_chickens"] == True:
            print("5. Give chickens")

    chicken_choice = input(">")
    
    if chicken_choice in ["1", "attack chicken people", "attack"]:
        dead("You are outnumbered. The chicken people kill you.")
    elif chicken_choice in ["2", "talk", "talk to them", "talk to chicken people"]:
        print("'Chicken Mommy wants to feel the wet.'")
        chicken_room("")
    elif chicken_choice in ["3", "ask about key", "ask", "key"] and game_state["chicken_key"] == False:
        print("Chicken Mommy wants 70 chickens in exchange for the key.")
        chicken_room("")
    elif chicken_choice in ["5", "give 70 chickens", "give chickens"] and game_state["seventy_chickens"] == True and game_state["chicken_key"] == False:
        print("You give Chicken Mommy the chickens, and she gives you the key.")
        game_state["chicken_key"] = True
        input()
        print("Chicken Mommy says: 'The door is by the eggs.'")
        chicken_room("")
    elif chicken_choice in ["4", "go back"]:
        start(go_back)
    elif chicken_choice == "3" and game_state["chicken_key"] == True:
        start(go_back)
    elif game_state["chicken_key"] == True:
        chicken_room(chicken_room_new_choices)
    else:
        chicken_room(chicken_room_choices)

     
#costco
def costco():
    print("You find yourself in a Costco.")
    input()
    print("What do you want to do?")
    print("1. Go shopping.")
    print("2. Go to poultry.")
    
    if game_state["chicken_key"] == True:
        print("3. Go to eggs")

    costco_choice = input(">")
    
    if costco_choice in ["1", "go shopping"]:
        dead("You get lost in the Costco. You give up and decide to live out your days here.")
    elif costco_choice == "go back":
        start()
    elif costco_choice in ["2", "go to poultry"]:
        chicken_line()
    elif costco_choice in ["3", "eggs", "go to eggs"] and game_state["chicken_key"] == True:
        egg_room(egg_room_intro, egg_room_choices)    
    else:
        print("Nothing happens.")
        costco()      

#chicken line
def chicken_line():
    print("You see a long line of people waiting for $5 rotisserie chickens. A Karen bosses people around and orders them to the back of the line.")
    
    while True:
        print("Do you (1) get in line or (2) cut the line?")
        chicken_line_choice = input(">")

        if chicken_line_choice in ["1", "get in line"]:
            dead("You wait in line for hours until finally you reach the front at closing time. They are out of chickens for the day. You die of starvation.")
        elif chicken_line_choice in ["2", "cut the line", "cut line", "cut"]:
            print("You stand back until the chickens start coming out. This is your moment.")
            input()
            print("You swoop in and ram your cart through the other shoppers. As you frantically load chickens into your cart, you see Karen in the corner of your eye flying at you in a fit of rage.")
            input()
            karen_fight()
        else:
            print("Nothing happens.")
        
#karen attacks you
def karen_fight():    
    print("Do you (1) ignore her or (2) fight back?")
    karen_choice = input(">")

    if karen_choice in ["1", "ignore her", "ignore"]:
        dead("Karen rips your face off and you die.")
    elif karen_choice in ["2", "fight back", "fight"]:
            print("You deliver a swift and decisive rear kick with the graceful strength of a drunken Clydesdale. The blow is fatal.")
            input()
            exit_line()

#exit lines at costco
def exit_line():
    print("You collect your chickens and make a mad dash for the registers. The lines are long, and the angry shoppers are gaining on you. Your chickens are at risk.")
    print("Do you (1) wait in line or (2) run?")

    line_choice = input(">")

    if line_choice in ["1", "wait in line", "wait"]:
        dead("The angry mob attack you and take all the chickens, killing you in the process.")

    elif line_choice in ["2", "run"]:
        print("You sprint to the exit. A 70-year-old woman stands by the door.")  
        input()
        print("Do you (1) stop to pay her or (2) keep running?")

        door_choice = input(">")

        if door_choice in ["1", "stop to pay her", "pay her", "pay"]:
            print("You hand her $350 cash and say “for Chicken Mommy.” She nods, understanding. You run out with your chickens.")
            game_state["seventy_chickens"] = True
            input()
            start(go_back)

        elif door_choice in ["2", "keep running"]:
            dead("The woman chases after you with a rifle. An expert marksman, she kills you with a perfect shot to the head.")
        
        else:
            dead("The angry mob attack you and take all the chickens, killing you in the process.")

#egg room
egg_room_intro = ["In the egg room you find a door decorated with chicken bones and feathers. No one else seems to notice it."]
egg_room_choices = ["What do you want to do?", "1. Open door", "2. Go back"]

def egg_room(a=[], b=[]):
    
    if a:
        for item in a:
            print(item)

    if b:
        input()
        for item in b:
            print(item)
        
        chicken_door_choice = input(">")

        if chicken_door_choice == ["2", "go back"]:
            costco()
        elif chicken_door_choice in ["1", "open door"]:
            comedy_club(comedy_club_origin, comedy_club_prompt, comedy_club_choices1, print_origin = True)
        else:
            print("Nothing happens.")
            egg_room(None, egg_room_choices) 
    
#comedy club

#"comedy_club_new": True, "comedian_alive": True, "gushers": False, "kissing_cousins": True,

#comedy club parameters

comedy_club_origin = ["You find yourself in a dingy comedy club."]
comedian_description = ["On stage a mediocre comedian does lazy crowd work to a room full of tourists."]
crowd_work = ["'Where are you from?'", "'What do you do?'", "'Any couples?'", "'What's your name?'"]
lifeforce_drain = ["The bad comedy drains your lifeforce. Your HP plummets to almost zero."]
comedy_club_prompt = ["What would you like to do?"] 
comedy_club_choices1 = ["1. Heckle comedian", "2. Go left", "3. Go back"] #if comedian alive and cousins true
comedy_club_choices2 = ["1. Eat gushers", "2. Go left", "3. Go back"] #f if comedian dead and gushers false
comedy_club_choices3 = ["1. Go left", "2. Go back"] #f if comedian dead and gushers true

def heckle_response():
    print("Comedian says: 'Oh wow - looks like we've got ourselves a comedian. Why don't you come up here and tell some jokes?'")
    input()
    dead("You go onstage and bomb so hard the building blows up, killing everyone inside.")

def eat_gushers():
    print("You eat all the gushers, replenishing your HP.")
    game_state["gushers"] = True
    input()
    comedy_club(a=comedy_club_origin, b=comedy_club_prompt, c=comedy_club_choices3, print_origin = False)

def comedian_death():
    print("You point out the incestuous cousins to the comedian.")
    input()
    print("'These are cousins AND a couple.'")
    input()
    print("Comedian says: 'Woah! Talk about getting in each other's jeans.'")
    input()
    print("The people do not laugh. They hate him.")
    input()
    print("Comedian says: 'Come on, people - I'm dying up here!'")
    input()
    print("Instantly the comedian explodes into thousands of gushers.")
    input()
    game_state["comedian_alive"] = False
    game_state["kissing_cousins"] = True
    comedy_club(a=comedy_club_origin, b=comedy_club_prompt, c=comedy_club_choices2, print_origin = False)

def comedy_club(a=None, b=None, c=None, print_origin = True):
    
    if print_origin and a:
        for item in a:
            print(item)
        input()

    if game_state["comedy_club_new"] == True:
        for item in comedian_description + crowd_work + lifeforce_drain:
            print(item)
            input()

    game_state["comedy_club_new"] = False

    if b:
        for item in comedy_club_prompt:
            print(item)

    if c:
        if game_state["comedian_alive"] == True and game_state["kissing_cousins"] == True:
            for item in comedy_club_choices1:
                print(item)
        elif game_state["comedian_alive"] == True and game_state["kissing_cousins"] == False:
            for item in comedy_club_choices1:
                print(item)
            print("4. Point out cousins")
        elif game_state["comedian_alive"] == False and game_state["gushers"] == False:
            for item in comedy_club_choices2:
                print(item)
        elif game_state["comedian_alive"] == False and game_state["gushers"] == True:
            for item in comedy_club_choices3:
                print(item)

    comedy_club_choice = input(">")
   
    if comedy_club_choice in ["1", "go left", "left"] and game_state["comedian_alive"] == False and game_state["gushers"] == True:
        living_room()
    elif comedy_club_choice in ["2", "go back", "back"] and game_state["comedian_alive"] == False and game_state["gushers"] == True:
        costco()
    elif comedy_club_choice in ["1", "heckle", "heckle comedian"] and game_state["comedian_alive"] == True:
        heckle_response()
    elif comedy_club_choice in ["1", "eat gushers", "eat", "gushers"] and game_state["comedian_alive"] == False and game_state["gushers"] == False:
        eat_gushers()
    elif comedy_club_choice in ["4", "point out cousins", "cousins"] and game_state["kissing_cousins"] == False and game_state["comedian_alive"] == True:
        comedian_death()
    elif comedy_club_choice in ["2", "go left", "left"]:
        living_room()
    elif comedy_club_choice in ["3", "go back", "back"]:
        costco()
    else:
        print("Nothing happens")
        input()
        comedy_club(a=comedy_club_origin, b=comedy_club_prompt, c=comedy_club_choices2, print_origin = False)

#living room

#living room parameters
living_room_origin = ["You find yourself in a nondescript living room."]
cousins_description = ["Two cousins are doing it doggy-style on a couch covered in stains. A camcorder on a tripod records it all."]
living_room_description1 = ["A door lies ahead. In the corner of the room you see a mannequin wearing big naturals and a strap-on."]
living_room_description2 = ["A door lies ahead. In the corner of the room is a mannequin with big naturals."]
living_room_description3 = ["A door lies ahead. In the corner of the room is a mannequin with a strap-on."]
living_room_description4 = ["A door lies ahead. In the corner of the room is a naked mannequin."]

living_room_choices1 = ["1. Open door", "2. Go back", "3. Look at mannequin", "4. Talk to cousins"]
living_room_choices2 = ["1. Open door", "2. Go back", "3. Look at mannequin", "4. Talk to cousins", "5. Tell cousins their parents are coming"]
living_room_choices3 = ["1. Open door", "2. Go back", "3. Look at mannequin", "4. Examine couch"]
living_room_choices4 = ["1. Open door", "2. Go back", "3. Look at mannequin"]

def living_room():
    
    for item in living_room_origin:
        print(item)
    input()

    if game_state["kissing_cousins"] == True:
        for item in cousins_description:
            print(item)

    if game_state["big_naturals"] == False and game_state["dildo"] == False:
        for item in living_room_description1:
            print(item)
    elif game_state["big_naturals"] == False and game_state["dildo"] == True:
        for item in living_room_description2:
            print(item)
    elif game_state["big_naturals"] == True and game_state["dildo"] == False:
        for item in living_room_description3:
            print(item)
    elif game_state["big_naturals"] == True and game_state["dildo"] == True:
        for item in living_room_description4:
            print(item)

    
    print("What would you like to do?")
    if game_state["kissing_cousins"] == False and game_state["sex_key"] == True:
        for item in living_room_choices4:
            print(item)
    elif game_state["kissing_cousins"] == False:
        for item in living_room_choices3:
            print(item)
    elif game_state["kissing_cousins"] == True and game_state["cousins_distracted"] == False:
        for item in living_room_choices1:
            print(item)
    elif game_state["kissing_cousins"] == True and game_state["cousins_distracted"] == True:
        for item in living_room_choices2:
            print(item)
    

    living_room_choice = input(">")

    if living_room_choice in ["1", "open door"] and game_state["sex_key"] == False:
        print("Locked.")
        living_room()
    elif living_room_choice in ["1", "open door"] and game_state["sex_key"] == True:
        hitler()
    elif living_room_choice in ["2", "go back", "back"]:
         comedy_club(comedy_club_origin)
    elif living_room_choice in ["3", "examine mannequin"]:
         mannequin()
    elif living_room_choice in ["4", "talk", "talk to cousins"] and game_state["kissing_cousins"] == True:
        print("The cousins are too wrapped up in their degenerate affair to notice you.")
        game_state["cousins_distracted"] = True

        living_room()
    elif living_room_choice in ["4", "examine couch", "couch"] and game_state["kissing_cousins"] == False:
        sex_key()
    elif living_room_choice in ["5", "tell cousins their parents are coming", "parents"] and game_state["kissing_cousins"] == True:
        print("'Oh shit.'")
        print("The cousins pull up their pants and scramble out.")
        game_state["kissing_cousins"] = False 
        living_room()
    else:
        print("Nothing happens.")    
        living_room()


def sex_key():
    print("On the couch there's a small key covered in cum.")
    input()
    sex_key_choices = ["Take key?", "1. Yes", "2. No - too gross"]
    for item in sex_key_choices:
        print(item)
    sex_key_choice = input(">")
    if sex_key_choice in ["1", "yes"]:
        game_state["sex_key"] = True
        print("You take the key.")
        living_room()
    else:
        dead("You hesitate, and the sex fumes suffocate you to death.") 

def mannequin():
    input()
    if game_state["big_naturals"] == True and game_state["dildo"] == True:
        print("It's a naked mannequin.")
    elif game_state["big_naturals"] == False and game_state["dildo"] == False:
        print("It's a mannequin with big naturals and a strap-on dildo.")
    elif game_state["big_naturals"] == False and game_state["dildo"] == True:
        print("It's a mannequin with big naturals.")
    elif game_state["big_naturals"] == True and game_state["dildo"] == False:
        print("It's a mannequin with a strap-on dildo.")
    
    
    print("What would you like to do?")
    if game_state["big_naturals"] == False and game_state['dildo'] == False:
        mannequin_choices = ["1. Jerk off", "2. Go back", "3. Take big naturals", "4. Take dildo"]
        for item in mannequin_choices:
            print(item)
    elif game_state["big_naturals"] == True and game_state['dildo'] == False:
        mannequin_choices = ["1. Jerk off", "2. Go back", "3. Take dildo"]
        for item in mannequin_choices:
            print(item)
    elif game_state["big_naturals"] == False and game_state['dildo'] == True:
        mannequin_choices = ["1. Jerk off", "2. Go back", "3. Take big naturals",]
        for item in mannequin_choices:
            print(item)
    elif game_state["big_naturals"] == True and game_state['dildo'] == True:
        mannequin_choices = ["1. Jerk off", "2. Go back"]
        for item in mannequin_choices:
            print(item)

    mannequin_choice = input(">")

    if mannequin_choice in ["1", "jerk off", "jerk"]:
        print("You nut. Ahh yes.")
        mannequin()
    elif mannequin_choice in ["2", "go back", "back"]:
        living_room()
    elif mannequin_choice in ["3",  "take big naturals", "big naturals", "take boobs", "boobs"] and game_state["big_naturals"] == False:
        print("You take the big naturals.")
        game_state["big_naturals"] = True
        mannequin()
    elif mannequin_choice in ["3", "take dildo", "take strap-on", "dildo", "strap-on"] and game_state["big_naturals"] == True and game_state['dildo'] == False:
        print("You take the dildo.")
        game_state["dildo"] = True
        mannequin()
    elif mannequin_choice in ["4", "take dildo", "take strap-on", "dildo", "strap-on"] and game_state["big_naturals"] == False and game_state['dildo'] == False:
        print("You take the dildo.")
        game_state["dildo"] = True
        mannequin()

        #TODO: create jerk-off portal gun

    else: 
        print("Nothing happens.")
        mannequin()
    input()

def hitler():
    input()
    if game_state["fat_hitler"] == False:
        print("You find yourself in a small room. A door lies ahead. In the corner is a time machine.")
    elif game_state["fat_hitler"] == True and game_state["hitler_new"]:
        print("You find yourself in a small room. The door is blocked by 600-pound Hitler stuffing his face with strudel. In the corner is a time machine.")
    game_state["hitler_new"] = False

    print("What would you like to do?")
    if game_state["fat_hitler"] == True:
        hitler_choices = ["1. Use time machine", "2. Talk to Hitler", "3. Go back"]
        for item in hitler_choices:
            print(item)
    elif game_state["fat_hitler"] == False:
        hitler_choices = ["1. Use time machine", "2. Open door", "3. Go back"]
        for item in hitler_choices:
            print(item)

    hitler_choice = input(">")

    if hitler_choice in ["1", "use time machine", "time machine"]:
        hitler_nanny()
    elif hitler_choice in ["2", "talk", "talk to Hitler"] and game_state["fat_hitler"] == True:
        print("600-pound Hitler says 'Ich bin ein strudel!'")
        hitler()
    elif hitler_choice in ["2", "open door"] and game_state["fat_hitler"] == False:
        n_word()
    elif hitler_choice in ["3", "back", "go back"]:
        living_room()
    else: 
        print("Nothing happens.")
        hitler()

def hitler_nanny():
    print("You find yourself in a German kitchen in 1894. Hitler's nanny prepares strudel for him. On the table is a shotgun.")
    
    nanny_choices = ["What would you like to do?", "1. Shoot nanny", "2. Don't shoot nanny"]
    for item in nanny_choices:
        print(item)
    
    nanny_choice = input(">")

    if nanny_choice in ["1", "shoot", "shoot nanny"]:
        print("You shoot Hitler's nanny. She dies instantly.")
        input()
        print("Skinny Hitler no longer blocks the door. Instead he commits genocide of 11 million people. Great job!")
        game_state["fat_hitler"] = False
        hitler()
    elif nanny_choice in ["2", "don't shoot", "don't shoot nanny"]:
        print("Nothing happens.")
        input()
        print("... you pussy.")
        hitler()

def n_word():
    input()
    if game_state["n_word_new"] == True:
        print("You find yourself in corporate harassment training.")

        print("You're stuck in a conversation with a white guy who REALLY wants to say the N-word.")
        input()
        print("White guy: 'If black people can say it, how come I can't say it? I should be able to say it.'")
        game_state["n_word_new"] = False
        input()
    print("What would you like to do?")
    print("1. Explain the history of the N-word and why it's insulting for white people to say it")
    print("2. Offer him $100 million and three Netflix specials specials") 
    print("3. Go back") 

    n_word_choice = input(">")

    if n_word_choice in ["1", "explain", "explain history"]:
        print("He still doesn't get it.")
        n_word()
    elif n_word_choice in ["2", "offer money"]:
       print("You buy his podcast for $100 million and give him three Netflix specials, but he still considers himself a victim.")
       input()
       print("The corporate overlords have fulfilled their obligation to conduct harassment training and are no longer liable if you commit sexual harassment.")
       print("The door unlocks.")
       input()
       print("Move ahead.")
       input()
       hallway()
    elif n_word_choice in ["3", "back", "go back"]:
        hitler()
    else:
        print("Nothing happens.")  
        n_word()
        

def hallway():
    if game_state["hallway_new"] == True:
        print("You find yourself in a dark hallway.")
        input()
        print("There's a box and a door.")
        input()


    if game_state["hallway_new"] == False:
        print("Open door")
        input()
        congress()

    elif game_state["hallway_new"] == True:
        print("What would you like to do?")
        print("1. Open box")
        print("2. Open door")
        print("3. Go back")
    else:
        print("Nothing happens.")
        hallway()
    

    hallway_choice = input(">")

    if hallway_choice in ["1", "open box"]:
        print("You open the box and inside you find a sex doll.")
        input()
        print("You take the sex doll because fuck you - take the fucking sex doll.")
        game_state["sex_doll"] = True
        game_state["hallway_new"] = False
        hallway()
    elif hallway_choice in ["2", "open door"]:
        congress()
    elif hallway_choice in ["3", "back", "go back"]:
        n_word()
    else:
        print("Nothing happens.")
        hallway()

def congress():
    print("You find yourself testifying before Congress.")
    input()
    if game_state["congress_new"] == True:
        print("Senator Lindsey Graham is questioning you.")
        input()
        print("Sen Graham: 'It just doesn't make sense that someone who's involved with women would want to be involved with men.")
        input()
        print("AOC rolls her eyes.")
        print("AOC: 'It's called bisexual, dumbass.'")
        input()
        print("Sen Graham: 'I don't believe I yielded my time to you, Miss Occasion Cortex.'")
        input()
        print("Lindsey Graham turns back to you and asks you to explain bisexual to him.")
        input()
    print("What would you like to do?")
    print("1. Explain bisexuality")
    print("2. Do a demonstration")
    print("3. Go back")

    congress_choice = input(">")

    if congress_choice in ["1", "explain", "explain bisexuality"]:
        print("You explain bisexuality.")
        input()
        print("He still doesn't get it.")   
    elif congress_choice in ["2", "do a demonstration", "do a demo", "demonstration", "demo"]: 
        print("You offer to demonstrate how bisexuality works and request a volunteer.")
        input()
        print("George Santos offers himself. What's he doing here?")
        if game_state["big_naturals"] == True and game_state["dildo"] == True and game_state["sex_doll"] == True and game_state["gushers"] == True:
            print("You sandwich between George Santos and the sex doll and thrust to the rhythm of Lady Gaga.")
            input()
            print("Lindsey Graham's face melts off. You're escorted off the premises.")
            game_state["tummyache"] = True
            start(origin, origin_description, choices2)
        elif game_state["big_naturals"] == True and game_state["dildo"] == True and game_state["sex_doll"] == True and game_state["gushers"] == False:
            dead("You attempt a bisexual demo, but your HP is too low. You die of exhaustion.")
    elif congress_choice in ["3", "back", "go back"]:
        hallway()
        else:
            print("He still doesn't get it.")
    congress()
            




start(origin, origin_description, choices)

