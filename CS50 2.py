def main():
    names = []
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        print("")
        print("Adieu, adieu, to ",end="")
        leng = len(names)
        last = names[leng-1]
        if leng == 1:
            print(last)
        elif leng != 1:
            names.pop(leng - 1)
            for i in names:
                if leng == 2:
                    print(i, end=" ")
                else:
                    print(i, end=", ")
            print("and " + last, end="\n")
main()