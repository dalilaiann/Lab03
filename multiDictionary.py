import dictionary as d
import richWord as rw

class MultiDictionary:
    ds={}

    def __init__(self, language):
       self.dict=d.Dictionary(language)
       self.ds[language]=self.dict

    def printDic(self, language):
        self.ds.get(language).printAll()

    def searchWord(self, words, language):
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
        wordsText = []
        dict=self.ds.get(language).dict

        for w in words:
            r = rw.RichWord(w)
            wordsText.append(r)
            for d in dict:
                if d.lower()==w.lower():
                    r.corretta=True
                    break

        return wordsText

    def searchWordDicotomica(self, words, language):
        wordsText = []
        dict=self.ds.get(language).dict

        for w in words:
            w=w.lower()
            r=rw.RichWord(w)
            wordsText.append(r)
            if dict[int(len(dict)/2)] == w:
                r.corretta=True
                break
            else:
                if w<dict[int(len(dict)/2)]:
                    for i in range(0, int(len(dict)/2)):
                        if dict[i] == w:
                            r.corretta=True
                            break
                else:
                    for i in range(int(len(dict)/2), len(dict)):
                        if dict[i] == w:
                            r.corretta=True
                            break

        return wordsText






