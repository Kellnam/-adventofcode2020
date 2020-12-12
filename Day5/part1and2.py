from allDays.read_input import open_file_to_list


def day5part1(para, part):
    seats = open_file_to_list(para)
    ID = []
    for seat in seats:
        seat = seat.replace('B', '1')
        seat = seat.replace('F', '0')
        seat = seat.replace('R', '1')
        seat = seat.replace('L', '0')

        dec_row = int(seat[0:7], 2)  # 2 is for binary to dec (base of the number)
        dec_column = int(seat[7:10], 2)
        ID.append(dec_row * 8 + dec_column)

    ID.sort()
    if part == 1:
        return ID[len(ID) - 1]
    else:
        for x in range(45, 816):
            if not ID.count(x):
                return x

        return ID
