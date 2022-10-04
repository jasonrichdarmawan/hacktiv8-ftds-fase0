from printLine import Print

def Speak(input: str | int) -> TypeError | None:
    if type(input) != str and type(input) != int:
        return TypeError("type not supported")

    if type(input) == str:
        Print("str")
        return
    elif type(input) == int:
        Print("int")
        return