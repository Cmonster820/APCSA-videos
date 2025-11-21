#figure out how to make truth tables. Stretch goal: logic gates (prob just use svgs for those)
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h TruthTableTest
class TruthTableTest(Scene):
    def construct(self):
        title = Text("Boolean Operators")
        title.to_edge(UP,buff = 0.2)
        self.add(title)
        notTable = Table(
            [["1","0"],
             ["0","1"]]
            ,include_outer_lines=True,
            col_labels = [Text("a"),Text("!a\nNOT a")]
        )
        andTable = Table(
            [["1","1","1"],
             ["1","0","0"],
             ["0","1","0"],
             ["0","0","0"]]
            ,include_outer_lines = True,
            col_labels = [Text("a"),Text("b"),Text("a&&b\nAND a b")]
        )
        orTable = Table(
            [["1","1","1"],
             ["1","0","1"],
             ["0","1","1"],
             ["0","0","0"]]
            ,include_outer_lines = True,
            col_labels = [Text("a"),Text("b"),Text("a||b\nOR a b")]
        )
        xorTable = Table(
            [["1","1","0"],
             ["1","0","1"],
             ["0","1","1"],
             ["0","0","0"]]
            ,include_outer_lines = True,
            col_labels = [Text("a"),Text("b"),Text("a^b\n((!a&&b)||(a&&!b))&&(a||b)\nXOR a b")]
        )
        nandTable = Table(
            [["1","1","0"],
             ["1","0","1"],
             ["0","1","1"],
             ["0","0","1"]]
            ,include_outer_lines = True,
            col_labels = [Text("a"),Text("b"),Text("!(a&&b)\nNAND a b")]
        )
        buffTable = Table(
            [["1","1"],
             ["0","0"]]
            ,include_outer_lines = True,
            col_labels = [Text("a"),Text("buffer")]
        )
        norTable = Table(
            [["1","1","0"],
             ["1","0","0"],
             ["0","1","0"],
             ["0","0","0"]]
            ,include_outer_lines = True,
            col_labels = [Text("a"),Text("b"),Text("!(a||b)\nNOR a b")]
        )
        xnorTable = Table(
            [["1","1","1"],
             ["1","0","0"],
             ["0","1","0"],
             ["0","0","1"]]
            ,include_outer_lines = True,
            col_labels = [Text("a"),Text("b"),Text("!(a^b)\n!(((!a&&b)||(a&&!b))&&(a||b))\nXNOR a b")]
        )
        notTable.height = 2
        andTable.height = 2
        orTable.height = 2
        nandTable.height = 2
        buffTable.height = 2
        xnorTable.height = 2
        xorTable.height = 2
        norTable.height = 2
        buffTable.to_corner(UL)
        nandTable.next_to(buffTable,RIGHT)
        andTable.to_corner(UR)
        notTable.next_to(andTable,LEFT)
        orTable.to_corner(BL)
        xnorTable.to_corner(BR)
        norTable.next_to(orTable,RIGHT)
        xorTable.next_to(xnorTable,LEFT)
        used = VGroup(notTable,andTable,orTable,xorTable)
        remaining = VGroup(nandTable,buffTable,xnorTable,norTable)
        self.play(Write(used))
        self.wait(2)
        self.play(Write(remaining))
        self.wait(4)
        self.play(LaggedStart(UnWrite(used)),UnWrite(remaining))
        self.wait(2)