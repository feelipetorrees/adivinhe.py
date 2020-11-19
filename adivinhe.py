from random import randint
print("--------------------")
print("Jogo da Adivinhação")
print("--------------------")
print("    De 1 a 10")
sortear = randint(1,10)
adivinhe = 0

while adivinhe != sortear:
    adivinhe = int(input("Digite um número: "))
   
    if adivinhe == sortear:
         print("\033[0;32mVocê VENCEU!\033[m")
       else: 
         if adivinhe > sortear:
             print("Seu chute foi ALTO")
       else:
             print("Seu chute foi BAIXO")

print("Jogo finalizado!")




