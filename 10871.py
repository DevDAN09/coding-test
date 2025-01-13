A, X = map(int, input().split());
list_a = list(map(int, input().split()));
output = [];

for i in list_a:
    if i < X:
        output.append(i);

for k in output:
    print(k, end=" ");
