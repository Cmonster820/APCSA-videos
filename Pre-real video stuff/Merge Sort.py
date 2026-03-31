%%manim -qm MergeSort
import random
class MergeSort(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.wait(1)
        title = Text("Merge Sort")
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(1)
        numtable = [3,5,4,8,2,6,7,1]
        table = []
        for num in numtable:
            item = Tex(num)
            square = Square(item.height*1.5)
            group = VGroup(item,square)
            table.append(group)
        table[0].move_to([(-len(table)//2*table[0].width)-table[0].width/2,0,0])
        for i in range(1,len(table)):
            table[i].next_to(table[i-1],buff=0)
        for item in table:
            self.play(Write(item),run_time=0.5)
        divider = Line(start = table[len(table)//2].get_corner(UL), end = table[len(table)//2].get_corner(DL), color = RED)
        self.play(Create(divider))
        subgroup1 = VGroup(*[item for item in table[:len(table)//2]])
        subgroup2 = VGroup(*[item for item in table[len(table)//2:]])
        self.play(subgroup1.animate.shift([-0.5,0,0]),subgroup2.animate.shift([0.5,0,0]),Uncreate(divider))
        divider1 = Line(start = table[len(table)//4].get_corner(UL), end = table[len(table)//4].get_corner(DL), color = RED)
        divider2 = Line(start = table[len(table)*3//4].get_corner(UL), end = table[len(table)*3//4].get_corner(DL), color = RED)
        self.play(Create(divider1),Create(divider2))
        subgroup3 = VGroup(*[item for item in table[:len(table)//4]])
        subgroup4 = VGroup(*[item for item in table[len(table)//4:len(table)//2]])
        subgroup5 = VGroup(*[item for item in table[len(table)//2:len(table)*3//4]])
        subgroup6 = VGroup(*[item for item in table[len(table)*3//4:]])
        self.play(subgroup3.animate.shift([-0.5,0,0]),subgroup6.animate.shift([0.5,0,0]),divider1.animate.shift([-0.25,0,0]),divider2.animate.shift([0.25,0,0]),Uncreate(divider1),Uncreate(divider2))
        dividerslist = [Line(start = item.get_corner(UL), end = item.get_corner(DL), color = RED) for item in table]
        del dividerslist[0::2]
        dividers = VGroup(*dividerslist)
        self.play(*[Create(item) for item in dividerslist])
        self.play(table[0].animate.shift([-1,0,0]),table[1].animate.shift([-0.5,0,0]),table[2].animate.shift([-0.5,0,0]),table[-3].animate.shift([0.5,0,0]),table[-2].animate.shift([0.5,0,0]),table[-1].animate.shift([1,0,0]), *[Uncreate(item) for item in dividerslist])
        self.wait(2)
        boxes = [SurroundingRectangle(item, buff=0.1) for item in [subgroup3,subgroup4,subgroup5,subgroup6]]
        self.play(*[Create(item) for item in boxes])
        self.play(*[Uncreate(item) for item in boxes])
        temp = table[-2].get_center()
        self.play(table[-2].animate.move_to(table[-1]),table[-1].animate.move_to(temp))
        self.wait(1)
        self.play(table[0].animate.shift([1,0,0]),table[1].animate.shift([0.5,0,0]),table[2].animate.shift([0.5,0,0]),table[-3].animate.shift([-0.5,0,0]),table[-1].animate.shift([-0.5,0,0]),table[-2].animate.shift([-1,0,0]))
        boxes = [SurroundingRectangle(item,buff=0.1) for item in [subgroup1,subgroup2]]
        self.play(*[Create(box) for box in boxes])
        self.play(*[Uncreate(box) for box in boxes])
        