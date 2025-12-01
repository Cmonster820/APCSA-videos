#intention: figure out how I want to style this stuff
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h big10FTC
class big10FTC(scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.wait(2)
        np = NumberPlane()