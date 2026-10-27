"""Check exact rounding and rank rejection on rational examples.

The inputs model an already-certified Frobenius-accurate reconstruction.
The test does not implement or certify the convex feasibility algorithm.
"""
from fractions import Fraction
from random import Random
import json

rng = Random(2026)

def nearest(x):
    # Deterministic nearest integer, ties upward. No tie occurs in good cases.
    return (2 * x.numerator + x.denominator) // (2 * x.denominator)

def rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    i = 0
    for j in range(len(a[0])):
        pivot = next((t for t in range(i, len(a)) if a[t][j]), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        div = a[i][j]
        a[i] = [x / div for x in a[i]]
        for t in range(i + 1, len(a)):
            div = a[t][j]
            a[t] = [x - div * y for x, y in zip(a[t], a[i])]
        i += 1
        if i == len(a):
            break
    return i

checked = 0
for m in (1, 2, 4, 7):
    for scale in (0, 1, 10 ** 6, 10 ** 40):
        for _ in range(8):
            e = [scale * rng.randint(-3, 3) for _ in range(m)]
            true = [[e[i] * e[j] for j in range(m)] for i in range(m)]
            error = [[Fraction(0) for _ in range(m)] for _ in range(m)]
            for i in range(m):
                for j in range(i, m):
                    error[i][j] = error[j][i] = Fraction(rng.randint(-5, 5), 100000 * m)
            frob2 = sum(x * x for row in error for x in row)
            assert frob2 < Fraction(1, 4)
            candidate = [[nearest(Fraction(true[i][j]) + error[i][j])
                          for j in range(m)] for i in range(m)]
            assert candidate == true
            assert rank(candidate) <= 1
            checked += 1
assert rank([[1, 0], [0, 1]]) == 2
assert rank([[0, 1], [1, 0]]) == 2
assert nearest(Fraction(-1, 2)) == 0
assert nearest(Fraction(-3, 2)) == -1
print(json.dumps({"status": "pass", "rational_reconstruction_cases": checked,
                  "largest_coordinate_scale": "10^40",
                  "rank_two_examples_rejected": 2,
                  "scope": "integer rounding and exact rank; no optimization implementation"},
                 indent=2))

