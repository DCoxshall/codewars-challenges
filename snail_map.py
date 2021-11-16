def snail(snail_map):
    compass = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
    ans = []
    direc = 'n'
    while snail_map != []:
        if direc == 'n':
            ans.extend(snail_map[0])
            print(ans)
            snail_map = snail_map[1:]
        
        if direc == 'e':
            newArr = [i[-1] for i in snail_map]
            ans.extend(newArr)
            print(ans)
            for i in snail_map:
                i.pop()
                
        if direc == 's':
            newArr = snail_map[-1]
            newArr.reverse()
            ans.extend(newArr)
            print(ans)
            snail_map = snail_map[:-1]
            
        if direc == 'w':
            newArr = [i[0] for i in snail_map]
            newArr.reverse()
            ans.extend(newArr)
            print(ans)
            for i in snail_map:
                i.pop(0)
                
        direc = compass[direc]
    return(ans)
