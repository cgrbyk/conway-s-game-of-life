import numpy as np
import time
from os import system, name
# Kurallar
# Bir canlı hücrenin, iki'den daha az canlı komşusu varsa "yalnızlık nedeniyle" ölür
# Bir canlı hücrenin, üç'ten daha fazla canlı komşusu varsa "kalabalıklaşma nedeniyle" ölür
# Bir canlı hücrenin, iki ya da üç canlı komşusu varsa değişmeden bir sonraki nesile kalır
# Bir ölü hücrenin tam olarak üç canlı komşusu varsa canlanır.

# Hücre class


class Cell:
    def __init__(self, *args, **kwargs):
        self.isDead = True
        self.neighbours = []  # Komşuluk dizisi
        self.aliveCount=0

    def AliveCountCalc(self):
        self.aliveCount = 0
        for n in self.neighbours:  # Hücresnin kaç canlı komşusu olduğunu hesaplayan for
            if(n.isDead == False):
                self.aliveCount += 1

    def DeadCalc(self):
        if(self.isDead == False):  # Canlı hücre sayısına göre yaşam veya ölüme karar
            if(self.aliveCount < 2):
                self.isDead = True
            elif(self.aliveCount > 3):
                self.isDead = True
        else:
            if(self.aliveCount == 3):
                self.isDead = False

    def __repr__(self):  # Print işleminde yaşam durumuna göre yazılacak harf
        if(self.isDead):
            return "D"
        else:
            return "A"


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
cells[2, 6].isDead = False
cells[3, 7].isDead = False
cells[4, 5].isDead = False
cells[4, 6].isDead = False
cells[4, 7].isDead = False

print(cells)
# Saniyede bir çalışan jenerasyon döngüsü
while(True):
    for row in cells:
        for c in row:
            c.AliveCountCalc()
    for row in cells:
        for c in row:
            c.DeadCalc()
    system('cls')
    print(cells)
    time.sleep(1)
