def print_honeycomb(rows, cols):
    hex_top = "  ___ "
    hex_middle_top = " /   \\"
    hex_middle_bottom = " \\___/"
    space = "   "

    for row in range(rows):

        for col in range(cols):
            # if row % 2 == 1:
                if col % 2 == 1:
                    print(space, end="")
                print(hex_top, end="")
        print()


        for col in range(cols):
            # if row % 2 == 1:
                if col % 2 == 1:
                    print(space, end="")
                print(hex_middle_top, end="")
        print()


        for col in range(cols):
            #if row % 2 == 1:
                if col % 2 == 1:
                    print(space, end="")
                print(hex_middle_bottom, end="")
        print()


input_str = input("input ")
rows, cols = map(int, input_str.split())


print_honeycomb(rows, cols)


