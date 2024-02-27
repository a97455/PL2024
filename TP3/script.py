import re
import sys

def calcular_soma(texto): ##calcula a soma dos doversos numeros entre dois stops (ON|OFF|=)
    soma = 0
    numeros = re.findall(r'\b\d+\b', texto)
    for num in numeros:
        soma += int(num)
    return soma


if __name__ == "__main__":
    with open (sys.argv[1],'r') as f:
        partes = re.split(r'\b(ON|OFF|equal)\b', f.read(), flags=re.I)
        total = 0
        ligado = False

        for parte in partes:
            if parte.upper() == 'ON':
                ligado = True
            elif parte.upper() == 'OFF':
                ligado = False
            elif parte.upper() == 'EQUAL':
                print("Soma dos números até o momento:", total)
            elif ligado:
                total += calcular_soma(parte)