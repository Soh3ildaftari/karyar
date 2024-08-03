class log:
    pass
class status:
    pass
class game:
    def __init__(self,players,rules) -> None:
        pass






class position:
   def __init__(self,x,y):
        self.__x=x
        self.__y=y
   def x(self):
       return self.__x
   def y(self):
       return self.__y
   def x(self,x):
       if isinstance(x,int) and x<=0:
           self.__x=x
       return self.__x
   def x(self,y):
       if isinstance(y,int) and y<=0:
           self.__y=y
       return self.__y
   def move(self,dir):
        self.dir=dir
        if dir=='up':
            self.position.y(self.position.y+1)
        if dir=='down':
            self.position.y(self.position.y-1)
        if dir=='right':
            self.position.x(self.position.x+1)
        if dir=='left':
            self.position.x(self.position.x-1)
class action:
    pass
class shout(position):
    def __init__(self,x,y,dir,shouter_id) -> None:
        self.x(x)
        self.y(y)
        self.d
class player:
    def __init__(self,name,x,y,hp=100,id=1):
        self.name=name
        self.id=id
        self.position = position
        self.state =status()
        self.hp=hp
        self.dir='up'
    def move(self,dir):
        self.dir=dir
        if dir=='up':
            self.position.y(self.position.y+1)
        if dir=='down':
            self.position.y(self.position.y-1)
        if dir=='right':
            self.position.x(self.position.x+1)
        if dir=='left':
            self.position.x(self.position.x-1)
    def shout(self):
        shout=shout(self.position,self.dir)
    def hitted(self):
        if self.hp<0:
            self.hp-=10
        else:
            self.state.dead()
            self.state.log.death()










class  register:
    pass