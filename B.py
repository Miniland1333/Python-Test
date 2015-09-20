class Gamepad:
    def __init__(self):
        self.name="name"

    def getName(self):
        self.update()
        return self.name

    def update(self):
        print("Updating")
        self.name="Hello World!"
