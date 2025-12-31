"""Command-line menu for launching project stubs.

Option 1 now launches a playable Tic Tac Toe game against a simple AI.
The menu continues to loop until the user chooses to exit.
"""

from __future__ import annotations


PROJECTS = {
    "1": "Tic Tac Toe (vs AI)",
    "2": "Report Generator",
    "3": "Dashboard Builder",
    "4": "Model Training",
    "5": "Exit",
}


def display_menu() -> None:
    """Print the numbered project menu."""

    print("Select a project to run:\n")
    for key, name in PROJECTS.items():
        print(f" {key}. {name}")
    print()


def display_board(board: list[str]) -> None:
    """Print the current state of the Tic Tac Toe board."""

    grid = "\n---+---+---\n"
    rows = [" | ".join(board[i : i + 3]) for i in range(0, 9, 3)]
    print(f"\n{grid.join(rows)}\n")


def winning_lines() -> list[tuple[int, int, int]]:
    """Return all index combinations that constitute a winning line."""

    return [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]


def find_winner(board: list[str]) -> str | None:
    """Return 'X' or 'O' if either player has won, or None otherwise."""

    for a, b, c in winning_lines():
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def available_moves(board: list[str]) -> list[int]:
    """Return a list of open board indices."""

    return [idx for idx, cell in enumerate(board) if cell == " "]


def find_finishing_move(board: list[str], marker: str) -> int | None:
    """Find a winning move for the given marker, if it exists."""

    for idx in available_moves(board):
        trial = board.copy()
        trial[idx] = marker
        if find_winner(trial) == marker:
            return idx
    return None


def choose_ai_move(board: list[str], ai_marker: str, human_marker: str) -> int:
    """Pick a move for the AI with basic strategy and fallback to first open."""

    winning_move = find_finishing_move(board, ai_marker)
    if winning_move is not None:
        return winning_move

    blocking_move = find_finishing_move(board, human_marker)
    if blocking_move is not None:
        return blocking_move

    preferred_spaces = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for idx in preferred_spaces:
        if board[idx] == " ":
            return idx

    # This should never occur because preferred_spaces covers all cells, but keep a safe fallback.
    return available_moves(board)[0]


def prompt_human_move(board: list[str]) -> int:
    """Prompt the human player for a valid board position."""

    while True:
        choice = input("Choose your move (1-9): ").strip()
        if not choice.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        position = int(choice) - 1
        if position not in range(9):
            print("Move must be between 1 and 9.")
            continue
        if board[position] != " ":
            print("That spot is already taken. Try again.")
            continue
        return position


def run_tic_tac_toe() -> None:
    """Play an interactive Tic Tac Toe game against a basic AI opponent."""

    board = [" "] * 9
    current = "X"  # Human starts first as X

    print("You are X. The AI is O. Enter positions using numbers 1-9.")
    display_board(board)

    while True:
        if current == "X":
            move = prompt_human_move(board)
        else:
            move = choose_ai_move(board, "O", "X")
            print(f"AI chooses position {move + 1}.")

        board[move] = current
        display_board(board)

        winner = find_winner(board)
        if winner:
            print(f"{winner} wins!\n")
            return

        if not available_moves(board):
            print("It's a tie!\n")
            return

        current = "O" if current == "X" else "X"


def run_data_cleaning() -> None:
    print("Starting the data cleaning pipeline...")
    print("- Loading raw data")
    print("- Removing duplicates")
    print("- Imputing missing values\n")


def run_report_generator() -> None:
    print("Generating reports...")
    print("- Aggregating metrics")
    print("- Exporting PDF and CSV outputs\n")


def run_dashboard_builder() -> None:
    print("Building dashboard...")
    print("- Fetching analytics data")
    print("- Rendering charts and tables\n")


def run_model_training() -> None:
    print("Training model...")
    print("- Splitting dataset")
    print("- Fitting and evaluating model\n")


def handle_choice(choice: str) -> bool:
    """Carry out the action associated with a menu choice.

    Returns True when the loop should continue, or False to exit.
    """

    actions = {
        "1": run_tic_tac_toe,
        "2": run_report_generator,
        "3": run_dashboard_builder,
        "4": run_model_training,
    }

    if choice not in PROJECTS:
        print("Invalid selection. Please choose a number from the menu.\n")
        return True

    if choice == "5":
        print("Exiting. Goodbye!")
        return False

    print(f"Launching: {PROJECTS[choice]}\n")
    actions[choice]()
    return True


def main() -> None:
    """Run the interactive menu loop."""

    keep_running = True
    while keep_running:
        display_menu()
        try:
            user_choice = input("Enter your selection (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):  # pragma: no cover - interactive guard
            print("\nExiting. Goodbye!")
            break

        keep_running = handle_choice(user_choice)


if __name__ == "__main__":
    main()
