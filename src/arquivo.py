# Um arquivo só é um arquivo só ¯\_(ツ)_/¯ 

# ===Definições===
from enum import IntEnum

class Triag(IntEnum):
    VERMELHO = 0
    LARANJA  = 1
    AMARELO  = 2
    VERDE    = 3
    AZUL     = 4

class ArvoreNo:
    def __init__(self,pergunta:str,pos_val:int=1):
        self.não:ArvoreNo|None = None
        #     ^ momento utf-8
        self.sim:ArvoreNo|None = None
        self.pergunta:str = pergunta
        self.val:int = pos_val

class Fila:
    def __init__(self) -> None:
        self.filas:list[list[str]] = [[] for _ in range(len(Triag))]
    
    def chamar_paciente(self)->str:
        for fila in self.filas:
            if len(fila)!=0:
                return fila.pop(0)
        return "Não há pacientes para chamar"
        
    def cadastrar_paciente(self,nome:str,triagem:Triag):
        if nome!="":
            self.filas[triagem.value].append(nome)
            return
        raise ValueError("Argumento 'nome' não pode estar vazio")



# ===funções===
def montar_arvore()->ArvoreNo:
    respirando  = ArvoreNo("Está respirando?")
    consciente  = ArvoreNo("Está consciente?")
    coerente    = ArvoreNo("Está coerente?")
    dor         = ArvoreNo("Está com dor?",-1)
    dor_intensa = ArvoreNo("Está com dor intensa?",-1)
    sangrando   = ArvoreNo("Está sangrando?",-1)
    
    respirando.sim = consciente
    
    consciente.sim = coerente
    coerente.sim = dor
    
    dor.não = sangrando
    dor.sim = dor_intensa

    dor_intensa.não = sangrando
    dor_intensa.sim = sangrando

    return respirando
    

def triagem(arvore:ArvoreNo) -> Triag:
    clear()
    print(cabeçalho)
    print("\n Iniciando triagem, responda as perguntas em relação ao paciente")
    triag_val = 0
    pos = arvore
    while pos!=None:
        print(pos.pergunta)
        match input(" (S)im/(N)ão > ").upper():
            case "N":
                triag_val = triag_val - pos.val
                pos = pos.não
            case _:
                triag_val = triag_val + pos.val
                pos = pos.sim

    if triag_val < Triag.VERMELHO:
        return Triag.VERMELHO
    elif triag_val > Triag.AZUL:
        return Triag.AZUL

    return Triag(triag_val)



# ===Interface===

cabeçalho = "=== SISTEMA DE TRIAGEM MANCHESTER ==="
#   ^ de proposito msm, sou malvado >:D

#  v utf-8 FTW 🥳
opções = """
    (A)dicionar paciente
    (C)hamar paciente
    (M)ostrar status das filas
    (S)air
"""

descrição = [
    "Vermelho - Emergência ATENDIMENTO IMEDIATO",
    "Laranja - muito urgente",
    "Amarelo - urgente",
    "Verde - pouco urgente",
    "Azul - não urgente"
]


# ===Programa principal===
import os
clear = lambda: os.system('cls & clear')
def main():
    batman = Fila()
    robin = montar_arvore()
    while True:
        clear()
        print(cabeçalho)
        print("\n Pacientes na filas:")
        ix = 0
        for fila in batman.filas:
            print(f'  {str(len(fila)).zfill(2)}: {descrição[ix]}') 
            ix = ix + 1
        print(opções)
        match input(" Selecione uma opção acima\n  > ").upper():
            case "A":
                clear()
                print(cabeçalho)
                print("\n ADICIONANDO PACIENTE")
                paciente_nome = input(" Digite o nome do paciente:\n  > ")
                triag = triagem(robin)
                clear()
                print(cabeçalho)
                print("\n PACIENTE ADICINADO")
                print(f'\n FILA: {descrição[triag]}')
                batman.cadastrar_paciente(paciente_nome,triag)
                input("\n Pressione enter para continuar")
            case "C":
                clear()
                print(cabeçalho)
                print("\n CHAMANDO PACIENTE: ",end="\n  ")
                print(batman.chamar_paciente())
                input("\n Pressione enter para continuar")
            case "M":
                clear()
                print(cabeçalho)
                print('Listagem de pacientes')
                ix = 0
                for fila in batman.filas:
                    print(f'{descrição[ix]}:') 
                    if len(fila)==0:
                        print(" Sem pacientes\n")
                    else:
                        for paciente in fila:
                            print(f' - {paciente}')
                    ix = ix + 1
                input("\n Pressione enter para continuar")
            case "S":
                match input("\n Tem certeza que deseja sair?\n (S)im/(N)ão > ").upper():
                    case "S":
                        print("Encerrando...")
                        exit(0)
main()