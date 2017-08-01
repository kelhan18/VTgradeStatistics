import reader
import matplotlib.pyplot as plt

class Main:

    def __init__(self):
        pass

    def getData(self):
        x = reader.Reader()
        data_set = x.readFile()
        print data_set


def main():
    run = Main()
    run.getData()

if __name__ == '__main__':
    main()