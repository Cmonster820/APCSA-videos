#Objective: create a Code Mobject, with one of the lines hidden, then write that line in
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h Test5
class Test5(Scene):
    def construct(self):
        code_string_complete = '''public class MyProgram
{
    public static void main(String[] args)
    {
        System.out.println("Hello, world!");
    }
}'''
        complete = Code(
            code_string=code_string_complete, tab_width=4, paragraph_config=dict(font="Monospace"), language = "java", add_line_numbers=True,
            formatter_style='github-dark'
        )
        extra = complete.code_lines[4].copy()
        complete.width = 11
        self.play(Write(complete),Unwrite(complete.code_lines[4]))
        self.wait(2)
        self.play(Write(extra))
        self.wait(4)
        self.play(Unwrite(extra))
        self.play(FadeOut(complete))
        self.wait(2)