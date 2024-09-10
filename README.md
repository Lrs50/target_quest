# Desafio Target Sistemas

Este repositório contém a solução desenvolvida para o desafio técnico proposto pela empresa Target.

1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

```
def fib(n):
    r0 = 0
    r1 = 1

    while r1 < n:
        r1 += r0
        r0 = r1 - r0
    
    return (n==r1 or n==r0)


def main():

    N = 145

    if fib(N):
        print(f" O número {N} pertence a sequência de Fibonacci!")
    else:
        print(f" O número {N} não pertence a sequência de Fibonacci!")

if __name__ == "__main__":
    main()
```

2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja 
maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

```
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

```

3) Observe o trecho de código abaixo: int INDICE = 12, 
SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

```
def main():

    INDICE,SOMA,K = 12,0,1
    
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print(SOMA)


if __name__ == "__main__":
    main()
```

4) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, **9**

→ Números impares, *n+1*

b) 2, 4, 8, 16, 32, 64, **128**

→ Número anterior vezes 2

c) 0, 1, 4, 9, 16, 25, 36, **49**

→ Números ao quadrado, *n²*

d) 4, 16, 36, 64, **100**

→ Números pares ao quadrado

e) 1, 1, 2, 3, 5, 8, **13**

→ Sequência de Fibonacci

f) 2,10, 12, 16, 17, 18, 19, **200**

→ Números que começam com a letra 'd'

5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas 
vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para 
descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

1. **Ligue o interruptor 1 e deixe-o ligado por aproximadamente 3 minutos.**

2. **Após 3 minutos, desligue o interruptor 1 e ligue o interruptor 2.**

3. **Vá até a Sala 1:**
   - Se a lâmpada estiver **acesa**, ela é controlada pelo **interruptor 2**.
   - Se a lâmpada estiver **apagada**, toque nela:
     - Se estiver **quente**, ela é controlada pelo **interruptor 1** (o que estava ligado por 3 minutos e depois desligado).
     - Se estiver **fria**, ela é controlada pelo **interruptor 3** (o que nunca foi ligado).

4. **Após identificar o interruptor da Sala 1, vá até a Sala 2:**
   - Use a mesma lógica para identificar qual interruptor controla a lâmpada na Sala 2.

5. **Por eliminação, você saberá qual interruptor controla a lâmpada na Sala 3, sem precisar entrar nela.**

   