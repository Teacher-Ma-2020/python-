import pygame
import sys
import traceback
from pygame.locals import *
import my_plane
import enemy
import bullet
import supply
from random import *
import tk1

#初始化
pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
pygame.display.set_caption("飞机_demo")

Black=(0,0,0)
Green=(0,255,0)
Red=(255,0,0)

bg_size=width,height=480,700


#音乐音效设置
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)

bullet_sound = pygame .mixer .Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame . mixer. Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.4)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.3)
get_bomb_sound = pygame .mixer . Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.3)
get_bullet_sound = pygame .mixer .Sound("sound/get_bullet.wav")
get_bullet_sound .set_volume(0.9)
upgrade_sound = pygame . mixer .Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.3)
enemy3_f1y_sound = pygame . mixer . Sound("sound/enemy3_flying.wav")
enemy3_f1y_sound.set_volume(0.4)
enemy1_down_sound = pygame .mixer .Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.4)
enemy2_down_sound = pygame . mixer .Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.7)
enemy3_down_sound = pygame . mixer . Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.8)
me_down_sound = pygame . mixer .Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)
loser_sound=pygame.mixer.Sound("sound/loser.wav")
loser_sound.set_volume(0.1)
winner_sound=pygame.mixer.Sound("sound/winner.wav")
winner_sound.set_volume(0.2)

#添加
def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1=enemy.smallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e1=enemy.midEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_big_enemies(group1,group2,num):
    for i in range(num):
        e1=enemy.bigEnemy(bg_size)
        #e1.speed=10 更改速度
        group1.add(e1)
        group2.add(e1)

def speed_add(group,speed):
    for each in group:
        each.speed+=speed

def main():
    pygame.mixer.music.play(-1)
    clock=pygame.time.Clock()

    screen=pygame.display.set_mode(bg_size)
    bg_image=pygame.image.load(r".\images\background.png").convert()

    me=my_plane.Myplane(bg_size)

    #敌机列表
    enemies=pygame.sprite.Group()
    #生成敌方小飞机
    small_enemies=pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,20)
    #生成敌方中飞机
    mid_enemies=pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,6)
    #生成敌方大飞机
    big_enemies=pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,2)


    #生成普通子弹
    bullet1_group=[]
    bullet1s_index=0
    bullet1_num=5
    for i in range(bullet1_num):
        bullet1_group.append(bullet.Bullet1(me.rect.midtop))

    #生成双倍子弹
    bullet2_group=[]
    bullet2s_index=0
    bullet2_num=10
    for i in range(bullet2_num//2):
        bullet2_group.append(bullet.Bullet2((me.rect.centerx-33,me.rect.centery)))
        bullet2_group.append(bullet.Bullet2((me.rect.centerx+30,me.rect.centery)))

    #爆炸索引
    e1_destory_index=0
    e2_destory_index=0
    e3_destory_index=0
    me_destory_index=0

    #分数
    score=0
    score_font=pygame.font.Font("font/font.ttf",36)
    score_font2=pygame.font.Font('font/SimHei.ttf',30)
    score_font3=pygame.font.Font('font/SimHei.ttf',15)
    score_font4=pygame.font.Font('font/SimHei.ttf',13)
    score_font5=pygame.font.Font('font/SimHei.ttf',22)

    #运行
    running=True
    #暂停
    paused=False
    pause_nor_image=pygame.image.load(r"images/pause_nor.png").convert_alpha()
    pause_pressed_image=pygame.image.load(r"images/pause_pressed.png").convert_alpha()
    resume_nor_image=pygame.image.load(r"images/resume_nor.png").convert_alpha()
    resume_pressed_image=pygame.image.load(r"images/resume_pressed.png").convert_alpha()
    pause_rect=pause_nor_image.get_rect()
    pause_rect.right,pause_rect.top=width-10, 10
    pause_image=pause_nor_image

    #难度
    level=1


    #全局炸弹
    bomb_image=pygame.image.load(r"images/bomb.png").convert_alpha()
    bomb_rect=bomb_image.get_rect()
    bomb_font=pygame.font.Font("font/font.ttf",48)
    bomb_num=3

    #20秒触发一次补给
    bullet_supply=supply.Bullet_Supply(bg_size)
    bomb_supply=supply.Bomb_Supply(bg_size)
    SUPPLY_TIME=USEREVENT
    pygame.time.set_timer(SUPPLY_TIME,20*1000)
    #双倍子弹定时器
    DOUBLE_BULLET_TIME=USEREVENT+1
    #是否使用双倍子弹
    is_double_bullet=False

    #无敌事件
    FLY_TIME=USEREVENT+2
    fly_num=180
    fly_now=180


    #切换图片
    switch_image=True
    #延迟
    delay=100
    #生命值
    life_image=pygame.image.load("images/life.png").convert_alpha()
    life_rect=life_image.get_rect()
    life_num=3
    #防止重复打开文件
    recorded=False

    loser_time=True

    #结束时的画面
    gameover_font=pygame.font.Font("font/font.ttf",48)
    again_image=pygame.image.load("images/again.png").convert_alpha()
    again_image_rect=again_image.get_rect()
    gameover_image=pygame.image.load("images/gameover.png").convert_alpha()
    gameover_image_rect=gameover_image.get_rect()


    #全屏设置+
    fullscreen=False

    print("加载完成！")




    while running:
        #事件
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            #键盘暂停
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1 and pause_rect.collidepoint(event.pos):
                    paused=not paused
                    if paused:
                        pause_image=resume_nor_image
                        pygame.time.set_timer(SUPPLY_TIME,0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pause_image=pause_nor_image
                        pygame.mixer.music.unpause()
                        pygame.time.set_timer(SUPPLY_TIME,20*1000)
                        pygame.mixer.unpause()
            #检测鼠标
            if event.type==MOUSEMOTION:
                if pause_rect.collidepoint(event.pos):
                    if paused:
                        pause_image=resume_pressed_image
                    else:
                        pause_image=pause_pressed_image
                else:
                    if paused:
                        pause_image=resume_nor_image
                    else:
                        pause_image=pause_nor_image


            if event.type==KEYDOWN:
                if event.key==K_F11:
                    fullscreen=not fullscreen
                    if fullscreen:
                        screen=pygame.display.set_mode((0,0),FULLSCREEN|HWSURFACE)
                    else:
                        screen=pygame.display.set_mode(bg_size)
                #回车炸弹
                if event.key==K_RETURN:
                    paused=not paused
                    if paused:
                        pause_image=resume_nor_image
                        pygame.time.set_timer(SUPPLY_TIME,0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pause_image=pause_nor_image
                        pygame.mixer.music.unpause()
                        pygame.time.set_timer(SUPPLY_TIME,20*1000)
                        pygame.mixer.unpause()

                #空格炸弹
                if event.key==K_SPACE:
                    if bomb_num:
                        bomb_num-=1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom>0:
                                each.active=False
            #重新绘制子弹
            if event.type==SUPPLY_TIME:
                supply_sound.play()
                if choice([True,False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            if event.type==DOUBLE_BULLET_TIME:
                is_double_bullet=False
                pygame.time.set_timer(DOUBLE_BULLET_TIME,0)
            if event.type==FLY_TIME:
                me.fly=False
                fly_now=180



        screen.blit(bg_image,(0,0))
        #增加难度
        if level==1 and score>=10000:
            level=2
            upgrade_sound.play()
            add_small_enemies(small_enemies,enemies,5)
            add_mid_enemies(mid_enemies,enemies,2)
        elif level==2 and score>=40000:
            level=3
            upgrade_sound.play()
            add_mid_enemies(mid_enemies,enemies,3)
            add_big_enemies(big_enemies,enemies,1)
            speed_add(small_enemies,1)
        elif level==3 and score>=150000:
            level=4
            upgrade_sound.play()
            add_big_enemies(big_enemies,enemies,2)
            speed_add(mid_enemies,1)
        elif level==4 and score>=300000:
            level=5
            upgrade_sound.play()
            add_big_enemies(big_enemies,enemies,2)
        elif level==5 and score>=500000:
            level=6
            speed_add(big_enemies,1)
        elif level==6 and score>=750000:
            level=7
            add_mid_enemies(mid_enemies,enemies,2)
            add_big_enemies(big_enemies,enemies,1)
        elif level==7 and score>=1000000:
            level=8
            winner_sound.play()







        #是否暂停
        if life_num and not paused:
            #检测操作
            key_pressed=pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveBottom()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()
            #炸弹补给
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image,bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply,me):
                    get_bomb_sound.play()
                    if bomb_num<3:
                        bomb_num+=1
                    bomb_supply.active=False
            #子弹补给
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image,bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply,me):
                    get_bullet_sound.play()
                    is_double_bullet=True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME,18*1000)


                    bullet_supply.active=False



            #子弹帧数以及重置
            if delay%10==0:
                bullet_sound.play()
                if is_double_bullet:
                    bullet2_group[bullet2s_index].reset((me.rect.centerx-33,me.rect.centery))
                    bullet2_group[bullet2s_index+1].reset((me.rect.centerx+30,me.rect.centery))
                    bullet2s_index=(bullet2s_index+2)%bullet2_num
                else:
                    bullet1_group[bullet1s_index].reset(me.rect.midtop)
                    bullet1s_index=(bullet1s_index+1)%bullet1_num
            #子弹碰撞检测
            for i in bullet1_group:
                if i.active:
                    i.move()
                    screen.blit(i.image,i.rect)
                    enemy_hit=pygame.sprite.spritecollide(i,enemies,False,pygame.sprite.collide_mask)
                    if enemy_hit:
                        #子弹
                        i.active=False
                        #敌机
                        for each in enemy_hit:
                            if each in mid_enemies or each in big_enemies:
                                each.hit=True
                                each.energy-=1
                                if each.energy==0:
                                    each.active=False
                            else:
                                each.active=False
            for i in bullet2_group:
                if i.active:
                    i.move()
                    screen.blit(i.image,i.rect)
                    enemy_hit=pygame.sprite.spritecollide(i,enemies,False,pygame.sprite.collide_mask)
                    if enemy_hit:
                        #子弹
                        i.active=False
                        #敌机
                        for each in enemy_hit:
                            if each in mid_enemies or each in big_enemies:
                                each.hit=True
                                each.energy-=1
                                if each.energy==0:
                                    each.active=False
                            else:
                                each.active=False

            #大敌机
            for each in big_enemies:
                #正常
                if each.active:
                    each.move()
                    #击中特效
                    if each.hit:
                        screen.blit(each.image_hit,each.rect)
                        each.hit=False
                    else:
                        if switch_image:
                            screen.blit(each.image,each.rect)
                        else:
                            screen.blit(each.image2,each.rect)
                    #绘制总血条
                    pygame.draw.line(screen,Black,(each.rect.left,each.rect.top-5),(each.rect.right,each.rect.top-5),2)
                    #当前血条与颜色
                    enemy_remain=each.energy/enemy.bigEnemy.energy
                    if enemy_remain>0.2:
                        enemy_color=Green
                    else:
                        enemy_color=Red
                    pygame.draw.line(screen,enemy_color,(each.rect.left,each.rect.top-5),(each.rect.left+(each.rect.width*enemy_remain),each.rect.top-5),2)

                    if each.rect.bottom==-50:
                        enemy3_f1y_sound.play(-1)

                else:
                    #爆炸
                    if delay%6==0:
                        if e3_destory_index==0:
                            enemy3_down_sound.play()

                        screen.blit(each.destory_images[e3_destory_index],each.rect)
                        e3_destory_index=(e3_destory_index+1)%6
                        #初始化
                        if e3_destory_index==0:
                            enemy3_f1y_sound.stop()
                            score+=10000
                            each.reset()


            #中型机
            for each in mid_enemies:
                if each.active:
                    each.move()
                    #击中特效
                    if each.hit:
                        screen.blit(each.image_hit,each.rect)
                        each.hit=False
                    else:
                        screen.blit(each.image,each.rect)
                    #绘制总血条
                    pygame.draw.line(screen,Black,(each.rect.left,each.rect.top-5),(each.rect.right,each.rect.top-5),2)
                    #当前血条与颜色
                    enemy_remain=each.energy/enemy.midEnemy.energy
                    if enemy_remain>0.2:
                        enemy_color=Green
                    else:
                        enemy_color=Red
                    pygame.draw.line(screen,enemy_color,(each.rect.left,each.rect.top-5),(each.rect.left+(each.rect.width*enemy_remain),each.rect.top-5),2)
                else:
                    if delay%6==0:
                        if e2_destory_index==0:
                            enemy2_down_sound.play()
                        screen.blit(each.destory_images[e2_destory_index],each.rect)
                        e2_destory_index=(e2_destory_index+1)%4
                        if e2_destory_index==0:
                            score+=6000
                            each.reset()
            #小型机
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                else:
                    if delay%3==0:
                        if e1_destory_index==0:
                            enemy1_down_sound.play()
                        screen.blit(each.destory_images[e1_destory_index],each.rect)
                        e1_destory_index=(e1_destory_index+1)%4
                        if e1_destory_index==0:
                            score+=1000
                            each.reset()
            #检测我方飞机撞击
            enemies_down=pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)

            if me.fly:
                score_text4=score_font4.render("无敌时间",1,(30,30,30))
                score_text4_rect=score_text4.get_rect()
                score_text4_rect.left,score_text4_rect.top=(me.rect.left+(me.rect.width-score_text4_rect.width)//2),me.rect.bottom+13
                screen.blit(score_text4,score_text4_rect)
                pygame.draw.line(screen,Black,(me.rect.left,me.rect.bottom+2),(me.rect.right,me.rect.bottom+2),2)
                fly_remain=fly_now/fly_num
                pygame.draw.line(screen,(0,255,255),(me.rect.left,me.rect.bottom+2),(me.rect.left+fly_remain*(me.rect.width),me.rect.bottom+2),2)
                fly_now-=1
            else:
                if enemies_down:
                    me.active=False

            for each in enemies_down:
                each.active=False
            #绘制我方飞机
            if me.active:
                if switch_image:
                    screen.blit(me.image,me.rect)
                else:
                    screen.blit(me.image2,me.rect)
            else:
                if delay%3==0:
                    if me_destory_index==0:
                        me_down_sound.play()
                    screen.blit(me.destory_images[me_destory_index],me.rect)
                    me_destory_index=(me_destory_index+1)%4
                    if me_destory_index==0:
                        #碰撞后重置
                        life_num-=1
                        me.reset()
                        pygame.time.set_timer(FLY_TIME,3*1000)

            #绘制技能图标
            bomb_text=bomb_font.render("× %d" %bomb_num,True,(255,255,255))
            text_rect=bomb_text.get_rect()
            screen.blit(bomb_image,(10,height-10-bomb_rect.height))
            screen.blit(bomb_text,(20+bomb_rect.width,height-5-text_rect.height))

            level_text=score_font5.render("第 %d 关" %level ,True,(255,255,255))
            screen.blit(level_text,(width-150,20))

            #绘制生命图标
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image,(width-10-(i+1)*life_rect.width,height-10-life_rect.height))
            #绘制分数
            score_text=score_font.render("Score: %s " % str(score),True,(255,255,255))
            screen.blit(score_text,(10,5))
            #绘制暂停图案
            screen.blit(pause_image,pause_rect)

            #相关帧数
            delay-=1
            if delay==0:
                delay==100
            if delay%5==0:
                switch_image=not switch_image


        elif paused:
            #暂停界面
            score_text2=score_font2.render("暂停中~",1,(64,64,64))
            score_text2_rect=score_text2.get_rect()
            screen.blit(score_text2,(width//2-score_text2_rect.width//2+10,height//2-score_text2_rect.height//2))
            #绘制分数
            score_text=score_font.render("Score: %s " % str(score),True,(255,255,255))
            screen.blit(score_text,(10,5))
            #绘制暂停图案
            screen.blit(pause_image,pause_rect)

            level_text=score_font5.render("第 %d 关" %level ,True,(255,255,255))
            screen.blit(level_text,(width-150,20))
        else:
            #停止音效
            if loser_time:
                pygame.mixer.music.stop()
                pygame.mixer.stop()
                pygame.time.set_timer(SUPPLY_TIME,0)
            if loser_time:
                loser_sound.play()
                loser_time=False
            #读文件
            if not recorded:
                recorded=True
                with open("score/palne_score.txt","r") as f:
                    record_score=int(f.read())
                if score>record_score:
                    with open("score/palne_score.txt","w") as f:
                        f.write(str(score))
                        record_score=score

            #绘制结束画面
            record_score_text=score_font.render("Best : %d" %record_score,True,(255,255,255))
            screen.blit(record_score_text,(50,50))

            gameover_text1=gameover_font.render("Your Score",True,(255,255,255))
            gameover_text1_rect=gameover_text1.get_rect()
            gameover_text1_rect.left,gameover_text1_rect.top=(width-gameover_text1_rect.width)//2,height//3
            screen.blit(gameover_text1,gameover_text1_rect)

            gameover_text2=gameover_font.render(str(score),True,(255,255,255))
            gameover_text2_rect=gameover_text2.get_rect()
            gameover_text2_rect.left,gameover_text2_rect.top=(width-gameover_text2_rect.width)//2,gameover_text1_rect.bottom+10
            screen.blit(gameover_text2,gameover_text2_rect)

            again_image_rect.left, again_image_rect.top=(width-again_image_rect.width)//2,gameover_text2_rect.bottom+50
            screen.blit(again_image,again_image_rect)

            gameover_image_rect.left, gameover_image_rect.top=(width-gameover_image_rect.width)//2,again_image_rect.bottom+10
            screen.blit(gameover_image,gameover_image_rect)

            #重新开始or结束
            if pygame.mouse.get_pressed()[0]:
                #获得鼠标位置
                pos=pygame.mouse.get_pos()
                if again_image_rect.left<pos[0]<again_image_rect.right and again_image_rect.top<pos[1]<again_image_rect.bottom:
                    main()
                elif gameover_image_rect.left<pos[0]<gameover_image_rect.right and gameover_image_rect.top<pos[1]<gameover_image_rect.bottom:
                    pygame.quit()
                    sys.exit()


        #图标印记
        score_text3=score_font3.render("zcj",1,(64,64,64))
        score_text3_rect=score_text3.get_rect()
        score_text3_rect.right,score_text3_rect.bottom=width-5,height-5
        screen.blit(score_text3,score_text3_rect)


        pygame.display.flip()
        clock.tick(60)

if  __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
