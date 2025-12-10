from model.model import Model

model = Model()
model.getAllFermate()
print(model._lista_fermate)

model.creaGrafo()

for nodo in model._grafo.nodes:
    print(f"{nodo} grado: {model._grafo.out_degree(nodo)}")
