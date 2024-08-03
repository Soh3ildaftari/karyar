
import time
class status:
    def __init__(self,name,hp,state='live') -> None:
        self.name=name
        self.hp = hp
        self.state=state
        self.last_action=0
    def dead(self):
        self.state='dead'
    def delay(self):  
        current_time = time.time()  # Get the current time  
        # Check if 2 seconds have passed since the last action  
        if current_time - self.last_action >= 2:  
            self.last_action = current_time  # Update last_action to current time  
            print("Action performed at:", current_time)  
            return True  
        else:  
            print("Action not allowed yet. Time remaining:", 2 - (current_time - self.last_action))  
            return False  
s1=status('sdsd',119)
s1.delay()
input()
s1.delay()
