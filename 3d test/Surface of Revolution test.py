#Intention: figure out how to do 3D
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h SurfaceOfRevolution
class SurfaceOfRevolution(Scene):
    def construct(self):