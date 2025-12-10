import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self,e):
        self._model.creaGrafo()



    def handleCercaRaggiungibili(self,e):
        pass

    def populate_dropdown(self,dd):
        self._model.getAllFermate()
        #Le fermate le trovo nel model, in _lista_fermate

        for fermata in self._model._lista_fermate:
            dd.options.append(ft.dropdown.Option(key=fermata.id_fermata,
                                                 text=fermata.nome))
