class Animal:
    def __init__ (self,name,poids,dodo) :
        self.nom = name
        self.poids = poids
        self.dodoJauge = dodo
    def mange (self,poids,dodoJauge):
        poids += 5
        dodoJauge -= 10
    def dodo (self,poids,dodoJauge): 
        poids -= 5
        dodoJauge += 5
    def deces (self,poids,dodoJauge):
        if poids <= 0:
            print("§§§§§§§§§§§§§§§§§§ le animale é mouru §§§§§§§§§§§§§§§§§§")
        if dodoJauge <= 0:
            print("§§§§§§§§§§§§§§§§§§ le animale é mouru §§§§§§§§§§§§§§§§§§")
            
class Chat(Animal):
    
    def __init__ (self,name,couleur):
        self.couleur = couleur 
        
        Animal.__init__ (self,name,"chat")
        self.cri = "miaule"
    def 
        
monChat = Chat("chien")

input() 
