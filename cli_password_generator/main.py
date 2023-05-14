import random
import string

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


class PasswordGenerator:
    """Class for generating passwords."""

    def __init__(self, length: int, use_symbols: bool, use_numbers: bool):
        self.length = length
        self.use_symbols = use_symbols
        self.use_numbers = use_numbers

        self.character_pool = ""
        self.password = ""

        self.generate_character_pool()

    def generate_character_pool(self):
        """Generate the pool of characters to choose from for the password."""
        lowercase_letters = string.ascii_lowercase
        numbers = string.digits
        symbols = string.punctuation

        if self.use_numbers:
            self.character_pool += numbers
        else:
            self.length += len(numbers)

        if self.use_symbols:
            self.character_pool += symbols
        else:
            self.length += len(symbols)

        self.character_pool += lowercase_letters

    def generate_password(self):
        """Generate the password."""
        password = "".join(random.sample(self.character_pool, self.length))
        self.password = password


@app.command()
def generate(
    length: int = typer.Option(12, prompt=True, show_default=True),
    use_symbols: bool = typer.Option(True, prompt=True, show_default=True),
    use_numbers: bool = typer.Option(True, prompt=True, show_default=True),
):
    """Generate a random password."""
    generator = PasswordGenerator(length, use_symbols, use_numbers)
    try:
        generator.generate_password()
        console.print(f"Generated password: [bold]{generator.password}[/bold]")
    except ValueError as error:
        console.print(f"[bold red]Error: {error}[/bold red]")


if __name__ == "__main__":
    app()
