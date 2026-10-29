def sobre():
    print ("Desenvolvido por: Beatris Antunes Silva")

#Função com parâmetros
def turma(turma, ano):
    print (f"Turma: {turma}")


#Função com retorno e com parametros 
def somar (numero1, numero2):
    return numero1 + numero2

sobre()
turma("AD-05", 2026)

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
resultado = somar(10, 5)
print(f"A somna de {numero1} = {numero2} = {resultado}")