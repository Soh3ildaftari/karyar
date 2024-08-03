from possision import possision
class shout(possision):
    def __init__(self, x, y, max_width, max_hight,direction, ms=5):
        super().__init__(x, y, max_width, max_hight, ms)
        self._direction=direction
    def move(self):
            return super().move(self._direction)
    