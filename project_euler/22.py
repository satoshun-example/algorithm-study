def names_scores():
    line = []
    with open('p022_names.txt') as f:
        for l in f:
            line = l.split(',')
            line = [l[1:len(l)-1] for l in line]
            break

    line = sorted(line)
    score = 0
    b = ord('A') - 1
    for w, name in enumerate(line):
        score += (w + 1) * sum(ord(n) - b for n in name)

    return score


print(names_scores())
