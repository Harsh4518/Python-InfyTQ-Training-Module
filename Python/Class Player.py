#Aggregate Relationship.
class Player:

    def __init__(self,name):

        self.name=name

    def getplayer(self):

        return self.name

class Team:

    def __init__(self):

        self.players=[]

    def addplayer(self,player):

        self.players.append(player)

p1=Player("sachin")
p2=Player("Kapil")
p3=Player("Virat")
t=Team()
t.addplayer(p1)
t.addplayer(p2)
t.addplayer(p3)
print(t.players[0].getplayer())
print(t.players[1].getplayer())
print(t.players[2].name)
del t
print(p1.getplayer())
print(p2.name)
