import pygame

#己方飞机的创建 属性
class Myplane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(r"images\me1.png").convert_alpha()
        self.image2=pygame.image.load(r"images\me2.png").convert_alpha()
        self.destory_images=[]
        self.destory_images.extend([
            pygame.image.load(r"images\me_destroy_1.png").convert_alpha(),
            pygame.image.load(r"images\me_destroy_2.png").convert_alpha(),
            pygame.image.load(r"images\me_destroy_3.png").convert_alpha(),
            pygame.image.load(r"images\me_destroy_4.png").convert_alpha(),
        ])
        self.active=True
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.rect.bottom=self.height-60
        self.rect.left=(self.width-self.rect.width)//2
        self.speed=8
        self.fly=False
        self.mask=pygame.mask.from_surface(self.image)
    #移动
    def moveUp(self):
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect.top-=self.speed
    def moveBottom(self):
        if self.rect.bottom>=self.height-60:
            self.rect.bottom=self.height-60
        else:
            self.rect.bottom+=self.speed
    def moveLeft(self):
        if self.rect.left<=0:
            self.rect.left=0
        else:
            self.rect.left-=self.speed
    def moveRight(self):
        if self.rect.right>=self.width:
            self.rect.right=self.width
        else:
            self.rect.right+=self.speed
    def reset(self):
        self.rect.bottom=self.height-60
        self.rect.left=(self.width-self.rect.width)//2
        self.active=True
        self.fly=True
