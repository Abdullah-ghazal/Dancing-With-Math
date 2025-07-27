from manim import *
import numpy as np

class LinearTransformationBasics(Scene):
    def construct(self):
        title = Title("Linear Transformation of Basis")
        self.play(Write(title))

        subtitle = Text("Scalar Transformation | Shearing | Rotation | Reflection", font_size=28)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Grid and Vector Setup
        grid = NumberPlane(x_range=[-5, 5], y_range=[-5, 5], background_line_style={"stroke_opacity": 0.4})
        self.play(Create(grid))

        origin = Dot(point=ORIGIN, color=YELLOW)
        vec = Arrow(ORIGIN, [2, 1, 0], color=BLUE, buff=0)
        label = MathTex(r"\vec{v} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}").next_to(vec.get_end(), RIGHT)
        self.play(GrowArrow(vec), Write(origin), Write(label))
        self.wait(1)

        # Transformation 1: Scalar
        self.scalar_transform(vec, label, grid)

        # Transformation 2: Shearing
        self.shear_transform(vec, label, grid)

        # Transformation 3: Rotation
        self.rotation_transform(vec, label, grid)

        # Transformation 4: Reflection
        self.reflection_transform(vec, label, grid)

    def scalar_transform(self, vec, label, grid):
        self.play(FadeOut(label))
        scalar_label = Text("1. Scalar Transformation", font_size=30).to_edge(UP)
        self.play(Write(scalar_label))
        self.wait(0.5)

        scalar_matrix = np.array([[2, 0], [0, 2]])
        matrix_tex = MathTex(r"A = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}", font_size=36).to_corner(UL)
        self.play(Write(matrix_tex))

        self.play(vec.animate.apply_matrix(scalar_matrix), run_time=2)
        new_label = MathTex(r"A\vec{v} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}").next_to(vec.get_end(), RIGHT)
        self.play(Write(new_label))
        self.wait(1.5)

        self.play(FadeOut(new_label), FadeOut(scalar_label), FadeOut(matrix_tex))
        self.reset_vector(vec)

    def shear_transform(self, vec, label, grid):
        shear_label = Text("2. Shearing", font_size=30).to_edge(UP)
        self.play(Write(shear_label))
        self.wait(0.5)

        shear_matrix = np.array([[1, 1], [0, 1]])
        matrix_tex = MathTex(r"A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}", font_size=36).to_corner(UL)
        self.play(Write(matrix_tex))

        self.play(vec.animate.apply_matrix(shear_matrix), run_time=2)
        new_label = MathTex(r"A\vec{v} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}").next_to(vec.get_end(), RIGHT)
        self.play(Write(new_label))
        self.wait(1.5)

        self.play(FadeOut(new_label), FadeOut(shear_label), FadeOut(matrix_tex))
        self.reset_vector(vec)

    def rotation_transform(self, vec, label, grid):
        rotation_label = Text("3. Rotation (90° Counter-Clockwise)", font_size=30).to_edge(UP)
        self.play(Write(rotation_label))
        self.wait(0.5)

        theta = np.pi / 2
        rot_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        matrix_tex = MathTex(r"A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}", font_size=36).to_corner(UL)
        self.play(Write(matrix_tex))

        self.play(vec.animate.apply_matrix(rot_matrix), run_time=2)
        new_label = MathTex(r"A\vec{v} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}").next_to(vec.get_end(), RIGHT)
        self.play(Write(new_label))
        self.wait(1.5)

        self.play(FadeOut(new_label), FadeOut(rotation_label), FadeOut(matrix_tex))
        self.reset_vector(vec)

    def reflection_transform(self, vec, label, grid):
        reflect_label = Text("4. Reflection across y-axis", font_size=30).to_edge(UP)
        self.play(Write(reflect_label))
        self.wait(0.5)

        reflect_matrix = np.array([[-1, 0], [0, 1]])
        matrix_tex = MathTex(r"A = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}", font_size=36).to_corner(UL)
        self.play(Write(matrix_tex))

        self.play(vec.animate.apply_matrix(reflect_matrix), run_time=2)
        new_label = MathTex(r"A\vec{v} = \begin{bmatrix} -2 \\ 1 \end{bmatrix}").next_to(vec.get_end(), LEFT)
        self.play(Write(new_label))
        self.wait(2)

        self.play(FadeOut(new_label), FadeOut(reflect_label), FadeOut(matrix_tex))

    def reset_vector(self, vec):
        self.play(Transform(vec, Arrow(ORIGIN, [2, 1, 0], color=BLUE, buff=0)), run_time=1.5)
