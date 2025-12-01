#intention: figure out how I want to style this stuff
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h big10FTC
%%manim -qm Big10FTC

class Big10FTC(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.wait(2)
        np1 = NumberPlane(
            x_range = (-5,7,1),
            y_range = (-3,3,1),
            x_length = 12,
            y_length = 5
        )
        trap1 = Polygon(np1.coords_to_point(-4,0),np1.coords_to_point(-2,2),np1.coords_to_point(-2,0), color=YELLOW, fill_opacity=0.5)
        trap2 = Polygon(np1.coords_to_point(-2,0),np1.coords_to_point(-2,2),np1.coords_to_point(0,2),np1.coords_to_point(0,0), color=YELLOW, fill_opacity=0.5)
        xvals = [-4,-2,0,2,6]
        yvals = [0,2,2,-2,2]
        self.play(Create(np1, run_time=3, lag_ratio=0.1))
        graph1 = np1.plot_line_graph(
            x_values=xvals,
            y_values=yvals,
            line_color=BLUE
        )
        label = Text("f(x)")
        label.move_to([-1,0,0])
        self.wait(1)
        self.play(Create(graph1, run_time=4),Write(label))
        self.wait(2)
        graphstuff = VGroup(np1,graph1,label)
        graphtarget = graphstuff.copy()
        graphtarget.width = 7
        graphtarget.to_corner(UL)
        self.play(Transform(graphstuff,graphtarget))
        self.wait(2)
        info = MathTex(r"g(x)=x+\int_{0}^{x}\!f(t)~dt")
        info.to_corner(UR)
        self.play(Write(info))
        self.wait(2)
        question = MathTex(r"find~g(-2)=",r"3")
        question.next_to(np1,DOWN)
        self.play(Write(question[0]))
        explanation1p1 = MathTex(r"g(x)=x+\int_{0}^{x}\!f(t)~dt")
        explanation1p1.next_to(question,DOWN)
        explanation1p2 = MathTex(r"g(-2)=(-2)+",r"\int_{0}^{-2}\!f(t)~dt")
        explanation1p2.move_to(explanation1p1)
        self.wait(2)
        self.play(Write(explanation1p1))
        self.wait(1)
        self.play(Transform(explanation1p1,explanation1p2))
        self.add(explanation1p2)
        self.remove(explanation1p1)
        self.wait(1)
        box1 = SurroundingRectangle(explanation1p2[1],buff=0.1)
        self.play(Create(box1))
        self.wait(2)