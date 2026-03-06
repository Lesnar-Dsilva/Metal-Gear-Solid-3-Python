import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=500, height=100)
        self.canvas.pack()
        self.canvas_text = self.canvas.create_text(10, 10, text='', anchor='nw')

        self.testArray = ['Can you hear me, Major Tom? This is Snake. Kept you waiting, huh?','This will be a sneaking mission. You must not be seen by the enemy. You must leave no trace of your presence. Is that clear? This kind of infiltration is the FOX unit\'s specialty. In ther words, weapons and equipment are procure on-site... that goes for food as well. You\'re completely naked, just as your name implies.','Great. Now I see why you asked me if I like snakes. I suppose calling me "snake" was your idea of a joke, too?','No, there\'s a good reason for that. I\'ll tell you later, when the time is right.','Gotcha. Getting back to the subject, how exactly am I supposed to feed myself?','You\'ve been issued a knife and a tranquilizer gun. Use them to hunt for food. You\'ll also find some medical supplies in your backpack.','Yeah, about the backpack... I lost it in a tree on the way down.','I see. Well, you\'d better go back and get it, then. Do you know where it is?','No problem, I can see it from here. It\'s stuck on a branch.','To climb a tree, stand in front of a tree that\'s covered in ivy and press the action button. I\'ll be monitoring your progress over the radio. We can\'t risk violating Soviet airspace, but I\'ll be in the gunship. My frequency is 140.85. I\'ll give you a CALL if I need to talk to you. If you need to talk to me, use the SEND function. OK, Snake, go get your backpack.']
        self.delay = 250  # milliseconds between characters
        self.index = 0

        self.animate_text()

    

    def animate_text(self):
        if self.index <= len(self.testArray)-1:
            self.canvas.itemconfigure(self.canvas_text, text=self.testArray[self.index][:])
            self.index += 1
            self.root.after(self.delay, self.animate_text)
        else:
            self.x()

App().root.mainloop()