# Tensor FE Covariance

## Covariance learning in quadratic tensor functional encryption

This repository develops a classical polynomial-time distinguishing argument for an explicit degree-two family of the tensor-based secret-key functional encryption construction of [Cini, Lai, Ünal and Woo, ePrint 2026/1977](https://eprint.iacr.org/2026/1977).

The adversary uses valid monomial functional keys and polynomially many honest encryptions of a known zero message. It learns an exact hidden integer Gram matrix from cross-covariances, removes the corresponding nuisance subspace, and distinguishes the challenge messages $0$ and $e_1$ by testing for a rank-one explanation. All requested functions agree on those two messages.

**The proved distinguishing gap is $1-\mathrm{negl}(\lambda)$ under the explicit dimension, smoothing, width and correctness conditions in the [main theorem](science/attack.md).** An [asymptotic parameter family](science/parameters.md) satisfies these conditions together with the target's numerical safeguards and compactness requirement. The result also applies directly to the corresponding degree-two secret-key tensor-preimage assumption experiment.

The claim is parameter-dependent. It supplies no ordinary-LWE algorithm and no practical attack timing.

## Central identity

For a known-zero encryption, the integer noise across the exposed keys has the form

```math
z=\mathcal K(ee^{\mathsf T})+C^{\mathsf T}\widetilde e
-H_s^{\mathsf T}(s\otimes e).
```

With independent encryption coordinates of common discrete-Gaussian variance $v$,

```math
\mathrm{Cov}(z)
=C_K+vC^{\mathsf T}C+v^2H_s^{\mathsf T}H_s.
```

Here $C_K$ and $C$ are known from the keys and the exact noise moments. Normalizing by $v$, estimating the covariance, subtracting the known terms, and rounding recovers the integer matrix $H_s^{\mathsf T}H_s$. This determines $\ker H_s$ without recovering $H_s$.

The [Gaussian measurement proof](science/gaussian_measurements.md) establishes the required geometry for the full correlated key columns before projection. The [reconstruction proof](science/reconstruction.md) then gives a finite-bit convex procedure, exact integer rounding and an exact residual test.

## Scientific account

| Page | Content |
|---|---|
| [Model and access](science/model.md) | Ciphertext expansion, the $p^2$ factor, legal monomial keys and both experiments |
| [Noise covariance](science/noise_covariance.md) | Exact moments, normalized sample bound, finite precision and Gram rounding |
| [Gaussian measurements](science/gaussian_measurements.md) | Affine-coset moments, concentration, joint restricted isometry and full-lattice smoothing |
| [Reconstruction](science/reconstruction.md) | Rational projection, bounded convex feasibility, integer reconstruction and decision |
| [Parameters](science/parameters.md) | An explicit compatible family and the resource accounting |
| [Main theorem](science/attack.md) | End-to-end argument and total failure probability |
| [Interpretation](science/interpretation.md) | Security consequences, limitations and open questions |
| [Related work](references/RELATED_WORK.md) | Closest sources, inherited methods and source-access boundaries |

For a first reading, start with the model, theorem and interpretation. For a proof audit, use the [scientific index](science/README.md).

## Reproducible checks

Run the four dependency-free checks with Python 3:

```bash
python3 verification/run_all.py
```

They verify the covariance identity by exact enumeration, the modular quadratic expansion, the dual theta moment formulas at finite widths, and exact integer rounding on rational examples. See [Verification](verification/README.md) for the outputs and their limits.

The statistical and polynomial-time conclusions are mathematical proofs in the scientific notes. These small checks do not implement the full scheme or the ellipsoid decoder.

## Scope and attribution

The target is the September 11, 2026 version of the cited preprint. Noise-based FE attacks, multiple-key observations, manifold distinctions, discrete-Gaussian methods and nuclear-norm recovery have prior literature. This project's contribution is their specific covariance-to-kernel-to-reconstruction connection, with a proof for the target's affine-lattice Gaussian model and a compatible parameter family. [Related work](references/RELATED_WORK.md) records what was verified and where full-source access remained limited.

The repository contains research notes and supporting checks. Independent review remains valuable, particularly for the full literature comparison and the boundary of the covered parameter regime.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[MIT license](LICENSE) · [Bibliography](references/references.bib) · [Machine-readable overview](llms.txt)

