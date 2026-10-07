class song:
    a = 45
    def __init__(self,name,age,platform):
        self.name = name
        self.age = age
        self.platform = platform

    def aish(self):
        print(f"Ride It {self.age}")

    @classmethod
    def riya(cls):
        print(f"Hello Riya {cls.a}")

    @staticmethod
    def jogi():
        print("jogi ji ")

songs = song("Aish",28,"Youtube")

print(songs.name)
songs.aish()
songs.riya()
songs.jogi()
