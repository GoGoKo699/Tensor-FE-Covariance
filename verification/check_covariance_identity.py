"""Exact finite-support check of the noise covariance formula.

This tests the algebra for independent centered samplers, not the target
scheme's lattice sampler, security, RIP, or asymptotic running time.
"""
from fractions import Fraction as F
from itertools import product
import json

L, m, n, mt = 4, 2, 1, 1
K = [ [[1,2],[-1,3]], [[-2,1],[4,0]],
      [[0,-3],[2,1]], [[3,0],[1,-2]] ]
Kt = [2,-1,3,1]
Hs = [ [1,2,-1,3], [2,-2,4,1] ]
probs = {-1:F(1,4), 0:F(1,2), 1:F(1,4)}
v, mu4 = F(1,2), F(1,2)
mean = [F(0) for _ in range(L)]
second = [[F(0) for _ in range(L)] for _ in range(L)]
for s, e0, e1, et in product(probs, repeat=4):
    weight = probs[s]*probs[e0]*probs[e1]*probs[et]
    e=[e0,e1]
    z = [sum(e[i]*K[l][i][j]*e[j] for i in range(m) for j in range(m))
         +et*Kt[l]-sum(s*e[i]*Hs[i][l] for i in range(m))
         for l in range(L)]
    for l in range(L):
        mean[l] += weight*z[l]
        for j in range(L):
            second[l][j] += weight*z[l]*z[j]
cov = [[second[l][j]-mean[l]*mean[j] for j in range(L)] for l in range(L)]
pred_mean=[v*sum(K[l][i][i] for i in range(m)) for l in range(L)]
known = [[(mu4-v*v)*sum(K[l][i][i]*K[j][i][i] for i in range(m))
          +v*v*(K[l][0][1]+K[l][1][0])*(K[j][0][1]+K[j][1][0])
          +v*Kt[l]*Kt[j]
          for j in range(L)] for l in range(L)]
gram=[[sum(Hs[i][l]*Hs[i][j] for i in range(m)) for j in range(L)] for l in range(L)]
recovered=[[(cov[l][j]-known[l][j])/(v*v) for j in range(L)] for l in range(L)]
assert mean == pred_mean
assert recovered == gram
out={"status":"pass", "enumerated_outcomes":81,
     "model":"independent centered ternary variables; exact rational arithmetic",
     "scope":"covariance identity and exact Gram subtraction only",
     "mean":[str(x) for x in mean], "recovered_gram": [[int(x) for x in row] for row in recovered]}

print(json.dumps(out,indent=2))
