import re
import sys


if __name__ == "__main__":
    with open (sys.argv[1],'r') as f:
        products = re.split(r'\n', f.read())
        saldo = 0 #em centimos

        while True:
            choice = input(">> ")
            if choice=="LISTAR":
                for product in products:
                    print(product)
            elif re.search(r'MOEDA',choice):
                values = re.findall(r'(\d+(?:euro|cent))',choice)
                for value in values:
                    if expreg := re.match(r'(\d+)euro',value):
                        saldo+= int(expreg.group(1))*100
                    elif expreg := re.match(r'(\d+)cent',value):
                        saldo+= int(expreg.group(1))
                print("Saldo =",str(saldo//100)+"euro",str(saldo%100)+"cent")
            elif id := re.search(r'SELECIONAR (\d+)',choice):
                pass
            elif re.search(r'SAIR',choice):
                print("Troco =",str(saldo//100)+"euro",str(saldo%100)+"cent")
                break