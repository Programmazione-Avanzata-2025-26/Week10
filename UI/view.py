import flet as ft
import os

class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Metro Paris"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        page.window.width = 1000
        page.window.height = 600
        page.window.center()
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self.lst_result = None
        self._title = None
        self._logo = None
        self._ddStazArrivo = None
        self._ddStazPartenza = None
        self._btnCrea = None

    def load_interface(self):
        # title
        self._title = ft.Text("Metro Paris", color="green", size=24)

        # ROW with title
        img_path = os.path.join(os.getcwd(), 'database/RATP.png')
        self._logo = ft.Image(src=img_path,
                              width=100,
                              height=100,
                              )

        row1 = ft.Row([self._title, self._logo],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Row with controls
        self._btnCrea = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo)
        self._ddStazPartenza = ft.Dropdown(label="Stazione di Partenza", width=250 )
        self._ddStazArrivo = ft.Dropdown(label="Stazione di Arrivo", width=250)
        self._btnCalcola = ft.ElevatedButton(text="Calcola Raggiungibili", on_click=self._controller.handleCercaRaggiungibili)

        self._controller.populate_dropdown(self._ddStazPartenza)
        self._controller.populate_dropdown(self._ddStazArrivo)


        row2 = ft.Row([self._btnCrea,
                       self._ddStazPartenza,
                       self._ddStazArrivo,
                       self._btnCalcola,
                       ], alignment=ft.MainAxisAlignment.CENTER, spacing=30)

        # Row with listview
        self.lst_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

        self._page.add(row1, row2, self.lst_result)

        self._page.update()

    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller