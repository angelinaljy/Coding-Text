def merge(L1, L2):

    if L1 is None or len(L1) == 0:
        X = L2
        return X
    elif L2 is None or  len(L2) == 0:
        X = L1
        return X


    else:
        X = []
        a = 0
        b = 0

        while True:
            if L1[a] >= L2[b]:
                X.append(L2[b])
                if b < len(L2)-1:
                    b += 1
                    continue
                else:
                    while True:
                        if a < len(L1)-1:
                            X.append(L1[a])
                            a += 1

                        else:
                            X.append(L1[a])
                            print(X)
                            break
                break
            else:
                X.append(L1[a])
                if a < len(L1)-1:
                    a += 1
                    continue
                else:
                    while True:
                        if b < len(L2)-1:
                            X.append(L2[b])
                            b += 1
                        else:
                            X.append(L2[b])
                            print(X)
                            break
                break

if __name__=="__main__":
    L1 = [1,2,3,4,9,10]
    L2 = [1,2,2,2,11,13]

    res=merge(L1, L2)
    print(res)