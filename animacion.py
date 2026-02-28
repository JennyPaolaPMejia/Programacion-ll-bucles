from manim import *
import math
import sys
x_final = float(sys.argv[-2])
rc = int(sys.argv[-1])

class GraficaTaylor(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, x_final],
            y_range=[-2, 2],
        )
        grafica = axes.plot(
            lambda x: math.sin(x),
            x_range=[0, x_final],
            color=YELLOW
        )
        punto = Dot(
            axes.coords_to_point(x_final, math.sin(x_final)),
            color=RED
        )
        texto = Text(f"x={x_final}  rc={rc}").scale(0.5).to_edge(UP)
        self.play(Create(axes))
        self.play(Create(grafica), run_time=3)
        self.play(FadeIn(punto))
        self.play(Write(texto))
        self.wait()