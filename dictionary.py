class Dictionary:
    def __init__(self, language):
        self._name=language
        self._dict=[]
        self.loadDictionary(language)

    @property
    def dict(self):
        return self._dict

    @dict.setter
    def dict(self, value):
        self._dict=value

    @property
    def dict(self):
        return self._dict

    def loadDictionary(self,path):
       """Metodo di caricamento del file del dizionario"""
       path=path[0].upper()+path[1:]+".txt"
       f=open(path,'r', encoding="utf-8")

       for line in f.readlines():
          line=line.strip("\n")
          self._dict.append(line.lower())

       f.close()


    def printAll(self):
        """Metodo di stampa di tutto il dizionario"""
        print (f"Dizionario in lingua {self._name}")
        for word in self._dict:
            print(word+"\n")

