from database.DB_connect import DBConnect
from model.Connessione import Connessione
from model.Fermata import Fermata


class DAO():
    pass

    @staticmethod
    def readAllFermate():
        conn = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM Fermata"
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            fermata = Fermata(row["id_fermata"], row["nome"] )
            result.append(fermata)
        cursor.close()
        conn.close()
        return result # Restituisco lista di oggetti Fermata (DTO)

    @staticmethod
    def existsConnessioneTra(u : Fermata, v : Fermata):
        # Verifica se esista una connessione tra nodo u e v
        conn = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM connessione c  WHERE c.id_stazP = %s AND c.id_stazA = %s"

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (u.id_fermata, v.id_fermata) ) # Parametri
        for row in cursor:
            result.append(row)
            print(row)
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def searchViciniAFermata(u : Fermata):
        # Cerco le fermate collegate a quella passata come parametro
        conn = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM connessione c  WHERE c.id_stazP = %s"

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (u.id_fermata, ) ) # Parametro con (, )
        for row in cursor:
            connessione = Connessione(row["id_connessione"],
                                      row["id_linea"],
                                      row["id_stazP"],
                                      row["id_stazA"])
            result.append(connessione)
            print(row)
        cursor.close()
        conn.close()
        return result