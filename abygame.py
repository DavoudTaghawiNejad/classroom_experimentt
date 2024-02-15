import pygame


pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((800, 1400))
screen.fill(black)

myFont = pygame.font.SysFont("Times New Roman", 15)

size = 15

class AbygameAgent:
    def __init__(self, goods, money, i, name):
        if i > 80:
            self.display = False
        else:
            self.display = True
            if name == 'endowed':
                self.x = 50
            else:
                self.x = 150

            self.y = size * i

            pygame.draw.rect(
                screen, 
                blue, 
                (self.x, self.y, size, size))

            if goods > 0:
                pygame.draw.circle(
                    screen, 
                    red, 
                    (self.x, self.y + size), 5)
            
            number_in_font = myFont.render(f'{money:.2f}', 1, green)
            screen.blit(number_in_font, (self.x + size, self.y - size))
            
            pygame.display.update()
            
    def update(self):
        if self.display:
            if self.goods == 0:
                pygame.draw.circle(
                    screen, 
                    black, 
                    (self.x, self.y + size), 5)
                
            else: 
                pygame.draw.circle(
                    screen, 
                    red, 
                    (self.x, self.y + size), 5)
                
            
            pygame.draw.rect(
                screen, 
                black, 
                (self.x + size, self.y - size, 40, size))    
            number_in_font = myFont.render(f'{self.money:.2f}', 1, green)
            screen.blit(number_in_font, (self.x + size, self.y - size))
            
            pygame.display.update()


def quit():
    pygame.quit()
