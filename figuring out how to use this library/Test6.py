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
            [[Text("Math.abs([any numerical type not byte or short] x):Input type"),MathTex(r"\lvert x \rvert")],
             [Text("Math.ceil(double x):double"),MathTex(r"\left\lceil x \right\rceil")],
             [Text("Math.floor(double x):double"),MathTex(r"\left\lfloor x \right\rfloor")],
             [Text("Math.round(double x):long\nMath.round(float x):int"),MathTex(r"\left\lfloor x \right\rceil")],
             [Text("Math.rint(double x):double"),MathTex(r"\left\lfloor x \right\rceil")],
             [Text("Math.pow(double b, double e):double"),MathTex(r"b^e")]
             [Text("Math.sqrt(double x):double"),MathTex(r"\sqrt{x}")],
             [Text("Math.cbrt(double x):double"),MathTex(r"\sqrt[3]{x}")],
             [MathTex(r"Math.sin(double \theta):double"),MathTex(r"\sin(\theta)")],
             [MathTex(r"Math.cos(double \theta):double"),MathTex(r"\cos(\theta)")],
             [MathTex(r"Math.tan(double \theta):double"),MathTex(r"\tan(\theta)")],
             [Text("Math.asin(double x):double"),MathTex(r"\arcsin(x)\\\\\sin^{-1}(x)")],
             [Text("Math.acos(double x):double"),MathTex(r"\arccos(x)\\\\\cos^{-1}(x)")],
             [Text("Math.atan(double x):double"),MathTex(r"\arctan(x)\\\\\tan^{-1}(x)")],
             [Text("Math.atan2(double x, double y):double"),MathTex(r"(x,y)\rarr(r,\theta):\theta")],
             [Text("Math.exp(double x):double"),MathTex(r"e^x")],
             [Text("Math.expm1(double x):double"),MathTex(r)]],include_outer_lines=True
        )