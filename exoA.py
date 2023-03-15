# A
class Player:
    """Class Player prenant arguments :
    pseudo : nom du joueur
    scoresMusiques : liste de taille 5 et contenant les scores du player
    Et avec comme méthodes :
    afficherScores(self)
    ajouterScore(self,musiqueId,score)
    afficherChansonBestScore(self)
    afficherChansonPireScore(self)
    moyenneScore(self)
    totalScore(self)
    """

    def __init__(self, pseudo, scoresMusiques=[0, 0, 0, 0, 0]):
        self.name = pseudo
        self.scores = scoresMusiques

    def afficherScores(self):
        for i in range(len(self.scores)):
            print("Pour la chanson a l'id", i, ", votre score est de ",
                  self.scores[i])

    def ajouterScore(self, musiqueId, score):
        if score > self.scores[musiqueId]:
            if score < 50:
                self.scores[musiqueId] = 50
            else:
                self.scores[musiqueId] = score

    def afficherChansonBestScore(self):
        varTempoScore = self.scores[0]
        varTempoId = 0
        for j in range(len(self.scores)):
            if varTempoScore < self.scores[j]:
                varTempoScore = self.scores[j]
                varTempoId = j
        print("Votre meilleur score est ", varTempoScore,"sur la musique",varTempoId)

    def afficherChansonPireScore(self):
        varTempoScore = self.scores[0]
        varTempoId = 0
        for l in range(len(self.scores)):
            # dans l'énoncé, il est écrit qu'une chanson à 0 est une chanson pas joué donc on doit faire en sorte que la méthode ne renvoie pas 0
            if varTempoScore > self.scores[l] and self.scores[l] != 0:
                varTempoScore = self.scores[l]
                varTempoId = l
        print("Votre pire score est ", varTempoScore,"sur la musique",varTempoId)

    def moyenneScore(self):
        varTempo = 0
        for x in range(len(self.scores)):
            varTempo += self.scores[x]
        print("La moyene est de", varTempo/len(self.scores))

    def totalScore(self):
        varTempo = 0
        for x in range(len(self.scores)):
            varTempo += self.scores[x]
        print("Le score total est de ", varTempo)


def game1():
    joueur1 = Player("AneTroTro")
    joueur1.ajouterScore(0, 89)
    joueur1.ajouterScore(1, 45)
    joueur1.ajouterScore(2, 75)
    joueur1.afficherScores()

    joueur1.ajouterScore(2, 56)
    joueur1.ajouterScore(3, 65)
    joueur1.afficherScores()

    joueur1.afficherChansonBestScore()
    joueur1.afficherChansonPireScore()
    joueur1.moyenneScore()
    joueur1.totalScore()
game1()

