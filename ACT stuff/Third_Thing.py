#This is a copied cell from a Jupyter notebook, generating this animation outside of the default
#Manim Community quick start notebook, with this pasted at the end, requires actually installing
#Manim Community on your computer and changing the first line to import all the required things
#and then use `manim --quality=h Third_Thing.py ACTThing3` from the terminal to generate the an
#imation. I don't know if ffmpeg automatically goes when manim generates a scene, but I would as
#sume that, since Manim requires ffmpeg (I think).
#I did write all of this, though. I just used the quick start guide Jupyter notebook to generate
#the animation for the slides.
%%manim -qh ACTThing3

class ACTThing3(Scene):
    def construct(self):
        banner = ManimBanner()      #make banner mobject
        self.play(banner.create())  #draw
        self.play(banner.expand())  #expand
        self.wait(0.5)              #wait
        self.play(Unwrite(banner))  #go away
        question = Tex(r"At the music store, the {{\underline{professional crafted}}} violins were \newline much more expensive than the beginner violins.",
                      tex_environment="flushleft") #you know the drill by now
        question.to_corner(UL)
        answers = Tex(r"\indent a) NO CHANGE \newline",
                      r"\indent b) profession crafted \newline",
                      r"\indent c) professionally crafted \newline",
                      r"\indent d) professional craft",
                      tex_environment="flushleft") #yeah seems about right
        answers.next_to(question, DOWN, aligned_edge = LEFT)
        group = VGroup(question,answers)
        self.play(Write(group))
        self.wait(2)
        box1 = SurroundingRectangle(question[1]) #slightly different here; this question only has 1 thing to be highlighted
        exp1 = Tex(r'''"professional" is, in this case, an adjective; \newline in order to modify "crafted," we need an adverb''',tex_environment="flushleft")
        exp1.to_corner(DR) #I originally called this explanation but then my chromebook crashed and then i redid it and then crashed again so I just wasn't bothered
        arr1 = Arrow(start = box1, end = exp1, color = BLUE)
        self.play(Create(box1), Write(exp1), Create(arr1))
        self.wait(2)
        self.play(Uncreate(arr1))
        self.wait(2)
        self.play(Uncreate(box1))
        self.wait()
        lines = []
        for line in answers:
            lines.append(Line(
            start=line.get_left(),
            end=line.get_right(),
            color=RED))
        del lines[2]        #mhmm seems about right
        for line in lines:
            self.play(Create(line),run_time=0.5)
        box = SurroundingRectangle(answers[2])
        self.play(Create(box))
        self.wait(2)
        for line in lines:
            self.play(Uncreate(line),run_time = 0.25)
        self.play(Uncreate(box), Unwrite(group), Unwrite(exp1))
        self.wait(2)    #good job