def repeat(xs, n):
    if n < 0:
        raise ValueError

    result = []
    for i in xs:
        result.extend([i] * n)
    
    return result

print(repeat(['a', 'b'], 3))