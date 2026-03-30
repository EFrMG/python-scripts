class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if val > 100:
            return
        if val < 0:
            self._health = 0
            return

        self._health = val

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, val):
        if val > 50:
            return
        if val < 0:
            self._mana = 0
            return

        self._mana = val

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")

    def __str__(self):
        return f"""\
Name: {self._name}
Level: {self._level}
Health: {self._health}
Mana: {self._mana}
        """
