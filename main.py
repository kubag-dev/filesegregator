from pathlib import Path

from directories.infrastructure.tasks.move import Move


class Main:
    Move(source=Path("~/Desktop").expanduser()).execute()


if __name__ == "__main__":
    Main()
