import click
import sys
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from pathlib import Path

console = Console()


def load_words() -> list[str]:
    """Load all words from words.txt file"""

    words = []
    file_name = Path(__file__).parent / "words.txt"
    with open(file_name, "r") as fobj:
        for line in fobj:
            words.append(line.strip())
    return words


def titlescreen():
    """Display the titlescreen and instructions"""

    banner = """
                       ▄▄ ▄▄                   ▄▄     
                       ██ ██                   ██ ▀▀  
██   ██ ▄███▄ ████▄ ▄████ ██ ▄█▀█▄       ▄████ ██ ██  
██ █ ██ ██ ██ ██ ▀▀ ██ ██ ██ ██▄█▀ ▀▀▀▀▀ ██    ██ ██  
 ██▀██  ▀███▀ ██    ▀████ ██ ▀█▄▄▄       ▀████ ██ ██▄
 """
    console.print(
        Panel(
            Align.center(banner),
            title="Welcome to wordle-cli",
            subtitle="Version v0.1.0",
            style="bold white",
            border_style="bright_blue",
            padding=(1, 2),
            height=10,
            width=60,
        )
    )

    console.print("Guess the 5-letter word in 6 tries! \n")
    console.print("🟩 = Correct letter, correct position", style="bold green")
    console.print("🟨 = Correct letter, wrong position", style="bold yellow")
    console.print("⬛ = Wrong letter", style="bold white")
    console.print()


def random_word(word_list: list[str]) -> str:
    """Randomly generates a 5 letter word"""

    rand = random.choice(word_list).upper()
    return rand


def check_match(input: str, output: str) -> list[tuple[str, str]]:
    """Check the matching characters and assigns appropriate colours"""
    status = []

    # Create lists of strings for assigning values
    output_letters = list(output)

    # First loop to check for green characters
    for i in range(5):
        if input[i] == output[i]:
            status.append((input[i], "green"))
            output_letters[i] = ""
        else:
            status.append((input[i], "check"))

    # Second loop to check for yellow or grey characters
    for i in range(5):
        if status[i][1] == "check":
            cur_letter = input[i]
            find_pos = -1

            for j in range(5):
                if cur_letter == output_letters[j]:
                    output_letters[j] = ""
                    find_pos = j
                    break

            if find_pos == -1:
                status[i] = (input[i], "grey")
            else:
                status[i] = (input[i], "yellow")
    return status


def guess_result(result: list[tuple[str, str]]):
    """Display guesses with colour"""
    text = Text()
    for score in result:
        if score[1] == "green":
            text.append(score[0], style="bold black on green")
        if score[1] == "yellow":
            text.append(score[0], style="bold black on yellow")
        if score[1] == "grey":
            text.append(score[0], style="bold black on rgb(74, 74, 74)")
    return text


def generate_scoreboard(total_result: list[list[tuple[str, str]]], attempts: int):
    """Generates a scoreboard like the official Wordle website"""

    score_board = f"Wordle-CLI {attempts}/6\n\n"
    for result in total_result:
        score_text = ""
        for score in result:
            if score[1] == "green":
                score_text += "🟩"
            if score[1] == "yellow":
                score_text += "🟨"
            if score[1] == "grey":
                score_text += "⬛"
        score_board += score_text + "\n"
    return score_board


@click.command()
def play():
    """Play Wordle in your terminal! (random word)"""

    titlescreen()

    word_list = load_words()
    correct_word = random_word(word_list)
    # console.print(correct_word) # Debug the correct word
    total_result = []
    win = False

    for i in range(6):
        count = 0
        while True:
            guess = console.input("Type in your word: ").upper().strip()

            valid_input = True
            message = ""

            # Checking conditions for valid 5 letter word
            if len(guess) != 5:
                valid_input = False
                message = Text("Please enter a 5 letter word", style="bold red")

            elif not (guess.isalpha()):
                valid_input = False
                message = Text("Only contain letters", style="bold red")

            elif guess.lower() not in word_list:
                valid_input = False
                message = Text("Please enter a valid word", style="bold red")

            # If not valid input, cleared last error message
            if not valid_input:
                if count > 0:
                    sys.stdout.write("\033[F")  # Move up
                    sys.stdout.write("\033[K")  # Clear line

                count += 1
                sys.stdout.write("\033[F")  # Move up
                sys.stdout.write("\033[K")  # Clear line
                sys.stdout.flush()
                console.print(message)
                continue
            # Break on valid input
            break

        result = check_match(guess, correct_word)
        total_result.append(result)
        round_score = guess_result(result)

        console.print(round_score)

        for check in result:
            if check[1] != "green":
                break
        else:
            win = True
            console.print(
                f"[bold green]You Win![/], number of guesses: [bold red]{i+1}/6[/]"
            )
            break

    if not win:
        console.print("Better luck next time!", style="bold red")
        console.print(f"The word was: [bold green]{correct_word}[/]")

    score_board = generate_scoreboard(total_result, len(total_result))
    console.print(
        Panel(
            Align.center(score_board),
            title="Your Score",
            style="bold white",
            border_style="bright_blue",
            height=13,
            width=20,
            padding=(1, 2),
        )
    )


@click.group()
def cli():
    """Wordle CLI - Guess the 5-letter word!"""
    pass


cli.add_command(play)
if __name__ == "__main__":
    cli()
