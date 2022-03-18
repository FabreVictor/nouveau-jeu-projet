class Animal:
    def __init__ (self,name,poids,dodo,cri,couleur,attaque) :
        self.nom = name
        self.poids = poids
        self.dodoJauge = dodo
        self.cri = cri
        self.couleur= couleur
        
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
    def mange (self,couleur):
       self.couleur ="la couleur de l'animel est " + self.couleur
            
            
            
            
            
            
            
class Chat(Animal):
    
    def __init__ (self,name,couleur):
        self.couleur = couleur 
        
        Animal.__init__ (self,name,)


        
monChat = Chat("chien")

input() 
