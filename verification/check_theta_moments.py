"""Numerical cross-check of the dual theta moment formulas.

Small widths permit direct primal enumeration as an independent reference.
This finite floating-point check is not a proof of certified evaluation at
large widths or of any asymptotic complexity bound.
"""
import json
from math import ceil, exp, fsum, pi

rows = []
for chi in (1.0, 1.25, 2.0, 4.0, 8.0, 32.0):
    cutoff = ceil(8 * chi)
    weights = [(j, exp(-pi * (j / chi) ** 2))
               for j in range(-cutoff, cutoff + 1)]
    mass = fsum(w for _, w in weights)
    primal2 = fsum(j ** 2 * w for j, w in weights) / mass
    primal4 = fsum(j ** 4 * w for j, w in weights) / mass
    sums = [fsum((j ** power) * exp(-pi * chi ** 2 * j ** 2)
                 for j in range(-12, 13)) for power in (0, 2, 4)]
    s0, s2, s4 = sums
    dual2 = chi ** 2 / (2 * pi) - chi ** 4 * s2 / s0
    dual4 = 3 * chi ** 4 / (4 * pi ** 2) - 3 * chi ** 6 / pi * s2 / s0 + chi ** 8 * s4 / s0
    rel2 = abs(primal2 - dual2) / primal2
    rel4 = abs(primal4 - dual4) / primal4
    assert max(rel2, rel4) < 1e-12
    rows.append({"width": chi, "max_relative_error": max(rel2, rel4)})
print(json.dumps({"status": "pass", "cases": rows,
                  "scope": "primal versus dual second/fourth moments at six finite widths"},
                 indent=2))

