def solution(phone_book):
    phone_book = set(phone_book)
    for i in phone_book:
        for j in range(1, len(i)):
            if i[:j] in phone_book:
                return False
        
    return True