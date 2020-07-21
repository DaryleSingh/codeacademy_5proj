class Trainer:
  def __init__(self,trainername,potion1,potion2,potion3,pokemonlist,activepokemon):                     
    self.trainername=trainername
    self.potion1=potion1
    self.potion2=potion2
    self.potion2=potion3
    self.activepokemon=activepokemon
    self.pokemonlist=pokemonlist
    
  def print_pokemon_list(self):
      print(str(self.trainername) +" pokemon list")
      for obj in self.pokemonlist: 
       obj.info() 

  def currenty_active_pokemon(self):
      print(str(self.trainername) +" active pokemon " + str(self.pokemonlist[self.activepokemon].name))

      
  def heal_current_pokemon(self):
      self.pokemonlist[self.activepokemon].gain_health(5)
      
  def damage_current_pokemon(self):
      self.pokemonlist[self.activepokemon].lose_health(5)

  def switch_active_pokemon(self,activepokemon):
      self.activepokemon=activepokemon
      self.currenty_active_pokemon()
      
  def attackedby(self,attacker):
    print(str(self.trainername) + " was attacked by " + str(attacker.trainername))
    
    print(str(self.trainername) + " currently active pokemon ")
    self.currenty_active_pokemon()
    print(str(self.trainername) + " current pokemon is damaged ")
    self.damage_current_pokemon()
    
    print(str(attacker.trainername) + " currently active pokemon ")
    attacker.currenty_active_pokemon()
    print(str(attacker.trainername) + " currently active pokemon is healed")
    attacker.heal_current_pokemon()
    
    

class Pokemon:
  def __init__(self,name,level,health,max_health,type,is_knocked_out):                     
    self.name=name,
    self.level=level 
    self.health=health
    self.max_health=max_health
    self.type=type
    self.is_knocked_out=is_knocked_out

  def lose_health(self,losehealth):
    self.health=self.health-losehealth
    print(str(self.name) +" health lost : " + str(losehealth))
    print(str(self.name) +" current health : " + str(self.health))

  def gain_health(self,gainhealth):
    self.health=self.health+gainhealth
    print(str(self.name) +" health gained : " + str(gainhealth))
    print(str(self.name) +" current health : " + str(self.health))

  def knock_out(self):
    self.health=0
    print(str(self.name) + " knocked out")

  def revive(self):
    self.health=10
    print(str(self.name) + " revived")

  def attackedby(self,attacker):
    print(str(self.name) + " was attacked by " + str(attacker.name))
    print(str(attacker.name) + " type is " + str(attacker.type))
    print(str(self.name) + " type is " + str(self.type))
    
    if(attacker.type=="Grass" and self.type=="Fire"):
       print(str(attacker.type) + " puts out " + str(self.type))
       print(str(attacker.name) + " Wins")
       damage=5
       self.lose_health(damage)
       attacker.gain_health(damage)


       
    if(attacker.type=="Water" and self.type=="Fire"):
       print(str(attacker.type) + " puts out " + str(self.type))
       print(str(attacker.name) + " Wins")
       damage=5
       self.lose_health(damage)
       attacker.gain_health(damage)


       
    if(self.type=="Grass" and attacker.type=="Fire"):
       print(str(self.type) + " puts out " + str(attacker.type))
       print(str(self.name) + " Wins")
       damage=5
       attacker.lose_health(damage)
       self.gain_health(damage)


       
    if(self.type=="Water" and attacker.type=="Fire"):
       print(str(self.type) + " puts out " + str(attacker.type))
       print(str(self.name) + " Wins")
       damage=5
       attacker.lose_health(damage)
       self.gain_health(damage)


    
    
  def info(self):
    print("----------Pokemon Info(" + str(self.name) + ")----------")
    print("Name :" + str(self.name))
    print("Level : " + str(self.level))
    print("Health : " + str(self.health))
    print("Max Health : " + str(self.max_health))
    print("Type: " + self.type)
    print("Knocked out: " + str(self.is_knocked_out))
    print("------------------------------")

    
    
    
    
#self,name,level,health,max_health,type,is_knocked_out
p1 = Pokemon("Zara",2000,10,50,"Fire",False)
p2 = Pokemon("Zara2",2000,10,50,"Grass",False)
p3 = Pokemon("Zara3",2000,10,50,"Water",False)
#p1.info()
#p1.attackedby(p2)
p3.attackedby(p1)


pokemonlist1 = []  
# appending instances to list  
pokemonlist1.append(p1) 
pokemonlist1.append(p2) 
pokemonlist1.append(p3)


t1=Trainer("trainer1","potion1","potion2","potion3",pokemonlist1,1)
t1.print_pokemon_list()
t1.currenty_active_pokemon()


#define new pokemon objects for trainer2
p4 = Pokemon("Zara4",2000,10,50,"Fire",False)
p5 = Pokemon("Zara5",2000,10,50,"Grass",False)
p6 = Pokemon("Zara6",2000,10,50,"Water",False)
pokemonlist2 = []  
pokemonlist2.append(p1) 
pokemonlist2.append(p2) 
pokemonlist2.append(p3)

t2=Trainer("trainer2","potion1","potion2","potion3",pokemonlist2,1)
t2.print_pokemon_list()
t2.currenty_active_pokemon()



t2.attackedby(t1)

