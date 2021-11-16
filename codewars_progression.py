class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, level):
        
        #throw errors for invalid levels
        if level > 8 or level < -8 or level == 0:
            raise(ValueError("Invalid Level"))
        
        if level > 0 and self.rank < 0:
            level -= 1
            
        if self.rank > 0 and level < 0:
            level += 1
        
        if self.rank < level:
            progPoints = 10 * (self.rank - level) ** 2

        if self.rank > level:
            difference = abs(level - self.rank)
            if difference >= 2:
                progPoints = 0
            if difference == 1:
                progPoints = 1

        if self.rank == level:
            progPoints = 3

        while progPoints > 0:
            if self.rank == 8:
                self.progress = 0
                progPoints = 0
            else:
                progPoints -= 1
                self.progress += 1
                if self.progress == 100 and self.rank < 8:
                    self.rank += 1
                    self.progress = 0
                    if self.rank == 0:
                        self.rank = 1
