%%manim -qm Recursions
class Recursions(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.wait(1)
        title = Text("Recursion")
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        code_first = Code(code_string='''...
    public static int factorial(int n) {
        if (n==1)
            return 1;
        return n*factorial(n-1);
    }
...''',
        language="java",
        formatter_style="monokai")
        code_second = Code(code_string='''...
    public static int factorial(int n) {
        return n==1?1:n*factorial(n-1);
    }
...''',
        language='java',
        formatter_style='monokai')
        self.play(Write(code_first))
        self.wait(2)
        code_second.height=code_first.height*(3/4)
        code_second.to_edge(LEFT)
        self.play(Transform(code_first,code_second))
        self.add(code_second)
        self.remove(code_first)