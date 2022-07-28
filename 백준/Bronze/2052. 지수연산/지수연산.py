from decimal import Decimal

print(f"{Decimal(2 ** -int(input())):.10000f}".rstrip("0").rstrip("."))