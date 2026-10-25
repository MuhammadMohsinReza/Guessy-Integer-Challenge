import random
import math
import sys
import time
from statistics import mode

# Added by AI
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
LIGHT_GREEN = "\033[38;2;144;238;144m"
YELLOWISH_BLUE = "\033[38;2;138;184;216m"
LAVA = "\033[38;2;255;69;0m"

# Added by AI
def color_text(text, color):
    return f"{color}{text}{RESET}"

# Added by AI
def play_intro_animation():
    colors = [CYAN, YELLOWISH_BLUE, LIGHT_GREEN, YELLOW]
    logo = [
        r"   ____ _   _ _____ ____ ____  __ ",
        r"  / ___| | | | ____/ ___/ ___|/ _|",
        r" | |  _| | | |  _| \___ \___ \ |_ ",
        r" | |_| | |_| | |___ ___) |__) |  _|",
        r"  \____|\___/|_____|____/____/|_| ",
    ]
    print()
    sys.stdout.write("\033[s\033[?25l")
    try:
        for frame in range(18):
            sys.stdout.write("\033[u")
            color = colors[frame % len(colors)]
            for line in logo:
                sys.stdout.write(f"  {color_text(line, color)}\033[K\n")
            progress = min(frame * 6, 100)
            filled = progress // 5
            bar = "#" * filled + "-" * (20 - filled)
            sys.stdout.write(
                f"  {color_text('INITIALIZING', CYAN)} "
                f"[{color_text(bar, color)}] {progress:3d}%\033[K\n"
            )
            sys.stdout.flush()
            time.sleep(0.055)
    finally:
        sys.stdout.write("\033[u")
        for _ in range(len(logo) + 1):
            sys.stdout.write("\033[2K\n")
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
    print(color_text("  *** GUESSY INTEGER CHALLENGE ***", CYAN))
    print()

# Added by AI
def play_confetti_animation():
    confetti_colors = [RED, YELLOW, GREEN, CYAN, LIGHT_GREEN, YELLOWISH_BLUE]
    width, height = 56, 16
    particles = []
    burst_symbols = ["*", "+", "x", ".", "o"]
    print()
    sys.stdout.write("\033[s\033[?25l")
    try:
        for frame_number in range(52):
            if frame_number % 13 == 0:
                center_x = random.randint(8, width - 9)
                center_y = random.randint(3, 7)
                for _ in range(34):
                    angle = random.uniform(0, 6.283)
                    speed = random.uniform(0.25, 0.95)
                    particles.append({
                        "x": float(center_x),
                        "y": float(center_y),
                        "dx": speed * math.cos(angle),
                        "dy": speed * math.sin(angle),
                        "life": random.randint(9, 17),
                        "symbol": random.choice(burst_symbols),
                        "color": random.choice(confetti_colors),
                    })

            frame = [[" "] * width for _ in range(height)]
            for particle in particles:
                row = int(particle["y"])
                column = int(particle["x"])
                if particle["life"] > 0 and 0 <= row < height and 0 <= column < width:
                    frame[row][column] = color_text(
                        particle["symbol"], particle["color"]
                    )
                particle["x"] += particle["dx"]
                particle["y"] += particle["dy"]
                particle["dy"] += 0.045
                particle["life"] -= 1

            sys.stdout.write("\033[u")
            for row in frame:
                sys.stdout.write("  " + "".join(row) + "\033[K\n")
            sys.stdout.flush()
            time.sleep(0.06)
    finally:
        sys.stdout.write("\033[u")
        for _ in range(height):
            sys.stdout.write("\033[2K\n")
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

    print(color_text("  +--------------------------------------------------+", GREEN))
    print(color_text("  |             YOU ARE THE GUESS MASTER!            |", GREEN))
    print(color_text("  +--------------------------------------------------+", GREEN))
    print()

# Added by AI
def play_lose_animation():
    frames = [
        (YELLOW, "  SIGNAL LOST..."),
        (RED, "  GUESS COUNTER: 0"),
        (LAVA, "  THE MYSTERY NUMBER ESCAPED!"),
        (RED, "  +----------------------------+"),
        (RED, "  |       GAME OVER :(         |"),
        (RED, "  +----------------------------+"),
    ]
    print()
    for color, message in frames:
        sys.stdout.write(f"\r\033[2K{color_text(message, color)}")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")


num1 = 1
num2 = 100
random_number = random.randint(num1, num2)
guess_count = 0
save_mode = "Not Selected Yet"
status = "In-Progress"
dateandtime = time.strftime("%d-%m-%Y %I:%M %p")
winning_messages = [
        "Congrats! You guessed the number!",
        "Correct Guess! You Won!",
        "You're a Guess Master! Welldone! You answer is Right!",
        f"The correct number was {random_number}! You guessed it right!"
]
high_messages = [
    "Too high!",
    "You guessed too high!",
    "Your thoughts and guesses are a little higher!",
    "Calm down! The number is smaller than what you guessed!"
]
low_messages = [
    "Too low!",
    "You guessed too low!",
    "Your thoughts and guesses are a little lower! Believe in yourself!",
    "Think Big! The number is greater than what you guessed!"
]
lose_messages = [
    f"Oopsie! You lose! {random_number} was the correct answer.",
    f"Practice more, then try again! The random number was {random_number}.",
    f"Sorry to say, but, you lost the game! The correct answer was {random_number}.",
    f"Looks like you're out of guesses! Here's the answer: {random_number}"
]

# Code Code Code Code Code Code Code Code Code Code

play_intro_animation()
print()
print(color_text('Welcome to the "GUESSY INTEGER CHALLENGE" !', CYAN))
print()
print(f"You will guess a number between {num1} and {num2}.")
player_name = input("Tell us your name first: ")

print("Thanks! Now choose the difficulty according to your status:-")
difficulty = input("easy, Medium or HARD: ").lower()
if difficulty == "easy":
    mode = color_text("easy", LIGHT_GREEN)
    save_mode = "easy"
    guess_count = 10
elif difficulty == "medium":
    mode = color_text("Medium", YELLOWISH_BLUE)
    save_mode = "Medium"
    guess_count = 7
elif difficulty == "hard":
    mode = color_text("HARD", LAVA)
    save_mode = "HARD"
    guess_count = 5

print()
print(f"{mode} mode activated! You'll have {guess_count} guesses!")
print()
print("Let the Game Begin!!!")

for countdown in range(3, 0, -1):
    print(color_text(f"{countdown}...", CYAN))
    time.sleep(1)
print(color_text("Go!", GREEN))
print()

while guess_count > 0:
    guessed_number = int(input("Guess a number: "))
    guess_count -= 1
    if guessed_number == random_number:
        print()
        play_confetti_animation()
        print(color_text(random.choice(winning_messages), GREEN))
        print(color_text("Thanks for playing! Can't wait to see you winning again!", CYAN))
        status = "Win"
        break
    elif guessed_number > random_number:
        print(color_text(random.choice(high_messages), RED))
    elif guessed_number < random_number:
        print(color_text(random.choice(low_messages), YELLOW))
else:
    play_lose_animation()
    if abs(guessed_number - random_number) <= 5:
        print()
        print(color_text(f"You were sooooo close! {random_number} was the correct answer.", YELLOW))
        print(color_text("Thanks for playing! Goodbye!", CYAN))
        status = "Close Lose"
    else:
        print()
        print(color_text(random.choice(lose_messages), RED))
        print(color_text("Thanks for playing! Goodbye!", CYAN))
        status = "Lose"

# Saving the player names in a file called Guessy Integer Challenge players.txt
with open("Guessy Integer Challenge players.txt", "a") as file:  # "a" is used for append
    file.write("Name: " + player_name + " || " + dateandtime + " || " + save_mode + " - " + status + "\n")  # "/n" is used to add a separate line