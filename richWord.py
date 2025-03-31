class RichWord:
    def __init__(self, parola):
        self._parola = parola.lower() # this is a string
        self._corretta = False #this is a bool

    @property
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        # print("setter of parola called" )
        self._corretta = boolValue

    @property
    def parola(self):
        return self._parola

    @parola.setter
    def parola(self, parola):
        self._parola = parola

    def __str__(self):
        return self._parola

    def __eq__(self,word):
        if self._parola==word:
            return True
        else:
            return False