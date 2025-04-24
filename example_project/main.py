# main.py serves as the entry point for your project

from .. import greet

def main():
    message = greet()
    print(message)

if __name__ == "__main__":
    main()
