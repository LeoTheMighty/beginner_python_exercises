class Object:
    def __init__(self, name):
        self.name = name

    def kill(self):
        self.name = "death"


objection = Object("Leo")

print(objection.name)

objection.kill()

print(objection.name)

