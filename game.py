import random
from sys import exit

class death(object):
    over=["\nGame Over! Play the game again\n","\nGame Over!You are very bad solving puzzles\n","\nGame Over!This game is not made for fools like you\n"]

    def __init__(self,health):
        self.health=health

    def gameov(self):
        print(random.choice(self.over))
        input("Press Enter to continue.")
        exit(1)

class level1(death):
    def __init__(self,death):
        self.death=death
    def enter(self):
        a=[["aad","bef","cih","doj","eul"],["abc","efg","ijk","mno","qrs"],["ace","bdf","ceg","dfh","egi"],["zyx","xwv","vut","tsr","rqp"]]
        correct=random.choice(a)
        print("\n\nWelcome to level 1\n")
        print("\nThis is very simple puzzle")
        print("For every wrong attempt 20 Health will reduced\n")
        print("In this puzzle you have to guess the next term")
        print("The sequence is ",end=' ')
        i=0
        while i<4:
            print(correct[i],end=",")
            i+=1
        print("?")
        print("\nEnter the next term")
        while self.death.health>0:
            answer=input("> ")
            if answer==correct[i]:
                print("\nCorrect answer")
                break
            elif answer=='health':
                print("Health :- ",self.death.health,"\n")
            else :
                print("\nWrong Answer")
                print("Try Again\n")
                if health!=0:
                    print("Enter again")
                self.death.health-=20
        if self.death.health<=0:
            print("You used up all of your life")
            self.death.gameov()
        input("Press Enter to continue.")

class level2(death):
    words=["geography","economy","question","reverse","circular"]
    def __init__(self,death):
        self.death=death
    def enter(self):
        print("\n\nWelcome to level 2\n\n")
        print("You will be given scrambled letters")
        print("You have to form a word from the given letters")
        print("\nFor every wrong answer 10 health will be reduced\n")
        ch=random.randint(0,4)
        answer=self.words[ch]
        scrambled=list(answer)
        random.shuffle(scrambled)
        print("The letters are: ",scrambled)
        print("\nTo see the letter again Type 'show'\n")
        while self.death.health>0:
            print("Enter the word")
            given=input("> ")
            if given == 'show':
                print("The letters are: ",scrambled,'\n')
            elif given == 'health':
                print("Health :- ",self.death.health,'\n')
            elif given == answer:
                print("\nCorrect Answer\n")
                break
            else:
                print("\nWrong answer")
                print("Try again\n")
                self.death.health-=10
        if self.death.health<=0:
            print("You used up all of your life")
            return self.death.gameov()
        print("Press Enter to continue")
        input()

class level3(death):
    def __init__(self,death):
        self.death=death
    def enter(self):
        words=['range','quick','quilt','crazy','joker']
        chance=0
        hint_answers=["Area of variation between lower limit and upper limit","Synonym of fast","It is used in winter season","Synonym of Mad","Person who make others laugh"]
        ch=random.randint(0,4)
        correct=words[ch]
        answer=correct
        correct=list(correct)
        guess=[]
        hint=0
        print("\nWelcome to level 3\n\n")
        print("You have to guess a word which consists of 5 letters and all letters of the word are in lowercase")
        print("For every wrong guess 5 health will be reduced\n")
        print("You can ask for hint any time by typing 'hint' ")
        print("But you can use hint only once\n")
        print("If you want to see the letters that you have guessed correctly.Type 'show'")
        print("If you want to see this information again type 'help'\n")
        while self.death.health>0:
            print("Enter a letter")
            guess_w=input("> ")
            if guess_w=="hint" and hint==0:
                hint=1
                print("Hint:-",end=' ')
                print(hint_answers[ch],'\n')

            elif guess_w=='help':
                print("\nYou have to guess a word which consists of 5 letters and all letters of the word are in lowercase")
                print("For every wrong guess 5 health will be reduced\n")
                print("You can ask for hint any time by typing 'hint' ")
                print("But you can you hint only once\n")
                print("If you want to see the letters that you have guessed correctly.Type 'show'")
                print("If you want to see this information again type 'help'\n")

            elif guess_w=='show' and chance==1:
                print("The letters which you have guessed correctly are ",guess,'\n')
            elif guess_w=='show' and chance==0:
                print("\nYou have not typed a single alphabet\n")

            elif guess_w=="hint" and hint==1:
                print("\nYou have used up your hint before\n")

            elif guess_w in correct and not guess_w in guess:
                print("\nCorrect choice\n")
                chance=1
                guess.append(guess_w)

            elif guess_w=='health':
                print("Health :- ",self.death.health)
            else:
                print("\nWrong choice")
                self.death.health-=5
                print("Try again\n")

            if len(guess)==5 :
                break

        if self.death.health<=0:
            print("\nYou used up all of your life\n")
            return self.death.gameov()
        else:
            print("\nYou have guessed all the letters of the word")

        print("The letters which you have guessed correctly are",end=' ')
        print(guess,'\n')
        print("Enter the word")
        while self.death.health>0:
            guess_w=input("> ")
            if answer==guess_w:
                print("\nYou have guessed word correctly\n")
                print("Voila!!! You have completed this game.")
                input("Press Enter to continue.\n")
                break
            elif guess_w=='health':
                print("Health :- ",self.death.health,'\n')
            else :
                print("\nWrong answer")
                print("Try again\n")
                self.death.health-=5

        if self.death.health<=0:
            print("\nYou used up all of your life")
            return self.death.gameov()

print("\nHello, This is a puzzle game ")
print("To enjoy this game ,You need to solve 3 puzzles\n\n")
print("You have total health = 100 ")
print("Part of the health will be reduced for every wrong answer")
print("To check your health you can type 'health'")
health=100
death1=death(health)
a=level1(death1)
a.enter()
b=level2(death1)
b.enter()
c=level3(death1)
c.enter()
