from arithmeticOperators import ArithmeticOperators
from comparisonOperators import ComparisonOperators
from printLine import Print
from overloadExample import Speak
from printStrings import PrintStrings
from printIntegers import PrintIntegers
from printLine import PrintLine

def PrintTuples():
    t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
    Print(t)
    Print(t[0])
    Print(t[-1])

def main():
    PrintLine()
    PrintIntegers()

    PrintLine()
    PrintStrings()

    PrintLine()
    ArithmeticOperators()

    PrintLine()
    ComparisonOperators()

    PrintLine()
    a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
    a[2] = 10
    a[-1] = 20 # index 0 from right
    Print(a)

    PrintLine()
    a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge'] # lists are mutable
    print(a[1:4])
    a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
    Print(a)

    PrintLine()
    PrintTuples() # tuples are immutable

    PrintLine()
    Speak("str")
    Speak(1)
    err = Speak(1.0) # expected
    if type(err) == TypeError:
        Print(err)
    else:
        raise err

    PrintLine()
    name = "Jack"
    age = 5
    Print('nama saya adalah ' + name + ' dengan umur ' + str(age))
    Print(f'nama saya adalah {name} dengan umur {age}')

    PrintLine()
    list = ["motor", "mobil"]
    list.insert(1, "pesawat")
    list.append("kereta")
    Print(list)

    PrintLine()
    list1 = ["motor","pesawat"]
    list2 = ["mobil", "kereta"]
    list1.extend(list2)
    Print(list1)

    PrintLine()
    # List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    # Dictionary is a collection which is ordered** and changeable. No duplicate members.
    set = {"a", "b"}
    set.add("c")
    Print(set)

if __name__ == "__main__":
    main()