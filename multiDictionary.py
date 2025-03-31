import dictionary as d
import richWord as rw

class MultiDictionary:
    ds={}

    def __init__(self, language):
       self.dict=d.Dictionary(language)
       self.ds[language]=self.dict

    def printDic(self, language):
        """Metodo per stampare tutto il dizionario"""
        if (language=="english" or language=="italian"):
            self.ds.get(language).printAll()
        else:
            print("Linguaggio non supportato")

    def searchWord(self, words, language):
        """Metodo per verificare se una parola è presente nel dizionario"""
        wordsText=[]

        for w in words:
            r=rw.RichWord(w)
            wordsText.append(r)

        for r in wordsText:
            if r.parola.lower() in self.ds.get(language).dict:
               r.corretta=True
            else:
               r.corretta=False

        return wordsText

    def searchWordLinear(self, words, language):
        """Metodo per verificare se una parola è presente nel dizionario tramite ricerca lineare"""
        wordsText = []
        dict=self.ds.get(language).dict

        for w in words:
            r = rw.RichWord(w)
            wordsText.append(r)
            for d in dict:
                if r==d.lower():
                    r.corretta=True
                    break

        return wordsText

    def searchWordDicotomica(self, words, language):
        """Metodo per verificare se una parola è presente nel dizionario tramite ricerca dicotomica"""
        wordsText = []
        dict=self.ds.get(language).dict

        for w in words:
            w=w.lower()
            r=rw.RichWord(w)
            r.corretta=self.searchDicotomica(w, dict)
            wordsText.append(r)

        return wordsText


    def searchDicotomica(self, word, language):
        """Ricerca dicotomica per la singola parola"""
        start_index = 0
        end_index = len(language)

        while (start_index != end_index):
                media=start_index +int((end_index-start_index)/2)
                parola=language[media]
                if parola==word:
                    return True
                elif word>parola:
                    start_index=media+1
                else:
                    end_index=media


        return False







