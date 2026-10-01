from random import choice

from pyfiglet import figlet_format
from rich import print
from rich.panel import Panel

with open("citations.txt", "r", encoding="utf-8") as f:
    citations = f.readlines()

citations = [c.strip() for c in citations]
citation, auteur = choice(citations).rsplit(" - ", 1)

print(figlet_format("Citation du jour"))

print(
    Panel(
        f"[italic gold1]{citation} »[/italic gold1]",
        title=auteur,
        border_style="gold1",
        expand=False,
    )
)