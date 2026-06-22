def tower(n, source, helper, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower(n - 1, source, destination, helper)
    print("Move disk", n, "from", source, "to", destination)
    tower(n - 1, helper, source, destination)


n = int(input("Enter number of disks: "))

tower(n, "A", "B", "C")