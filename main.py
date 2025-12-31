"""Command-line menu for launching project stubs.

This script presents a simple numbered menu for five placeholder projects
and loops until the user chooses to exit.
"""

from __future__ import annotations


PROJECTS = {
    "1": "Data Cleaning Pipeline",
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
        "1": run_data_cleaning,
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
