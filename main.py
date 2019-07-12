import numpy as np
import time
from os import system, name
# Kurallar
# Bir canlı hücrenin, iki'den daha az canlı komşusu varsa "yalnızlık nedeniyle" ölür
# Bir canlı hücrenin, üç'ten daha fazla canlı komşusu varsa "kalabalıklaşma nedeniyle" ölür
# Bir canlı hücrenin, iki ya da üç canlı komşusu varsa değişmeden bir sonraki nesile kalır
# Bir ölü hücrenin tam olarak üç canlı komşusu varsa canlanır.

# Hücre class

isDeadArray=[[1,1,0,0,1,1,1,1,1],[1,1,1,0,1,1,1,1,1]]

class Cell:
    def __init__(self, *args, **kwargs):
        self.isDead = 1
        self.neighbours = []  # Komşuluk dizisi
        self.aliveCount=0

    def AliveCountCalc(self):
        self.aliveCount = 0
        for n in self.neighbours:  # Hücresnin kaç canlı komşusu olduğunu hesaplayan for
                self.aliveCount += 1-n.isDead

    def DeadCalc(self): # Canlı hücre sayısına göre yaşam veya ölüme karar
            self.isDead=isDeadArray[self.isDead][self.aliveCount]

    def __repr__(self):  # Print işleminde yaşam durumuna göre yazılacak harf
            return str(chr((1-self.isDead)*32+32+(1-self.isDead)))


column, row = 20, 20
cells = []
for i in range(column*row):
    cells.append(Cell())
cells = np.reshape(cells, (column, row))
for i in range(1, column-1):
    for j in range(1, row-1):
        cells[i][j].neighbours.append(cells[i-1][j-1])
        cells[i][j].neighbours.append(cells[i][j-1])
        cells[i][j].neighbours.append(cells[i+1][j-1])
        cells[i][j].neighbours.append(cells[i-1][j])
        cells[i][j].neighbours.append(cells[i+1][j])
        cells[i][j].neighbours.append(cells[i-1][j+1])
        cells[i][j].neighbours.append(cells[i][j+1])
        cells[i][j].neighbours.append(cells[i+1][j+1])
# Başlangıç değerleri
cells[8, 8].isDead = 0
cells[8, 9].isDead = 0
cells[8, 10].isDead = 0

cells[9, 8].isDead = 0
cells[9, 10].isDead = 0

cells[10, 8].isDead = 0
cells[10, 9].isDead = 0
cells[10, 10].isDead = 0

cells[11, 8].isDead = 0
cells[11, 9].isDead = 0
cells[11, 10].isDead = 0

cells[12, 8].isDead = 0
cells[12, 9].isDead = 0
cells[12, 10].isDead = 0

cells[13, 8].isDead = 0
cells[13, 10].isDead = 0

cells[14, 8].isDead = 0
cells[14, 9].isDead = 0
cells[14, 10].isDead = 0


# Saniyede bir çalışan jenerasyon döngüsü
while(True):
    print(cells)
    time.sleep(1)
    for row in cells:
        for c in row:
            c.AliveCountCalc()
    for row in cells:
        for c in row:
            c.DeadCalc()
    system('cls')

