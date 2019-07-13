import numpy as np
import time
import random
import pygame
import threading
# Kurallar
# Bir canlı hücrenin, iki'den daha az canlı komşusu varsa "yalnızlık nedeniyle" ölür
# Bir canlı hücrenin, üç'ten daha fazla canlı komşusu varsa "kalabalıklaşma nedeniyle" ölür
# Bir canlı hücrenin, iki ya da üç canlı komşusu varsa değişmeden bir sonraki nesile kalır
# Bir ölü hücrenin tam olarak üç canlı komşusu varsa canlanır.

# Hücre class
#komşu sayısına göre ölüm veya yaşamı belirlemek için kullanılan matris
isDeadArray=[[1,1,0,0,1,1,1,1,1],[1,1,1,0,1,1,1,1,1]]
jen=0
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
            return str(chr((1-self.isDead)*33+32))

#Cells matrisindeki her bir ücre için yaşam ve ölüm durumunun hesaplanması recursive yapıda
def CellsCalc():
    global jen
    jen+=1
    for row in cells:
        for c in row:
            c.AliveCountCalc()
    for row in cells:
        for c in row:
            c.DeadCalc()
    timer = threading.Timer(0.3, CellsCalc) #jenerasyonlar arası geçecek süre
    timer.start() 


column, row = 80, 60
cells = []
for i in range(column*row):
    cells.append(Cell())
#cells dizisini verilen satır ve sütüna göre matrise çevirmek
cells = np.reshape(cells, (column, row))
#Komşulukların verilmesi köşeler dışındaki tüm hücreler için gerçekleştiriliyor
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
        cells[i][j].isDead=random.randint(0,1)
#pygame init ve ekran özelliklerinin verilmesi
pygame.init()
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('Conways Game of Life')
clock=pygame.time.Clock()
gameDisplay.fill((255,255,255))
#jenerasyon labelı için font ayarlaması
font = pygame.font.SysFont("comicsansms", 12)
text = font.render('jenerasyon :'+str(jen), True, (0, 128, 0))
isCrashed=0
CellsCalc()
while(isCrashed != 12):
    #cells matrixindeki elemanları oyun alanına çiziyor her bir eleman 10x10 pikselden oluşuyor yaşayanlar siyah ölüler beyaz
    for i in range(0, column):
        for j in range(0, row):
            pygame.draw.rect(gameDisplay,(cells[i][j].isDead*255,cells[i][j].isDead*255,cells[i][j].isDead*255),pygame.Rect(i*10,j*10,10,10))
    text = font.render('jenerasyon :'+str(jen), True, (0, 128, 0))
    gameDisplay.blit(text,(0,0))
    for event in pygame.event.get():
            isCrashed=event.type
    pygame.display.update()
    #oyunu 60 fps'e sabitliyor
    clock.tick(60)

pygame.quit()
quit()

