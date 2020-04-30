# use to separate functionality of one massive class
# to separate platforms, DBs, etc.

from abc import abstractmethod


class Letter:
    def __init__(self, font):
        self.font = font

    @abstractmethod
    def display_letter(self):
        pass


class LetterA(Letter):
    def display_letter(self):
        print(f"A in {self.font.upgrade_letter()}")


class LetterB(Letter):
    def display_letter(self):
        print(f"B in {self.font.upgrade_letter()}")


class Font:

    @abstractmethod
    def upgrade_letter(self):
        pass


class TimesNewRoman(Font):
    def upgrade_letter(self):
        return f"Times New Roman"


class Consolas(Font):
    def upgrade_letter(self):
        return f"Consolas"


times_new_roman = TimesNewRoman()
consolas = Consolas()

lowercase_a = LetterA(times_new_roman)
capital_b = LetterB(consolas)

lowercase_a.display_letter()
capital_b.display_letter()

# Too boring. Let's swap them!
lowercase_a.font = consolas
capital_b.font = times_new_roman

lowercase_a.display_letter()
capital_b.display_letter()
