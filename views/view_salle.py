from services.services_salle import ServiceSalle

class ViewSalle:

    def __init__(self):
        self.service = ServiceSalle()

    def menu(self):
        while True:
            print("\n1. Ajouter salle")
            print("2. Afficher salles")
            print("3. Supprimer salle")
            print("4. Quitter")

            choix = input("Choix: ")

            if choix == "1":
                code = input("Code: ")
                libelle = input("Libelle: ")
                type_salle = input("Type: ")
                capacite = int(input("Capacite: "))
                self.service.ajouter(code, libelle, type_salle, capacite)
                print("Salle ajoutée")

            elif choix == "2":
                salles = self.service.afficher()
                for s in salles:
                    print(s)

            elif choix == "3":
                code = input("Code à supprimer: ")
                self.service.supprimer(code)
                print("Salle supprimée")

            elif choix == "4":
                break

            else:
                print("Choix invalide")