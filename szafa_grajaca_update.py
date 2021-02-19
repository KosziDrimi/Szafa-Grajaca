# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class Piosenka(ABC):
    
    @abstractmethod
    def zagraj(self):
        pass


class Piosenka1(Piosenka):
    
    def __init__(self, tytul='remedium'):
        self._tytul = tytul

    def zagraj(self):
        self._text = 'wsiąść do pociągu byle jakiego...'
        print(self._text)


class Piosenka2(Piosenka):
    
    def __init__(self, tytul='we dwoje'):
        self._tytul = tytul

    def zagraj(self):
        self._text = 'lubisz to co znasz i masz zupełnie tak jak ja...'
        print(self._text)
    
    
class Piosenka3(Piosenka):
    def __init__(self, tytul='scenariusz dla moich sąsiadów'):
        self._tytul = tytul

    def zagraj(self):
        self._text = 'wieczorem przed mym domem wystawię ekran i wyświetlę film...'
        print(self._text)


class Piosenka4(Piosenka):
    def __init__ (self, tytul='hej Wy'):
        self._tytul = tytul
            
    def zagraj(self):
        self._text = 'pamiętam jak mówili na mnie z nim będzie trudno bo to zbój...'
        print(self._text)


class SzafaGrajaca:
    
    
    global piosenki
    piosenki = [Piosenka1(), Piosenka2(), Piosenka3()]
    
    
    def znajdz_piosenke(self, tytul):
        
        for piosenka in piosenki:
            if tytul == piosenka._tytul:
                return piosenka
        else:
            return None
            
    
    def zagraj(self, tytul):
        if self.znajdz_piosenke(tytul) != None:
            self.znajdz_piosenke(tytul).zagraj()    
        else:
            print(f"brak piosenki o tytule: '{tytul}'")


    def dodaj(self, Piosenka):
        piosenki.append(Piosenka())
        print('dodano piosenkę')
        
               

if __name__ == "__main__":

    
    szafa = SzafaGrajaca()
    
    szafa.zagraj('we dwoje')
    szafa.zagraj('scenariusz dla moich sąsiadów')
    szafa.zagraj('remedium')
    szafa.zagraj('hej Wy')
    szafa.dodaj(Piosenka4)
    szafa.zagraj('hej Wy')
    
    
    
    
     
        
        
    

