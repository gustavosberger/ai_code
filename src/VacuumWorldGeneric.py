from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aicode.search.Graph import State
import sys
import copy
import time


class VacuumWorldGeneric(State):

    def __init__(self, Room ,PosX,PosY, op):
        self.operator = op
        self.PosX = PosX
        self.PosY = PosY
        self.Room = Room
        self.x = len(Room[0])
        self.y = len(Room)


    def env(self):
        return str(self.PosX)+","+str(self.PosY)+";"+self.Room


    def sucessors(self):
        sucessors = []
        if self.Room[self.PosY][self.PosX] == "1":
            clean_room = copy.deepcopy(self.Room)
            clean_room[self.PosY][self.PosX] = "0"
            sucessors.append(VacuumWorldGeneric(clean_room,self.PosX,self.PosY,'limpar'))
       
       
        if self.PosX <= (self.x - 1) and self.PosX > 0 :
            sucessors.append(VacuumWorldGeneric(self.Room, self.PosX - 1,self.PosY,'Move Left'))

        if self.PosX >= 0 and self.PosX < (self.x - 1):
            sucessors.append(VacuumWorldGeneric(self.Room, self.PosX + 1,self.PosY,'Move Right'))
        
        if self.PosY < (self.y - 1) and self.PosY >= 0:
            sucessors.append(VacuumWorldGeneric(self.Room, self.PosX,self.PosY + 1,'Move Down'))

        if self.PosY > 0 and self.PosY < (self.y - 1):
            sucessors.append(VacuumWorldGeneric(self.Room, self.PosX,self.PosY - 1,'Move Up'))


        return sucessors
    

    def is_goal(self):
        for i in self.Room:
            for j in i:
                if j == "1":
                    return False
        return True


    def description(self):
        return "Problema do aspirador de pó, realizando a leitura de um arquivo genérico"
    

    def cost(self):
        return 1


    def print(self):
        return str(self.operator)


def main(positionx,positiony,actualroom):
    print('Busca em profundidade iterativa')
    state = VacuumWorldGeneric(actualroom,positionx,positiony,'')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result)
        print(result.show_path())
    else:
        print('Nao achou solucao')

def convert_file_to_map(path):
    matriz = []
    with open(path) as f:
        lines = f.readlines() 
        for linha in lines:
            linha = linha.strip()
            linha = linha.split(";")
            matriz.append(linha)

    return matriz


if __name__ == '__main__':
    path = sys.argv[1]
    positionx = int(sys.argv[2])
    positiony = int(sys.argv[3])

    actualroom = convert_file_to_map(path)
    main(positionx,positiony,actualroom)
