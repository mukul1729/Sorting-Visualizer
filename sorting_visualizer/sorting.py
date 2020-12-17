import pygame 
import random
import time
class sorting:
    def __init__(self):
        self.x,self.y = 1910,1000
        self.sorted = (123,199,50)
        self.unsorted = (152,30,30)
        self.runn = (30,30,30)

    def bar(self,screen,x,y,color,height,width):
        font = pygame.font.Font('/usr/share/fonts/TTF/OpenSans-Regular.ttf',20)
        pygame.draw.rect(screen,color,(x,y,width,-8*height))
        txt = font.render(str(height),True,(20,20,20))
        screen.blit(txt,(x,y-8*height-40))

    def make(self,arr,screen,i,j,ele,name):
        if name == 'bubble':
            x = 350
            for r in range(len(arr)):
                if r == j+1 or r==j:
                    self.bar(screen,x,930,self.runn,arr[r],20)
                elif r >= len(arr)-i:
                    self.bar(screen,x,930,self.sorted,arr[r],20)
                else:
                    self.bar(screen,x,930,self.unsorted,arr[r],20)
                x+=30
        elif name == 'insertion':
            x = 350
            for r in range(len(arr)):
                if r == j:
                    self.bar(screen,x,930,self.runn,ele,20)
                elif r<=i-1:
                    self.bar(screen,x,930,self.sorted,arr[r],20)
                else:
                    self.bar(screen,x,930,self.unsorted,arr[r],20)
                x+=30
        elif name == 'merge':
            x = 350
            for r in range(len(arr)):
                if r == j:
                    self.bar(screen,x,930,self.runn,arr[r],20)
                elif r==i:
                    self.bar(screen,x,930,self.sorted,arr[r],20)
                else:
                    self.bar(screen,x,930,self.unsorted,arr[r],20)
                x+=30

    def bubblesort(self,arr,screen,speed):
        for i in range(len(arr)):
            for j in range(len(arr)-1-i):
                screen.fill((255,255,255))
                self.make(arr,screen,i,j,None,'bubble')
                clock.tick(speed)
                pygame.display.update()
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    screen.fill((255,255,255))
                    self.make(arr,screen,i,j,None,'bubble')
                    clock.tick(speed)
                    pygame.display.update()

    def insertionsort(self,arr,screen,speed):
        for i in range(1,len(arr)):
            ele = arr[i]
            j = i
            while j>0 and arr[j-1]>ele:
                arr[j] = arr[j-1]
                screen.fill((255,255,255))
                self.make(arr,screen,i,j,ele,'insertion') 
                j-=1
                clock.tick(speed)
                pygame.display.update()             
            screen.fill((255,255,255))
            arr[j] = ele
            self.make(arr,screen,i,j,ele,'insertion') 
            clock.tick(speed)
            pygame.display.update()             

    def mergesort(self,s1,s2,screen,speed):
        i,j = 0,0
        arr = [0]*(len(s1)+len(s2))
        while i+j<len(arr):
            if j == len(s2) or (i<len(s1) and s1[i]<s2[j]):
                arr[i+j] = s1[i]
                i+=1
            else:
                arr[i+j] = s2[j]
                j+=1
        screen.fill((255,255,255))
        self.make(arr,screen,i,j,None,'insertion') 
        clock.tick(speed)
        pygame.display.update()             
        return arr
        
    def merge(self,arr,ori,screen,speed):
        if len(arr)==1:
            return arr
        else:
            n = len(arr)
            mid = n//2
            s1 = arr[0:mid]
            s2 = arr[mid:]
            s1 = self.merge(s1,ori,screen,speed)
            s2 = self.merge(s2,ori,screen,speed)
            arr = self.mergesort(s1,s2,screen,speed)
        return arr
        

pygame.init()
sort = sorting()
screen = pygame.display.set_mode((sort.x,sort.y))
screen.fill((255,255,255))
clock = pygame.time.Clock()
run = True
arr = [random.randint(1,90) for i in range(40)]
speed = 60
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #sort.bubblesort(arr,screen,speed)
    sort.insertionsort(arr,screen,speed)
    #sort.merge(arr,arr,screen,speed)
    
    time.sleep(5)
    run = False
