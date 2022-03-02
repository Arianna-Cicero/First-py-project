#variables
global opcao
global i
i=0
opcao = 1
opcao1 = 1
resposta = 1
media = float(0)
puta_array = []
popped = 0
resposta_final = 1
sum = float(0)
global temp


#decoration function
def deco():
    for i in range(70):
        print("*", end='')

#Function from the option 1 from the menu
def opc1():
    print("\t\tInserção de temperaturas")
    deco()
    temp = input("\nEscreva o valor da temperatura em graus Celcius: ")
    float(temp)
    deco()
    print("\n\t\tTemperaturas inseridas")
    deco()
    try:
        #open the file and write the information inside bc of the "w"
        with open("D:\\py\\tests\\information.txt", "w") as writer:
            puta_array.append(temp)
            for i in puta_array:
                writer.write(i)   
        
    except NameError:
        print("NameError:",NameError)
        #for i, element in enumerate(writer.readlines()):
        #    print(i, element)
    finally:
        print("Processo terminado.")

def opc2():
    try:
        #open the file and read the information inside bc of the "r"
        with open("D:\\py\\tests\\information.txt", "r") as reader:
            print("\n\t\tTemperaturas inseridas")
            deco()
            for i, element in enumerate(reader.readlines()):
                puta_array.append(element)
                print(i, element)
    except NameError:
        print("NameError:",NameError)    
    finally:
        print("Processo terminado.")

def opc3():
    try:
        #open the file and read the information inside bc of the "r"
        with open("D:\\py\\tests\\information.txt", "r") as reader:
            print("\t\tTemperaturas inseridas")
            deco()
            for i, element in enumerate(reader.readlines()):
                print(i, element)
        popped = input("\nInsira a posição da temperatura que deseja eliminar: ")
        int(popped)
        for i in puta_array:
            puta_array.pop(popped)
    except NameError:
        print("NameError:",NameError)    
    finally:
        print("Processo terminado.")

def opc4():
    try:
        with open("D:\\py\\tests\\information.txt", "r") as reader:
            print("\t\tTemperaturas inseridas")
            deco()
            for i, element in enumerate(reader.readlines()):
                print(i, element, end="\n")
        line_modify = input("Qual é o número da linha que deseja alterar?")
        int(line_modify)
        modify = input("Escreva a nova temperatura: ")
        float(modify)
        for i in puta_array:
            puta_array[line_modify] = modify
    except NameError:
        print("NameError:",NameError)    
    finally:
        print("Processo terminado.")
    

def opc5():
    try:
        with open("D:\\py\\tests\\information.txt", "r") as reader:
            print("\t\tTemperaturas inseridas")
            deco()
            for element, line in enumerate(reader.readlines()):
                puta_array.append(line)

        for i in len(puta_array):
            sum = sum + puta_array[i]
        media = sum / len(puta_array)
        print("\nMedia das temperaturas: " + media)
    except NameError:
        print("NameError:",NameError)    
    finally:
        print("Processo terminado.")


def menu():
    final = 1
    int(final)
    while final != 0:
        print("\n\t\t\tMENU DE TEMPERATURAS")
        deco()
        print("\n1. Inserir")
        print("2. Listar")
        print("3. Apagar")
        print("4. Alterar")
        print("5. Media")
        print("0. Fechar programa")
        deco()
        opcao = input("\nQual a opcao? ")
        
        if(opcao=='1'):
            opc1()
            resposta = input("Quer inserir outra temperatura? ")
            if (resposta == 's' or resposta == 'S'):
                deco()
                opc1()
            else:
                deco()
                menu()
        elif(opcao=='2'):    
            opc2()
            menu()
                    
        elif(opcao=='3'):
            opc3()
            resposta = input("Quer eliminar outra temperatura? (S - N): ")         
            if (resposta == 's' or resposta == 'S'):
                deco()
                opc3()
            else:
                deco()
                menu()
        elif(opcao=='4'):
            opc4()
            resposta = input("Quer alterar outra temperatura? ")
            if (resposta == 's' or resposta == 'S'):
                deco()
                opc4()
            else:
                deco()
                menu()
        elif(opcao=='5'):
            opc5()
            deco()
            menu()
        elif (opcao == '0'):
            print("Fechando...")
            final = 0
        else:
            print("Opção invalida. Por favor insira uma opção valida: ")
            menu()


print("Programa de temperaturas")
deco()
menu()





