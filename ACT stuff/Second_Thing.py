#This is a copied cell from a Jupyter notebook, generating this animation outside of the default
#Manim Community quick start notebook, with this pasted at the end, requires actually installing
#Manim Community on your computer and changing the first line to import all the required things
#and then use `manim --quality=h Second_Thing.py ACTThing2` from the terminal to generate the an
#imation. I don't know if ffmpeg automatically goes when manim generates a scene, but I would as
#sume that, since Manim requires ffmpeg (I think).
#I did write all of this, though. I just used the quick start guide Jupyter notebook to generate
#the animation for the slides.
%%manim -qm ACTThing2

class ACTThing2(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait(0.5)
        self.play(Unwrite(banner))