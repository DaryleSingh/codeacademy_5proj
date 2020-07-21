import random

money = 100

#Write your game of chance functions here

def flipcoin(betamount,headsortailscall):
  #Heads=1 Tails=2
  print("------heads tails-----");
  print("My call " + headsortailscall);
  print("$Money before " + str(money));
  print("My Bet " + str(betamount));
  callint=1
  if headsortailscall=="Tails":callint=2
  num = random.randint(1, 2)
  if (num==callint): print("You Won");return betamount
  if (num !=callint): print("You Lost");return -betamount

def chohan(betamount,oddoreven):
  print("-----chohan--------");
  print("My call " + oddoreven);
  print("$Money before " + str(money));
  print("My Bet " + str(betamount));
  #Odd=1 Even=2
  callint=1
  if oddoreven=="Even":callint=2
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  result=dice1+ dice2
  result2="Odd"
  if (result % 2==0):result2="Even"
  if (oddoreven==result2): print("You Won");return betamount
  if (oddoreven !=result2): print("You Lost");return -betamount

def hicard(betamount,player1,player2):
  print("-----hi card-----");
  print ("player1 (me)" + str(player1))
  print("$Money before " + str(money));
  print("My Bet " + str(betamount));
  print ("player2 " + str(player2))
  if (player1>player2): print("You Won");return betamount
  if (player1<player2): print("You Lost");return -betamount
  if (player1==player2): return 0

def roulette(betamount,guess):
  if(guess=="Odd" or guess=="Even"):
   print("---roulette OddEven---");
   print("My call " + guess);
   print("$Money before " + str(money));
   print("My Bet " + str(betamount));
   callint=1
   if guess=="Odd":callint=2
   num = random.randint(1, 2)
   if (num==callint): print("You Won");return betamount
   if (num !=callint): print("You Lost");return -betamount

  if(guess=="0" or guess=="00"):
   print("-0 00 35/1 American roulette-");
   print("My call " + guess);
   print("$Money before " + str(money));
   print("My Bet " + str(betamount));
   callint=1
   if guess=="0":callint=2
   num = random.randint(1, 2)
   if (num==callint):print("You Won"); return 35 * betamount
   if (num !=callint): print("You Lost");return -betamount

#Call your game of chance functions here
# (1) heads tails
money=money + flipcoin(20,"Tails");
print("$Money after " + str(money));

# (2) chohan
money=money + chohan(20,"Odd");
print("$Money after " + str(money));

# (3) 2 players picking card from same deck
list1=[1,2,3,4,5,6,7,8,9]
randomindex=random.randint(0, len(list1)-1)
player1=list1[randomindex]
#print("card removed " + str(player1))
list1.pop(randomindex)  #card gone simulates probability/same deck
randomindex=random.randint(0, len(list1)-1)
player2=list1[randomindex]
money=money + hicard(20,player1,player2);
print("$Money after " + str(money));


#roulette
money=money + roulette(20,"Odd")
print("$Money after " + str(money));
money=money + roulette(20,"0")
print("$Money after " + str(money));






