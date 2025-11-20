#Intention: Make a table and have it be a specific size, then move it or discard parts of it
#personal note: screen is 14.22x8 manim units
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h Test4
import copy
class Test4(Scene):
    def construct(self):
        completeEscapeTable = Table(
            [["Escape Sequence","What They Mean"],
             ["\\n","New Line"],
             ["\\r","Return Carriage to\nBeginning of Line"],
             ["\\t","Jump Carriage to Next\nIndentation Level (inserts a tab)"],
             ["\\b","Jump Carriage Back 1 Position,\nReplacing the Character with the Next"],
             ["\\f","\"Form Feed\", Inserts Page Break"],
             ["\\'","Inserts '"],
             ['''\\"''','''Inserts "'''],
             ["\\\\","Inserts \\"]],include_outer_lines=True
        )
        completeEscapeTable.height = 6
        completeEscapeTable.width = 8
        EscapeTable = Table(
            [["Escape Sequence", "What They Mean"],
             ["\\n","New Line"],
             ["\\t","Insert Tab/Indent"],
             ["\\\\","\\"],
             ["\\\"","\""]],
            include_outer_lines=True
        )
        EscapeTable.height = 5
        EscapeTable.width = 7
        EscapeTable.move_to([-3,1,0])
        label = Text("These are the ones we use")
        label.move_to([3.5,1,0])
        label.width = 5
        self.play(Write(completeEscapeTable), run_time=4)
        self.wait(2)
        self.play(Transform(completeEscapeTable,EscapeTable))
        self.play(FadeIn(EscapeTable),FadeOut(completeEscapeTable),Write(label))
        self.wait(2)