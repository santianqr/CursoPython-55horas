class Pawns:
    
    def __init__(self):
        self.letters = []
    
    def addPawn(self, c):
        self.letters.append(c.upper())
    
    def addPawns(self, c, n):
        for _ in range(n):
            self.addPawn(c)
    
    def createBag(self):
        with open("/content/drive/MyDrive/Colab Notebooks/datasets/bag_of_pawns.csv") as f:
            count = 0
            for line in f:
                if count >= 1:
                    fi_tot = line.split(sep = ',')
                    self.addPawns(fi_tot[0], int(fi_tot[1]))
                count += 1

    def showPawns(self):
        f_pawns = self.getFrequency()
        f_pawns.showFrequency()

    def takeRandomPawn(self):
        from numpy import random
        return self.letters.pop(random.randint(0, len(self.letters) -1 ))
    
    def getFrequency(self):
        f = FrequencyTable()
        for c in self.letters:
            f.update(c)
        return f
    
    def takePawn(self, c):
        self.letters.remove(c)
    
    def getTotalPawns(self):
        return len(self.letters)

class Word:

    def __init__(self, word = []):
        self.word = word

    def __str__(self):
        return "".join(self.word)
    
    def areEqual(self, w):
        return self.word == w.word
    
    def isEmpty(self):
        return len(self.word) == 0
    
    @classmethod
    def readWord(cls):
        in_word = list(input().upper())
        return cls(in_word)
    
    @staticmethod
    def readWordFromFile(f):
        file_word = list(f.readline()[:-1])
        w = Word(file_word)
        return w

    def getFrequency(self):
        f = FrequencyTable()
        for c in self.word:
            f.update(c)
        return f

class Dictionary:

    filepath = "/content/drive/MyDrive/Colab Notebooks/datasets/dictionary.txt"

    @staticmethod
    def validateWord(word):
        with open(Dictionary.filepath, 'r') as f:
            w = Word.readWordFromFile(f)
            while not word.areEqual(w) and not w.isEmpty():
                w = Word.readWordFromFile(f)
            if word.areEqual(w) and not w.isEmpty():
                return True
            else:
                return False
                
class FrequencyTable:

    def __init__(self):
        letters = []
        frequencies = []
        import csv
        with open("/content/drive/MyDrive/Colab Notebooks/datasets/bag_of_pawns.csv", "r") as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if count >= 1:
                    letters.append(row[0])
                count += 1
        self.letters = letters
        frequencies = [0] * len(letters)
        self.frequencies = frequencies
    
    def showFrequency(self):
        for i in range(len(self.frequencies)):
            if self.frequencies[i] != 0:
                print("{}: {}".format(self.letters[i], self.frequencies[i]))

    @staticmethod
    def isSubset(f1, f2):
        for i in range(len(f1.frequencies)):
            if f1.frequencies[i] > f2.frequencies[i]:
                return False
        return True
    
    def update(self, c):
        idx = self.letters.index(c)
        self.frequencies[idx] += 1

class Board:
    
    def __init__(self):
        board = [[" " for j in range(15)] for i in range(15)]
        self.board = board
        self.totalWords = 0
        self.totalPawns = 0
    
    def showBoard(self):
        count_row = 0
        
        for i in range(len(self.board) * 2 + 2):
            
            if i == 0:
                for j in range(len(self.board)):
                    print("  {}".format('0'+str(j) if j < 10 else str(j)), end = '')
                print()
            
            elif i % 2 == 0 :
                for j in range(len(self.board)):
                    if j == len(self.board) -1:
                        print("| {} | {}".format(self.board[count_row][j], 
                                                 '0'+str(count_row) if count_row < 10 else str(count_row) ),
                                                  end = "")
                    else:
                        print("| {} ".format(self.board[count_row][j]), end = "")
                count_row += 1
                print()
            
            else:
                print("+---"*15)
    
    def placeWord(self, player_pawns, word, x, y, dir): # player_pawns -> obj Pawns, word -> obj Word

        for l in word.word:
            if l != self.board[x][y]:
                player_pawns.takePawn(l)
                self.totalPawns += 1
                self.board[x][y] = l

            if dir == 'V':
                x += 1
            if dir == 'H':
                y += 1
        self.totalWords += 1