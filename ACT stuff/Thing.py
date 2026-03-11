#This is a copied cell from a Jupyter notebook, generating this animation outside of the default
#Manim Community quick start notebook, with this pasted at the end, requires actually installing
#Manim Community on your computer and changing the first line to import all the required things
#and then use `manim --quality=h Second_Thing.py ACTThing2` from the terminal to generate the an
#imation. I don't know if ffmpeg automatically goes when manim generates a scene, but I would as
#sume that, since Manim requires ffmpeg (I think).
#I did write all of this, though. I just used the quick start guide Jupyter notebook to generate
#the animation for the slides.
%%manim -qh ACTThing

class ACTThing(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait(0.5)
        self.play(Unwrite(banner))
        question = Tex(r"Adele {{has}} become popular for her unique voice, and \newline she {{\underline{had published}}} four studio albums.",
                      tex_environment="flushleft")
        question.to_corner(UL)
        answers = Tex(r"\indent a) NO CHANGE \newline", r"\indent b) has published \newline",r"\indent c) published \newline",r"\indent d) have published",
                     tex_environment="flushleft")
        answers.next_to(question,[0,-2,0])
        answers.to_edge(LEFT,buff=0.75)
        group = VGroup(question,answers)
        self.play(Write(group))
        self.wait(2)
        box1 = SurroundingRectangle(question[1])
        box2 = SurroundingRectangle(question[3])
        exp1 = Tex(r"Present perfect")
        exp2 = Tex(r"Past perfect")
        exp2.move_to(RIGHT)
        exp1.next_to(exp2,DOWN)
        arr1 = Arrow(start = box1, end = exp1, color = BLUE)
        arr2 = Arrow(start = box2, end = exp2, color = BLUE)
        self.play(Create(box2), Create(box1), Write(exp1), Write(exp2), Create(arr1), Create(arr2))
        self.wait(2)
        expGroup = VGroup(exp1,exp2)
        explanation = Tex(r"Must stay the same")
        explanation.move_to(expGroup)
        self.play(Uncreate(arr1), Uncreate(arr2),Transform(expGroup,explanation))
        self.add(explanation)
        self.remove(expGroup)
        self.wait(2)
        self.play(Uncreate(box1), Uncreate(box2))
        self.wait(2)
        lines = []
        for line in answers:
            lines.append(Line(
            start=line.get_left(),
            end=line.get_right(),
            color=RED))
        del lines[1]
        for line in lines:
            self.play(Create(line))
        box = SurroundingRectangle(answers[1])
        self.play(Create(box))
        self.wait(2)
        for line in lines:
            self.play(Uncreate(line))
        self.play(Uncreate(box), Unwrite(group), Unwrite(explanation))
        self.wait(2)