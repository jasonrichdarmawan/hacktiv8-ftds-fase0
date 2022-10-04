import inspect

# reference: https://stackoverflow.com/a/45796693/13285583
def Print(values: object):
    print(f'{inspect.stack()[1][1].split("/")[-1]}:'
          f'{inspect.stack()[1][2]}'
          f':{inspect.stack()[1][3]} {values}')

def PrintLine():
    for i in range(23):
        print("=", end="")
    print("")