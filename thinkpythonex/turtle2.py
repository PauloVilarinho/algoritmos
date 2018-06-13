import turtle

bob = turtle.Turtle()
tamanho = int(input("qualo tamanho dos lados"))
lados = int(input("quantos lados"))

def poligon(turtle,tamanho,lados):
    for i in range (lados):
        turtle.fd(tamanho)
        turtle.lt(360/lados)

poligon(bob,tamanho,lados)
