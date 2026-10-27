"""Check quadratic expansion and the exact p^2 noise factor.

The small modular matrices are constructed to satisfy the preimage equations.
They are not sampled from the scheme's key distribution. This checks algebra,
tensor index order, and balanced lifting only.
"""
from random import Random
import json

rng = Random(1977)
q, p, k, n, m, mt = 1009, 2, 2, 1, 2, 4
h, cols = k + n, k * k

def mat(rows, columns, bound):
    return [[rng.randint(-bound, bound) for _ in range(columns)]
            for _ in range(rows)]

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def mvrow(v, a):
    return [sum(v[i] * a[i][j] for i in range(len(v)))
            for j in range(len(a[0]))]

def kronv(x, y):
    return [a * b for a in x for b in y]

def kron(a, b):
    return [[a[i][j] * b[t][u]
             for j in range(len(a[0])) for u in range(len(b[0]))]
            for i in range(len(a)) for t in range(len(b))]

def mm(a, b):
    return [[sum(a[i][t] * b[t][j] for t in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def eye(d):
    return [[int(i == j) for j in range(d)] for i in range(d)]

a = mat(h, m, 20)
key = mat(m * m, cols, 3)
fl, fr = mat(h * m, cols, 3), mat(m * h, cols, 3)
selector = [[int(i == j) for j in range(k)] for i in range(h)]
target = kron(selector, selector)
ak = mm(kron(a, a), key)
lk, rk = mm(kron(a, eye(m)), key), mm(kron(eye(m), a), key)
# C is the identity, so these choices solve all three equations exactly mod q.
at2 = [[(target[i][j] - ak[i][j]) % q for j in range(cols)]
       for i in range(h * h)]
atl = [[(-lk[i][j] - p * fl[i][j]) % q for j in range(cols)]
       for i in range(h * m)]
atr = [[(-rk[i][j] - p * fr[i][j]) % q for j in range(cols)]
       for i in range(m * h)]

checked, lifts, wrapped = 0, 0, 0
for case in range(160):
    x = [rng.randint(-1, 1) for _ in range(k)]
    s = [rng.randint(-2, 2) for _ in range(n)]
    error_bound = 2 if case < 144 else 20
    e = [rng.randint(-error_bound, error_bound) for _ in range(m)]
    et = [rng.randint(-2, 2) for _ in range(mt)]
    u = x + s
    c = [(v + p * err) % q for v, err in zip(mvrow(u, a), e)]
    t2, tl, tr = mvrow(kronv(u, u), at2), mvrow(kronv(u, e), atl), mvrow(kronv(e, u), atr)
    ct = [(t2[j] + p * tl[j] + p * tr[j] + p * p * et[j]) % q
          for j in range(mt)]
    observed = [(v + ct[j]) % q for j, v in enumerate(mvrow(kronv(c, c), key))]
    qnoise = mvrow(kronv(e, e), key)
    lnoise, rnoise = mvrow(kronv(u, e), fl), mvrow(kronv(e, u), fr)
    noise = [qnoise[j] + et[j] - lnoise[j] - rnoise[j] for j in range(cols)]
    values = kronv(x, x)
    for j in range(cols):
        integer = values[j] + p * p * noise[j]
        assert observed[j] == integer % q
        balanced = observed[j] if observed[j] <= q // 2 else observed[j] - q
        if abs(integer) < q / 2:
            assert balanced == integer
            if values[j] == 0:
                assert balanced % (p * p) == 0
                assert balanced // (p * p) == noise[j]
                lifts += 1
        else:
            assert balanced != integer
            wrapped += 1
        checked += 1
assert lifts > 0 and wrapped > 0
print(json.dumps({"status": "pass", "coordinate_identities": checked,
                  "verified_zero_output_lifts": lifts,
                  "wrapped_cases_detected": wrapped,
                  "scope": "modular expansion and p^2 factor; synthetic preimages"},
                 indent=2))

