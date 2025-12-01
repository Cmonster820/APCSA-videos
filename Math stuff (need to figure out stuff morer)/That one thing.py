#intention: figure out how I want to style this stuff
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h big10FTC
class big10FTC(Scene):
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
        self.wait(1)
        self.play(Create(graph1))
        self.wait(2)