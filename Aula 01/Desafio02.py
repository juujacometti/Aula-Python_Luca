# Verificar se o ano é bissexto ou não:

ano = int(input("Digite um ano para saber se ele é bissexto:\n"))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")

else:
    print(f"O ano {ano} não é bissexto.")