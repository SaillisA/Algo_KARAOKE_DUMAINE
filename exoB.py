class Player:
    """Class Player prenant en arguments :
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

    def __init__(self, pseudo, scoresMusiques=[]):
        self.name = pseudo
        self.scores = scoresMusiques

    def afficherScores(self, musiqueId):
        varTempo = self.scores[musiqueId]
        return varTempo

    def ajouterScore(self, musiqueId, score):
        if self.scores == None:
            self.scores.append(score)
        if len(self.scores) > 0:
            if score > self.scores[musiqueId]:
                if score < 50:
                    self.scores[musiqueId] = 50
                else:
                    self.scores[musiqueId] = score

    def afficherChansonBestScore(self):
        varTempoScore = 0
        for j in range(len(self.scores)):
            if varTempoScore < self.scores[j]:
                varTempoScore = self.scores[j]
        return varTempoScore

    def afficherChansonPireScore(self):
        varTempoScore = self.scores[0]
        varTempoId = 0
        for l in range(len(self.scores)):
            # dans l'énoncé, il est écrit qu'une chanson à 0 est une chanson pas joué donc on doit faire en sorte que la méthode ne renvoie pas 0
            if varTempoScore > self.scores[l] and self.scores[l] != 0:
                varTempoScore = self.scores[l]
                varTempoId = l
        print("Votre pire score est ", varTempoScore,
              "sur la musique", varTempoId)

    def moyenneScore(self):
        varTempo = 0
        for x in range(len(self.scores)):
            varTempo += self.scores[x]
        return varTempo/len(self.scores)

    def totalScore(self):
        varTempo = 0
        for x in range(len(self.scores)):
            varTempo += self.scores[x]
        return varTempo


class Karaoke:
    """Class Karaoke prenant en arguments :
    listeJoueurs : contient tous les objets joueurs
    listeChansons : liste regroupant le nom des musiques (leurs identifiants étant leurs emplacements dans la liste)
    Et avec comme méthodes :
    ajouterPlayer()
    nombrePlayer()
    supprimerPlayer()
    afficherBestScoreChansonsPrecise()
    afficherBestScoreTouteChanson()
    afficherBestScoreTotal()
    afficherbestMoyenne()
    """

    def __init__(self, listeJoueurs=[], listeChansons=[]):
        self.players = listeJoueurs
        self.chansons = listeChansons

    def ajouterPlayer(self, playerAjouter):
        self.players.append(playerAjouter)

    def nombrePlayer(self):
        print("Il y a ", len(self.players), " joueurs.")

    def supprimerPlayer(self, playerSupprimer):
        varTempo = 0
        for i in range(len(self.players)):
            if self.players[i] == playerSupprimer:
                varTempo = i
        self.players.pop(varTempo)

    def afficherBestScoreChansonsPrecise(self, nomChanson):
        idChanson = 0
        for i in range(len(self.chansons)):
            if self.chansons[i] == nomChanson:
                idChanson = i

        varTempo = 50
        for j in range(len(self.players)):
            if self.players[j].afficherScores(idChanson) > varTempo:
                varTempo = self.players[j].afficherScores(idChanson)
        return varTempo

    def afficherBestScoreTouteChanson(self):
        varTempo = 0
        for j in range(len(self.players)):
            if self.players[j].afficherChansonBestScore() > varTempo:
                varTempo = self.players[j].afficherChansonBestScore()
        return varTempo

    def afficherBestScoreTotal(self):
        varTempo = 0
        for j in range(len(self.players)):
            if self.players[j].totalScore() > varTempo:
                varTempo = self.players[j].totalScore()
        return varTempo

    def afficherbestMoyenne(self):
        varTempo = 0
        for j in range(len(self.players)):
            if self.players[j].moyenneScore() > varTempo:
                varTempo = self.players[j].moyenneScore()
        return varTempo


def game():
    joueur1 = Player("AneTro Tro",)
    joueur1.ajouterScore(0, 89)
    joueur1.ajouterScore(1, 45)
    joueur1.ajouterScore(2, 75)
    joueur1.ajouterScore(3, 34)

    joueur2 = Player("Tchoutcoupi")
    joueur2.ajouterScore(0, 32)
    joueur2.ajouterScore(1, 87)
    joueur2.ajouterScore(2, 0)
    joueur2.ajouterScore(3, 98)

    joueur3 = Player("Don Dora")

    kako = Karaoke([joueur1, joueur2], ["La vie en rose",
                   "La boheme", "Resiste", "Les sardines"])

    kako.ajouterPlayer(joueur3)
    print(kako.nombrePlayer())
    kako.supprimerPlayer(joueur3)
    print(kako.nombrePlayer())

    # ne fonctionnent pas ;-;
    """print(kako.afficherBestScoreChansonsPrecise("La boheme"))
    print(kako.afficherBestScoreTouteChanson())
    print(kako.afficherBestScoreTotal())
    print(kako.afficherbestMoyenne())"""

game()
