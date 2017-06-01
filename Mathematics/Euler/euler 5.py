

def is_answer(n):
    for d in range(1,21):
        if n%d != 0:
            return False
    return True


n = 20
while True:
    if is_answer(n):
        print n
        break
    n += 20
