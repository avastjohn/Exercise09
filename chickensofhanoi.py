n = 5
start = [5, 4, 3, 2, 1]
end = []
buffy = []

def towers(n, start, end, buffy):
    if n == 1:
        end.append(start.pop())
    else: 
        towers(n-1, start, buffy, end)
        end.append(start.pop())
        towers(n-1,buffy, end, start)

print towers(n, start, end, buffy)
print start
print end
print buffy