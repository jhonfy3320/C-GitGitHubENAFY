# Descripcion de mi proyecto del curso 
# Realizar un juego Cualquiera en python 
# Hay nuevas ideas para este juego 

import tkinter as tk
import random

class JuegoMatematicas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Matemáticas")
        
        self.score = 0
        self.pregunta_actual = None
        self.respuesta_actual = None
        
        self.label_pregunta = tk.Label(root, text="", font=("Arial", 24))
        self.label_pregunta.pack(pady=20)
        
        self.entry_respuesta = tk.Entry(root, font=("Arial", 24))
        self.entry_respuesta.pack(pady=20)
        
        self.boton_comprobar = tk.Button(root, text="Comprobar", command=self.comprobar_respuesta, font=("Arial", 24))
        self.boton_comprobar.pack(pady=20)
        
        self.label_resultado = tk.Label(root, text="", font=("Arial", 24))
        self.label_resultado.pack(pady=20)
        
        self.label_score = tk.Label(root, text="Puntuación: 0", font=("Arial", 24))
        self.label_score.pack(pady=20)
        
        self.nueva_pregunta()
    
    def nueva_pregunta(self):
        operadores = ['+', '-']
        operador = random.choice(operadores)
        
        if operador == '+':
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            self.respuesta_actual = a + b
        else:
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            self.respuesta_actual = a - b
        
        self.pregunta_actual = f"{a} {operador} {b}"
        self.label_pregunta.config(text=self.pregunta_actual)
        self.entry_respuesta.delete(0, tk.END)
    
    def comprobar_respuesta(self):
        respuesta = self.entry_respuesta.get()
        if respuesta.isdigit() and int(respuesta) == self.respuesta_actual:
            self.label_resultado.config(text="Correcto!", fg="green")
            self.score += 1
        else:
            self.label_resultado.config(text="Incorrecto!", fg="red")
        
        self.label_score.config(text=f"Puntuación: {self.score}")
        self.nueva_pregunta()

def main():
    root = tk.Tk()
    juego = JuegoMatematicas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
