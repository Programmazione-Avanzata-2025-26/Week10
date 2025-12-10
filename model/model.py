import networkx as nx

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
        self._grafo = nx.Graph()
        for fermata in self._lista_fermate:
            self._grafo.add_node(fermata)
        # PRIMO MODO DI AGGIUNGERE I NODI, CON 619*619 QUERY SQL
        """
        for u in self._grafo: # Per ognuno dei 619 nodi
            for v in self._grafo: # Per ognuno dei possbili nodi connessi
                risultato = DAO.existsConnessioneTra(u, v)
                if(len(risultato) > 0): # C'è almeno una connessione
                    self._grafo.add_edge(u, v) # Creo l'arco
                    print(f"Aggiunto arco tra {u} e {v}")
        """

        # SECONDO MODO, CON 619 QUERY A CERCARE I NODI VICINI
        conta = 0
        for u in self._grafo:
            connessioniAVicini = DAO.searchViciniAFermata(u)
            for connessione in connessioniAVicini:
                fermataArrivo = self._dizionario_fermate[connessione.id_stazA]
                self._grafo.add_edge(u, fermataArrivo)
                print(f"Aggiunto arco tra {u} e {fermataArrivo}")
                print(len(self._grafo.edges()))

        print(self._grafo)