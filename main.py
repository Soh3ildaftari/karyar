import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
from pygame.locals import*
import random
# import numpy as np
import sys
import time
import random as rand

g = 10
ground = 10
p = 0
player_data = []
plat_data = []
enemy_data = ["enemy"]
projectile_data = ["projectile"]
game_speed = 1
c = None
h = 1


pg.init()
pg.display.init()

pg.display.set_caption("my game")



def q():
    pg.quit()
    sys.exit()


white = (255, 255, 255 )
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (255, 248, 220)
cyan = (173, 216, 230)
light_black = (25, 25, 25)
yellow = (255, 255, 224)
oarnge = (255, 165 ,0) 





class player():
    global player_data
    def __init__(self, x, y):
        self.width = 50
        self.height = 100
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.x = int(x)
        self.y = int(y)  
        self.color = blue
        self.pressed = {
            "jump" : False,
            "right" : False,
            "left" : False,
            "shoot" : False
        }
        self.speed = 350
        self.jump = 1000
        self.mass = 350
        self.uy = 0
        self.isground = False
        self.isplat = [False, -1]
        self.lifes = 4
        #state for platform or ground
        self.s = 0
        self.state = "vulnerable"

        
        player_data.append({
            "width" : self.width,
            "height" : self.height,
            "x" : self.x,
            "y" : self.y,
            "speed" : self.speed,
            "jump" : self.jump,
            "uy" : self.uy,
            "lifes" : self.lifes
        })
        




    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)






    def lifecheck(self):
        self.life_x = 12

        
        if collision_type == "collide":
            self.lifes -= 1
            
        

        if self.lifes > 0:
            for i in range(self.lifes):
                self.life_x += 24
                pg.draw.circle(screen, red, (self.life_x, 50), 10)
        else:
            q()







    def update(self, dt, game_speed):
        global plat_data
        global player_data

        self.ux = 0



        if int(self.y) == (height - ground_height - self.height):
            self.isground = True
            self.isplat[1] = -1

        else:

            for item in plat_data:
    
                if (
                    item["y"] + item["thick"] >= (self.y + self.height) and
                    (item["y"] - 1) <= (self.y + self.height)
                    or (
                        int(item["y"]) == int(self.y + self.height)
                    )
                ) and (
                    (int(self.x + self.width) >= int(item["x"])) and
                    (int(self.x) <= int(item["x"] + item["width"]))
                ) and (
                    int(self.uy) <= 0
                ):
                    self.isplat[1] = item["num"]
                    item["isplayer"] = True
                    self.isplat[0] = True
                    self.isground = False
                    self.y = item["y"] - self.height

                    self.uy = 0
                    

                    break
                else:
                    item["isplayer"] = False
                    self.isplat[0] = False
                    self.isground = False


        #print(self.isground, self.isplat)
        if self.pressed["jump"] and (self.isground or self.isplat[0]) :

            self.uy = self.jump

        elif self.pressed["right"] and not self.pressed["left"] :
            self.ux += self.speed


        elif self.pressed["left"] and not self.pressed["right"] :
            self.ux -= self.speed
        



        
        if (self.x >= (width - self.width)) :
            self.x = width - self.width

        elif self.x < 0:
            self.x = 0

        else:
            if self.isplat[0] == True and self.s == 0:
                self.x += (self.ux + item["ux"])*dt*game_speed
                self.s = 1

            else:
                self.x += self.ux*dt*game_speed
        

        
        if self.x < 0:
            self.x = 0
        
        else:
            if self.isplat[0] == True and self.s == 0:
                self.x += (self.ux + item["ux"])*dt*game_speed
            
            else:
                self.x += self.ux*dt*game_speed
        


        if self.y >= (height - ground_height - self.height) :
            self.y = height - ground_height - self.height
            
        else:
            self.y -= self.uy*dt*game_speed

        
        if self.y <= 0:
            pass
        
        else:
            self.y -= self.uy*dt*game_speed
        

        


        if not self.pressed["jump"]:
            if self.y > (height - ground_height - self.height):
                self.y = height - ground_height - self.height
        

        if not (self.isground and self.isplat[0]) :
            self.uy -= self.mass*g*dt*game_speed
            self.pressed["jump"] = False
            self.isplat[1] = - 1


        
            


        
        self.s = 0

        self.rect = pg.Rect(self.x, self.y, 50, 100)



        
        if self.isground :
            pass
            # self.uy = 0

        player_data[0]["uy"] = self.uy
        player_data[0]["ux"] = self.ux
        player_data[0]["x"] = self.x
        player_data[0]["y"] = self.y

        


    

        
class platform():
    def __init__(self, x, y, plat_width, color, curve, num, moving, ux):
        global plat_data
        self.x = x
        self.x_in = x
        self.y = y
        self.width = plat_width
        self.thick = 20
        self.Rect = pg.Rect(self.x, self.y, self.width, self.thick)
        self.in_color = color
        self.color = color
        self.curve = curve
        self.num = num
        self.moving = moving
        self.ux = ux
        
        
        

        
        #gia sygkriseis
        plat_data.append({
            "x" : self.x,
            "y" : self.y,
            "width" : self.width,
            "thick" : self.thick,
            "color" : self.color,
            "isplayer" : False,
            "ux" : 0,
            "num" : self.num
        })
        

    def draw(self):
        pg.event.get(eventtype = color_change, pump = True)
        if plat_data[self.num]["isplayer"] == True:

            self.color = cyan

        else:
            self.color = self.in_color


        pg.draw.rect(screen, self.color, self.Rect, border_radius = self.curve)


    def update(self, dt, game_speed, travel):
        if self.moving == True:
            
            if int(self.x) < self.x_in - (travel):
               self.ux = - self.ux

        
            if int(self.x) >= self.x_in + travel:
                self.ux =  - self.ux
        

            self.x += self.ux*dt*game_speed
            
            
            
        

        

            plat_data[self.num]["x"] = self.x
            plat_data[self.num]["ux"] = self.ux
        
            self.Rect = pg.Rect(self.x, self.y, self.width, self.thick)


        
class enemy():
    global enemy_data
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 25
        self.height = 40
        self.Rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.speed = 175
        self.color = oarnge
        self.num = None

        enemy_data.append({
            "x": self.x,
            "y" : self.y,
            "width" : self.width,
            "height" : self.height,
            "type" : None
        })


        

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.Rect)





    def kill(self):
        enemy_data[self.num].clear()
            

        


class plat_enemy(enemy):

    def __init__(self):
        super(plat_enemy, self).__init__()
        random_plat = rand.randint(0, len(plat_data))
        selected = plat_data[random_plat]
        self.y = selected["y"]
        self.x = random.randint(selected["x"], selected["width"])
                    



class ground_enemy(enemy):

    def __init__(self, num):
        super(ground_enemy, self).__init__()
        self.num = num
        self.y = height - ground_height - self.height
        self.x = random.randint(100, 700)
        self.ux = self.speed
        
       
        enemy_data[self.num + 1]["type"] = "ground"
        enemy_data[self.num + 1]["y"] = self.y



    def update(self, dt, game_speed):
        global enemy_data

        if int(self.x) <= 0:
            self.ux = -self.ux

        if int(self.x) > width - self.width:
            self.ux =  -self.ux


        
        self.x += self.ux*dt*game_speed

        
        enemy_data[self.num + 1]["x"] = self.x
        enemy_data[self.num + 1]["ux"] = self.ux


        self.Rect = pg.Rect(self.x, self.y, self.width, self.height)

        

class air_enemy(enemy):
    def __init__(self):
        super(air_enemy, self).__init__()
        self.y = random.randint(800, 1000)







class collect():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 2
        self.Rect = pg.Rect(self.x, self.y, self.side, self.side)


    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)






class goal(collect):
    def __init__(self):
        super(goal, self).__init__()


    def check_win():
        pass




    

class projectile():
    global projectile_data
    def __init__(self, state):
        self.state = state #hostile or ally
        self.x = None
        self. y = None









class hostile_projectile(projectile):
    global projectile_data
    def __init__(self):
        super(hostile_projectile, self).__init__()
        self.state = "hostile"















class ally_projectile(projectile):
    global projectile_data
    def __init__(self):
        super(ally_projectile, self).__init__()
        self.state = "ally"







def collision(data, h = h):
    global collision_type
    global sprite_type
    collision_type = None
    sprite_type = None

    
    if data[0] == "enemy":
        sprite_type = "enemy"
    elif data[0] == "projectile":
        sprite_type = "projectile"
    
    
    data.pop(0)
    

    for item in data:

        
        if (
            item["y"] + item["height"] >= (player.y + player.height) and
            (item["y"] - 1) <= (player.y + player.height)
        ) and (
            (int(player.x + player.width) >= int(item["x"])) and
            (int(player.x) <= int(item["x"] + item["width"]))
        ) and (
        int(player.uy) < 0
        ) and h == 1 :
            
            collision_type = "stomp"
            h = 0
            #print(collision_type)
       


        
        



        if ((
            item["y"] + item["height"] <= int(player.y) and
            (item["y"]) >= (player.y + player.height)
        ) and (
            (int(player.x + player.width) >= int(item["x"])) and
            (int(player.x) <= int(item["x"] + item["width"]))
        ) and not (
        int(player.uy) <= 0
        )) and ((
            player.x + player.width >= item["x"]
        ) and (
            player.x <= item["x"] + item["width"] 
            )
        ) and (
            player.state == "vulnerable"
        )and (
            h == 1
        ):

            collision_type = "collide"

            player.state = "invulnerable"
            pg.time.set_timer(vulnerability_state, 1000)
            
    
    

    
    data.insert(0, sprite_type)
    
    return collision_type
    return player.state
    
    



fps = 2400
clock = pg.time.Clock()
clock.tick(fps)
start_time = time.time()


width = 1000
height = 800
centre = (425, 500)
screen = pg.display.set_mode((width, height), flags = pg.SHOWN)
screen.fill(black)

ground_height = 100

player = player((width-50)/2, (height - ground_height))

level = 1


color_change = pg.USEREVENT + 1
pg.time.set_timer(color_change, 500)


vulnerability_state = pg.USEREVENT + 2




platform1 = platform(600, 500, 100, red, 5, 0, True, 200)
platform2 = platform(400, 300, 100, green, 20, 1, True, 100)
platform3 = platform(300, 200, 75, brown, 3, 2, False, 0)



ground_enemy1 = ground_enemy(0)




while True:
    clock.tick(fps)
    now = time.time()
    dt = now - start_time
    start_time = time.time()

    screen.fill((12, 24, 36))
    #edafos
    pg.draw.rect(screen, brown, (0, (height - ground_height), width, ground_height))
    

    



    for event in pg.event.get():
        if event.type == QUIT:
            q()
        
        if event.type == KEYDOWN:

            if event.key == K_SPACE or event.key == K_UP:
                player.pressed["jump"] = True
            elif event.key == K_d or event.key == K_RIGHT:
                player.pressed["right"] = True
            elif event.key == K_a or event.key == K_LEFT:
                player.pressed["left"] = True


        if event.type == KEYUP:
            
            if event.key == K_d or event.key == K_RIGHT:
                player.pressed["right"] = False
            elif event.key == K_a or event.key == K_LEFT:
                player.pressed["left"] = False

        

        if event.type == vulnerability_state:

            player.state = "vulnerable"
            pg.time.set_timer(vulnerability_state, 0)



            

    



    if level == 1:
        platform1.update(dt, game_speed, 150)
        platform1.draw()
        platform2.update(dt, game_speed, 50)
        platform2.draw()
        platform3.draw()
    
        ground_enemy1.draw(screen)
        ground_enemy1.update(dt, game_speed)
        
    
    player.update(dt, game_speed)

    
    collision(enemy_data)
    
            
            

    player.lifecheck()


    player.draw(screen)


    
    pg.display.flip()






q()







