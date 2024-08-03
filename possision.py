class possision:
   def __init__(self,x,y,max_width,max_hight,ms=1):
        self.__x=x
        self.__y=y
        self.max_width=max_width
        self.max_hight=max_hight
        self._ms=ms
        self.dir=None
   def get_x(self):
       return self.__x
   def get_y(self):
       return self.__y
   def set_x(self,x):
       if isinstance(x,int) and x>=0 and x<=self.max_width-50:
           self.__x=x
           return True
       else: return False
   def set_y(self,y):
       if isinstance(y,int) and y>=0 and y<=self.max_hight-50:
           self.__y=y
           return True
       else:
           return False 
   def move(self,dir):
        self.dir=dir
        if dir=='down':
            return self.set_y(self.get_y()+self._ms)
        elif dir=='up':
            return self.set_y(self.get_y()-self._ms)
        elif dir=='right':
            return self.set_x(self.get_x()+self._ms)
        elif dir=='left':
            return self.set_x(self.get_x()-self._ms)
        
       