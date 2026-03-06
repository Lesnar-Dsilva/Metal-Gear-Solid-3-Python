import tkinter as tk
#from tkinter import tk

# [2026-03-03 14:17] imported ttkbootstrap for a clearner look replacing tkinter's tk

# PLEASE REMEMBER TO DEACTIVATE THE PYTHON VIRTUAL ENVIRONEMENT AFTER FINISHING THE PROJECT
# .env $ deactivate

# [2026-03-03 13:40] test needs to be replaced with the final product name

# character frame counter    



# [2026-03-05 13:07] This function will run when the user presses TUNE or selects a frequency relating to a character in the MENU



    # window
    

    # [2026-03-03 18:17] This counter keeps track of which image of the character is being shown, but there will be buttons to control the current image shown, cycling through 4 for each character
    

    # {1} setGlobalFreq function
    # [2026-03-03 13:54] = I'm creating a variable to store the frequency input value
    # [2026-03-03 13:57] created an else statement, which in the future will have a GUI element
    


    
    # [2026-03-03 18:06] Added textvariable because DON'T want a user to cause a runtime error, because there isn't a value in the input

    # [2026-03-03 13:51] had to use the command parameter to utilize the setGlobalFreq function, this was added after I decided to create the function
    # [2026-03-03 17:18] Had to work with setGlobalFreq because I need to pass values to it, but the command parameter doesn't accept functions with parentheses otherwise it get's called at app startup, so had to use lambda
    

    # [2026-03-03 13:43] take the widgets and place them in the frame
    # [2026-03-03 13:45] then place the frame in the window

    

    # [2026-03-03 13:48] pack the widgets to solidfy their place in the frame
    # [2026-03-03 13:49] now pack the frame to insert it into the window

    

    # [2026-03-04 16:26] Now I'll add a MENU button that renders the frame, otherwise there will be a dialogue
    
    # run
    

# [2026-03-03 13:50] now I need a function that is called when the tune button is called to tune the radio to a frequency
# {1} refer to the setGlobalFreq function

# [2026-03-03 14:30] now I'm going to add the MENU which will be a drop-down menu for users to go to commonly used frequencies which in MGS3 were often used to communicate to important characters/saving
# combobox
# [2026-03-03 16:32] created a variable to store the frequency selected by the user
# [2026-03-03 16:35] have to use tkinter StringVar to have a value that shows up as a placeholder when the app launches
# freqSelect = tk.StringVar(value="MENU");
# [2026-03-03 17:26] Now the combobox is read-only, because otherwise it would act like another input which isn't necesssary
# freqMenu = tk.Combobox(master=window, textvariable=freqSelect,state='readonly')
# menuFreqs = {'MAJOR ZERO':'140.85','SAVE':'140.96','PARA-MEDIC':'145.73','EVA':'142.52','SIGINT':'148.41'}
# # [2026-03-03 15:35] finished rendering the MENU as in the game used Python's comprehension as I was being stubborn about using a dictionary
# freqMenu['values'] = [' '.join(reversed(i)) for i in list(menuFreqs.items())]
# freqMenu.pack()
# [2026-03-04 11:59] Commenting out the Combobox code

# combobox event
# [2026-03-03 16:36] Anytime any option is selected by the user, the bind method's function is called
# [2026-03-03 16:38] Used the freqSelect variable to fetch the value selected by the user, now I can work with the specific frequency selected
# [2026-03-03 17:24] Now when an option is selected, the setGlobalFreq function will parse it, still need to work on deciding whether to display a label or simply use the input
# freqMenu.bind('<<ComboboxSelected>>', lambda e: setGlobalFreq(freqSelect.get().split()[0]))


# [2026-03-04 11:25] I'm going to try to display the menu in a table, rather than a drop-down menu to increase the complexity of the app
# Table replacing Combobox

# [2026-03-04 12:34] Need to customize the buttons because I want the text to align to the left
# [2026-03-04 12:34] 1. I need the class name to which I am applying the style
# print(majorZeroBTN.winfo_class()) # [2026-03-04 12:35] >> TButton

# [2026-03-04 12:35] I can apply a style to a specific widget, but I'm trying to learn about how to apply it to a group
# majorZeroBTN['style']

# [2026-03-04 12:38] Creating a new style
# style.configure('Emergency.TButton', font='helvetica 24', foreground='red', padding=10,background='green')
# [2026-03-04 12:52] I will build my own style, && apply it to the menu buttons
# [2026-03-04 16:23] I wanted the user to have visual feedback of when they click the button

# [2026-03-04 12:39] You can't use this style earlier in the code, because of how code is run (TOP -> BOTTOM)
# [2026-03-04 12:57] It seems as though certain words are reserved...
# [2026-03-04 14:00] config method doesn't work for ttkbootstrap widgets...
# majorZeroBTN['style'] = 'MyStyle.TButton'

# [2026-03-04 12:41] To look at the logical structure of HOW a style NEEDS to be applied
# print(style.layout('MyStyle.TButton'))
# [2026-03-04 12:42] This prints each element and their default configuration && each one of these elements has different options

# [2026-03-04 12:47] Now were looking at what can be configured for every button
# print(style.element_options('Button.label'))

# [2026-03-04 12:48] Retrieve the current value of an option
# print(style.lookup('Button.label', 'font'))
# [2026-03-04 12:50] It won't print out anything, if you didn't configure it, even for the default TButton style

# [2026-03-04 12:51] Even state specific styling can be done
# style.map('TButton', 
#     background=[('disabled','#d9d9d9'), ('active','#ececec')],
#     foreground=[('disabled','#a3a3a3')],
#     relief=[('pressed', '!disabled', 'sunken')])

# [2026-03-04 13:22] Ended up using layout, couldn't figure out how to access the Button.label element, IT'S NOT THE SAME AS CONFIGURE

# [2026-03-04 16:02] Now I will apply the style, because I don't want the style I made being applied to the TUNE button

# [2026-03-04 17:22] removed ttkbootstrap from the app, it overcomplicated the program while writing it

# [2026-03-03 18:11] Ending Day 1
# [2026-03-03 18:11] Input Frequency WORKS
# [2026-03-03 18:12] Menu Frequency WORKS
# [2026-03-03 18:12] Need to decide on how to inform user that both are/aren't connected to the same frequency value(s)
# [2026-03-04 18:18] Ending Day 2
# [2026-03-04 18:18] Now the Menu is a Frame that contains buttons like the game where the user can select which frequency they want
# [2026-03-04 18:19] The TUNE and MENU buttons are on the same row
# [2026-03-04 18:19] The app is using a grid to render the widgets, it made it easier for me to position them
# [2026-03-04 18:36] Added the dialogue frame, so user's experience some of the dialogue between Naked Snake and the frequencies
# [2026-03-04 18:36] It needs a lot more work to incorporate it with the menu buttons to run the dialogue OR even if the user manually tunes into a frequency

import tkinter as tk
# [2026-03-05 19:41] I'm creating this file, because the use of self might help me...yet to be discovered


class App:
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("test")
        self.window.geometry('500x300')

        self.charIMG = tk.Label(master = self.window, text = f'0{self.charFramesFunc()}/ 04', font='Helvetica 24 bold')
        self.charIMG.grid(row=0, column=0, sticky='s')

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

        self.testArray = ['Can you hear me, Major Tom? This is Snake. Kept you waiting, huh?','This will be a sneaking mission. You must not be seen by the enemy. You must leave no trace of your presence. Is that clear? This kind of infiltration is the FOX unit\'s specialty. In ther words, weapons and equipment are procure on-site... that goes for food as well. You\'re completely naked, just as your name implies.','Great. Now I see why you asked me if I like snakes. I suppose calling me "snake" was your idea of a joke, too?','No, there\'s a good reason for that. I\'ll tell you later, when the time is right.','Gotcha. Getting back to the subject, how exactly am I supposed to feed myself?','You\'ve been issued a knife and a tranquilizer gun. Use them to hunt for food. You\'ll also find some medical supplies in your backpack.','Yeah, about the backpack... I lost it in a tree on the way down.','I see. Well, you\'d better go back and get it, then. Do you know where it is?','No problem, I can see it from here. It\'s stuck on a branch.','To climb a tree, stand in front of a tree that\'s covered in ivy and press the action button. I\'ll be monitoring your progress over the radio. We can\'t risk violating Soviet airspace, but I\'ll be in the gunship. My frequency is 140.85. I\'ll give you a CALL if I need to talk to you. If you need to talk to me, use the SEND function. OK, Snake, go get your backpack.']

        self.delay = 250 # milliseconds between sentences
        self.index = 0
    
    def frequencyDialogue(self):
        print("Frequency Dialogue")
        # [2026-03-05 13:47] I am returned a float, for the frequency of the button pressed
        print(type(self.freqVal))

        match self.freqVal:
            case 140.85:
                print('Major Zero Dialogue TRIGGERED')
                self.majorZeroDialogue = ['Can you hear me, Major Tom? This is Snake. Kept you waiting, huh?','This will be a sneaking mission. You must not be seen by the enemy. You must leave no trace of your presence. Is that clear? This kind of infiltration is the FOX unit\'s specialty. In ther words, weapons and equipment are procure on-site... that goes for food as well. You\'re completely naked, just as your name implies.','Great. Now I see why you asked me if I like snakes. I suppose calling me "snake" was your idea of a joke, too?','No, there\'s a good reason for that. I\'ll tell you later, when the time is right.','Gotcha. Getting back to the subject, how exactly am I supposed to feed myself?','You\'ve been issued a knife and a tranquilizer gun. Use them to hunt for food. You\'ll also find some medical supplies in your backpack.','Yeah, about the backpack... I lost it in a tree on the way down.','I see. Well, you\'d better go back and get it, then. Do you know where it is?','No problem, I can see it from here. It\'s stuck on a branch.','To climb a tree, stand in front of a tree that\'s covered in ivy and press the action button. I\'ll be monitoring your progress over the radio. We can\'t risk violating Soviet airspace, but I\'ll be in the gunship. My frequency is 140.85. I\'ll give you a CALL if I need to talk to you. If you need to talk to me, use the SEND function. OK, Snake, go get your backpack.']

                self.animate_text()
                print('STARTING to Dialogue')
                
                print("Major Zero Dialogue ENDED")
            case 140.96:
                print('Save TRIGGERED')

                self.saveDialogue = ['Saving the game, please wait...']

                self.animate_text()
                print('STARTING to Dialogue')
            
                print("SAVE Dialogue ENDED")
            case 145.73:
                print('Para-Medic Dialogue TRIGGERED')

                self.paraMedicDialogue = ['Hello, Snake. I\'m Para-Medic. Nice to meet you.','Para...Medic?','As in a medic who comes in by parachute.','Aren\'t you going to tell me your real name?','Are you going to tell me yours, Mr. Snake?','My name, huh... It\'s John Doe.','And they call you Jack for short? You\'re a regular Captain Nemo.','A name means nothing on the battlefield. After a week, no one has a name. What\'s your name?','Jane Doe.','Very funny.','I wasn\'t joking but I\'ll tell you my name only if you manage to make it back alive. My frequency is 145.73.']

                self.animate_text()
                print('STARTING to Dialogue')

                print("Para-Medic Dialogue ENDED")
            case 142.52:
                print('Eva Dialogue TRIGGERED')

                self.evaDialogue = ['Snake, are you there?','Eva?','Did you miss me?','Did you make it without any trouble?','No one saw me.','So you\'re back with Volgin?','In a matter of speaking.','What about The Boss?','Yeah, she\'s here too.','Better be careful.','Thanks, I will. The Boss and I get along pretty well, though. I guess we traitors have a lot in common.','Why would anyone want to defect? Betraying your country like... I... I just don\'t get it.','Are you talking about The Boss?','Why\'d you do it? Weren\'t you born and raised in America?','Yes, in a small rural town. I never even knew there were other countries, other cultures, other ways of thinking. Until I went to work for the NSA. Then, one day, I\'d found I\'d lost faith in the things I\'d been taking for granted.','What did you see? What was it that made you want to change sides?','You wouldn\'t believe me if I told you.','Try me.','I saw the universe.','The universe?','Not the actual universe. The universe as the intelligence community sees it. I realized that the gravity in this universe was holding me back. That\'s all. People and their countries are both changed by the environment. And by the times.','That sounds like what The Boss was saying.','There\'s a world of difference between this country and America. But it\'s only a difference of position. A difference of perspective. Coming here made me realize something. Half of what I\'d been told was a complete and utter lie... the other half was a conveniently constructed lie.','Where\'s the truth then?','It\'s hidden in the lies.','Are you lying, too?','Who knows? I\'ve been trained to make even the most severe falsehood sound like the honest truth. Weren\'t you?','No. I... believe because I have to. Even if it is a lie. That\'s part of my mission.','I\'ll have to remember that. If you need to give me a call on the radio, my frequency is 142.52. See ya.']

                self.animate_text()
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
    
    def charFramesFunc(self):
        self.i = 4;
        if (self.i < 4):
            return self.i;
        else:
            return 1;

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