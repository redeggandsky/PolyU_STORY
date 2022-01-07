from model import Model 
# coding=utf-8
class Controller:
    def __init__(self, model : Model) -> None:
        self.model = model
        self.num = dict()
    
    def number_of_words(self):
        self.num.clear()
        mx_num = 0
        for i in self.model.words[1:]:
            if(i[1] not in self.num):
                self.num[i[1]] = 0
            self.num[i[1]] += 1
            mx_num = max(mx_num, i[1])
        for i in range(0, mx_num+1):
            if(self.num[i] > 0):
                print("PTS: "+str(i)+" | WORDS: "+str(self.num[i]))
        pass
    
    def mode1(self, mx_num):
        c = 0
        n = 0
        while(1):
            print("======================================|correct rate: "+str(c)+"/"+str(n))
            k = self.model.words[1]
            if(k[1] > mx_num):
                print("No word's points less than " +str(mx_num))
                break
            n += 1
            print(k[0]+"   "+str(k[1]))
            print("--------------------------------------")
            s = input()
            print(k[2])
            while(1):
                s = input("Y/N?: ")
                if(s.upper() != 'Y' and s.upper() != 'N' and s.upper() != 'Q'):
                    print("Unexcepted input")
                else:
                    break
            if(s.upper() == 'Y'):
                c += 1
                k[1] += 1
            elif(s.upper() == 'Q'):
                break
            elif(s.upper() == 'N'):
                k[1] = 0
                    
            self.model.pop()
            self.model.inst(k)

    def run(self):
        while(1):
            print("'I' to get words list")
            s = input("'D' to get the detail\n'R' to reset the words' points(UNABLE)\n'L' to lower the points of words\n'1' to run Mode 1\n'Q' to quit\nInput: ")
            if(s.upper() == 'D'):
                self.number_of_words()
            elif(s.upper() == 'R'):
                pass
            elif(s.upper() == 'L'):
                pass
            elif(s.upper() == '1'):
                k = eval(input("Input the max point limits: "))
                self.mode1(k)
            elif(s.upper() == 'Q'):
                break
            elif(s.upper() == 'I'):
                k = eval(input("Input the range of words like [a, b] ([0,0] to print all): "))
                #print(self.model.words)
                if(k[0] == k[1] and k[1] == 0):
                    for i in self.model.words:
                        print(i)
                    continue
                for i in range(eval(k[0]), eval(k[1]) + 1):
                    print(self.model.words[i])
            else:
                print("Unexcepted input")
        self.model.writefile()
        pass