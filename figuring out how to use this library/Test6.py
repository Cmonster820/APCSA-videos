#Math class methods PoC (splitting a table up)
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h Test6
class Test6(Scene):
    def construct(self):
        title = Text("The Math Class")
        self.add(title.to_edge(UP))
        completeTable = Table(
            [[Text("Math.abs([any numerical type not byte or short] x):Input type"),MathTex("$\lvert x \rvert$")],
             [Text("Math.ceil(double x):double"),MathTex("$\left\lceil x \right\rceil$")],
             [Text("Math.floor(double x):double"),MathTex("$\left\lfloor x \right\rfloor$")],
             [Text("Math.round(double x):long\nMath.round(float x):int"),MathTex("$\left\lfloor x \right\rceil$")]],include_outer_lines=True
        )