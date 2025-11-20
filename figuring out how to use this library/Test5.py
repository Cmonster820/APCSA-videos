#Objective: create a Code Mobject, with one of the lines hidden, then write that line in
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h Test5
import copy
class Test5(Scene):
    def construct(self):
        code_string_complete = '''public class MyProgram
{
    public static void main(String[] args)
    {
        System.out.println("Hello, world!");
    }
}'''
        code_string_incomplete = '''public class MyProgram
{
    public static void main(String[] args)
    {
        
    }
}'''
        incomplete = Code(
            code_string=code_string_incomplete, tab_width=4, paragraph_config=dict(font="Monospace"), language = "java", add_line_numbers=True,
            formatter_style='github-dark'
        )
        complete = Code(
            code_string=code_string_complete, tab_width=4, paragraph_config=dict(font="Monospace"), language = "java", add_line_numbers=True,
            formatter_style='github-dark'
        )
        extra = complete.code_lines[4]
        complete.width = 11
        incomplete.width = 11
        #incomplete.height = complete.height
        self.play(Write(complete))
        self.remove(extra)
        self.wait(2)
        self.play(Write(extra))
        self.wait(2)