import os
from manim import *

class BAPSLogoAnimationBlack(Scene):
    def construct(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__)) 

        # Construct the relative path to the SVG (assuming it's in the same directory)
        svg_path = os.path.join(script_dir, "White_Logo.svg")  

        # Load the SVG file
        logo = SVGMobject(svg_path)

        # Center the logo
        logo.move_to(ORIGIN)

        # Scale the logo to twice its size
        logo.scale(2)

        # Animate each submobject with color fill
        self.play(LaggedStart(*[DrawBorderThenFill(submobject) for submobject in logo.submobjects], lag_ratio=0.1))

        # Scale down the logo to 0.5 of its size
        self.play(logo.animate.scale(0.2))  

        # Move the logo to the bottom right corner
        self.play(logo.animate.to_corner(DR)) 

        # Keep the logo visible indefinitely
        self.wait(3)

class BAPSLogoAnimationWhite(Scene):
    def construct(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__)) 

        # Construct the relative path to the SVG (assuming it's in the same directory)
        svg_path = os.path.join(script_dir, "Logo_Black.svg")  

        # Load the SVG file
        logo = SVGMobject(svg_path)

        # Center the logo
        logo.move_to(ORIGIN)

        # Scale the logo to twice its size
        logo.scale(2)

        # Animate each submobject with color fill
        self.play(LaggedStart(*[DrawBorderThenFill(submobject) for submobject in logo.submobjects], lag_ratio=0.1))

        # Scale down the logo to 0.5 of its size
        self.play(logo.animate.scale(0.2))  

        # Move the logo to the bottom right corner
        self.play(logo.animate.to_corner(DR)) 

        # Keep the logo visible indefinitely
        self.wait(3)