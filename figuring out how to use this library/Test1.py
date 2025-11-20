#intention: write "Hello, world!" to screen, transform H to square, discard rest.
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h Test1
class Test1(Scene):
    def construct(self):
        HW = Text("Hello, world!")
        Hlet = HW[0:5]
        HW.move_to(UP*3)
        square = Square(color = RED, fill_opacity = 0.5)
        square.move_to(ORIGIN)
        self.play(Write(HW), run_time = 2)
        self.wait(2)
        self.play(Transform(Hlet,square),run_time = 1)
        self.wait(1)