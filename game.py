class Game(object):
    def __init__(self,name,players,type):
        self.name=name
        self.players=players
        self.type=type
    def start(self):
        a = int(input("Enter a number=>"))
        b = a**2
        print(b)
game1=Game("Mario",1,"Platformer")
print(game1.name)
game1.start()


        

    