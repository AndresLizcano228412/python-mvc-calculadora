# src/view/app_view.py
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import Tuple, Optional


class AppView(tk.Tk):
    """Vista de la aplicación (tkinter)."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Calculadora MVC (Python)")
        self.geometry("820x360")
        self.resizable(False, False)

        self._controller = None  # type: Optional[object]

        # Widgets
        frm = tk.Frame(self, padx=12, pady=12)
        frm.pack(fill=tk.BOTH, expand=True)

        tk.Label(frm, text="Operando A:").grid(row=0, column=0, sticky="w")
        tk.Label(frm, text="Operando B:").grid(row=1, column=0, sticky="w")

        self.entry_a = tk.Entry(frm, width=20)
        self.entry_b = tk.Entry(frm, width=20)
        self.entry_a.grid(row=0, column=1, padx=6, pady=4)
        self.entry_b.grid(row=1, column=1, padx=6, pady=4)

        # Botones de operaciones
        ops = tk.Frame(frm)
        ops.grid(row=2, column=0, columnspan=2, pady=8)

        self.btn_add = tk.Button(ops, text="+", width=5)
        self.btn_sub = tk.Button(ops, text="−", width=5)
        self.btn_mul = tk.Button(ops, text="×", width=5)
        self.btn_div = tk.Button(ops, text="÷", width=5)
        self.btn_mod = tk.Button(ops, text="mod", width=5)
        self.btn_pow = tk.Button(ops, text="^", width=5)
        self.btn_fact = tk.Button(ops, text="Factorial", width=5)
        self.btn_ex = tk.Button(ops, text="e**x", width=5)
        self.btn_seno = tk.Button(ops, text="sin(x)", width=5)
        self.btn_coseno = tk.Button(ops, text="cos(x)", width=5)
        self.btn_arcotangente = tk.Button(ops, text="arcotan(x)", width=5)
        self.btn_pi = tk.Button(ops, text="π", width=5)

        self.btn_add.grid(row=0, column=0, padx=4, pady=2)
        self.btn_sub.grid(row=0, column=1, padx=4, pady=2)
        self.btn_mul.grid(row=0, column=2, padx=4, pady=2)
        self.btn_div.grid(row=0, column=3, padx=4, pady=2)
        self.btn_mod.grid(row=0, column=4, padx=4, pady=2)
        self.btn_pow.grid(row=0, column=5, padx=4, pady=2)
        self.btn_fact.grid(row=0, column=6, padx=4, pady=2)
        self.btn_ex.grid(row=1, column=0, padx=4, pady=2)
        self.btn_seno.grid(row=1, column=1, padx=4, pady=2)
        self.btn_coseno.grid(row=1, column=2, padx=4, pady=2)
        self.btn_arcotangente.grid(row=1, column=3, padx=4, pady=2)
        self.btn_pi.grid(row=1, column=4, padx=4, pady=2)

        # Resultado
        self.result_var = tk.StringVar(value="Resultado: ")
        self.lbl_result = tk.Label(frm, textvariable=self.result_var, anchor="w")
        self.lbl_result.grid(row=3, column=0, columnspan=2, sticky="we", pady=8)

        # Acciones
        actions = tk.Frame(frm)
        actions.grid(row=4, column=0, columnspan=2, pady=6)
        self.btn_clear = tk.Button(
            actions, text="Limpiar", width=10, command=self.clear
        )
        self.btn_exit = tk.Button(actions, text="Salir", width=10, command=self.destroy)
        self.btn_clear.grid(row=0, column=0, padx=6)
        self.btn_exit.grid(row=0, column=1, padx=6)

    # ---------- API de la Vista ----------

    def set_controller(self, controller: object) -> None:
        """Asigna el controlador y conecta callbacks."""
        self._controller = controller
        # Diferimos la asociación de comandos para evitar referencias circulares previas
        self.btn_add.config(command=self._controller.on_add)
        self.btn_sub.config(command=self._controller.on_sub)
        self.btn_mul.config(command=self._controller.on_mul)
        self.btn_div.config(command=self._controller.on_div)
        self.btn_mod.config(command=self._controller.on_mod)
        self.btn_pow.config(command=self._controller.on_pow)
        self.btn_fact.config(command=self._controller.on_factorial)
        self.btn_ex.config(command=self._controller.on_ex)
        self.btn_seno.config(command=self._controller.on_seno)
        self.btn_coseno.config(command=self._controller.on_coseno)
        self.btn_arcotangente.config(command=self._controller.on_arcotangente)
        self.btn_pi.config(command=self._controller.on_pi)

    def get_operands(self) -> Tuple[int, int]:
        """Obtiene los dos operandos de los campos de entrada."""
        a_text = self.entry_a.get().strip()
        b_text = self.entry_b.get().strip()

        if not a_text:
            raise ValueError("Por favor, ingrese un valor en el Operando A.")
        if not b_text:
            raise ValueError("Por favor, ingrese un valor en el Operando B.")

        try:
            a = int(a_text)
            b = int(b_text)
            return a, b
        except ValueError:
            raise ValueError(
                "Por favor, ingrese números enteros válidos en ambos operandos."
            )

    def get_single_operand(self) -> int:
        """Obtiene solo el primer operando."""
        a_text = self.entry_a.get().strip()
        if not a_text:
            raise ValueError("Por favor, ingrese un valor en el Operando A.")

        try:
            return int(a_text)
        except ValueError:
            raise ValueError(
                "Por favor, ingrese un número entero válido en el Operando A."
            )

    def set_result(self, text: str) -> None:
        self.result_var.set(f"Resultado: {text}")

    def show_error(self, msg: str) -> None:
        messagebox.showerror("Error", msg)

    def clear(self) -> None:
        self.entry_a.delete(0, tk.END)
        self.entry_b.delete(0, tk.END)
        self.result_var.set("Resultado: ")
        self.entry_a.focus_set()
