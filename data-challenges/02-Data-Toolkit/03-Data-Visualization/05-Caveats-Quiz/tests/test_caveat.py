# pylint: disable-all

import unittest
from quiz import question_bar_plot, question_line_plot, \
    question_bar_plot_columns, question_color_uses, question_color_palette, \
    question_color_blind_palette, question_diverging_color_palette


class TestCaveatQuiz(unittest.TestCase):

    def test_question_bar_plot(self):
        # Question:
        # With a bar plot you should ALWAYS...
        possible_answers = [
            "Set the start of the Y-axis at zero",
            # "Set the start of the Y-axis closest to the minimal value of my bars"
        ]
        self.assertEqual(question_bar_plot(), possible_answers)

    def test_question_line_plot(self):
        # Question:
        # With a line plot I should...

        possible_answers = [
            # "Never start the Y-axis at zero",
            "Experiment and find the most relevant start value for the Y-axis",
            # "Always keep the start of the Y-axis at zero"
        ]
        self.assertEqual(question_line_plot(), possible_answers)

    def test_question_bar_plot_columns(self):
        # Question:
        # In general, bar plots with 10+ columns are simpler to read...

        possible_answers = [
            "With columns name on the y axis",
            # "With columns name on the x axis",
            # "With columns having a unique color."
        ]
        self.assertEqual(question_bar_plot_columns(), possible_answers)

    def test_question_color_uses(self):
        # Question:
        # I can use color...

        possible_answers = [
            "To show groups",
            "To highlight an item",
            "To represent a value",
        ]
        self.assertEqual(question_color_uses(), possible_answers)

    def test_question_color_palette(self):
        # Question:
        # I should never use...

        possible_answers = [
            "rainbow color palette",
            # "Bi-hues color palette",
            # "Mono-hue color palette",
        ]
        self.assertEqual(question_color_palette(), possible_answers)

    def test_question_color_blind_palette(self):
        # Question:
        # For color blind people, I should choose these color palettes...

        possible_answers = [
            "Blue and yellow",
            # "Red and green",
            # "Red and yellow",
            "Blue and red"
        ]
        self.assertEqual(question_color_blind_palette(), possible_answers)

    def test_question_diverging_color_palette(self):
        # Question:
        # If you want to emphasize how a variable diverts from a baseline...

        possible_answers = [
            # "You should use a mono-hue color gradient",
            "You should use a diverging color gradient"
        ]
        self.assertEqual(question_diverging_color_palette(), possible_answers)
