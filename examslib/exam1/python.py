class Python:
    def __init__(self,note):
        self.note=note
    def validate(self):
        return self.note >= 10
    
    def printInfos(self):
        print(f"Note: {self.note}")
    