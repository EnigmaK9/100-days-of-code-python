import random

frases_reconfortantes = [
    "Andy, eres una persona maravillosa.",
    "Todo va a estar bien, Andy.",
    "Andy, eres una chica fuerte y valiente.",
    "¡Sonríe, Andy! Tu sonrisa ilumina el mundo.",
    "Andy, tienes un futuro brillante por delante.",
    "Andy, eres amada y cuidada.",
]

def mostrar_frase_reconfortante():
    frase = random.choice(frases_reconfortantes)
    print(frase)

# Loop para mostrar frases reconfortantes
while True:
    input("Presiona Enter para ver una frase reconfortante para Andy...")
    mostrar_frase_reconfortante()

