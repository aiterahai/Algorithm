inp = int(input())
for _ in range (inp):
    LT, WT, LE, WE = map(int, input().split())
    print("TelecomParisTech" if LT * WT > LE * WE else ("Eurecom" if LT * WT < LE * WE else "Tie"))