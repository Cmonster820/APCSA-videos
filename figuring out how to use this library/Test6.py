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
        completeTablePart1 = MobjectTable(
            [[Text("Math.abs([int,long,float,double] x):Input type"),MathTex(r"\lvert x \rvert")],
             [Text("Math.ceil(double x):double"),MathTex(r"\left\lceil x \right\rceil")],
             [Text("Math.floor(double x):double"),MathTex(r"\left\lfloor x \right\rfloor")],
             [Text("Math.round(double x):long\nMath.round(float x):int"),MathTex(r"\left\lfloor x \right\rceil")],
             [Text("Math.rint(double x):double"),MathTex(r"\left\lfloor x \right\rceil")],
             [Text("Math.pow(double b, double e):double"),MathTex(r"b^e")],
             [Text("Math.sqrt(double x):double"),MathTex(r"\sqrt{x}")],
             [Text("Math.cbrt(double x):double"),MathTex(r"\sqrt[3]{x}")],
             [MathTex(r"\mathrm{Math.sin(double  \theta):double}"),MathTex(r"\sin(\theta)")],
             [MathTex(r"\mathrm{Math.cos(double  \theta):double}"),MathTex(r"\cos(\theta)")],
             [MathTex(r"\mathrm{Math.tan(double  \theta):double}"),MathTex(r"\tan(\theta)")],
             [Text("Math.sinh(double x):double"),MathTex(r"\sinh(x)")],
             [Text("Math.cosh(double x):double"),MathTex(r"\cosh(x)")],
             [Text("Math.tanh(double x):double"),MathTex(r"\tanh(x)")],
             [Text("Math.asin(double x):double"),MathTex(r"\arcsin(x)\\\sin^{-1}(x)")],
             [Text("Math.acos(double x):double"),MathTex(r"\arccos(x)\\\cos^{-1}(x)")],
             [Text("Math.atan(double x):double"),MathTex(r"\arctan(x)\\\tan^{-1}(x)")],
             [Text("Math.atan2(double x, double y):double"),MathTex(r"(x,y) (r,\theta):\theta")]]
             ,include_outer_lines=True
        )
        completeTablePart2=MobjectTable(
            [[Text("Math.exp(double x):double"),MathTex(r"e^x")],
             [Text("Math.expm1(double x):double"),MathTex(r"(e^x)-1")],
             [Text("Math.log(double x):double"),MathTex(r"\ln(x)\\\log_{e}(x)")],
             [Text("Math.log10(double x):double"),MathTex(r"\log(x)\\\log_{10}(x)")],
             [Text("Math.log1p(double x):double"),MathTex(r"\ln(1+x)\\\log_{e}(1+x)")],
             [Text("Math.max(type a, type b):input type"),MathTex(r"\max(a,b)")],
             [Text("Math.min(type a, type b):input type"),MathTex(r"\min(a,b)")],
             [Text("Math.random():double"),Text("No notation for this, random double\nfrom 0 to less than 1")],
             [MathTex(r"\mathrm{Math.toDegrees(double  \theta):double}"),MathTex(r"\mathrm{\theta\circ} \rightarrow mathrm{\theta^{rad}}")],
             [MathTex(r"\mathrm{Math.toRadians(double  \theta):double}"),MathTex(r"\mathrm{\theta^{rad}} \rightarrow \mathrm{\theta\circ}")],
             [Text("Math.signum(float,double x):input type"),Text("sign(x)")],
             [Text("Math.floorDiv(int x, int y):int"),MathTex(r"\left\lfloor x \div y \right\rfloor")],
             [Text("Math.floorMod(int x, int y):int"),MathTex(r"\left\lfloor\mathrm{mod(}x,y\mathrm{)}\right\rfloor")],
             [Text("Math.hypot(double x, double y):double"),MathTex(r"\sqrt{x^2\mathrm{+}y^2}")],
             [Text("Math.copySign(double x, double y):double"),MathTex(r"\left\lvert x \right\rvert \times \mathrm{sign(}y\mathrm{)}")]
            ],include_outer_lines=True
        )
        completeTablePart1.height = 7
        completeTablePart2.height = 7
        completeTablePart1.move_to([-4,0,0])
        completeTablePart2.move_to([4,0,0])
        self.play(Write(completeTablePart1),Write(completeTablePart2))
        self.wait(2)