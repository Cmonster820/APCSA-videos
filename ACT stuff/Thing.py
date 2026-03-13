#This is a copied cell from a Jupyter notebook, generating this animation outside of the default
#Manim Community quick start notebook, with this pasted at the end, requires actually installing
#Manim Community on your computer and changing the first line to import all the required things
#and then use `manim --quality=h Thing.py ACTThing` from the terminal to generate the an
#imation. I don't know if ffmpeg automatically goes when manim generates a scene, but I would as
#sume that, since Manim requires ffmpeg (I think).
#I did write all of this, though. I just used the quick start guide Jupyter notebook to generate
#the animation for the slides.
%%manim -qh ACTThing

class ACTThing(Scene):
    def construct(self):
        banner = ManimBanner()      #Make Manim logo mobject
        self.play(banner.create())  #draw Manim logo mobject
        self.play(banner.expand())  #expand                 
        self.wait(0.5)              #wait                   
        self.play(Unwrite(banner))  #go away                
        question = Tex(r"Adele {{has}} become popular for her unique voice, and \newline she {{\underline{had published}}} four studio albums.",
                      tex_environment="flushleft") #define the question mobject
        question.to_corner(UL)
        answers = Tex(r"\indent a) NO CHANGE \newline", r"\indent b) has published \newline",r"\indent c) published \newline",r"\indent d) have published",
                     tex_environment="flushleft") #define the answers mobject
        answers.next_to(question,[0,-2,0]) #move the answers next to the question 
        answers.to_edge(LEFT,buff=0.75) #set the answers to the side of the screen (I was unaware of the `aligned_edge` kwarg at the time)
        group = VGroup(question,answers)
        self.play(Write(group))
        self.wait(2)
        box1 = SurroundingRectangle(question[1]) #create the box around "has"
        box2 = SurroundingRectangle(question[3]) #create the box around the underlined stuff
        exp1 = Tex(r"Present perfect")  #self explanatory
        exp2 = Tex(r"Past perfect")     #↲
        exp2.move_to(RIGHT)             #↲
        exp1.next_to(exp2,DOWN)         #↲
        arr1 = Arrow(start = box1, end = exp1, color = BLUE) #define first arrow
        arr2 = Arrow(start = box2, end = exp2, color = BLUE) #↲ second
        self.play(Create(box2), Create(box1), Write(exp1), Write(exp2), Create(arr1), Create(arr2)) #draw the stuff on the screen
        self.wait(2)
        expGroup = VGroup(exp1,exp2)
        explanation = Tex(r"Must stay the same")
        explanation.move_to(expGroup)
        self.play(Uncreate(arr1), Uncreate(arr2),Transform(expGroup,explanation))
        self.add(explanation)   #swap out the `expGroup` mobject with the `explanation` mobject 
        self.remove(expGroup)   #↲
        self.wait(2)
        self.play(Uncreate(box1), Uncreate(box2)) #go away boxes
        self.wait(2)
        lines = []
        for line in answers: #insert the `line` mobjects into the `lines` list
            lines.append(Line(
            start=line.get_left(),
            end=line.get_right(),
            color=RED))
        del lines[1]    #remove the strikethrough line from the correct answer
        for line in lines:          #loop through the `line`s in `lines` and draw them to the screen
            self.play(Create(line)) #↲
        box = SurroundingRectangle(answers[1]) #create the box for the right answer
        self.play(Create(box))  #draw the aforementioned box to the screen
        self.wait(2)
        for line in lines:              #loop through all the `line`s in `lines` and remove them from the screen
            self.play(Uncreate(line))   #↲
        self.play(Uncreate(box), Unwrite(group), Unwrite(explanation))  #fancily remove everything left
        self.wait(2)    #wait 2 seconds