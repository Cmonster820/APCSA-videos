%%manim -qh Recursions
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
        code_second.width=code_first.width/2
        code_second.to_edge(LEFT)
        self.play(Transform(code_first,code_second))
        self.add(code_second)
        self.remove(code_first)
        code_third = Code(code_string='''...
        factorial(5);
...''',
                          language="java",
                          formatter_style="monokai")
        code_third.next_to(code_second,RIGHT)
        self.play(Write(code_third))
        self.wait(2)
        self.play(code_third.animate.to_corner(UR))
        squares = []
        answers = [120, 24, 6, 2, 1]
        for i in range(5,0,-1):
            code = Code(code_string=f"factorial({i});",language = "java",formatter_style = "monokai")
            table = MobjectTable( [[code]],
                           include_outer_lines=True)
            table.to_edge(RIGHT)
            squares.append(table)
        for table in squares:
            box = SurroundingRectangle(code_second)
            self.play(Create(box),run_time=0.5)
            self.play(Write(table),run_time=0.5)
            self.play(Uncreate(box),run_time=0.5)
        for i in range(4,0,-1):
            newTable = Table([[str(answers[i])]], include_outer_lines=True)
            self.play(Transform(squares[i],newTable))
            self.add(newTable)
            self.remove(squares[i])
            thing = MathTex(answers[i])
            thing.move_to(newTable)
            self.add(thing)
            self.play(Unwrite(newTable),thing.animate.move_to(code_second))
            self.play(Unwrite(thing))
        answer = MathTex(answers[0])
        self.play(Transform(squares[0],answer))
        self.add(answer)
        self.remove(squares[0])
        self.play(answer.animate.move_to(code_third))
        self.play(Unwrite(answer))
        self.play(FadeOut(code_third),FadeOut(code_second),Unwrite(title))
        self.wait(2)