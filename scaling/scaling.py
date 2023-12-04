import tkinter as tk

def mostrar_respuesta():
    numero_seleccionado = scale.get()

    if numero_seleccionado <= 3:
        respuesta_label.config(text="Lo siento mucho de escuchar que estás triste. Siempre hay luz al final del túnel, ¡ánimo!")
    elif numero_seleccionado <= 7:
        respuesta_label.config(text="Estás en un punto intermedio, ¡sigue adelante y busca lo que te hace feliz!")
    elif numero_seleccionado <= 10:
        respuesta_label.config(text="¡Eso es genial! Te encuentras muy feliz, ¡disfruta tu día al máximo!")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Pregunta de escala")

# Crear una escala (slider) para seleccionar el número
scale = tk.Scale(ventana, from_=1, to=10, orient="horizontal", label="Selecciona un número:")
scale.pack()

# Botón para mostrar la respuesta
boton_mostrar = tk.Button(ventana, text="Mostrar Respuesta", command=mostrar_respuesta)
boton_mostrar.pack()

# Etiqueta para mostrar la respuesta
respuesta_label = tk.Label(ventana, text="")
respuesta_label.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()

