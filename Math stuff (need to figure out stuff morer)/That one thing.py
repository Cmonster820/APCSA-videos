#intention: figure out how I want to style this stuff
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h big10FTC
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
        question = MathTex(r"")