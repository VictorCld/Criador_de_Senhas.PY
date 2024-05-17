import random

senha = ""

caracteres = "zaq12xvfr4bgr5nht!@#$%&*"

for digito in range(8):
  aleatorio = random.choice(caracteres)
  senha += aleatorio

print("-"*20)
print(senha)
print("-"*20)