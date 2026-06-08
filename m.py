A=[ ['a','b','c','d'],
    ['g','h','m'],
    ['g','h','m']
    ]
B=['yahya','hamza','musa','ali']

def replica_len(Arr):
    count = 0
    try:
        while True:
            x=Arr[count]
            count +=1
    except:
        pass
    return count
a=replica_len(B)
print(type(a))
print(a)
def rsi(value):
    if value<20:
        print('Buy stock--------')
    elif value>80:
        print('--------sell stock')
    else:
        print('hold on')
