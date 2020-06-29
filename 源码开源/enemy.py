from random import *
import pygame

#小型飞机
class smallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.width,self.height=bg_size[0],bg_size[1]
        self.image=pygame.image.load('images\enemy1.png').convert_alpha()

        self.destory_images=[]
        self.destory_images.extend([
            pygame.image.load(r"images\enemy1_down1.png").convert_alpha(),
            pygame.image.load(r"images\enemy1_down2.png").convert_alpha(),
            pygame.image.load(r"images\enemy1_down3.png").convert_alpha(),
            pygame.image.load(r"images\enemy1_down4.png").convert_alpha()
        ])
        self.mask=pygame.mask.from_surface(self.image)
        self.active=True
        self.rect=self.image.get_rect()
        self.speed=2
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-5*self.height,0)

    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    #位置重置
    def reset(self):
        self.active=True
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-5*self.height,0)

#中型飞机
class midEnemy(pygame.sprite.Sprite):
    energy=8
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.width,self.height=bg_size[0],bg_size[1]
        self.image=pygame.image.load('images\enemy2.png').convert_alpha()
        self.image_hit=pygame.image.load('images\enemy2_hit.png').convert_alpha()
        self.destory_images=[]
        self.destory_images.extend([
            pygame.image.load(r"images\enemy2_down1.png").convert_alpha(),
            pygame.image.load(r"images\enemy2_down2.png").convert_alpha(),
            pygame.image.load(r"images\enemy2_down3.png").convert_alpha(),
            pygame.image.load(r"images\enemy2_down4.png").convert_alpha()
        ])
        self.mask=pygame.mask.from_surface(self.image)
        self.active=True
        self.rect=self.image.get_rect()
        self.speed=1
        self.hit=False
        self.energy=midEnemy.energy
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-8*self.height,-self.height)
        #self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-5*self.height,0)
        #self.speed=2

    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    #位置重置
    def reset(self):
        self.active=True
        self.energy=midEnemy.energy
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-8*self.height,-self.height)


#大型飞机
class bigEnemy(pygame.sprite.Sprite):
    energy=20
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.width,self.height=bg_size[0],bg_size[1]
        self.image=pygame.image.load('images\enemy3_n1.png').convert_alpha()
        self.image2=pygame.image.load('images\enemy3_n2.png').convert_alpha()
        self.image_hit=pygame.image.load('images\enemy3_hit.png').convert_alpha()
        self.destory_images=[]
        self.destory_images.extend([
            pygame.image.load(r"images\enemy3_down1.png").convert_alpha(),
            pygame.image.load(r"images\enemy3_down2.png").convert_alpha(),
            pygame.image.load(r"images\enemy3_down3.png").convert_alpha(),
            pygame.image.load(r"images\enemy3_down4.png").convert_alpha(),
            pygame.image.load(r"images\enemy3_down5.png").convert_alpha(),
            pygame.image.load(r"images\enemy3_down6.png").convert_alpha()
        ])
        self.mask=pygame.mask.from_surface(self.image)
        self.active=True
        self.rect=self.image.get_rect()
        self.speed=1
        self.hit=False
        self.energy=bigEnemy.energy
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-12*self.height,-4*self.height)
        #self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-5*self.height,0)

    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    #位置重置
    def reset(self):
        self.energy=bigEnemy.energy
        self.active=True
        self.rect.left,self.rect.top=randint(0,self.width-self.rect.width),randint(-12*self.height,-4*self.height)
