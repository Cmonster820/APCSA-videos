%%manim -qh IndefiniteIntegralCalc
class IndefiniteIntegralCalc(Scene):
    def construct(self):
        button_shape = RoundedRectangle(height = 3.0, width = 8.0)
        button_divider = Line(start = [0,1.5,0], end = [0,-1.5,0])
        button_label_left = MathTex(r"\left| \square \right| \begin{cases} \square \\ \square \end{cases}")
        button_label_left.move_to([-2,0,0])
        button_label_right = Text("🕮",font_size = 128)
        button_label_right.move_to([2,0,0])
        button = VGroup(button_shape,button_divider,button_label_left,button_label_right)
        self.play(Write(button), run_time=2)
        self.wait(1)
        highlight = SurroundingRectangle(button_label_left,buff = 0.1)
        self.play(Create(highlight))
        self.play(Uncreate(highlight))
        menu = MathTable(
            [[r"\mathrm{I'm}",r"\mathrm{not}",r"\mathrm{making}",r"\mathrm{this}",r"\mathrm{whole}",r"\mathrm{menu}",r"\mathrm{and}",r"\mathrm{you}",r"\mathrm{can't}",r"\mathrm{make}",r"\mathrm{me}"],
             [r"-",r"-",r"-",r"-",r"-",r"\sum_{\square = \square}^{\square} \square", r"\prod_{\square = \square}^{\square} \square", r"\frac{\mathrm{d}}{\mathrm{d}\square}\square",r"\frac{\mathrm{d}^2}{\mathrm{d}\square}\square",r"\frac{\mathrm{d}^n}{\mathrm{d}\square}\square",r"\int_{\square}^{\square}\square \mathrm{d}\square"],
             [r"\int\square\mathrm{d}\square",r"\lim_{\square \to \square} \square",r"\square_{\square}",r"-",r"-", r"-", r"-", r"-", r"-", r"-", r"-"]],
            include_outer_lines = True
        )
        menu.width = 14
        self.play(Unwrite(button))
        self.play(Write(menu))
        self.wait(2)
        thing = menu.get_entries((3,1)).copy()
        newmenu = menu.copy()
        newmenu.add_highlighted_cell((3,1), color = BLUE)
        self.play(FadeIn(newmenu),FadeOut(menu))
        self.wait(1)
        self.add(thing)
        self.play(FadeOut(newmenu))
        self.play(thing.animate.move_to(ORIGIN).scale(2))
        self.wait(2)
        self.play(Unwrite(thing))
        self.wait(2)