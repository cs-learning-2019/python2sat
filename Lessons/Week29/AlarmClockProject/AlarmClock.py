import datetime

class AlarmClock:
    def __init__(self):
        current_time = datetime.datetime.now()
        self.Hour = current_time.strftime("%I")
        self.Min = current_time.strftime("%M")
        self.Sec = current_time.strftime("%S")
        self.AM_PM = current_time.strftime("%p")
        self.Month = current_time.strftime("%B")
        self.MonthNumber = int(current_time.strftime("%m"))
        self.PossibleMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.Day = current_time.strftime("%d")
        self.Year = current_time.strftime("%Y")
        self.isSet = False
        self.startTime = None
        
    def update_time(self):
        current_time = datetime.datetime.now()
        self.Hour = current_time.strftime("%I")
        self.Min = current_time.strftime("%M")
        self.Sec = current_time.strftime("%S")
        self.AM_PM = current_time.strftime("%p")
        self.Month = current_time.strftime("%B")
        self.MonthNumber = int(current_time.strftime("%m"))
        self.Day = current_time.strftime("%d")
        self.Year = current_time.strftime("%Y")
    
    def isAlarmClockSet(self):
        return self.isSet
    
    def startAlarm(self):
        self.isSet = True
        self.startTime = datetime.datetime.now()
    
    def stopAlarm(self):
        self.isSet = False
        self.startTime = None
    
    def timeTargetReached(self):
        current_time = datetime.datetime.now()
        targetTime = datetime.datetime.strptime(self.Hour + "/" + self.Min + "/" + self.Sec + "/" + self.AM_PM + "/" + self.Month + "/" + self.Day + "/" + self.Year, "%I/%M/%S/%p/%B/%d/%Y")
        delta = targetTime - current_time
        
        if abs(delta.total_seconds()) < 0.5:
            return [True, 1.0]
        else:
            delta2 = targetTime - self.startTime
            delta3 = current_time - self.startTime
            return [False, delta3.total_seconds() / delta2.total_seconds()]
    
    def increaseHour(self):
        self.Hour = str((int(self.Hour) + 1) % 13)
        if self.Hour == "0":
            self.Hour = "01"
        elif len(self.Hour) == 1:
            self.Hour = "0" + self.Hour
    
    def increaseMin(self):
        self.Min = str((int(self.Min) + 1) % 60)
        if self.Min == "0":
            self.Min = "00"
        elif len(self.Min) == 1:
            self.Min = "0" + self.Min
    
    def increaseSec(self):
        self.Sec = str((int(self.Sec) + 1) % 60)
        if self.Sec == "0":
            self.Sec = "00"
        elif len(self.Sec) == 1:
            self.Sec = "0" + self.Sec
    
    def toggle_AM_PM(self):
        if self.AM_PM == "AM":
            self.AM_PM = "PM"
        else:
            self.AM_PM = "AM"

    def increaseMonth(self):
        self.MonthNumber = (self.MonthNumber + 1) % 13
        if self.MonthNumber == 0:
            self.MonthNumber = 1
            
        self.Month = self.PossibleMonths[self.MonthNumber - 1]
        
    def increaseDay(self):
        self.Day = str((int(self.Day) + 1) % 32)
        if self.Day == "0":
            self.Day = "01"
        elif len(self.Day) == 1:
            self.Day = "0" + self.Day
        
    def increaseYear(self):
        self.Year = str(int(self.Year) + 1)
        if int(self.Year) > 2100:
            self.Year = "2021"
    
