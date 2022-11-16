

listt = [1,2,3,4,5]
iterr = iter(listt)

while True:
    try:
        ele = next(iterr)
        print(ele)
    except StopIteration:
        break

