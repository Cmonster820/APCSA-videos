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
        numtable = [i for i in range(1,9)]
        random.shuffle(numtable)
        table = []
        for num in numtable:
            item = Tex(num)
            square = Square(item.height*1.5)
            group = VGroup(item,square)
            table.append(group)
        table[0].move_to([-len(table)//2*table[0].width,0,0])
        for i in range(1,len(table)):
            table[i].next_to(table[i-1],buff=0)
        for item in table:
            self.play(Write(item),run_time=0.5)
        