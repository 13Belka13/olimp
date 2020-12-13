n = int(input())
c = 0
for o in range(n):
    board = []


    for i in range(8):
        board.append(input().split())

    def rook_and_queen_search():
        pos = {'w':{'R':[], 'Q':[]}, 'b':{'R':[], 'Q':[]}}
        for y in range(len(board)):
            for x in range(len(board)):
                k = board[y][x]
                if k[-1] == 'R' or k[-1] == 'Q':
                    pos[k[0]][k[-1]].append([y, x])
        return pos

    def check_the_check(pos):
        for side in pos:
            for figure in pos[side]:
                for l in pos[side][figure]:
                    for x in range(0, 8):
                        z = board[l[0]][x]
                        if z != '0' and z[-1] != 'K' and z[-1] != 'R' and z[-1] != 'Q':
                            break
                        elif z[-1] == 'K' and z[0] != side:
                            return True
                    for y in range(0, 8):
                        z = board[y][l[-1]]
                        if z != '0' and z[-1] != 'K' and z[-1] != 'R' and z[-1] != 'Q':
                            break
                        elif z[-1] == 'K' and z[0] != side:
                            return True
                    if figure == 'Q':
                        x = l[-1]
                        y = l[0]
                        in_start_pos = False
                        while y <= 7 and x <= 7:
                            if x == 0 or y == 0:
                                in_start_pos = True
                            if in_start_pos:
                                x += 1
                                y += 1
                            else:
                                x -= 1
                                y -= 1
                            if y <= 7 and x <= 7:
                                z = board[y][x]
                                if z != '0' and z[-1] != 'K' and z[-1] != 'Q':
                                    break
                                elif z[-1] == 'K' and z[0] != side:
                                    return True
                        x = l[-1]
                        y = l[0]
                        in_start_pos = False
                        while y <= 7 and x <= 7:
                            if x == 0 or y == 7:
                                in_start_pos = True
                            if in_start_pos:
                                x += 1
                                y -= 1
                            else:
                                x -= 1
                                y += 1
                            if y <= 7 and x <= 7:
                                z = board[y][x]
                                if z != '0' and z[-1] != 'K' and z[-1] != 'Q':
                                    break
                                elif z[-1] == 'K' and z[0] != side:
                                    return True

        return False

    if check_the_check(rook_and_queen_search()):
        c += 1
print(c)
