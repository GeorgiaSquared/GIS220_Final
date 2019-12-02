"""
Final Project
Georgia Mackay ITN160-401
11/11/19
v1
"""

# Variables
# Decision Structures
# Repetition Structures
# Functions
# GUI's
# Lists / Dictionaries / File Streaming / A library or module not covered as a part of the class.

from guizero import *


def main():
    progress = App(title="Progress Bar", width=300, height=200, layout="grid")
    Text(progress, text="Loading", grid=[1, 1])
    progress_bar = Waffle(progress, height=1, width=10, pad=0, grid=[1, 2])
    progress_perc = Text(progress, text="XX%", grid=[2, 2])

    # Padding
    Text(progress, text=" " * 8, grid=[0, 0])

    progress.display()


main()
