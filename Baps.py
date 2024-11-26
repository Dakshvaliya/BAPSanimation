from manim import *

class BAPSLogoAnimation(Scene):
    def construct(self):
        # Define colors
        gray = "#808080"  # Gray background
        red = "#FF0000"   # Red circle
        gold = "#FFD700"  # Gold U-shape
        black = "#808080" # Black text

        # Create the main symbol
        symbol = VGroup()

        # Top portion
        top = Line(start=[-3, 2, 0], end=[3, 2, 0], color=black, stroke_width=6)
        flag = Triangle(color=black, fill_opacity=1).scale(0.2).next_to(top, UP, buff=0)
        top_decoration = VGroup(
            Line(start=[-2.5, 2, 0], end=[-2.5, 2.5, 0], color=black, stroke_width=6),
            Line(start=[-1.5, 2, 0], end=[-1.5, 2.5, 0], color=black, stroke_width=6),
            Line(start=[1.5, 2, 0], end=[1.5, 2.5, 0], color=black, stroke_width=6),
            Line(start=[2.5, 2, 0], end=[2.5, 2.5, 0], color=black, stroke_width=6),
        )
        symbol.add(top, flag, top_decoration)

        # Middle portion (Corrected U-shape)
        u_shape = VGroup(
            Line(start=[-1, 1.8, 0], end=[-1, -0.5, 0], color=gold, stroke_width=10),
            ArcBetweenPoints(start=[-1, -0.4, 0], end=[1, -0.4, 0], angle=PI, color=gold, stroke_width=10),  # Changed angle to PI
            Line(start=[1, -0.5, 0], end=[1, 1.8, 0], color=gold, stroke_width=10)
            
        )
        circle = Circle(radius=0.5, color=red, fill_opacity=1).move_to(u_shape.get_center())
        symbol.add(u_shape, circle)

        # Bottom portion
        bottom = Line(start=[-3, -1, 0], end=[3, -1, 0], color=WHITE, stroke_width=6)
        bottom_decoration = VGroup(
            Line(start=[-2.5, -0.8, 0], end=[-2.5, -1.3, 0], color=black, stroke_width=6),
            Line(start=[-1.5, -0.8, 0], end=[-1.5, -1.3, 0], color=black, stroke_width=6),
            Line(start=[1.5, -0.8, 0], end=[1.5, -1.3, 0], color=black, stroke_width=6),
            Line(start=[2.5, -0.8, 0], end=[2.5, -1.3, 0], color=black, stroke_width=6),
        )
        symbol.add(bottom, bottom_decoration)

        # Create the text (Using a different font that supports Sanskrit)
        sanskrit_text = Text("स्वामिनारायण", font="Arial", color=WHITE).scale(0.8).next_to(symbol, DOWN, buff=0.2)
        baps_text = Text("BAPS", font="Arial", color=WHITE, weight=BOLD).scale(1.2).next_to(sanskrit_text, DOWN, buff=0.1)

        # Animations
        self.play(
            LaggedStart(
                Create(top),
                Create(flag),
                Create(top_decoration),
                Create(u_shape),
                Create(circle),
                Create(bottom),
                Create(bottom_decoration),
                lag_ratio=0.2
            )
        )
        self.play(Write(sanskrit_text))
        self.play(Write(baps_text))

        # Center the entire logo
        logo = VGroup(symbol, sanskrit_text, baps_text)
        self.play(logo.animate.move_to(ORIGIN)) 

        self.wait(1)