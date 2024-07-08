def recursive_func(len: int, start: int):
        if(start == len):
                return len
        print(start)
        start += 1
        return recursive_func(len, start)


recursive_func(10, 0)