N = int(input());

list_a = [i for i in range(1, N + 1)];

flag = True;

while(len(list_a) > 1):
    if(flag):
        print(list_a.pop(0), end=" ");
        flag = False;
    else:
        list_a.append(list_a.pop(0));
        flag = True;

print(list_a.pop(0));