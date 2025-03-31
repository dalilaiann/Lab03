import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.italianDict=md.MultiDictionary("italian")
        self.englishDict=md.MultiDictionary("english")
     #  self.spanishDict=md.MultiDictionary("spanish")


    def handleSentence(self, txtIn, language):
        """Metodo di stampa del tempo impiegato per cercare la parola con il metodo contains"""
        words=txtIn.split(" ")
        result=[]
        #Contains
        print("---------------------\nUsing contains")
        startTime=time.perf_counter()

        for i in range(len(words)):
            words[i]=self.replaceChars(words[i])

        if language=="italian":
            results=self.italianDict.searchWord(words, language)

        elif language=="english":
            results = self.englishDict.searchWord(words, language)

        endtime=time.perf_counter()
        self.printResults(results)
        print("Time elapsed "+str(endtime-startTime))
        self.handleSentenceLinear(txtIn,language)
        self.handleSentenceDicotomica(txtIn,language)

    def handleSentenceLinear(self, txtIn, language):
        """Metodo di stampa per ricerca le parole con ricerca lineare"""
        words=txtIn.split(" ")
        result=[]
        #Contains
        print("---------------------\nUsing Linear search")
        startTime=time.perf_counter()

        for i in range(len(words)):
            words[i]=self.replaceChars(words[i])

        if language=="italian":
            results=self.italianDict.searchWordLinear(words, language)

        elif language=="english":
            results = self.englishDict.searchWordLinear(words, language)

        endtime=time.perf_counter()
        self.printResults(results)
        print("Time elapsed "+str(endtime-startTime))

    def handleSentenceDicotomica(self, txtIn, language):
        """Metodo di stampa per ricercare le parole con ricerca dicotomica"""
        words=txtIn.split(" ")
        result=[]
        #Contains
        print("---------------------\nUsing Dicotomic search")
        startTime=time.perf_counter()

        for i in range(len(words)):
            words[i]=self.replaceChars(words[i])

        if language=="italian":
            results=self.italianDict.searchWordDicotomica(words, language)

        elif language=="english":
            results = self.englishDict.searchWordDicotomica(words, language)

        endtime=time.perf_counter()
        self.printResults(results)
        print("Time elapsed "+str(endtime-startTime))


    def printResults(self, results):
        """Metodo di stampa dei risultati errati"""
        for r in results:
            if r.corretta is False:
                print(str(r))


    def printMenu(self):
        """Metodo di stampa del menu"""
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


    def replaceChars(self, text):
        """Metodo di rimozione dei caratteri speciali"""
        chars="\\*_{}[]()>#+-.!$%^;,=_"
        for c in chars:
            text=text.replace(c,"")

        return text
