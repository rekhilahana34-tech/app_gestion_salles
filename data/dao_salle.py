import mysql.connector
import json

class DataSalle:

    def get_connection(self):
        with open("data/config.json") as f:
            config = json.load(f)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return conn

    def ajouter_salle(self, code, libelle, type_salle, capacite):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        values = (code, libelle, type_salle, capacite)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

    def afficher_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM salle"
        cursor.execute(query)

        salles = cursor.fetchall()

        cursor.close()
        conn.close()

        return salles

    def supprimer_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM salle WHERE code = %s"
        values = (code,)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()