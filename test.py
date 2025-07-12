import os
from pathlib import Path
os.system("cls")
path = Path("C:\\My_Coding_Projects\My_Practice_With_Python\\basic_games_and_applications_(simple_projects)\\recipe_book\\recipes")
for paths in path.glob("Dessert/*.txt"):
    print(paths)