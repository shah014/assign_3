class Mario:

    def __init__(self, name, height, width, color):
        self.name = name
        self.height = height
        self.width = width
        self.color = color

    def display(self):
        return f'{self.name} has {self.height} height and {self.width} width wearing {self.color} cap'


a = Mario('Mario', 20, 15, 'red')
print(a.display())

