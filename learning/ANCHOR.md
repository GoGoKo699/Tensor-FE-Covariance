# Peikert anchor and source-to-project map

## Selected source

**Chris Peikert, _A Decade of Lattice Cryptography_.** _Foundations and Trends in Theoretical Computer Science_ **10**(4), 283–424 (2016). [DOI: 10.1561/0400000074](https://doi.org/10.1561/0400000074).

The public survey is [ePrint 2015/939](https://eprint.iacr.org/2015/939), revised February 18, 2016; an [author-hosted PDF](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf) is also available. The section numbers below refer to the full survey. They are preferable to page numbers, which differ between its preprint and journal layouts.

This is the one educational anchor for the project. The [bridge](BRIDGE.md) develops the additional ideas locally; the [research bibliography](../references/references.bib) retains the primary sources needed for attribution and checking technical ingredients.

## Focused reading map

| Survey location | Background to extract | Connection in this repository |
|---|---|---|
| §§2.1–2.2: notation and lattices | Modular vectors, lattice bases, duality and lattice problems | [Model §1](../science/model.md#1-parameters-and-conventions); the full preimage lattice in [Gaussian measurements](../science/gaussian_measurements.md) |
| §2.3: (discrete) Gaussians and subgaussians | Gaussian width conventions, discrete laws and tail control | Exact discrete moments in [Noise covariance](../science/noise_covariance.md); smoothing and affine-coset estimates in [Gaussian measurements](../science/gaussian_measurements.md) |
| §2.4 and §§4.2.1–4.2.2: cryptographic background and LWE | Distinguishing experiments, noisy modular equations and the role of hardness assumptions | The permitted FE observations in [Model §§3–4](../science/model.md#3-ciphertexts-and-the-observable-integer-noise); the scope in [Interpretation](../science/interpretation.md) |
| §5.4, especially Theorem 5.4.2 | Sampling a discrete Gaussian on a lattice coset using a short basis | The full-column ideal extension in [Model §2](../science/model.md#2-the-public-key-columns-and-hidden-extension) and its [smoothing proof](../science/gaussian_measurements.md) |
| Optional §5.2.1: Regev's LWE cryptosystem | A concrete encryption application of LWE | Context for separating encryption randomness, fixed setup data and correctness bounds |

Use these sections when the corresponding object appears in the [milestone map](MILESTONES.md). The rest of the survey is not a prerequisite for this project's route.

## Translate the notation before using a formula

| Source convention or object | Project notation and meaning |
|---|---|
| A Gaussian parameter often written $s$ | The short-key width is $\sigma$; the encryption width is $\chi$. Here $s$ itself denotes a fresh randomizer vector. |
| An LWE error distribution written $\chi$ in §4.2 | Here $\chi$ is a numerical width, and the coordinate distribution is $D_{\mathbb Z,\chi}$. |
| The lattice Gaussian weight $\exp(-\pi\|z\|_2^2/s^2)$ | The same width convention is used. Its continuous coordinate variance is $s^2/(2\pi)$; the exact discrete variance is a separate quantity $v_\chi$. |
| An affine lattice coset and its Gaussian sampler | A complete key column lies in an affine preimage coset. The congruence constraints may correlate its coordinates. |
| An LWE dimension or sample count | Project dimensions $k,n,m,\widetilde m,L$ have their own roles, listed in [Model §1](../science/model.md#1-parameters-and-conventions). Equal symbols alone do not identify two experiments. |

The project also uses $\alpha=\sigma\sqrt{L/(2\pi)}$ for the measurement normalization. This $\alpha$ is distinct from a relative LWE error rate in the survey. The full-column dimension bound is $N_{\rm col}$; the structured measurement domain has the smaller dimension $D=m(m+1)/2+d_0$.

Two assumptions need particular care. A spherical Gaussian weight on a constrained lattice coset does not make the coordinates independent. Also, a sampling theorem's closeness in statistical distance must be applied to the actual output marginal being observed. [Model §2](../science/model.md#2-the-public-key-columns-and-hidden-extension) states that marginal precisely; [Gaussian measurements](../science/gaussian_measurements.md) retains the resulting dependencies.

## The steps supplied by this project

| Step beyond the anchor | Local explanation | Authoritative account |
|---|---|---|
| Identify lawful observations whose function values agree on both challenges | Bridge §§1–2 | [Model](../science/model.md) |
| Use exact cross-covariances to learn an integer Gram matrix | Bridge §§3–4 | [Noise covariance](../science/noise_covariance.md) |
| Remove a nuisance subspace while retaining enough measurements | Bridge §§5–6 | [Gaussian measurements](../science/gaussian_measurements.md), then [Main theorem §3](../science/attack.md#3-joint-geometry-before-projection) |
| Turn stable low-rank recovery into an exact finite-bit decision | Bridge §7 | [Reconstruction](../science/reconstruction.md) |
| Make access, sample count, precision, smoothing and compactness coexist | Bridge §§8–9 | [Parameters](../science/parameters.md), [Main theorem](../science/attack.md), [Related work](../references/RELATED_WORK.md) |

The survey supplies foundations. The target FE construction and its sampler come from Cini–Lai–Ünal–Woo; matrix-recovery and finite optimization have their own prior literature. The specific connection among observable covariance, an exact hidden kernel and a finite-bit distinguishing test is developed in the scientific pages. The result leaves ordinary LWE hardness as an assumption and concerns the explicitly stated construction and parameter regime.

[Learning route](README.md) · [Project bridge](BRIDGE.md) · [Milestones](MILESTONES.md)
