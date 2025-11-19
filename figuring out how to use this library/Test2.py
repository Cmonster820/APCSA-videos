%%manim -qm Test2
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
            [["Intro to Algorithms, Programming,\n and Compilers", "Variable and Data Types"],
            ["Expressions and Output", "Assignment Statements and Inputs"],
            ["Casing and Range of Variables", "Compound Assignment Operators"]],
            include_outer_lines=True,
            element_to_mobject=Text)
        sect1 = copy.deepcopy(ToC.get_entries()[0])
        sect1.scale(1/2)
        ToC.scale(1/2)
        sect1.move_to(ToC.get_entries()[0])
        self.play(Transform(title,updatedTitle))
        self.play(DrawBorderThenFill(ToC), run_time=4)
        self.add(sect1)
        self.wait(2)
        self.play(sect1.animate.move_to(ORIGIN).scale(2),FadeOut(ToC))
        self.wait(2)
        self.play(FadeOut(sect1))