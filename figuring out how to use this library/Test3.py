#intention: draw code to the screen, then do syntax highlighting, then fade out
import manim as mn
from manim import *
config.media_width = "75%"
config.verbosity = "WARNING"
print(mn.__version__)
manim --quality=h Test2
import copy
class Test3(Scene):
    def construct(self):
        example = '''public class Example1
{
    public static String[] sortStrs(String[] toSort)
    {
        boolean sorted = false;
        while (!sorted) {
            for (int i = 0; i < toSort.length-1; i++) {
                if (toSort[i].compareTo(toSort[i+1])>0) {
                    String temp = toSort[i];
                    toSort[i] = toSort[i+1];
                    toSort[i+1] = temp;
                }
            }
            for (int i = 0; i < toSort.length-1; i++) {
                if (toSort[i].compareTo(toSort[i+1])>0)
                    break;
                if (i == toSort.length-2)
                    sorted = true;
            }
        }
        for (int i = 0; i < toSort.length-1; i++) {
            if (toSort[i]==toSort[i+1])
                toSort[i] = "";
        }
        return toSort 
    }
}'''
        highlighted = Code(
            code_string=example, tab_width=4,
            language="Java", paragraph_config=dict(font="Monospace")
        )
        unhighlighted = Text(example)
        self.play(Write(unhighlighted))
        self.wait(2)
        self.play(Transform(unhighlighted,highlighted))
        self.wait(2)