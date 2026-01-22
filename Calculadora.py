import math
import tkinter as tk
from tkinter import font

class CalculadoraCientifica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora Científica")
        self.ventana.geometry("500x600")
        self.ventana.config(bg="#2b2b2b")
        
        # Variable para almacenar la entrada
        self.expresion = ""
        
        # Display
        self.display = tk.Entry(
            ventana, 
            font=("Arial", 20), 
            borderwidth=2, 
            relief="solid",
            bg="#1e1e1e",
            fg="#00ff00",
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)
        
        # Frame para botones
        frame_botones = tk.Frame(ventana, bg="#2b2b2b")
        frame_botones.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Definir los botones
        botones = [
            ["C", "DEL", "π", "e"],
            ["sin", "cos", "tan", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "√"]
        ]
        
        # Crear botones
        for fila in botones:
            frame_fila = tk.Frame(frame_botones, bg="#2b2b2b")
            frame_fila.pack(fill="both", expand=True, pady=5)
            
            for boton in fila:
                btn = tk.Button(
                    frame_fila,
                    text=boton,
                    font=("Arial", 14, "bold"),
                    bg="#404040",
                    fg="#00ff00",
                    relief="raised",
                    command=lambda b=boton: self.on_click(b),
                    activebackground="#505050",
                    activeforeground="#00ff00"
                )
                btn.pack(side="left", fill="both", expand=True, padx=2)
    
    def on_click(self, boton):
        if boton == "C":
            self.expresion = ""
            self.display.delete(0, tk.END)
        
        elif boton == "DEL":
            self.expresion = self.expresion[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expresion)
        
        elif boton == "=":
            try:
                resultado = eval(self.expresion)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
                self.expresion = str(resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expresion = ""
        
        elif boton == "π":
            self.expresion += str(math.pi)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expresion)
        
        elif boton == "e":
            self.expresion += str(math.e)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expresion)
        
        elif boton == "√":
            try:
                resultado = math.sqrt(float(self.expresion))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
                self.expresion = str(resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expresion = ""
        
        elif boton == "sin":
            try:
                resultado = math.sin(math.radians(float(self.expresion)))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
                self.expresion = str(resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expresion = ""
        
        elif boton == "cos":
            try:
                resultado = math.cos(math.radians(float(self.expresion)))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
                self.expresion = str(resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expresion = ""
        
        elif boton == "tan":
            try:
                resultado = math.tan(math.radians(float(self.expresion)))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
                self.expresion = str(resultado)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expresion = ""
        
        else:
            self.expresion += boton
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expresion)

# Ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    calculadora = CalculadoraCientifica(ventana)
    ventana.mainloop()
