N = int(input())
shortcuts = []

for i in range(N):
    opt = input()
    index = 0
    words = opt.split()

    for w in words:
        if w[0] not in shortcuts and w[0].upper() not in shortcuts and w[0].lower() not in shortcuts:
            shortcuts.append(w[0])
            break;
        index += len(w)+1 
    else:
        index = 0
        for c in opt:
            if c == ' ':
                index += 1
                continue;
            if c not in shortcuts and c.upper() not in shortcuts and c.lower() not in shortcuts:
                shortcuts.append(c)
                break;
            index += 1
            
    if index == len(opt)-1: #runtime error
        print(opt[:index] + "[" + opt[index] + "]")
    elif index > len(opt)-1: #runtime error
        print(opt)
    else:
        print(opt[:index] + "[" + opt[index] + "]" + opt[index+1:])
    
        
    
