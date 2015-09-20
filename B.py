class Gamepad:
    def __init__(self):
        self.name="name"

    def getName(self):
        __update()
        return self.name

    def __update(self):
        print("Updating")
        self.name="Hello World!"
