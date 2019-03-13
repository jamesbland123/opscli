from .command import Command
import sys

def main():
    args = sys.argv[1:]
    Command(args)

if __name__ == "__main__":
    main()