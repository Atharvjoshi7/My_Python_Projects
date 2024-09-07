import keyword
from numpy import append


def main():
    try:
        bookList = []
        infile = open("theBookList", "r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("The File is not found")
        print("starting a new list")
        bookList = []


    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1. Add a Book")
        print("2. Lookup a Book")
        print("3. Display all Books")
        print("4. Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a Book...")
            nBook = input("Enter the name of the Book >>>")
            nAuthor = input("Enter the name of the Author >>>")
            nPages = input("Enter the number of pages >>>")
            bookList.append([nBook, nAuthor, nPages])
        elif choice == 2:
            print("Looking for a book...")
            keyword = input("Enter Search Term: ")
            for book in bookList:
                if keyword in book:
                    print(book)
        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(bookList)):
                print(bookList[i])
        elif choice == 4:
            print("Goodbye...")
    print("Program Terminated!")

    outfile = open("BookList.txt", "w")
    for book in bookList:
        outfile.write(",".join(book) + "\n")
    outfile.close


if __name__ == "__main__":
    main()