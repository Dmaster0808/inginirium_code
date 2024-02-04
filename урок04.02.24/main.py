class car:
    def __init__(self, color, mark, max_speed, weight ):
        self.color = color
        self.mark = mark
        self.max_speed = max_speed
        self.weight = weight

    def sound(self):
        print('beep')

    def long_sound(self):
        print('Beep beep')

Gasel = car ('со вкусом чернаголовка, наверно дальбойная, самая топавая хз, ', "хз")

Gasel.sound()
Gasel.long_sound()



