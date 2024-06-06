import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user= int(input("what do you want? 0=rock, 1= paper, 2= scissors\n "))
if user ==0:
    print(f"you chose rock \n {rock}")
elif user ==1:
    print(f"you chose paper\n {paper}")
else:
    print(f"you chose scissors\n {scissors}")
computer= random.randint(0,2)

if computer ==0:
    print(f"computer chose rock \n {rock}")
elif computer ==1:
    print(f"computer chose paper\n {paper}")
else:
    print(f"computer chose scissors\n {scissors}")

if user==0 and computer ==2:
    print("you win ")
elif user==2 and computer ==0:
    print("you lose")
elif computer>user:
    print("computer wins")
elif computer==user:
    print("its a draw")
#print(rock)