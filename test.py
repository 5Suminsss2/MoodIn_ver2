x, y, w, h = map(int, input().split())
total = []
total.append(x)
total.append(w-x)
total.append(h-y)
total.append(y)

print(min(total))
