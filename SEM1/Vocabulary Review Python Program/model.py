# coding=utf-8

class Model:
    def __init__(self) -> None:
        self.date = 0
        self.words = [['words',0,'单词']]
        self.n = 0
        self.info = []
        pass
    def create_new_file(self):
        FL = open("words.txt","x")
        FL.close()
    
    def readfile(self):
        print("Read file.")
        try:
            FL = open("words.txt", "r", encoding = "UTF-8")
        except FileNotFoundError:
            self.create_new_file()
            FL = open("words.txt", "r", encoding = "UTF-8")
        finally:
            for i in FL.readlines():
                self.info.append(i.strip('\n'))
            FL.close()
    
    def writefile(self):
        FL = open("words.txt", "w", encoding= "UTF-8")
        for i in self.words[1:]:
            FL.write(i[0]+'#'+i[2]+'#'+str(i[1])+'\n')
        FL.close()
        FL = open("EN_words.txt","x")
        FL.close()
        FL = open("EN_words.txt","w", encoding= "UTF-8")
        for i in self.words[1:]:
            FL.write(i[0]+'\n')
        FL.close()

    def inst(self, x: list):
        #print('inst ', x)
        self.n += 1
        self.words.append(x)
        p = self.n
        while(p > 1 and self.words[p][1] < self.words[p//2][1]):
            #print(str(p) + " - ", self.words[p], " : ", self.words[p//2])
            self.words[p//2], self.words[p] = self.words[p], self.words[p//2]
            p //= 2

    def pop(self):
        #print('pop: ',self.words[1])
        self.words[1], self.words[self.n] = self.words[self.n], self.words[1]
        self.words.pop()
        self.n -= 1
        p = 1
        while(1):
            #print("!" + str(p)+ "  "+str(self.n))
            
            if(p * 2 > self.n):
                break
            elif(p * 2 + 1 > self.n):
                #print(self.words[p],self.words[p*2])
                if(self.words[p * 2][1] <= self.words[p][1]):
                    self.words[p * 2], self.words[p] = self.words[p], self.words[p * 2]
                    p = p * 2
                else:
                    break
            else:
                #print(self.words[p],self.words[p*2],self.words[p*2+1])
                if(self.words[p * 2 + 1][1] <= self.words[p * 2][1] and self.words[p * 2 + 1][1] <= self.words[p][1]):
                    self.words[p * 2 + 1], self.words[p] = self.words[p], self.words[p * 2 + 1]
                    p = p * 2 + 1
                elif (self.words[p * 2][1] <= self.words[p * 2 + 1][1] and self.words[p * 2][1] <= self.words[p][1]):
                    self.words[p * 2], self.words[p] = self.words[p], self.words[p * 2]
                    p = p * 2
                else:
                    break


    def init(self):
        self.readfile()
        for i in self.info:
            #print(i)
            k = [j for j in i.split('#')]
            #print(i)
            #print(k)
            self.inst([k[0], eval(k[2]), k[1]])

