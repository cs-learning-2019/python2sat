import datetime

class Clock:
    def __init__(self):
        current_time = datetime.datetime.now()
        self.Hour = current_time.strftime("%I")
        self.Min = current_time.strftime("%M")
        self.Sec = current_time.strftime("%S")
        self.AM_PM = current_time.strftime("%p")
        self.Month = current_time.strftime("%B")
        self.Day = current_time.strftime("%d")
        self.Year = current_time.strftime("%Y")
    
    def is_afternoon(self):
        if self.AM_PM == "AM":
            return False
        else:
            return True
        
    def update_time(self):
        current_time = datetime.datetime.now()
        self.Hour = current_time.strftime("%I")
        self.Min = current_time.strftime("%M")
        self.Sec = current_time.strftime("%S")
        self.AM_PM = current_time.strftime("%p")
        self.Month = current_time.strftime("%B")
        self.Day = current_time.strftime("%d")
        self.Year = current_time.strftime("%Y")
        
        
