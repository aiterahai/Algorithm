import decimal
decimal.getcontext().prec = 1000
for _ in range(int(input())):
    board = input()
    N = decimal.Decimal(board) ** decimal.Decimal(decimal.Decimal("1")/decimal.Decimal("3"))
    N = round(N, 500)
    N = decimal.Decimal(N).quantize(decimal.Decimal(".0000000001"), rounding=decimal.ROUND_DOWN)
    print(N)