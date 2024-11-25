# Ethan Lawrence
# Nov 25 2024
# Text adventure game

# --- imports --- #
from time import sleep

# --- Basic Global Variables --- #
lives = 3
score = 0

rucksack = ['key', 'duck', 'brush']

# --- Functions --- #
def lives_score():
    '''List Score and lives'''
    print('\n*******************************')
    print(f'You have {lives} lives left.')
    print(f'Your score is: {score}.')
    print('*******************************\n')
# --- Welcome --- #

name = input('What is your name: ')
print(f'Welcome {name} to the adventure\n')
lives_score()
sleep(1)

# --- Scenario 1 --- #

print("You awake to the sound of an old crone cooking in her pot.\n")
sleep(0.5)
print("She is singing an old song about cooking.\n")
sleep(0.5)
print(".... I think she is about to cook you!\n")

#  --- Choice 1 --- #

choice1 = input('Press "r" to run away or "e" to use magic: ')
if choice1 == 'r':
    print('The old crone catches you and puts you in the pot.') 
    lives -= 1
else:
    print('You cast a spell on her and she explodes!')
    score += 5
lives_score()
sleep(1)

# --- Scenario 2 --- #

print("You move further into the forest. It is full of.")
print("strange and worrying noises. What other strange creatures")
print("might you encounter\n")
sleep(1)
print('You hear a scratching noise\n')
sleep(1)
print('It\'s getting closer...!\n')
sleep(1)
print('Oh phew! It\'s just a cute fluffy bunny!\n\n')

# --- Choice 2 --- #

choise2 = input('Press s to stroke it, press k to kill it, or press r to run away: ')
if choise2 == 's':
    print('The bunny reveals ENORMOUS fangs and bites your head off!')
    lives -= 1
elif choise2 == 'k':
    print('The bunny reveals ENOURMOUS fangs, but you kill it before it can bite you!')
    score += 5
else:
    print(""" The bunny is quicker then it looks, and before you
           know it, it hops onto you, reveals ENOURMAS fangs, and bites
           your head off.""")
    lives -= 1
lives_score()
sleep(1)

# --- Scenario 3 --- #

print("You come across a large tree, for a second")
print("you marval at it. you suddenly see a large troll!")
print("You dont have much time!\n")
sleep(2)

# --- Choice 3 --- #

choise3 = input('Press c to climb the tree, press a to attack it, or press r to run away: ')
if choise3 == 'c':
    print('You grab onto a branch.')
    sleep(1)
    print('Another, and another.')
    sleep(1)
    print('You are at the top!')
    sleep(1)
    print('You look down and see the troll grunt and walk away.')
    score += 5
elif choise3 == 'a':
    print('Turns out the club it weilds isn\'t for show... ow.')
    lives -= 1
else:
    print('The troll is fast, but you are faster and excape!')
lives_score()