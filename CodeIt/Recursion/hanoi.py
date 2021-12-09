
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):

    if num_disks == 0:
        return

    else :
        another_peg = 6 - start_peg - end_peg
        hanoi(num_disks-1, start_peg, another_peg)
        move_disk(1, start_peg, end_peg)
        hanoi(num_disks-1, another_peg, end_peg)


# test
hanoi(3, 1, 3)