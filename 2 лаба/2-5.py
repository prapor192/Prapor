def is_prime(number:int):
    if number<=1:
        return False
    if number==2:
        return True
    for d in range(2,number):
        if number%d==0:
            return False
    return True
print(is_prime(13))
