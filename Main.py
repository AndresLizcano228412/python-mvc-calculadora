from __future__ import annotations
from src.controller.app_controller import AppController
from src.model.calculator import Calculator
from src.view.app_view import AppView


class Main:
    """Clase que inicializa y ejecuta la aplicación calculadora (POO)."""

    def __init__(self) -> None:
        self.model = Calculator()
        self.view = AppView()
        # El controlador se enlaza con la vista dentro de su constructor
        self.controller = AppController(view=self.view, model=self.model)

    def run(self) -> None:
        """Inicia el bucle principal de la GUI."""
        self.view.mainloop()


if __name__ == "__main__":
    Main().run()
