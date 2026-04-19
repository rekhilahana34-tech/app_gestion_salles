from data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()

    def ajouter(self, code, libelle, type_salle, capacite):
        self.dao.ajouter_salle(code, libelle, type_salle, capacite)

    def afficher(self):
        return self.dao.afficher_salles()

    def supprimer(self, code):
        self.dao.supprimer_salle(code)