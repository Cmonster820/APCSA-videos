#This is a copied cell from a Jupyter notebook, generating this animation outside of the default
#Manim Community quick start notebook, with this pasted at the end, requires actually installing
#Manim Community on your computer and changing the first line to import all the required things
#and then use `manim --quality=h Second_Thing.py ACTThing2` from the terminal to generate the an
#imation. I don't know if ffmpeg automatically goes when manim generates a scene, but I would as
#sume that, since Manim requires ffmpeg (I think).
#I did write all of this, though. I just used the quick start guide Jupyter notebook to generate
#the animation for the slides.
%%manim -qh ACTThing2

class ACTThing2(Scene):
    def construct(self):
        banner = ManimBanner()      #Make Manim logo mobject
        self.play(banner.create())  #draw Manim logo mobject
        self.play(banner.expand())  #expand                 
        self.wait(0.5)              #wait                   
        self.play(Unwrite(banner))  #go away                
        question = Tex(r"Sitting in the comfort of {{our}} living room, {{\underline{Bad Bunny’s halftime performance that we were watching}}} \newline was interesting and exciting.",
                      tex_environment="flushleft") #^define question mobject
        question.to_corner(UL) #put it in the corner
        answers = Tex(r"\indent a) Bad Bunny’s halftime performance watched \newline",
                      r"\indent b) there was Bad Bunny’s halftime performance that we \newline \indent \medskip watched \newline",
                      r"\indent c) watching Bad Bunny’s halftime performance that \newline",
                      r"\indent d) we watched Bad Bunny’s halftime performance that",
                      tex_environment="flushleft") #define the answer mobject
        answers.next_to(question,[0,-2,0])  #put the answers in the right place
        answers.to_edge(LEFT,buff=0.75)     #↲
        group = VGroup(question,answers)    #group them together
        self.play(Write(group))         #write stuff to screen
        self.wait(2)                #wait
        new_q = question.copy()     #I don't want to subject you to understanding the hellish fuckery going on here
        new_q.font_size = question.font_size/2
        new_q.to_corner(UL)
        new_a = Tex(r"\indent a) Bad Bunny’s halftime performance watched \newline",
                      r"\indent b) there was Bad Bunny’s halftime performance that we watched \newline",
                      r"\indent c) watching Bad Bunny’s halftime performance that \newline",
                      r"\indent d) we watched Bad Bunny’s halftime performance that",
                      tex_environment="flushleft")
        new_a.font_size = new_q.font_size
        new_a.next_to(new_q, DOWN, aligned_edge = LEFT)
        new_group = VGroup(new_q,new_a)
        self.play(Transform(group,new_group))
        box1 = SurroundingRectangle(question[3])
        box2 = SurroundingRectangle(question[1])
        exp2 = Tex(r'"our" states that we are the subject',tex_environment="flushleft")                                     #define explanations
        exp1 = Tex(r'''Structure implies that the performance is the subject, but it's "we."''',tex_environment="flushleft")#↲
        exp1.font_size = exp1.font_size*0.75#set font size
        exp2.font_size = exp1.font_size     #↲
        exp2.to_corner(DR)                          #move to corner
        exp2.to_edge(RIGHT, buff = 3)               #↲
        exp1.next_to(exp2,UP, aligned_edge = LEFT)  #↲
        arr1 = Arrow(start = box1, end = exp1, color = BLUE)    #define arrows
        arr2 = Arrow(start = box2, end = exp2, color = BLUE)    #↲
        self.play(Create(box2), Create(box1), Write(exp1), Write(exp2), Create(arr1), Create(arr2)) #draw all that to the screen
        self.wait(2)
        expGroup = VGroup(exp1,exp2)                                                #####################################
        expGroup.font_size = exp1.font_size                                         #Man I wish I knew                  #
        explanation = Tex(r"Subject must be first word after comma.")               #                                   #
        explanation.to_corner(DR)                                                   #                                   #
        self.play(Uncreate(arr1), Uncreate(arr2),Transform(expGroup,explanation))   #                                   #
        self.add(explanation)                                                       #                                   #
        self.remove(expGroup)                                                       #                                   #
        self.wait(2)                                                                #                                   #
        self.play(Uncreate(box1), Uncreate(box2))                                   #                                   #
        self.wait(2)                                                                #####################################
        lines = []
        for line in answers:            #see previous
            lines.append(Line(          #
            start=line.get_left(),      #
            end=line.get_right(),       #
            color=RED))                 #
        del lines[3]    #delete strikethrough for right answer
        for line in lines:
            self.play(Create(line),run_time=0.5)    #actually strike through
        box = SurroundingRectangle(answers[3])
        self.play(Create(box))
        self.wait(2)
        for line in lines:
            self.play(Uncreate(line),run_time = 0.25)                   #remove all
        self.play(Uncreate(box), Unwrite(group), Unwrite(explanation))  #↲
        self.wait(2)