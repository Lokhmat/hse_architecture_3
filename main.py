from container import Container
import sys


# Main program to work with container.
def main():
    container = Container()
    if len(sys.argv) == 5 and sys.argv[1] == '-n' and sys.argv[2].isdecimal():
        try:
            container.random_in(amount=int(sys.argv[2]))
        except Exception as error:
            print(f'Something went wrong. Your input probably incorrect\n{error}\nAnswer may or may not be correct.')
            return
    elif len(sys.argv) == 5 and sys.argv[1] == '-f':
        try:
            container.file_in(path=sys.argv[2])
        except Exception as error:
            print(f'Something went wrong. Your input probably incorrect\n{error}\nAnswer may or may not be correct.')
            return
    else:
        print('Incorrect command line! You must write: python main -n/-f <numOfItems>/<inputFileName>'
              ' <outputFileName1> <outputFileName2>')
        return
    container.write_to(path=sys.argv[3])
    container.sort()
    container.write_to(path=sys.argv[4])


if __name__ == '__main__':
    main()
