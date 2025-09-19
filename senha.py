contador = 0
while contador < 3:
    print("Para proseguir, digite a senha")
    senha = input("Senha: ")
    if senha == "pedrinho123":
        print("seja bem vindo")
        break
    else:
        print("tente novamente")
        contador +=1
    if contador == 3:
        print("limite ultrapassado, fim...")
            