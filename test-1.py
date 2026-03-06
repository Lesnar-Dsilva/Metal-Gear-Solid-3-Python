
import tkinter as tk
from PIL import ImageTk, Image
import os
# [2026-03-05 19:41] I'm creating this file, because the use of self might help me...yet to be discovered
# [2026-03-06 12:11] This file is for the final product


class App:
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("test")
        self.window.geometry('1000x500')

        self.char1 = 0
        self.char2 = 0
        self.charFrame = tk.Frame(master=self.window)

        self.char1Frame = tk.Frame(master=self.charFrame)
        self.char1File = Image.open('assets/sigintIMG.png').resize((200,300))
        self.char1Photo = ImageTk.PhotoImage(self.char1File)
        self.char1IMG = tk.Label(master=self.char1Frame,image = self.char1Photo)
        self.char1Lbl = tk.Label(master = self.char1Frame, text = f'0{self.char1+1} / 04', font='Helvetica 24 bold')
        self.char1PrevBTN = tk.Button(master=self.char1Frame,text='<',command=lambda: self.prevChar1Func())
        self.char1NextBTN = tk.Button(master=self.char1Frame,text='>',command=lambda: self.nextChar1Func())

        self.char2Frame = tk.Frame(master=self.charFrame)
        self.char2File = Image.open('assets/sigintIMG.png').resize((200,300))
        self.char2Photo = ImageTk.PhotoImage(self.char2File)
        self.char2IMG = tk.Label(master=self.char2Frame,image = self.char2Photo)
        self.char2Lbl = tk.Label(master = self.char2Frame, text = f'0{self.char2+1} / 04', font='Helvetica 24 bold')
        self.char2PrevBTN = tk.Button(master=self.char2Frame,text='<',command=lambda: self.prevChar2Func())
        self.char2NextBTN = tk.Button(master=self.char2Frame,text='>',command=lambda: self.nextChar2Func())

        self.char1PrevBTN.configure(state=tk.DISABLED)
        self.char1NextBTN.configure(state=tk.DISABLED)

        self.char2PrevBTN.configure(state=tk.DISABLED)
        self.char2NextBTN.configure(state=tk.DISABLED)

        # [2026-03-06 15:11] The buttons will be active when the dialogue is running

        self.char1IMG.grid(row=0,column=1)
        self.char1Lbl.grid(row=1,column=1)
        self.char1PrevBTN.grid(row=2,column=0,sticky='W')
        self.char1NextBTN.grid(row=2,column=2,sticky='E')

        self.char2IMG.grid(row=0,column=1)
        self.char2Lbl.grid(row=1,column=1)
        self.char2PrevBTN.grid(row=2,column=0,sticky='W')
        self.char2NextBTN.grid(row=2,column=2,sticky='E')

        self.charFrame.grid_columnconfigure(1, weight=1)
        self.char1Frame.grid(row=0,column=0,sticky='W')
        self.char1Frame.grid_columnconfigure(1, weight=1)
        self.char2Frame.grid(row=0,column=2,sticky='E')
        self.char2Frame.grid_columnconfigure(1, weight=1)

        self.charFrame.grid(row=0, column=0, sticky='ew',padx=10)

        self.dialogueCanvas = tk.Canvas(master = self.window,width=500,height=500)
        self.dialogueCanvasText = self.dialogueCanvas.create_text(10,10,width=500,text='', anchor=tk.NW)
        self.freqTable = tk.Frame(master=self.window)
        self.freqVal = tk.StringVar(value="140.00")

        self.freqFrame = tk.Frame(master=self.window)
        self.freqFrame.grid(row=1,column=0)

        self.freqInput = tk.Entry(master=self.freqFrame,textvariable=self.freqVal)
        self.freqInput.pack()

        self.btnsFrame = tk.Frame(master=self.window)
        self.tuneBTN = tk.Button(master=self.btnsFrame,text='TUNE',command=lambda:self.setGlobalFreq(self.freqInput.get()))
        self.menuBTN = tk.Button(master=self.btnsFrame,text='MENU',command=lambda: self.stateFunc())

        self.btnsFrame.grid_columnconfigure(1, weight=1)
        self.tuneBTN.grid(row=0,column=2,sticky='W')
        self.menuBTN.grid(row=0,column=0,sticky='E')

        self.btnsFrame.grid(row=2, column=0, sticky='ew',padx=10)
        self.window.grid_columnconfigure(0,weight=1,minsize=100)

        self.freqTableState = 0

        self.carouselArray = [];
        self.majorZeroArray = ['assets/majorZeroIMG-A.png','assets/majorZeroIMG-B.png','assets/majorZeroIMG-C.png','assets/majorZeroIMG-D.png']
        self.paraMedicArray = ['assets/paraMedicIMG-A.png','assets/paraMedicIMG-B.png','assets/paraMedicIMG-C.png','assets/paraMedicIMG-D.png']
        self.evaArray = ['assets/evaIMG-A.png','assets/evaIMG-B.png','assets/evaIMG-C.png','assets/evaIMG-D.png']

        self.delay = 2500 # milliseconds between sentences
        self.index = 0
    
    def loadCarousel(self):
        self.char1PrevBTN.configure(state=tk.ACTIVE)
        self.char1NextBTN.configure(state=tk.ACTIVE)

        self.char2PrevBTN.configure(state=tk.ACTIVE)
        self.char2NextBTN.configure(state=tk.ACTIVE)
        match self.freqVal:
            case 140.85:
                self.carouselArray = self.majorZeroArray
                self.char1File = Image.open(self.carouselArray[self.char1]).resize((200,300))
                self.char1Photo = ImageTk.PhotoImage(self.char1File)
                self.char1IMG = tk.Label(master=self.char1Frame,image = self.char1Photo)
                self.char1IMG.grid(row=0,column=1)
            case 140.96:
                self.carouselArray = self.paraMedicArray
                self.char1File = Image.open(self.carouselArray[self.char1]).resize((200,300))
                self.char1Photo = ImageTk.PhotoImage(self.char1File)
                self.char1IMG = tk.Label(master=self.char1Frame,image = self.char1Photo)
                self.char1IMG.grid(row=0,column=1)
            case 145.73:
                self.carouselArray = self.paraMedicArray
                self.char1File = Image.open(self.carouselArray[self.char1]).resize((200,300))
                self.char1Photo = ImageTk.PhotoImage(self.char1File)
                self.char1IMG = tk.Label(master=self.char1Frame,image = self.char1Photo)
                self.char1IMG.grid(row=0,column=1)
            case 142.52:
                self.carouselArray = self.evaArray
                self.char1File = Image.open(self.carouselArray[self.char1]).resize((200,300))
                self.char1Photo = ImageTk.PhotoImage(self.char1File)
                self.char1IMG = tk.Label(master=self.char1Frame,image = self.char1Photo)
                self.char1IMG.grid(row=0,column=1)
            case 148.41:
                self.carouselArray = self.testArray
        

    def prevChar1Func(self):
        if self.char1 >0:
            print('Was ===>'+self.carouselArray[self.char1])
            self.char1 -= 1
            self.char1Lbl['text'] = f'0{self.char1+1} / 04'
            print('Now ===>'+self.carouselArray[self.char1])
            self.loadCarousel()
        else:
            self.char1 = 3
            self.char1Lbl['text'] = f'0{self.char1+1} / 04'
            self.loadCarousel()

    def nextChar1Func(self):
        if self.char1 <3:
            print(self.carouselArray)
            print('Was ===>'+self.carouselArray[self.char1])
            self.char1Lbl['text'] = f'0{self.char1+2} / 04'
            self.char1 += 1
            print('Now ===>'+self.carouselArray[self.char1])

            self.loadCarousel()
        else:
            self.char1 = 0
            self.char1Lbl['text'] = f'0{self.char1+1} / 04'
            self.loadCarousel()

    def prevChar2Func(self):
        if self.char2 > 1:
            self.char2 -= 1
            self.char2Lbl['text'] = f'0{self.char2} / 04'
        else:
            self.char2 = 4
            self.char2Lbl['text'] = f'0{self.char2} / 04'

    def nextChar2Func(self):
        if self.char2 < 4:
            self.char2 += 1
            self.char2Lbl['text'] = f'0{self.char2} / 04'
        else:
            self.char2 = 1
            self.char2Lbl['text'] = f'0{self.char2} / 04'

    def frequencyDialogue(self):
        print("Frequency Dialogue")
        # [2026-03-05 13:47] Returned a float, for the frequency of the button pressed
        print(type(self.freqVal))

        match self.freqVal:
            case 140.85:
                print('Major Zero Dialogue TRIGGERED')
                self.majorZeroDialogue = ['Can you hear me, Major Tom? This is Snake. Kept you waiting, huh?','This will be a sneaking mission. You must not be seen by the enemy. You must leave no trace of your presence. Is that clear? This kind of infiltration is the FOX unit\'s specialty. In ther words, weapons and equipment are procure on-site... that goes for food as well. You\'re completely naked, just as your name implies.','Great. Now I see why you asked me if I like snakes. I suppose calling me "snake" was your idea of a joke, too?','No, there\'s a good reason for that. I\'ll tell you later, when the time is right.','Gotcha. Getting back to the subject, how exactly am I supposed to feed myself?','You\'ve been issued a knife and a tranquilizer gun. Use them to hunt for food. You\'ll also find some medical supplies in your backpack.','Yeah, about the backpack... I lost it in a tree on the way down.','I see. Well, you\'d better go back and get it, then. Do you know where it is?','No problem, I can see it from here. It\'s stuck on a branch.','To climb a tree, stand in front of a tree that\'s covered in ivy and press the action button. I\'ll be monitoring your progress over the radio. We can\'t risk violating Soviet airspace, but I\'ll be in the gunship. My frequency is 140.85. I\'ll give you a CALL if I need to talk to you. If you need to talk to me, use the SEND function. OK, Snake, go get your backpack.']

                self.animate_text()
                self.loadCarousel()
                print('STARTING to Dialogue')
                
                print("Major Zero Dialogue ENDED")
            case 140.96:
                print('Save TRIGGERED')

                self.saveDialogue = ['Saving the game, please wait...']

                self.animate_text()
                self.loadCarousel()
                print('STARTING to Dialogue')
            
                print("SAVE Dialogue ENDED")
            case 145.73:
                print('Para-Medic Dialogue TRIGGERED')

                self.paraMedicDialogue = ['Hello, Snake. I\'m Para-Medic. Nice to meet you.','Para...Medic?','As in a medic who comes in by parachute.','Aren\'t you going to tell me your real name?','Are you going to tell me yours, Mr. Snake?','My name, huh... It\'s John Doe.','And they call you Jack for short? You\'re a regular Captain Nemo.','A name means nothing on the battlefield. After a week, no one has a name. What\'s your name?','Jane Doe.','Very funny.','I wasn\'t joking but I\'ll tell you my name only if you manage to make it back alive. My frequency is 145.73.']

                self.animate_text()
                self.loadCarousel()
                print('STARTING to Dialogue')

                print("Para-Medic Dialogue ENDED")
            case 142.52:
                print('Eva Dialogue TRIGGERED')

                self.evaDialogue = ['Snake, are you there?','Eva?','Did you miss me?','Did you make it without any trouble?','No one saw me.','So you\'re back with Volgin?','In a matter of speaking.','What about The Boss?','Yeah, she\'s here too.','Better be careful.','Thanks, I will. The Boss and I get along pretty well, though. I guess we traitors have a lot in common.','Why would anyone want to defect? Betraying your country like... I... I just don\'t get it.','Are you talking about The Boss?','Why\'d you do it? Weren\'t you born and raised in America?','Yes, in a small rural town. I never even knew there were other countries, other cultures, other ways of thinking. Until I went to work for the NSA. Then, one day, I\'d found I\'d lost faith in the things I\'d been taking for granted.','What did you see? What was it that made you want to change sides?','You wouldn\'t believe me if I told you.','Try me.','I saw the universe.','The universe?','Not the actual universe. The universe as the intelligence community sees it. I realized that the gravity in this universe was holding me back. That\'s all. People and their countries are both changed by the environment. And by the times.','That sounds like what The Boss was saying.','There\'s a world of difference between this country and America. But it\'s only a difference of position. A difference of perspective. Coming here made me realize something. Half of what I\'d been told was a complete and utter lie... the other half was a conveniently constructed lie.','Where\'s the truth then?','It\'s hidden in the lies.','Are you lying, too?','Who knows? I\'ve been trained to make even the most severe falsehood sound like the honest truth. Weren\'t you?','No. I... believe because I have to. Even if it is a lie. That\'s part of my mission.','I\'ll have to remember that. If you need to give me a call on the radio, my frequency is 142.52. See ya.']

                self.animate_text()
                self.loadCarousel()
                print('STARTING to Dialogue')

                print("Eva Dialogue ENDED")
            case 148.41:
                print('SIGINT Dialogue TRIGGERED')

                self.sigintDialogue = ['SORRY, this is exclusive to MGS3: Snake Eater']

                self.animate_text()
                print('STARTING to Dialogue')

                print("SIGINT Dialogue ENDED")
        
        self.freqTable.grid_forget()
        self.dialogueCanvas.grid(row=3,column=0)
        print('freqTable DISAPPEAR\nDialogue APPEAR')
        print('EXITED Dialogue match case') 

    def x(self):

        self.index = 0
        # [2026-03-05 20:15] Dialogue text content is cleared because the scripted event is over
        # [2026-03-05 21:34] DON'T use delete('all), as trying to render other text in the canvas WON'T work
        self.dialogueCanvas.itemconfigure(self.dialogueCanvasText,text='')
        self.menuBTN.configure(state=tk.ACTIVE)
        self.tuneBTN.configure(state=tk.ACTIVE)
        # [2026-03-05 20:42] Entry widget will need to be restored to NORMAL state
        self.freqInput.configure(state=tk.NORMAL)
        
        self.char1 = 0
        self.char2 = 0

        self.char1File = Image.open('assets/sigintIMG.png').resize((200,300))
        self.char1Photo = ImageTk.PhotoImage(self.char1File)
        self.char1IMG = tk.Label(master=self.char1Frame,image = self.char1Photo)  
        self.char1IMG.grid(row=0,column=1)    
        self.char1Lbl['text'] = f'0{self.char1+1} / 04'

        self.char2File = Image.open('assets/sigintIMG.png').resize((200,300))
        self.char2Photo = ImageTk.PhotoImage(self.char2File)
        self.char2IMG = tk.Label(master=self.char2Frame,image = self.char2Photo)  
        self.char2IMG.grid(row=0,column=1)    
        self.char2Lbl['text'] = f'0{self.char2+1} / 04'

        self.char1PrevBTN.configure(state=tk.DISABLED)
        self.char1NextBTN.configure(state=tk.DISABLED)

        self.char2PrevBTN.configure(state=tk.DISABLED)
        self.char2NextBTN.configure(state=tk.DISABLED)
        # [2026-03-06 15:11] Dialogue finished, so buttons are disabled again

        print('UI RESTORED')
        print("Talking done!!!")

    def animate_text(self):
        array = [];

        match self.freqVal:
            case 140.85:
                array = self.majorZeroDialogue
            case 140.96:
                array = self.saveDialogue
            case 145.73:
                array = self.paraMedicDialogue
            case 142.52:
                array = self.evaDialogue
            case 148.41:
                array = self.sigintDialogue
            
        self.menuBTN.configure(state=tk.DISABLED)
        self.tuneBTN.configure(state=tk.DISABLED)
        self.freqInput.configure(state=tk.DISABLED)
        if self.index <= len(array)-1:
            self.dialogueCanvas.itemconfigure(self.dialogueCanvasText, text=array[self.index][:])
            self.index += 1
            self.window.after(self.delay, self.animate_text)
            # [2026-03-05 21:21] +len(array[self.index-1])*20 = DELAY FORMULA
            # [2026-03-05 20:26] There is a modifier to the delay; depending on the length of the sentence being displayed, the user will have a longer/shorter amount of time to view the text (HARDCODING WOULD BE A ROOKIE MOVE OR for debugging)
        else:
            self.x()

    def stateFunc(self):
        if self.freqTableState == 0:
            # [2026-03-05 17:21] App starts with 0, so frequency menu needs to be rendered
            self.renderMenuTable()

    def setGlobalFreq(self,i):
        self.freqInput.delete(0,tk.END)
        self.freqInput.insert(0,i)
        # [2026-03-05 15:17]ONLY after deleting the input and displaying the user-selected frequency will the frequency dialogue be executed
        # [2026-03-05 15:19] I'm passing validating the value as an incorrect frequency, should return STATIC or DIALOGUE ONLY then am I assigning it to freqVal which is a system-wide variable
        if(float(i) >= 140.00 and float(i) <= 149.99):
            self.freqVal = float(i);
            print(f'TUNE: {self.freqVal}')
            self.frequencyDialogue()
        else:
            print('INVALID frequency')

    def renderMenuTable(self):
        # [2026-03-05 20:14] The widget in row 3 of the root grid can ONLY be deleted here it seems, tried after talking was done to no avail
        self.dialogueCanvas.grid_forget()
        print('Dialogue DISAPPEAR')

        print('MENU RENDER')
        self.frequenciesWithNames = {'MAJOR ZERO':'140.85','SAVE':'140.96','PARA-MEDIC':'145.73','EVA':'142.52','SIGINT':'148.41'}
        self.btnFreqs = [' '.join(reversed(i)) for i in list(self.frequenciesWithNames.items())]
        # [2026-03-04 12:05] this variable ONLY exists to stop the repition of the comprehension
        self.majorZeroBTN=tk.Button(master=self.freqTable, text=self.btnFreqs[0],command= lambda:self.setGlobalFreq(self.btnFreqs[0].split()[0]))
        self.majorZeroBTN.grid(row=1,column=0,sticky='NSEW')
        self.saveBTN=tk.Button(master=self.freqTable, text=self.btnFreqs[1],command=lambda: self.setGlobalFreq(self.btnFreqs[1].split()[0]))
        self.saveBTN.grid(row=1,column=1,sticky='NSEW')
        self.paraMedicBTN=tk.Button(master=self.freqTable, text=self.btnFreqs[2],command=lambda: self.setGlobalFreq(self.btnFreqs[2].split()[0]))
        self.paraMedicBTN.grid(row=2,column=0,sticky='NSEW')
        self.evaBTN=tk.Button(master=self.freqTable, text=self.btnFreqs[3],command=lambda: self.setGlobalFreq(self.btnFreqs[3].split()[0]))
        self.evaBTN.grid(row=2,column=1,sticky='NSEW')
        self.sigintBTN=tk.Button(master=self.freqTable, text=self.btnFreqs[4],command=lambda: self.setGlobalFreq(self.btnFreqs[4].split()[0]))
        self.sigintBTN.grid(row=3,column=0,sticky='NSEW')

        self.freqTable.grid(row=3,column=0)

App().window.mainloop()

# [2026-03-05 21:35] Ending Day 3 
# [2026-03-05 21:35] Wanted to finish more of the grunt work for the project
# [2026-03-05 21:35] Tomorrow the last thing left to work on are the images, the user will have access to a carousel for 2 characters at a time
# [2026-03-05 21:36] Depending on who they are conversing with

# [2026-03-06 15:14] Ending Day 4
# [2026-03-06 15:14] Project finished
# [2026-03-06 15:15] It's reached a state with which, I feel I have accomplished my objective
# [2026-03-06 15:15] The goal was to simply try to emulate the Metal Geart Solid 3 Codec
# [2026-03-06 15:15] I worked on the carousel today, took 2 hours.