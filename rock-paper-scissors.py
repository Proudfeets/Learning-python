import random
for x in range(1):
  machine = random.randint(1,3)

player=raw_input("Choose rock (r), paper (p), or scissors (s):")

if ( player == 'r' ) : print("You choose rock.")
elif ( player == 'p' ) : print("You choose paper.")
elif ( player == 's' ) : print("You choose scissors.")
else: print("I don't understand.  Please start over.")

# choice = "rock" or "scissors" or "paper"
if ( machine == 1 ):
    choice = "rock"
elif (machine == 2):
    choice = "paper"
elif (machine == 3):
    choice = "scissors"
else: print(machine)


print("The computer chose " + choice)


if (machine == 1 and player == 'p') or (machine == 2 and player == 's') or (machine == 3 and player == 'r'):
    print("Player wins!")
elif (machine == 2 and  player == 'p') or (machine == 3 and player == 's') or (machine == 1 and player == 'r'):
    print("Tie! The battle between humanity and the machines is over.")
else:
    print("Machine wins!")
