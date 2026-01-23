#Intention: figure out how to do 3D
import manim as mn
from manim import *
import numpy as np
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
%%manim -qm SurfaceOfRevolution

class SurfaceOfRevolution(ThreeDScene):
    def surface1(self, u, v):
        return np.array([
                u,
                (u) * np.cos(v),
                (u) * np.sin(v)
            ])
    def surface2(self, u, v):
        return np.array([
            u,
            (u**2) * np.cos(v),
            (u**2) * np.sin(v)
            ])
    def surface3(self, u, v):
        return np.array([
            u,
            (u-(u**2)) * np.cos(v),
            (u-(u**2)) * np.sin(v)
            ])
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        axes = ThreeDAxes(
            x_range=(-2,2,1),
            y_range=(-2,2,1),
            z_range=(-2,2,1)
        )
        surface = Surface(
            lambda u, v: axes.c2p(*self.surface1(u,v)),
            u_range=[0, 1],
            v_range=[0, TAU],
            resolution=20,
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E]
        )
        self.add(axes)
        self.play(Create(surface))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(1)
        surface2 = Surface(
            lambda u, v: axes.c2p(*self.surface2(u,v)),
            u_range = [0,1],
            v_range = [0,TAU],
            resolution = 20,
            fill_opacity = 0.7,
            checkerboard_colors = [YELLOW_D,YELLOW_E]
        )
        self.play(Create(surface2))
        self.wait(4)
        surface3 = Surface(
            lambda u, v: axes.c2p(*self.surface3(u, v)),
            u_range = [0,1],
            v_range = [0,TAU],
            resolution = 20,
            fill_opacity = 0.7,
            checkerboard_colors = [BLUE_D,BLUE_E]
        )
        self.play(Uncreate(surface),Uncreate(surface2),Create(surface3))
        self.wait(5)