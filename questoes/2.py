"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
"""

def main():
    string ="A alma que falar com os olhos, também pode calar com a ausência deles"

    count = 0
    for c in string:
        if c == "a" or c=="A":
            count+=1

    if count>0:
        print(f"Temos letras 'a' ou 'A' no texto e elas somadas ocorem {count} vezes!")
    else:
        print("Não temos a letra 'a' no texto, nem em sua forma minúscula nem maiúscula :(")

if __name__ == "__main__":
    main()