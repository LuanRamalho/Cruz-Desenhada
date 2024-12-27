import turtle
import random

def desenhar_cruz():
    # Configuração da tela
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Cruz com Turtle")

    # Configuração da tartaruga
    cruz = turtle.Turtle()
    cruz.speed(3)
    
    # Escolher uma cor aleatória
    cores = ["red", "blue", "green", "purple", "orange", "yellow", "pink"]
    cor_aleatoria = random.choice(cores)
    cruz.color(cor_aleatoria)

    # Desenhar uma cruz
    tamanho_braço = 100  # Define o tamanho de cada braço da cruz

    cruz.pensize(5)  # Espessura da linha

    # Desenhar o braço vertical
    cruz.penup()
    cruz.goto(0, -tamanho_braço)
    cruz.pendown()
    cruz.goto(0, tamanho_braço)

    # Desenhar o braço horizontal
    cruz.penup()
    cruz.goto(-tamanho_braço, 0)
    cruz.pendown()
    cruz.goto(tamanho_braço, 0)

    # Finalizar
    cruz.hideturtle()
    screen.mainloop()

# Chamar a função para desenhar a cruz
desenhar_cruz()
