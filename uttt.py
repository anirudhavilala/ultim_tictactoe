'''
Implementation of Ultimate Tic Tac Toe 
using Mini-Max with alpha-beta pruning and an evaluation function
'''

import numpy as np # Used in the program to perform simple array functions
import random # Used in the program to generate random number
import math # Used in the program to use -inf and +inf
from copy import deepcopy as dp # Used in the program to deepcopy lists
import sys # Used in the program to print to stderr
import time # Used in the program to calculate time taken by minimax algorithm

class Ulttt:
    def playerinput(self):#To take in the player input
        print("Select X or O: ",file = sys.stderr)
        pl1 = input()
        pll1 = pl1.upper()
        return pll1
    
    def currentmove(self,winch,p1,p2,cp):# To perform the current move
        wincheck = dp(winch)
        prev11[p1][p2]=cp
        if cp == 'X':
            wincheck[p1][p2]=p11
        else:
            wincheck[p1][p2]=p22
        return wincheck
    
    def display(self,prevp):# To modify the lists so it is easier to display the board
        prev = dp(np.array(prevp))
        prevm = []
        for i in prev:    
            prevm.append(['-' if x==None else x for x in i])
        for i in range(3):
            for j in range(3):
                print(*prevm[3*i][j*3:j*3+3],'|',*prevm[3*i+1][j*3:j*3+3],'|',*prevm[3*i+2][j*3:j*3+3],sep=' ',file = sys.stderr)
            if i != 2:print("_______________________\n",file = sys.stderr)
        return(prevm)

    def validity(self,p1,p2,moveslt):# To check the validity of the move
        valtest = dp(moveslt)
        if valtest[p1][p2] is None:
            print("Valid",file = sys.stderr)
            return 1
        else:
            print("Invalid Move",file = sys.stderr)
            return 0
    
    def currentplayer(self,move):# To know the current player
        if move%2 == 0:
            return 'X'
        else:
            return 'O'
    
    def winfull(self,wwww): # To check if board is full
        w7 = dp(wwww)
        a2 = 1
        for i in range(9):
            for j in range(9):
                if w7[i][j] is None:
                    a2=0
        return a2
    
    def winner2(self,wincheck2):# Checks for the winner of a mini-board
        sump2 = [0]*2
        win2=dp(wincheck2)
        for k in range(len(win2)):
            if win2[k] is None:
                win2[k] = 100
        win=np.reshape(win2,(3,3))
        for i in range(3):
            if (sum(win[:,i])== 3 or sum(win[i,:])== 3 or sum(win.diagonal())== 3  or sum(np.fliplr(win).diagonal())== 3):
                sump2[1] = 50
            if (sum(win[:,i])== 0 or sum(win[i,:])== 0 or sum(win.diagonal())== 0 or sum(np.fliplr(win).diagonal())==0):
                sump2[0] = -50
        return(sump2)
    
    def winner(self,wincheck1):# Checks for the winner
        sump = 0
        sump3 = [0]*2
        sump4 = [0]*2
        sump5 = [0]*2
        l1 = [None]*9
        l2 = [None]*9
        win3=dp(wincheck1)
        for j in range(9):
            win22 = win3[j]
            sump3 = self.winner2(win22)
            if sump3[1] is 50:
                    l1[j] = 1
            if sump3[0] == -50:
                    l2[j] = 0
        sump4 = self.winner2(l1)
        sump5 = self.winner2(l2)
        if sump4[1] is 50:
            sump = 1000
            return(sump)
        elif sump5[0] == -50:
            sump = -1000
            return(sump)
        else:
            sump = 0
        return(sump)
    
    def minimaxalbe(self,win2,p22):#Minimax algorithm
        alpha=-math.inf
        beta = math.inf
        play=-1
        w2 = dp(win2)
        p2=self.boardcheck(w2,p22)
        m= self.mlist1(w2)
        bmove = [None]*2
        bscore = math.inf
        for i in range(9):
            if m[p2][i] is not 1:
                continue
            w = self.mmmove(w2,play,p2,i)
            lscore = self.mmplay(w,-play,i,alpha,beta,d=0)
            if lscore < bscore:
                bscore = lscore
                bmove[0] = p2
                bmove[1] = i
        return bmove
    
    def mmplay(self,wc,pl,pos1,alpha,beta,d):# Function containing the min and max logic to be called by the minimax function
        a1=0
        w3= dp(wc)
        if self.winfull(w3):
                a1=1 
        if self.winner(w3) is not 0 or a1 is 1:
            return (self.winner(w3))
        if d == 4:
            return(self.hscore(w3))
        mov = self.mlist1(w3)
        if pl == -1:
            be = math.inf
            for i in range(9):
                if mov[pos1][i] is 1:
                    ww1 = self.mmmove(w3,pl,pos1,i)
                    www1 = dp(ww1)
                    be = min(be, self.mmplay(www1,-pl,i,alpha,beta,d+1))
                    if be <= alpha:
                        return be
                    beta = min(beta,be)
            return be
        if pl == 1:
            al = -math.inf
            for i in range(9):
                if mov[pos1][i] is 1:
                    ww2 = self.mmmove(w3,pl,pos1,i)
                    www2 = dp(ww2)
                    al = max(al, self.mmplay(www2,-pl,i,alpha,beta,d+1))
                    if al >= beta:
                        return al
                    alpha = max(alpha,al)
            return al
    
    def hscore(self,www):# Heuristic to calculate the score
        w6 = dp(www)
        sumps = [0]*2
        score=0
        for i in range(9):
            sumps = self.winner2(w6[i])
            if w6[i][4] is 1:
                score = score + 5
            elif w6[i][4] is 0:
                score = score - 5
            wp22  =dp(w6[i])
            wp1=np.reshape(wp22,(3,3))
            if (list(wp1.diagonal()).count(1)>=2 or list(np.fliplr(wp1).diagonal()).count(1)>=2):
                score = score+10
            if (list(wp1.diagonal()).count(0)>=2 or list(np.fliplr(wp1).diagonal()).count(0)>=2):
                score = score-10
            for j in range(3):
                if (list(wp1[:,j]).count(1)>= 2 or list(wp1[j,:]).count(1)>= 2):
                    score = score+10
                if (list(wp1[:,j]).count(0)>= 2 or list(wp1[j,:]).count(0)>= 2):
                    score = score-10
            score = score + sumps[1] + sumps[0]
        return score  
                        
    def boardcheck(self,wwww,pos):# To check if the mini-board is full and if the mini-board is full then returns a random empty board no.
        w8 = dp(wwww)
        a=0
        for i in range(9):
            if w8[pos][i] is None:
                a=1
                return(pos)
        if a is not 1:
            self.boardcheck(w8,random.randint(0,8))
            
            
    def mmmove(self,w2,pl,i,j):# To perform the move in mmplay
        w4 = dp(w2)
        if pl == -1:
            w4[i][j]=0
        else:
            w4[i][j]=1
        return w4
    
    def mlist1(self,ww):#To find and return the empty spaces
        w5 = dp(ww)
        remmoves = [[None]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if w5[i][j] is None:
                    remmoves[i][j] = 1
                else:
                    remmoves[i][j] = None
        return remmoves

if __name__ == '__main__':
    ttt = Ulttt()
    move=-1
    while(1):
            if move == -1:
                prev11 = [[None]*9 for _ in range(9)]
                prev1 = [[None]*9 for _ in range(9)]
                moveslist = [[None]*9 for _ in range(2)]
                possible_move=[1,2,3,4,5,6,7,8,9]
                cp='X'
                p11= 1
                p22= 0
                wincheck = [[None]*9 for _ in range(9)]
                move=-1
                pos = [None]*2
                print("Ultimate 9-Board TIC-TAC-TOE \n RULES:\nThe Player should choose a board number and place on that Board.\nThe Board should be same as the place on board in the previous play(i.e., opponents place on board), if the board is full the player can choose a random board. The player to win three boards in a row is said to be the winner.\nEnjoy!!!!!\nDisclaimer: Player who choses X is assumed to play first",file = sys.stderr)
                print("The board in the game is:",file = sys.stderr)
                ttt.display(prev1)
                inpplayer = ttt.playerinput()# To take the player input
                if inpplayer in ('X','O','x','O'):
                    move = 0
                    if inpplayer in ('O','o'):
                        p11 = 0
                        p22 = 1
                        pos[1] = random.randint(0,8)
                else:
                    print ("Invalid Entry",file = sys.stderr)
                    continue
            w8 = dp(wincheck)
            if cp == inpplayer :
                print("\nEnter your Move - Board Number ",file = sys.stderr)
                pos[0]= int(input())
                if not move==0:
                    if ttt.boardcheck(w8,pos[1]) == pos[1]:
                        x=pos[1]
                        if not (pos[0]-1) == pos[1]:
                            print ("Invalid Board Entry",file = sys.stderr)
                            continue
                print("Enter your Move - Place on Board  ",file = sys.stderr)
                pos[1]= int(input())
                if pos[0] not in possible_move or pos[1] not in possible_move:
                    print('Invalid Move',file = sys.stderr)
                    continue 
                pos[0]=pos[0]-1
                pos[1]=pos[1]-1
            else :
                st = time.perf_counter()
                pos=ttt.minimaxalbe(w8,pos[1])
                print("Time taken = ",(time.perf_counter()-st),"s",file = sys.stderr)
            if not ttt.validity(pos[0],pos[1],wincheck):
                pos[1] = x
                continue
            '''
            If you want to play another program with this program, include the below if statement
            if cp != inpplayer :
                print(pos[0]+1)
                print(pos[1]+1)
            '''
            move=move+1
            wincheck = ttt.currentmove(wincheck,pos[0],pos[1],cp)
            cp = ttt.currentplayer(move)
            ttt.display(prev11)
            if ttt.winner(wincheck) == 1000:
                    print("Game Over",file = sys.stderr)
                    print("Player is the winner",file = sys.stderr)
                    move = -1
                    continue
            elif ttt.winner(wincheck) == -1000:
                    print("Game Over",file = sys.stderr)
                    print("Computer is the winner",file = sys.stderr)
                    move = -1
                    continue
            elif ttt.winfull(wincheck):
                    print("Game Over",file = sys.stderr)
                    print("Draw",file = sys.stderr)
                    move = -1
                    continue
    
