import os

class Toe:
    def __init__(self) -> None:
        self.board={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        self.counter=0
        self.victory=0
        self.it=0
        self.vict={}
        self.vin=[['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]
        self.score_dict={}
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        
        
    def select(self):
        turn=input("Enter The Player X or O : ")
        if turn not in ("X","O","x","o"):
            print("!!!Invalid input!!!!")
            print("Try Again")
            return self.select()
        else:
            
            return turn.upper()


    def show(self,board):
        if self.re==0:
            self.clear_screen()
        print()
        print("  {} | {} | {} ".format(board["1"],board["2"],board["3"]))
        print("-------------")
        print("  {} | {} | {} ".format(board["4"],board["5"],board["6"]))
        print("-------------")
        print("  {} | {} | {} ".format(board["7"],board["8"],board["9"]))
        print()


    def switch(self,turn):
        if turn=="X":
            return "O"
        else:
            return "X"


    def swap(self,pos,turn):
        if pos.isdigit() and int(pos)>0 and int(pos)<10:
            if isinstance(self.board[pos], int):
                self.board[pos]=turn
            else:
                print("!!!!! illegal move !!!!! ")
                print("TRY AGAIN")
                self.go(turn)
        else:
            print("Enter a valid num")
            print("TRY AGAIN")
            self.go(turn)


    def go(self,turn):
        if self.counter > 0:
            print(f"Player {turn}")
        pos=input("Enter the Position : ")
        if turn == "X":
            self.swap(pos,"X")
        elif turn=="O":
            self.swap(pos,"O")



    def check(self,turn):
        
        for sublist in self.vin:
            if self.board[sublist[0]]==self.board[sublist[1]]==self.board[sublist[2]]:
                self.victory=1
                print("!! Player {} Won !!".format(turn))
                self.board[sublist[0]]="*"
                self.board[sublist[1]]="*"
                self.board[sublist[2]]="*"
                self.show(self.board)
                print("!! Player {} Won !!".format(turn))
            elif self.counter>9:
                print("!!!!! DRAW !!!!!")


    def loop(self,turn):
        self.counter+=1
        if self.victory==0 and self.counter<10:     
            self.go(turn)
            self.show(self.board)
        
            if self.counter>2 :
                self.check(turn)
            turn=self.switch(turn)
            self.loop(turn)
            

    def save_score(self,turn):
        self.it+=1
        if self.counter<9:
            self.score_dict[f"Game : {self.it}"]=[self.board,f"Victor : {turn}",turn]
        else:
            self.score_dict[f"Game : {self.it}"]=[self.board,"Draw"]
        self.board={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

    def scores(self):
        temp_x=0
        temp_o=0

        print("\n\n!!!!!|SCORE BOARD|!!!!!")
        for i in self.score_dict:
            print("\n"+i+"\n")
            print((self.score_dict[i])[1])
            if self.score_dict[i][2]=="X":
                temp_x=temp_x+1
            elif self.score_dict[i][2]=="O":
                temp_o=temp_o+1
            self.show((self.score_dict[i])[0])
        print(f"X won {temp_x} times")
        print(f"O won {temp_o} times")
    
    def replay(self):
        self.re=input("Do you wanna play again(Y) or show Score(N) : ")
        if self.re in ("Y" ,"y"):
            self.counter=0
            self.victory=0
            self.tictac()
        elif self.re in ("N","n"):
            self.clear_screen()
            self.scores()
        else:
            print("!!!!!Invalid input!!!!!")
            self.replay()
            

    def tictac(self):
        self.re=0
        turn=self.select()
        self.show(self.board)
        self.loop(turn)
        self.save_score(turn)
        self.replay()
        
def main() -> None:
    abc=Toe()
    abc.tictac()

if __name__=="__main__":
    main()