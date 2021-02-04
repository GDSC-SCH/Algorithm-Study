x, y, w, h = map(int, input().split())

result = []
result.append(w - x)
result.append(abs(0 - x))
result.append(h - y)
result.append(abs(0 - y))

result = sorted(result)
print(result[0])