import pygame
from pygame.locals import *
import random
import time
SIZE = 20


class Apple:
    def __init__(self,parent_screen):
        self.image = pygame.image.load('resources/image.png').convert()
        self.image = pygame.transform.scale(self.image,(20,20))
        self.parent_screen  = parent_screen
        self.x = 100
        self.y = 100

    def draw(self):  
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    def move(self):
        self.x= random.randint(0, 40)*SIZE
        self.y = random.randint(0,30)* SIZE

class Snake:
    def __init__(self, parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('resources/ai.png').convert()
        self.block = pygame.transform.scale(self.block,(20,20))
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'
    def increase(self):
        self.length+=1
        self.y.append(-1)
        self.x.append(-1)    
    def draw(self):
        self.parent_screen.fill((150,150,6))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_down(self):
         self.direction = 'down'
    def move_up(self):
       self.direction = 'up'
    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'up':
            self.y[0]-= SIZE
        if self.direction == 'down':
            self.y[0]+=SIZE
        if self.direction == 'left':
            self.x[0]-=SIZE
        if self.direction == 'right':
            self.x[0]+=SIZE
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((900,600))
        self.surface.fill((150,150,6))
        self.snake = Snake(self.surface, 3)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
    def play(self):
         self.snake.walk()
         self.apple.draw()
         self.display_score()
         pygame.display.flip()
         if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x,self.apple.y):
             self.snake.increase()
             self.apple.move()
         for i in range(3, self.snake.length):
             if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "game over dumbass"
         if self.snake.x[0]<0 or self.snake.x[0]> 900:
             raise Exception
         if self.snake.y[0]<0 or self.snake.y[0]>600:
             raise Exception
                
                #  print("game over dumbass")
                #  exit(0)
             #print("coliiii")
    
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"score: {self.snake.length-3}", True, (255,255,255))
        self.surface.blit(score, (700, 10))
    def collision(self, x1,y1,x2,y2):
        if x1 >= x2 and x1<x2+SIZE:
            if y1 >= y2 and y1<y2+SIZE:
                return True
        return False
            
    def game_over(self):
        self.surface.fill((150,150,6))
        font = pygame.font.SysFont('arial', 20)
        line1 = font.render(f"YOU LOST.... SCORE: {self.snake.length-3}", True, (255,255,255))
        self.surface.blit(line1, (200,300))
        line2 = font.render(f"Press ENTER key to play again, ESC to exit", True, (255,255,255))
        self.surface.blit(line2, (200,250))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, 3)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause= False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()


                elif event.type == QUIT:
                    running = False
            try:
                
                if not pause:
                    self.play()
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()
            
            
            time.sleep(0.1)









if __name__== "__main__":
   game = Game()
   game.run()

    
    

   