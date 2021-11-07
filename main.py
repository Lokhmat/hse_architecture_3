from container import Container
import sys

# Main program to work with container.
if __name__ == '__main__':
    container = Container()
    if len(sys.argv) == 5 and sys.argv[1] == '-n' and sys.argv[2].isdecimal():
        try:
            container.random_in(amount=int(sys.argv[2]))
        except Exception as error:
            print(f'Something went wrong. Your input probably incorrect\n{error}\nAnswer may or may not be correct.')
            exit()
    elif len(sys.argv) == 5 and sys.argv[1] == '-f':
        try:
            container.file_in(path=sys.argv[2])
        except Exception as error:
            print(f'Something went wrong. Your input probably incorrect\n{error}\nAnswer may or may not be correct.')
            exit()
    else:
        print('Incorrect command line! You must write: python main -n/-f <numOfItems>/<inputFileName>'
              ' <outputFileName1> <outputFileName2>')
        exit()
    container.write_to(path=sys.argv[3])
    container.sort()
    container.write_to(path=sys.argv[4])
