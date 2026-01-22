import os
os.system('cls')

print('''
********************************************************************************

                              .sssssssss.
                        .sssssssssssssssssss
                      sssssssssssssssssssssssss
                     ssssssssssssssssssssssssssss
                      @@sssssssssssssssssssssss@ss
                      |s@@@@sssssssssssssss@@@@s|s
               _______|sssss@@@@@sssss@@@@@sssss|s
             /         sssssssss@sssss@sssssssss|s
            /  .------+.ssssssss@sssss@ssssssss.|
           /  /       |...sssssss@sss@sssssss...|
          |  |        |..........s@ss@sss.......|
          |  |        |.......sss@sss@ssss......|
          |  |        |...........@ss@..........|
           \  \       |............ss@..........|
            \  '------+...........ss@...........|
             \________ .........................|
                      |.........................|
                     /...........................\
                    |.............................|
                       |.......................|
                           |...............|
********************************************************************************      
      ''')
print("Welcome to Beer Pong Bar")
print("Your mission is to find your friends")
direction = input('You\'re on the bar counter, where do you want to go?\n\t Type "left" or "right"\n').lower() #lowercase every decision

if direction == "left": #main logical decision
    girl = input('You found a girl inviting you to her table, do you go or wait?\n\t Type "go" or "wait"\n').lower()

    if girl == "wait": #second level decision logic
        table = input('Suddenly you see 3 tables, which one would you choose?\n\t Type "A" or "B" or "C"\n').upper() #uppercase last decision because tables use capital letters

        if table == "A":
            print("You found Dante and went to the DJ booth!\nGame over!")
        elif table == "B":
            print("YES! You found your pals\nYou win!")
        elif table == "C":
            print("You made the manager mad and he attacked you\nGame over!")
        else:
            print("Oh no! You went outside and got lost in the wind\nGame over!") #catch-all for invalid table inputs
    else:
      print("Damn, this chic kissed you till death and now you can't run away!\nGame over!")

elif direction == "right":
     print("You entered the bathroom and can't get out!\nGame over!")

else:
    print("Choose a valid direction!\nGame over!") #catch-all for invalid first input
