"""Modulo controlador para la aplicación calculadora."""

# src/controller/app_controller.py
from __future__ import annotations


from typing import Optional

from src.model.calculator import (
    Calculator,
    DivisionPorCeroError,
    ExponenteInvalidoError,
)
from src.view.app_view import AppView


class AppController:
    """Controlador: conecta la Vista con el Modelo."""

    def __init__(self, view: AppView, model: Calculator) -> None:
        self.view = view
        self.model = model
        self.view.set_controller(self)

    # ------------- Handlers -------------

    def _with_operands(self, op_name: str, func) -> None:
        try:
            a, b = self.view.get_operands()
            result = func(a, b)
            self.view.set_result(str(result))
        except DivisionPorCeroError as e:
            self.view.show_error(str(e))
        except ExponenteInvalidoError as e:
            self.view.show_error(str(e))
        except ValueError as e:
            self.view.show_error(str(e))
        except Exception:
            self.view.show_error(
                f"Ocurrió un error inesperado en la operación {op_name}."
            )

    def _with_single_operand(self, op_name: str, func) -> None:
        try:
            a = self.view.get_single_operand()
            result = func(a)
            self.view.set_result(str(result))
        except ValueError as e:
            self.view.show_error(str(e))
        except Exception:
            self.view.show_error(
                f"Ocurrió un error inesperado en la operación {op_name}."
            )

    def on_add(self) -> None:
        self._with_operands("suma", self.model.suma)

    def on_sub(self) -> None:
        self._with_operands("resta", self.model.resta)

    def on_mul(self) -> None:
        self._with_operands("multiplicación", self.model.multiplicacion)

    def on_div(self) -> None:
        self._with_operands("división", self.model.division)

    def on_mod(self) -> None:
        self._with_operands("módulo", self.model.modulo)

    def on_pow(self) -> None:
        self._with_operands("potenciación", self.model.potenciacion)

    def on_factorial(self) -> None:
        self._with_single_operand("factorial", self.model.factorial)

    def on_ex(self) -> None:
        self._with_single_operand("exponencial", self.model.ex)

    def on_seno(self) -> None:
        self._with_single_operand("seno", self.model.seno)

    def on_coseno(self) -> None:
        self._with_single_operand("coseno", self.model.coseno)

    def on_arcotangente(self) -> None:
        self._with_single_operand("arcotangente", self.model.arcotangente)

    def on_pi(self) -> None:
        try:
            resultado = self.model.leibniz_pi(500000)
            self.view.set_result(str(resultado))
        except Exception:
            self.view.show_error("error al calcular pi")
