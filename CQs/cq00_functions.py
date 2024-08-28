"""practice question in class"""

__author__ = "730673654"


# the primary mimic function will print back the message
def mimic(message: str) -> str:
    """repeats user's message back to them"""
    return message


# main function pulls together everything, need to prompt users
def main() -> None:
    """bring together other functions"""
    return print(mimic(message=input("What is your message?")))


# allows you to use Run and Interact
if __name__ == "__main__":
    main()
