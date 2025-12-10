import networkx as nx
from geopy.distance import geodesic

from database.DAO import DAO

class Model:
    def __init__(self):
        self._lista_fermate = []
        self._dizionario_fermate = {}
        self._grafo = None

    def getAllFermate(self):
        fermate = DAO.readAllFermate()
        self._lista_fermate = fermate
        # Mi sono costruito un dizionario di fermate, con chiave
        # l'id_fermata e valore l'oggetto fermata corrispondente
        for fermata in self._lista_fermate:
            self._dizionario_fermate[fermata.id_fermata] = fermata


    def creaGrafo(self):
        self._grafo = nx.MultiDiGraph() # Posso avere più archi tra due nodi
        for fermata in self._lista_fermate:
            self._grafo.add_node(fermata)
        # PRIMO MODO DI AGGIUNGERE GLI ARCHI, CON 619*619 QUERY SQL
        """
        for u in self._grafo: # Per ognuno dei 619 nodi
            for v in self._grafo: # Per ognuno dei possbili nodi connessi
                risultato = DAO.existsConnessioneTra(u, v)
                if(len(risultato) > 0): # C'è almeno una connessione
                    self._grafo.add_edge(u, v) # Creo l'arco
                    print(f"Aggiunto arco tra {u} e {v}")
        """

        # SECONDO MODO, CON 619 QUERY A CERCARE I NODI VICINI
        """
        conta = 0
        for u in self._grafo:
            connessioniAVicini = DAO.searchViciniAFermata(u)
            for connessione in connessioniAVicini:
                fermataArrivo = self._dizionario_fermate[connessione.id_stazA]
                self._grafo.add_edge(u, fermataArrivo)
                print(f"Aggiunto arco tra {u} e {fermataArrivo}")
                print(len(self._grafo.edges()))
        """

        # TERZO MODO, CON UNA QUERY SOLA CHE ESTRAE IN UN COLPO SOLO TUTTE LE CONN.
        """
        listaConnessioni = DAO.readAllConnessioni()
        for c in listaConnessioni:
            u_nodo = self._dizionario_fermate[c.id_stazP]
            v_nodo = self._dizionario_fermate[c.id_stazA]
            self._grafo.add_edge(u_nodo, v_nodo)
            print(f"Aggiunto arco tra {u_nodo} e {v_nodo}")
        """

        # COSTRUISCO UN GRAFO PESATO
        """
        listaConnessioni = DAO.readAllConnessioni()
        for c in listaConnessioni:
            u_nodo = self._dizionario_fermate[c.id_stazP]
            v_nodo = self._dizionario_fermate[c.id_stazA]
            #print(f"{self._grafo[u_nodo][v_nodo]}")
            if self._grafo.has_edge(u_nodo, v_nodo):
                self._grafo[u_nodo][v_nodo]["peso"] += 1
            else:
                self._grafo.add_edge(u_nodo, v_nodo, peso=1)

            print(f"Aggiunto arco tra {u_nodo} e {v_nodo}, peso: {self._grafo[u_nodo][v_nodo]}")
        """
        # COSTRUISCO UN MULTI-GRAFO NEL QUALE IL PESO DEGLI ARCHI E' IL T. PERCORR.
        listaConnessioni = DAO.readAllConnessioni()
        for c in listaConnessioni:
            u_nodo = self._dizionario_fermate[c.id_stazP]
            v_nodo = self._dizionario_fermate[c.id_stazA]
            punto_u = (u_nodo.coordX, u_nodo.coordY)
            punto_v = (v_nodo.coordX, v_nodo.coordY)
            distanza = geodesic(punto_u, punto_v).km
            velocita = DAO.readVelocita(c._id_linea)
            print(f"Distanza: {distanza}, velocità: {velocita}")
            tempo_perc = distanza / velocita * 60 # Tempo percorrenza in min.
            self._grafo.add_edge(u_nodo, v_nodo, tempo = tempo_perc)
            print(f"Aggiunto arco tra {u_nodo} e {v_nodo}, tempo: {self._grafo[u_nodo][v_nodo]}")


        print(self._grafo)


