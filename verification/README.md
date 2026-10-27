# Reproducible algebra checks

Run from the repository root with Python 3:

```bash
python3 verification/run_all.py
```

All scripts use the Python standard library. They write no files and make no network calls.

| Check | Evidence supplied | Boundary |
|---|---|---|
| [Covariance identity](check_covariance_identity.py) | Exact rational enumeration of 81 outcomes; recovers the displayed integer Gram | Uses a centered ternary law, not the lattice key sampler |
| [Quadratic identity](check_quadratic_identity.py) | 640 coordinate identities; checks the exact $p^2$ factor and balanced lifts, including wrap cases | Synthetic preimages satisfy the equations algebraically; they are not scheme-generated keys |
| [Theta moments](check_theta_moments.py) | Compares primal and dual second/fourth moments at widths 1, 1.25, 2, 4, 8 and 32; relative tolerance $10^{-12}$ | A finite floating-point check; certified precision and complexity are proved in the note |
| [Integer recovery](check_integer_recovery.py) | 128 exact rational perturbation cases, coordinate scales through $10^{40}$, and two rank-two rejection examples | Assumes an already accurate matrix; does not implement convex optimization |

Each script prints a JSON result with a status and its scope. The runner exits nonzero if any assertion fails, and prints “All four checks passed.” after success.

## Exact covariance output

The finite-law test uses nonsymmetric quadratic matrices and a non-Gaussian fourth moment. It recovers

```math
G=
\begin{pmatrix}
5&-2&7&5\\
-2&8&-10&4\\
7&-10&17&1\\
5&4&1&10
\end{pmatrix}.
```

Every entry is compared with the independently formed hidden Gram using rational arithmetic. This catches diagonal-moment, off-diagonal symmetrization, and variance-scaling errors in the identity.

## Mathematical validation

The full argument requires statements beyond finite examples:

- [Noise covariance](../science/noise_covariance.md) proves uniform moments, the median-of-means sample count and finite-precision rounding.
- [Gaussian measurements](../science/gaussian_measurements.md) proves smoothing, the affine-coset concentration theorem and the joint geometry before projection.
- [Reconstruction](../science/reconstruction.md) proves polynomial bit complexity through an explicit feasible ball and rational separation.
- [Parameters](../science/parameters.md) checks asymptotic compatibility and all charged exceptional events.
- [The main theorem](../science/attack.md) combines these statements with the permitted-key security experiment.

No test output certifies the underlying cryptographic claim by itself. There is no full scheme implementation, benchmark, or claim about an off-the-shelf floating-point optimizer in this repository.

