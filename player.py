from possision import possision
from status import status
from shout import shout
import time
class player(possision,status):
    def __init__(self, x, y, max_width, max_hight,name, ms=1):
        super().__init__(x, y, max_width, max_hight, ms)
        status.__init__(name,hp=100,state='live')
    def hiited(self):
        if self.hp<0:
            self.hp-=10
        else:
            self.dead()
    def shout(self):
         if self.delay(time.time()):
            return shout(self.get_x(),self.get_y(),self.max_width,self.max_hight,self.dir)
         else:
             pass