def test(a, b):
    max_x, max_y = a[0][0], b
    for i in a:
        for j in i:
            if j[0] <= max_x[0] and abs(j[1]) > max_x[1]:
                max_x = j
            if j[0] >= max_y[0] and abs(j[1]) > max_y[1] and max_y[1] != j[1]:
                max_y = j

    y = (max_x[0]-max_y[0]) + (max_x[1]-max_y[1])
    print(max_x, max_y)
    return abs(y)


print(test([[[4, 0], [4, -5], [7, -5], [7, 0]]], [1, 1]))
print(test([[[4, 0], [4, -5], [7, -5], [7, 0]],
            [[0.4, -2], [0.4, -5], [2.5, -5], [2.5, -2]]], [-3.5, 1]))
