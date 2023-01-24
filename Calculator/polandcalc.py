

def str2pool(expression_string):
    result=[]
    pool=list(expression_string)
    num=''
    znak=""
    for token in pool:
        if token=='-':
            if num=='':
                znak="-"
            else:
                result.append(znak+num)
                result.append(token)
                num=znak=""
  
        elif token in '+/*()':
            if num!='':
                result.append(znak+num)
                num=znak=''
                
            result.append(token)
            
        elif token.isnumeric() or token=='.':
            num+=token
            
        elif token==' ':
            pass
    return result

def priority_of_operations(operation):
    match operation:
        case "+" | "-":
            return 1
        case "/" | "*":
            return 2
        case "^":
            return 3
    return 0


def infix2polan(pool):
    #  https://ru.wikipedia.org/wiki/Обратная_польская_запись#Вычисления_на_стеке
    result = []
    stack = []
    while (True):
        if len(pool) == 0:
            break
        token = pool.pop(0)
        if token.isnumeric():
            result.append(token)
            continue
        elif token in "-+*/^":
            if len(stack)> 0:
                wt_token = priority_of_operations(token)
                while(wt_token<=priority_of_operations(stack[-1])  ):
                    result.append(stack.pop()) 
            result.append(token)
            continue        
        elif token == ")":
            while (True):
                if len(stack) == 0:
                    print("error")
                    exit()
                if stack[-1] == '(':
                    stack.pop()
                    break
                result.append(stack.pop())
            continue
        elif token=="(":
            stack.append("(")



test='( -12-2)*-3+5'
print(str2pool(test))
print(infix2polan(str2pool(test)))