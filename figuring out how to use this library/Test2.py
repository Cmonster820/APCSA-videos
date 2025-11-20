import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h Test2
import copy
class Test2(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.wait(2)
        title = Text("Unit 1: Using Objects and Methods")
        updatedTitle = Text("Unit 1A: Using Objects and Methods")
        updatedTitle.move_to(UP*3.5)
        self.play(Write(title))
        self.wait(2)
        ToC = Table(
            [["Intro to Algorithms, Programming,\nand Compilers", "Variable and Data Types"],
            ["Expressions and Output", "Assignment Statements and Inputs"],
            ["Casting and Range of Variables", "Compound Assignment Operators"]],
            include_outer_lines=True,
            element_to_mobject=Text)
        sectTitle = copy.deepcopy(ToC.get_entries()[0])
        sectTitle.scale(1/2)
        ToC.scale(1/2)
        sectTitle.move_to(ToC.get_entries()[0])
        self.play(Transform(title,updatedTitle))
        self.play(DrawBorderThenFill(ToC), run_time=4)
        self.add(sectTitle)
        self.wait(2)
        self.play(sectTitle.animate.move_to(ORIGIN).scale(2),FadeOut(ToC))
        self.wait(2)
        self.play(FadeOut(title),sectTitle.animate.move_to(UP*3.1))
        self.wait(2)
        subSectTitle = Text("IDE's")
        subSectTitle.move_to(sectTitle)
        self.play(Transform(sectTitle,subSectTitle))
        self.wait(2)