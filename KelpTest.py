info_dict = {}
inp = int(input("Enter the number of actions to be performed: "))
for i in range(inp):
    user_in = list(map(str, input().split()))
    if user_in[0]=="CREATE":
        info_dict[user_in[1]] = [user_in[2], 0]
    if user_in[0]=="DEPOSIT":
        info_dict[user_in[1]][1] += int(user_in[2])
    if user_in[0]=="WITHDRAW":
        info_dict[user_in[1]][1] -= int(user_in[2])
    if user_in[0]=="BALANCE":
        print(*info_dict[user_in[1]])
    """ 
    l = []
    On line 14, we can do l.append(*info_dict[user_in[1]])
    and print the result at the end if we don't want o/p
    in between
    """