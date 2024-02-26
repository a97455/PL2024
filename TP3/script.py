import re
import sys

def sumOnOff(file):
    sum = 0
    on = False
    numeros = re.findall(r'\d+', file)
    for num in numeros:
        if on:
            sum += int(num)
        if re.search(r'ON', file, re.I):
            on = True
        elif re.search(r'OFF', file, re.I):
            on = False
        ## elif re.search(r'=', file):
        print("Soma até o momento:", sum)


if __name__ == "__main__":
    with open(sys.argv[1],'r', encoding='utf-8') as f:
        sumOnOff(f.read())