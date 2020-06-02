num1 = num2 = res = 0
gol = "Tipo gobal"

def endRua():
    global rua 
    local = 30
    rua = "Rua 10"

endRua()

print(rua)

print("----------------")
# Tipos de dados

x = 1 #int 
x = "Cadeira" #string
x = 15.6 # float
x = True #bool
n1 = 5; n2 = 2; x = complex(1j) # numeros complexos
x = ["Carro", "Aviao", "Navio", 1, 43.2, False] #list / Array
x = ("Carro", "Aviao", "Navio", 1, 43.2, False) # Tupla

x = range(0, 100, 1) # List

x = { #Dictonare - dict
    "aluno":"jose silva",
    "matricula":"2125",
    "turno":"Manha"
}

x = {3, 32, 32, 64, 64, 96, 10} #set = nao repete os valores no print
x = frozenset({3, 32, 32, 64, 64, 96, 10}) #nao sera alterado

print("Valor: " + str(x))
print("Tipo: ", str(type(x)))