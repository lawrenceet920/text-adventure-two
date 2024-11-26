# Ethan Lawrence
# Nov 25 2024
# Text adventure game

# --- imports --- #
from time import sleep
import sys

# --- Basic Global Variables --- #
lives = 3
score = 0

rucksack = ['key', 'duck', 'brush']

# --- Functions --- #
def gameover():
    if lives <= 0:
        print(f'You have run out of lives {name}')
        print('GAME OVER')
        lives_score()
        sys.exit()

def lives_score():
    '''List Score and lives'''
    print('\n*******************************')
    print(f'You have {lives} lives left.')
    print(f'Your score is: {score}.')
    print(f'Your rucksack contains: {rucksack}')
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

print("Behind you, in the forest, there is a great ROAR!\n")
sleep(2)
print("You begin to run very quickly - fearing for your life\n")
sleep(1)
print("""Up ahead you see another house. Unlike the old
      crone's cottage, it is warm, inviting and rather homely.\n""")
print('You try the door, but it is locked!\n')
sleep(1)
print('The roaring and footsteps are right behind you. You need to make a quick decision!\n')
print('Perhaps there is something in you back which can help?\n')
print(f'You look in your rucksack and find: {rucksack}')
# --- Choice 3 --- #

choise3 = input('Press k to use the key, press d to release the duck to buy you some time, or press b to throw the duck at the monster: ')
if choise3 == 'k':
    print('To your great luck, the key fits the door, and you fall into the house in the nick of time.')
    score += 5
    rucksack.remove('key')
elif choise3 == 'd':
    print('The duck quacks nervously as you pull it from the bag, but it seems to distrack the terrible monster following you\n')
    score += 2
    rucksack.remove('duck')

    # Subchoice
    choise3a = input('You still aren\'t in the house, press k to use the key, or b to throw the brush.')
    if choise3a == 'k':
        print("""The duck buys you enough time to use the key,
and to your great fortune, it opens the door and you nip
safely inside.""")
        score += 3
        rucksack.remove('key')
    else:
        print('You throw the brush at the monster, but like the duck before you, you are gobbled up in moments...!')
        lives -= 1
        rucksack.remove('brush')
        gameover()
    # End of subchoice
else:
    print('You throw the brush at the monster, but it bounces off its head and it gobbles you up instead.')
    lives -= 1
    rucksack.remove('brush')
    gameover()
lives_score()

# --- Scenario 4 --- #
print("""You look around yourself in the cottage. It is a
very nice, homely and comfortable cottage. You get the
feeling someone kind lives here\n""")
sleep(1)
print("""You look around yourself again and see a table with
a cake1 Your stomach rumbles noisily. You did not realise how
hungary you were. Beside the cake is a knife. You decide it
wouldn't be a problem to slice the cake.\n""")
sleep(1)

# --- Choice 4 --- #
choise4 = input('Press a to eat the cake now, or b to put in in your rucksack for later: ')
if choise4 == "a":
    print('You eat the cake. It\'s very delicous and you feel a bit better, even though that monster is still outside.')
    score += 2
else:
    print('You carefully wrap and stow the cake for later.')
    rucksack.append('cake')
lives_score()

# --- scenario 5 --- #
print('The door to the cottage opens! You are suprised\n\n')
sleep(2)
print('Standing there is a little old man. He is suprised to see you too.\n')
sleep(1)

if 'cake' in rucksack:
    print('The man sees the cake has been cut.')
    sleep(1)
    print('He asks if you took some of his cake')
    sleep(1)
    print('Guiltily, you nod and reveal the cake in your bag')
    sleep(2)
    print('He shrugs and says you can keep it for later')
    print('He cuts you a new slice')
    score += 30
else:
    print('The man sees the cake has been cut and there are crumbs round your mouth and on your clothes')
    sleep(1)
    print('He looks angry! He accuses you of stealing the cake')
    print('He curses you!')
    lives -= 1
    gameover()
lives_score()

print('You have reached the end of the story {name} well done for avoid traps.')

lives_score()

print('THE END')