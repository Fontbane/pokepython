class Species:
    '''Pokemon Species'''
    species.speciesList=[]
    def __init__(self,id,baseStats,types,ability1,ability2,hiddenAbility,moveset,evolutions):
        self.id=id
        self.baseHP=baseStats["HP"]
        self.baseAttack=baseStats["ATTACK"]
        self.baseDefense=baseStats["DEFENSE"]
        self.baseSpAttack=baseStats["SPECIAL ATTACK"]
        self.baseSpDefense=baseStats["SPECIAL DEFENSE"]
        self.baseSpeed=baseStats["SPEED"]
        self.baseStats=[self.baseHP,self.baseAttack,self.baseDefense,self.baseSpAttack,self.baseSpDefense,self.baseSpeed]
        self.bst=sum(self.baseStats)
        self.types=types
        self.type1=types[0]
        self.type2=types[1]
        self.ability1=ability1
        self.ability2=ability2
        self.abilityH=hiddenAbility
        self.moveset=moveset
        self.evolutions=evolutions
        speciesList.append(self)
        print("Added species "+id+" with BST "+str(bst))