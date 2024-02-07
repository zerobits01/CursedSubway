class GlobalTime:

    
    def __init__(self):
        self.hour = 6
        self.minute = 0
        self.day = 1


    def read_time(self):
        return (self.hour, self.minute)


    def get_date_time(self):
        return f"{self.day}-1-1403 {self.hour}:{self.minute}"


    def increase_time(self):
        # 0 6 12 18 24 30 36 42 48 54 60
        # if self.day == 31 and self.hour == 22:
        #     exit()
        self.minute = self.minute + 6
        if self.minute == 60:
            self.hour = self.hour + 1
            self.minute = 0
        if self.hour == 22 and self.minute == 6:
            self.day = self.day + 1
            self.hour = 6
            self.minute = 0
