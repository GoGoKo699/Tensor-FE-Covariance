# Sources and related work

The scientific claim concerns a particular degree-two, many-key regime of the September 11, 2026 version of Cini–Lai–Ünal–Woo. The comparison below credits earlier noise attacks and matrix-recovery tools. It does not claim that covariance attacks, manifold separation, or nuclear-norm recovery are new in isolation.

## CLUW26

**Valerio Cini, Russell W. F. Lai, Akin Ünal, and Ivy K. Y. Woo.** *Lattice-based Secret-Key Functional Encryption for Constant-Degree Polynomials*. Cryptology ePrint Archive, 2026/1977, version dated September 11, 2026. [Canonical record](https://eprint.iacr.org/2026/1977) · [Inspected full PDF](https://eprint.iacr.asia/2026/1977.pdf).

This preprint proposes the tensor-preimage assumption and construction studied here. It distinguishes its new degree-greater-than-one assumption from ordinary LWE; the degree-one case has a separate reduction. The present result does not contradict a reduction from ordinary LWE for the quadratic construction, because the source gives no such reduction.

| Source location | Role in this project |
|---|---|
| Figure 1 | Selective known-message experiment and permitted functional keys |
| Theorems 1–2, Figure 2 | Tensor trapdoor bounds and ideal full Gaussian preimage extension |
| Figures 3–4 | Direct secret-key tensor-assumption experiments and the extra challenge row |
| Figure 5, Table 1 | FE ciphertext/key arithmetic and numerical parameter safeguards |
| Appendix C.1, equations (19), (22), (28)–(30) | Integer error expression and its correctness bound |
| Section 7, especially Strategy 3 and Section 7.2 | Existing noise and polynomial-equation attacks considered by the source |
| Appendix D | Different error-image manifolds and the unknown hidden coefficients |

The source already recognizes that the two integer-error distributions lie on different polynomial images and that large Gaussian width does not erase this support distinction. The remaining problem is efficient distinction with hidden encryption matrices and hidden mixed coefficients.

The result here learns the hidden mixed-term **Gram matrix** from normalized cross-covariances, removes its row space, and uses a rank-one measurement test. It proves the needed joint geometry for the actual affine-lattice Gaussian extension before projection. This addresses the hidden-coefficient obstacle in the explicit dimension regime proved in [Parameters](../science/parameters.md).

## Earlier noise-based FE attacks

**Akin Ünal.** *Impossibility Results for Lattice-Based Functional Encryption Schemes*. EUROCRYPT 2020, pp. 169–199. [DOI](https://doi.org/10.1007/978-3-030-45721-1_7) · [ePrint 2020/163](https://eprint.iacr.org/2020/163) · [Official conference slides](https://iacr.org/submit/files/slides/2020/eurocrypt/ec2020/444/slides.pdf).

This work establishes substantial earlier limitations using decryption-noise information, including many-key observations and second-moment reasoning. Those ideas are antecedents, not a new contribution of this repository. The inspected theorem presentation includes a polynomial modulus-to-scaling ratio in the relevant efficient attack regime.

**Erkan Tairi and Akin Ünal.** *Lower Bounds for Lattice-based Compact Functional Encryption*. EUROCRYPT 2024, Part II, LNCS 14652, pp. 249–279. [DOI](https://doi.org/10.1007/978-3-031-58723-8_9) · [ePrint 2023/719](https://eprint.iacr.org/2023/719) · [Official conference slides](https://iacr.org/submit/files/slides/2024/eurocrypt/eurocrypt2024/323/slides.pdf).

The verified abstract and conference presentation concern linearly compact FE and low-degree polynomial functionality; the attack presentation and the target's discussion account for a cost polynomial in the modulus-to-scaling ratio. The family here has a logarithmically growing ciphertext-coordinate overhead and a superpolynomial modulus-to-scaling ratio. Its proof gives polynomial cost in binary scale lengths through a different recovery mechanism.

| Comparison axis | Earlier verified results / target discussion | Result established here |
|---|---|---|
| Noise information | Noise statistics and multiple keys already exploited | Full cross-covariance identifies an integer hidden Gram |
| Large modulus/noise | Relevant cited attack costs depend polynomially on the numerical ratio | Statistical normalization and finite-bit recovery depend polynomially on encoded lengths |
| Ciphertext dimension | Linearly compact lower-bound regime is an explicit prior focus | A sufficient measurement-versus-nuisance condition, with a quasilinear explicit family |
| Hidden coefficients | Target observes different images but leaves efficient hidden-image separation unresolved | Kernel elimination followed by a uniform rank-one residual separation |
| Random matrix model | General recovery tools are prior | Joint geometry proved for correlated coordinates in affine-lattice Gaussian columns |

**Source-access boundary.** The current ePrint metadata, official slides, and the target's comparisons were inspected. The full PDFs of the 2020 and 2024 papers were not retrievable in the working environment. Consequently this comparison states verified regimes and the concrete mechanism developed here; it does not make an exhaustive priority or “first attack” claim. Further literature review should compare the full earlier papers against the exact hypotheses of [the main theorem](../science/attack.md).

## Gaussian and matrix-recovery foundations

**Daniele Micciancio and Chris Peikert.** *Trapdoors for Lattices: Simpler, Tighter, Faster, Smaller*. EUROCRYPT 2012. [ePrint 2011/501](https://eprint.iacr.org/2011/501) · [Author-hosted PDF](https://web.eecs.umich.edu/~cpeikert/pubs/efftrap.pdf).

Discrete-Gaussian moment-generating functions and lattice trapdoor techniques are established tools. [Gaussian measurements](../science/gaussian_measurements.md) supplies its own Poisson, derivative, concentration, and sublattice-smoothing details so the exact constants and full-column hypotheses can be checked directly.

**Benjamin Recht, Maryam Fazel, and Pablo A. Parrilo.** *Guaranteed Minimum-Rank Solutions of Linear Matrix Equations via Nuclear Norm Minimization*. SIAM Review 52(3), 471–501, 2010. [DOI](https://doi.org/10.1137/070697835) · [Author-hosted full paper](https://www.mit.edu/~parrilo/pubs/files/RechtFazelParrilo-GuaranteedMinimumRankSolutionsOfLinearMatrixEquationsViaNuclearNormMinimization-SIAM.pdf).

Restricted isometry, tangent-space decomposition and nuclear-norm minimization are prior methods. [Reconstruction](../science/reconstruction.md) proves the particular robust bound used here, supplies an explicit feasible ball for finite-bit optimization, and closes the decision with exact integer rounding and a rational residual check.

**Martin Grötschel, László Lovász, and Alexander Schrijver.** *Geometric Algorithms and Combinatorial Optimization*. Springer, 1988. [Author-hosted full book](https://www.zib.de/userpage/groetschel/pubnew/paper/groetschellovaszschrijver1988.pdf).

Theorem 3.2.1 supplies the rounded-ellipsoid feasibility algorithm and small-volume alternative. The repository uses this general theorem with a constructed interior-ball bound, rather than assuming exact polynomial-time solvability of arbitrary semidefinite programs.

## Contribution and limits

The surviving contribution is the complete connection between normalized noise covariance, exact hidden-Gram learning, joint affine-Gaussian measurement geometry, and a finite-bit decision procedure in a legal many-key experiment. Each inherited component is credited above.

The proof is asymptotic and parameter-dependent. It supplies neither practical attack timings nor an ordinary-LWE algorithm. It does not establish a failure for every permitted parameter choice, every constant degree, or every consequence proposed in the target preprint. See [Interpretation](../science/interpretation.md) for the precise conclusion.

