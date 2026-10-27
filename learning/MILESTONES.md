# Thirty milestones for the covariance-to-reconstruction argument

This map organizes the understanding needed for the project's degree-two tensor-FE result. Its targets describe the science and apply to any reader. The exact statements, proofs, assumptions and examples remain in the linked scientific pages.

The single educational anchor is **Chris Peikert, *A Decade of Lattice Cryptography*, the 2016 revision**. [The anchor map](ANCHOR.md) identifies the relevant source sections. [The source-to-project bridge](BRIDGE.md) translates notation and distinguishes those foundations from the statistical and matrix-recovery arguments supplied locally. Primary research references support attribution and proof dependencies throughout the scientific account.

## Allocation and reading structure

| Phase | Milestones | Scientific role |
|---|---|---|
| Background/preliminaries | M01–M14 | Assemble modular arithmetic, lattice sampling, statistics and matrix recovery into the security framework needed for the problem |
| Narrative/innovation | M15–M30 | Follow the legal observations through hidden-Gram learning, joint geometry and finite computation to the complete distinguishing result |

The **14/16 allocation** reflects the connection between three areas: lattice cryptography, statistical inference and low-rank matrix recovery. Fourteen background milestones give these ingredients a common language. Sixteen narrative milestones keep the distinct proof obligations visible while connecting them into one argument. M14 integrates the background; M30 integrates the contribution, its resources and its limits. The map targets global understanding of the result rather than every specialist calculation.

Dependencies name only earlier milestones. Source pointers distinguish the foundational route through [Peikert](ANCHOR.md) and the [local bridge](BRIDGE.md) from the project's authoritative statements. The [scientific account](../science/README.md) provides a direct route to those statements.

## Phase 1: Background and preliminaries

### M01: Modular information and binary size

**Phase:** Background/preliminaries.

**Central question:** What information does an integer linear relation retain after reduction modulo a public integer?

**Understanding target:** Interpret matrix-vector products over integers and modulo $q$, distinguish a residue from an integer representative, and explain when a balanced representative recovers a bounded integer. Distinguish the numerical magnitude of an integer from the number of bits used to encode it.

**Dependencies and story role:** None. This introduces the arithmetic objects and size conventions used by every later observation and runtime statement.

**Conceptual connection:** Correctness bounds can turn modular ciphertext arithmetic into observable integer noise; binary encoding determines whether processing that noise is efficient.

**Source pointers:** [Peikert §§2.1 and 2.4, via the anchor map](ANCHOR.md); [Model, §§1 and 3](../science/model.md); [Reconstruction, §8](../science/reconstruction.md).

### M02: Lattices, kernels and affine preimages

**Phase:** Background/preliminaries.

**Central question:** Why do solutions to a modular linear equation form a translated lattice?

**Understanding target:** Explain a lattice as the integer span of independent vectors, identify the lattice of homogeneous modular solutions, and describe a fixed-target solution set as an affine coset. Keep the integer lattice distinct from its real linear span and from the corresponding finite residue space.

**Dependencies and story role:** M01. Modular equations become geometric sets on which short-key distributions can be defined.

**Conceptual connection:** Functional keys satisfy modular preimage equations, while their sizes and statistical properties are analyzed as integer vectors in Euclidean space.

**Source pointers:** [Peikert §2.2.1, via the anchor map](ANCHOR.md); [Model, §2](../science/model.md); [Gaussian measurements, §§1 and 7](../science/gaussian_measurements.md).

### M03: Discrete Gaussian width, variance and tails

**Phase:** Background/preliminaries.

**Central question:** What does a Gaussian width specify when the random variable takes integer values?

**Understanding target:** Interpret weights proportional to $\exp(-\pi x^2/\chi^2)$, their normalization and their tail behavior. Distinguish the width $\chi$ from the exact variance $v_\chi$, and distinguish the encryption width $\chi$ from the short-preimage width $\sigma$.

**Dependencies and story role:** M01–M02. The geometric support now carries the probability laws used for both encryption errors and key columns.

**Conceptual connection:** Accurate covariance subtraction depends on the discrete distribution's actual moments; key geometry depends on a separate Gaussian scale.

**Source pointers:** [Peikert §2.3, via the anchor map](ANCHOR.md); [Model, §1](../science/model.md); [Noise covariance, §2](../science/noise_covariance.md).

### M04: Duality and smoothing of affine Gaussian laws

**Phase:** Background/preliminaries.

**Central question:** How can a discrete distribution on different lattice cosets have nearly the same Gaussian-scale behavior?

**Understanding target:** Explain the role of the dual lattice, Poisson summation and the smoothing parameter. Distinguish control of Gaussian mass across cosets from the stronger derivative estimates needed to control means and second moments.

**Dependencies and story role:** M02–M03. This connects an individual Gaussian law to a uniform statement over affine targets.

**Conceptual connection:** The later measurement theorem needs near-isotropy uniformly over the actual preimage cosets, including cosets selected by the public setup.

**Source pointers:** [Peikert §§2.2.1 and 2.3, via the anchor map](ANCHOR.md); [Gaussian measurements, §§1–2 and 7.1](../science/gaussian_measurements.md).

### M05: What cross-covariance records

**Phase:** Background/preliminaries.

**Central question:** What can joint fluctuations reveal that separate means and variances do not describe?

**Understanding target:** Distinguish means, second moments and covariances. Explain how independence and zero odd moments simplify products, and why quadratic expressions require a fourth moment as well as a variance.

**Dependencies and story role:** M03. The probability law is converted into statistics that can carry information about shared coefficients.

**Conceptual connection:** Different functional-key outputs use the same fresh encryption randomness, so their cross-covariances can reveal a common hidden matrix even though each output is noisy.

**Source pointers:** [Local statistical bridge](BRIDGE.md); [Noise covariance, §1](../science/noise_covariance.md); [Exact covariance check](../verification/check_covariance_identity.py).

### M06: Normalization, concentration and simultaneous estimation

**Phase:** Background/preliminaries.

**Central question:** When can a large-valued random observation be estimated accurately with a manageable number of samples?

**Understanding target:** Relate standardized moments to sampling error, explain the purpose of median-of-means estimation, and distinguish independence across fresh observations from dependence among coordinates of one observation. Account for simultaneous estimates with a union bound and separate statistical error from arithmetic error.

**Dependencies and story role:** M01, M03 and M05. A population identity becomes a candidate finite-data inference procedure.

**Conceptual connection:** The attack's sample count is controlled by normalized moments and short-key sizes, while the width of the raw integers enters the precision calculation through its encoded length.

**Source pointers:** [Local statistical bridge](BRIDGE.md); [Noise covariance, §§2–4 and 6](../science/noise_covariance.md).

### M07: Gram matrices and removable subspaces

**Phase:** Background/preliminaries.

**Central question:** What useful information about a matrix survives when only its Gram matrix is known?

**Understanding target:** Interpret $G=H^{\mathsf T}H$ through inner products and positive semidefiniteness, derive $\ker G=\ker H$, and explain orthogonal projection onto a common kernel. Distinguish identifying a nuisance subspace from identifying a particular hidden matrix factor.

**Dependencies and story role:** M01–M02. Pairwise numerical information is organized into a geometric object that supports exact elimination.

**Conceptual connection:** Covariance will reveal a Gram matrix; its kernel is precisely the information needed to remove the hidden bilinear contribution.

**Source pointers:** [Local matrix bridge](BRIDGE.md); [Reconstruction, §3](../science/reconstruction.md); [Main theorem, §2](../science/attack.md).

### M08: Quadratic lifting and rank-one structure

**Phase:** Background/preliminaries.

**Central question:** How does a quadratic expression become a linear measurement of a matrix?

**Understanding target:** Connect $e\otimes e$, $ee^{\mathsf T}$ and $e^{\mathsf T}Ke$. Explain the Frobenius inner product, the role of symmetrizing a measurement matrix, and why the lifted unknown is a positive-semidefinite matrix of rank at most one.

**Dependencies and story role:** M01 and M07. The algebra introduces the structured unknown that remains after nuisance elimination.

**Conceptual connection:** The attack can reconstruct a matrix encoding all quadratic products without recovering the sign of the original error vector.

**Source pointers:** [Local bridge to quadratic lifting](BRIDGE.md); [Model, §§1 and 4](../science/model.md); [Reconstruction, §1](../science/reconstruction.md).

### M09: Uniform geometry of structured measurements

**Phase:** Background/preliminaries.

**Central question:** What must a measurement map preserve to distinguish every low-rank explanation from a transverse error term?

**Understanding target:** Interpret restricted isometry as a simultaneous norm comparison over a structured set. Distinguish a statement about one fixed vector from a statement uniform over all low-rank matrices and nuisance coordinates, and explain why uniformity matters when a later operation depends on the same measurements.

**Dependencies and story role:** M06–M08. Local concentration and matrix structure are joined into the geometric promise needed for reconstruction.

**Conceptual connection:** The learned projector depends on the keys, so the proof must establish geometry before choosing that projector.

**Source pointers:** [Local matrix-recovery bridge](BRIDGE.md); [Gaussian measurements, main statement and §§3–5](../science/gaussian_measurements.md); [Reconstruction, §1](../science/reconstruction.md).

### M10: Convex recovery and finite computation

**Phase:** Background/preliminaries.

**Central question:** How can a continuous optimization description yield an algorithm on finitely encoded data?

**Understanding target:** Explain the nuclear norm, its positive-semidefinite split representation and the purpose of a convex relaxation. Distinguish a stable reconstruction theorem from a computational implementation, and identify the roles of bounded regions, separation oracles, interior radii and rational accuracy.

**Dependencies and story role:** M01 and M07–M09. The geometric promise is connected to algorithmic resources rather than only to existence of a low-rank fit.

**Conceptual connection:** A recovery argument must control both how accurately a matrix is determined and how many bits and operations are needed to obtain it.

**Source pointers:** [Local optimization bridge](BRIDGE.md); [Reconstruction, §§4–6 and 8](../science/reconstruction.md); [Matrix-recovery and optimization attribution](../references/RELATED_WORK.md#gaussian-and-matrix-recovery-foundations).

### M11: Ordinary LWE and the meaning of a security assumption

**Phase:** Background/preliminaries.

**Central question:** Which computational task does ordinary LWE assert is hard, and what changes when additional correlated information is supplied?

**Understanding target:** Describe noisy modular linear samples, distinguish secret recovery from distributional distinction, and interpret polynomial-time security and negligible advantage. Track the public information and distributions specified by an assumption before drawing a security conclusion.

**Dependencies and story role:** M01, M03 and M06. The arithmetic and probabilistic framework is placed inside a computational security claim.

**Conceptual connection:** The project studies a richer tensor-preimage experiment; its conclusion must be matched to that experiment's additional information.

**Source pointers:** [Peikert §§2.4, 4.2.1 and 4.2.2, via the anchor map](ANCHOR.md); [Related work: CLUW26](../references/RELATED_WORK.md#cluw26); [Interpretation](../science/interpretation.md).

### M12: Trapdoors and distributions of short preimages

**Phase:** Background/preliminaries.

**Central question:** How does a lattice trapdoor enable short preimages, and why does the distribution of those preimages matter?

**Understanding target:** Explain the difference between solving a modular preimage equation and sampling from a specified short-preimage distribution. Relate a short full-rank set to smoothing, and keep the public output distribution distinct from hidden variables used to analyze it.

**Dependencies and story role:** M02–M04 and M11. The security vocabulary is connected to the key-generation mechanism that supplies the later measurements.

**Conceptual connection:** The attack uses the source construction's ideal Gaussian extension through a statistical replacement of the public marginal, with hidden mixed blocks serving as analysis variables.

**Source pointers:** [Peikert §5.4 and Theorem 5.4.2, via the anchor map](ANCHOR.md); [Model, §2](../science/model.md); [Gaussian measurements, §7](../science/gaussian_measurements.md).

### M13: Functional encryption and permitted observations

**Phase:** Background/preliminaries.

**Central question:** What information may an adversary obtain when a functional key reveals only an authorized function of a message?

**Understanding target:** Explain functional keys, agreement of queried functions on two challenge messages, and the timing of a selective known-message experiment. Identify which ciphertexts, keys and arithmetic operations are available without access to the hidden encryption matrices.

**Dependencies and story role:** M08 and M11–M12. The mathematical objects are assembled into the operational security interface.

**Conceptual connection:** A statistical distinguisher matters only if its observations and functional-key requests are admitted by the actual experiment.

**Source pointers:** [Local bridge to functional encryption](BRIDGE.md); [Peikert §2.4 for the security background](ANCHOR.md); [Model, §§3–5](../science/model.md); [CLUW26 source map, Figure 1](../references/RELATED_WORK.md#cluw26).

### M14: Background synthesis—an interface, a distribution and an algorithm

**Phase:** Background/preliminaries.

**Central question:** Which separate ingredients must be specified before the proposed distinction can be evaluated as a cryptographic result?

**Understanding target:** Assemble the permitted observations, modular-to-integer passage, Gaussian sampling model, statistical inference problem, structured measurement geometry and finite computational resources into one framework. Identify which claims are algebraic, probabilistic, computational or assumptions imported from the construction.

**Dependencies and story role:** M04, M06–M10 and M13. This integrates the background into a complete set of obligations for the project-specific argument.

**Conceptual connection:** Legal access, correct distributions, sufficient information and efficient computation are separate conditions that the final proof must satisfy together.

**Source pointers:** [Anchor map](ANCHOR.md) and [complete bridge](BRIDGE.md); [Scientific account](../science/README.md); [Main theorem, §1](../science/attack.md).

## Phase 2: Narrative and innovation

### M15: A legal family of equal-output keys

**Phase:** Narrative/innovation.

**Central question:** Which many-key observation family agrees on the challenge messages while retaining useful joint information?

**Understanding target:** Explain the choices $x_0=0$ and $x_1=e_1$, zero training messages, and the distinct monomials $x_ix_j$ with $i\le j$ except $x_1^2$. Derive the count $L=k(k+1)/2-1$ and identify why every requested function is admissible.

**Dependencies and story role:** M08, M13 and M14. The general security interface becomes a concrete observation design.

**Conceptual connection:** Equality of authorized function values permits many simultaneous views of encryption noise, whose correlations remain available to the adversary.

**Source pointers:** [Model, §4](../science/model.md); [Main theorem, §§1 and 5](../science/attack.md); [CLUW26 source map](../references/RELATED_WORK.md#cluw26).

### M16: The exact observable integer noise

**Phase:** Narrative/innovation.

**Central question:** What integer does ciphertext arithmetic expose for each zero-output functional key?

**Understanding target:** Follow the quadratic expansion and the preimage relations to the exact factor $p^2$. Identify the known quadratic term, the auxiliary linear term, the hidden bilinear term and the extra challenge term in the observation model. State the bound under which balanced lifting returns this integer.

**Dependencies and story role:** M01, M08, M12 and M15. The observation design is reduced to a precise algebraic signal model.

**Conceptual connection:** The attack's statistics concern an explicitly computable integer derived from honest ciphertexts and functional keys.

**Source pointers:** [Model, §§2–4](../science/model.md); [Parameters, §3](../science/parameters.md); [Quadratic identity check](../verification/check_quadratic_identity.py).

### M17: Cross-covariance isolates the hidden Gram

**Phase:** Narrative/innovation.

**Central question:** Which part of the zero-message covariance contains the hidden mixed coefficients?

**Understanding target:** Derive the decomposition $\mathrm{Cov}(z)=C_K+vC^{\mathsf T}C+v^2G$, where $G=H_s^{\mathsf T}H_s$. Explain the vanishing cross terms, the known mean, the off-diagonal symmetrization of $K_\ell$, and the discrete fourth-moment correction inside $C_K$.

**Dependencies and story role:** M03, M05, M07 and M16. The algebraic observation is converted into a population identity containing an integer invariant.

**Conceptual connection:** Joint noise statistics determine the geometry needed for elimination even though the individual hidden mixed coefficients remain unknown.

**Source pointers:** [Noise covariance, §1](../science/noise_covariance.md); [Main theorem, §2](../science/attack.md); [Covariance identity check](../verification/check_covariance_identity.py).

### M18: Exact Gram learning at large Gaussian width

**Phase:** Narrative/innovation.

**Central question:** How can finitely many observations recover an integer Gram exactly when the encryption noise is superpolynomial in magnitude?

**Understanding target:** Connect normalization, standardized-moment bounds and median-of-means estimation to entrywise error below $1/2$. Account for certified computation of the discrete moments using dual theta sums, the finite-arithmetic budget and rounding. Track the common known Gaussian law and polynomial short-key bound, and explain why the sample schedule can be fixed from public bounds before setup.

**Dependencies and story role:** M03–M06, M15 and M17. The population identity becomes an efficient statistical procedure with explicit precision and failure guarantees.

**Conceptual connection:** Integrality converts controlled statistical accuracy into an exact algebraic object; normalization and binary arithmetic control the cost at large width.

**Source pointers:** [Noise covariance, §§2–6](../science/noise_covariance.md); [Theta-moment check](../verification/check_theta_moments.py); [Parameters, §5](../science/parameters.md).

### M19: Removing the nuisance image without factoring the Gram

**Phase:** Narrative/innovation.

**Central question:** How does the learned Gram remove hidden bilinear noise from a new observation?

**Understanding target:** Construct the orthogonal projector onto $\ker(G+C^{\mathsf T}C)=\ker H_s\cap\ker C$ using exact rational linear algebra. Explain why this removes both nuisance terms and why recovering a factor $H_s$ is unnecessary. Identify the remaining need to establish useful geometry for the projected quadratic measurements.

**Dependencies and story role:** M07, M16 and M18. The learned statistic is turned into an operation on challenge data.

**Conceptual connection:** An exact covariance invariant gives a usable subspace while leaving the hidden coefficients themselves unresolved.

**Source pointers:** [Reconstruction, §3](../science/reconstruction.md); [Main theorem, §2](../science/attack.md); [Noise covariance, §7](../science/noise_covariance.md).

### M20: The actual full-column Gaussian model

**Phase:** Narrative/innovation.

**Central question:** Which distributional statement about the source construction justifies a random-measurement argument?

**Understanding target:** Describe the full affine-lattice Gaussian extension and its public marginal. Explain conditional independence across columns, possible dependence within a column, and the smoothing bound obtained from a short full-rank set after appending the auxiliary block. Track the statistical replacement back to the real observation distribution.

**Dependencies and story role:** M02–M04, M12 and M16. The geometric argument is tied to the construction's actual sampling theorem.

**Conceptual connection:** The joint measurements inherit controlled moments and tails from a structured discrete Gaussian, with no need to assume independent coefficients inside each key.

**Source pointers:** [Model, §2](../science/model.md); [Gaussian measurements, §§1–2 and 7](../science/gaussian_measurements.md); [Peikert §§2.3 and 5.4, with Theorem 5.4.2, via the anchor map](ANCHOR.md).

### M21: Joint restricted isometry before projection

**Phase:** Narrative/innovation.

**Central question:** Why do the complete key columns preserve the geometry of low-rank matrices together with all nuisance directions?

**Understanding target:** Explain the isometric embedding of the tensor coefficients, including the factors of two from the mixed blocks. Connect fixed-vector concentration, a low-rank covering net and a whole-space norm bound to a uniform joint RIP statement. Identify the measurement-versus-nuisance inequality that makes the failure probability negligible.

**Dependencies and story role:** M06, M08–M09 and M20. The sampler model yields the uniform geometric theorem needed after a data-dependent projection.

**Conceptual connection:** Uniformity over the full structured set keeps the later learned projector inside the proven event.

**Source pointers:** [Gaussian measurements, main theorem and §§3–6](../science/gaussian_measurements.md); [Main theorem, §3](../science/attack.md).

### M22: A rank-one image and a separated alternative

**Phase:** Narrative/innovation.

**Central question:** What geometric distinction remains between the two challenge cases after nuisance projection?

**Understanding target:** Obtain the projected lower bound by taking an infimum over nuisance vectors. Explain why the zero case is a measurement of $ee^{\mathsf T}$, while the alternative contains a residual term separated from every symmetric rank-at-most-one fit. Distinguish this rank-two separation argument from the higher RIP order used for reconstruction.

**Dependencies and story role:** M08–M09, M16, M19 and M21. Projection and joint geometry combine into the decisive structural separation.

**Conceptual connection:** The proof handles the dependence between keys and projector by establishing the bound uniformly before projection.

**Source pointers:** [Gaussian measurements, §8](../science/gaussian_measurements.md); [Reconstruction, §3](../science/reconstruction.md); [Main theorem, §§3–4](../science/attack.md).

### M23: Stable recovery through a nuclear-norm bound

**Phase:** Narrative/innovation.

**Central question:** Why does an approximately optimal, approximately fitting matrix have to be close to the true rank-one matrix?

**Understanding target:** Explain the tangent-space and spectral-block decomposition in the robust nuclear-norm lemma. Track the roles of measurement error and objective slack, and explain why a rank-two tangent part plus a rank-eight block makes rank-10 RIP sufficient for the stated stability bound.

**Dependencies and story role:** M08–M10 and M22. Geometric uniqueness is strengthened into stable recovery suitable for a finite-accuracy algorithm.

**Conceptual connection:** A quantitative error bound supplies the accuracy target for computation and, ultimately, exact integer reconstruction.

**Source pointers:** [Reconstruction, §4](../science/reconstruction.md); [Matrix-recovery attribution](../references/RELATED_WORK.md#gaussian-and-matrix-recovery-foundations).

### M24: Bounded convex feasibility with polynomial bit complexity

**Phase:** Narrative/innovation.

**Central question:** How is the stable-recovery argument implemented without an idealized exact SDP oracle?

**Understanding target:** Explain rational normalization, PSD split variables, the known outer radius and the padded interior ball. Follow exact separation, the rounded-ellipsoid small-volume alternative and objective bisection. Distinguish an unsuccessful search for a ball of prescribed radius from proof that a feasible set is empty.

**Dependencies and story role:** M01, M10, M19 and M23. The recovery promise is converted into a terminating algorithm with controlled bit lengths.

**Conceptual connection:** Explicit geometric slack makes the required feasibility calls efficient even when the recovered matrix and encryption width have very large numerical values.

**Source pointers:** [Reconstruction, §§1, 5–6 and 8](../science/reconstruction.md); [Optimization attribution](../references/RELATED_WORK.md#gaussian-and-matrix-recovery-foundations).

### M25: Integer rounding and an exact decision

**Phase:** Narrative/innovation.

**Central question:** How does a small matrix-reconstruction error become a sound distinction between the two experiments?

**Understanding target:** Explain why Frobenius error below $1/2$ permits exact entrywise recovery of the integer matrix $ee^{\mathsf T}$. Follow the rejection of rounded rank greater than one and the final rational residual comparison. Identify why the alternative bound applies to every candidate and why $e=0$ remains an explicit exception.

**Dependencies and story role:** M08, M22–M24. The geometric and computational arguments become a complete decision rule.

**Conceptual connection:** Integrality strengthens approximate recovery into an exact output, while uniform residual separation controls all unsuccessful or misleading fits on the alternative branch.

**Source pointers:** [Reconstruction, §§2 and 7](../science/reconstruction.md); [Main theorem, §4](../science/attack.md); [Integer-recovery check](../verification/check_integer_recovery.py).

### M26: The complete probability and access accounting

**Phase:** Narrative/innovation.

**Central question:** How do the separate statistical and geometric guarantees imply advantage $1-\mathrm{negl}(\lambda)$ in the permitted experiment?

**Understanding target:** Combine setup replacement, key tails, exact Gram learning, joint RIP, correct lifting and the challenge norm bound in one failure ledger. Include the zero-error event and explain why a union bound needs no independence among these events. Keep moment identities in the unwrapped model and transfer observations through a separate coupling bound.

**Dependencies and story role:** M15–M16, M18, M20–M21 and M25. The conditional component results are assembled into the security theorem with the correct interface and error budget.

**Conceptual connection:** A nearly certain decision on the good events becomes a valid probabilistic adversary only after every exceptional event and permitted resource is accounted for.

**Source pointers:** [Main theorem, §§1 and 5](../science/attack.md); [Reconstruction, §9](../science/reconstruction.md); [Noise covariance, §5](../science/noise_covariance.md).

### M27: A compatible asymptotic parameter family

**Phase:** Narrative/innovation.

**Central question:** Can the sampling, measurement, correctness and resource requirements hold simultaneously within the source construction's numerical constraints?

**Understanding target:** Follow the explicit family with $k=\lambda^2$ and $T=2^{\lceil\log_2\lambda\rceil^2}$. Compare the number of keys with the nuisance dimension, check smoothing and lifting slack, and explain how polynomial total cost coexists with superpolynomial noise and modulus. Interpret the compactness bound and the sufficiently-large-parameter qualification.

**Dependencies and story role:** M18, M20–M21, M24 and M26. The theorem's hypotheses are shown to describe a nonempty regime.

**Conceptual connection:** Numerical admissibility, asymptotic efficiency and conjectured ordinary-LWE hardness are distinct claims; the family checks the first two while preserving the distinction from the third.

**Source pointers:** [Parameters, §§1–6](../science/parameters.md); [Main theorem, §1](../science/attack.md); [CLUW26 source map, Table 1](../references/RELATED_WORK.md#cluw26).

### M28: What the reproducible evidence establishes

**Phase:** Narrative/innovation.

**Central question:** Which parts of the argument can finite computations check, and which require the analytical proofs?

**Understanding target:** Match the covariance, quadratic-identity, theta-moment and integer-recovery checks to their precise algebraic claims. Explain the limits of finite-law enumeration, selected numerical widths and perturbation examples, and identify where sampling concentration, asymptotic geometry and optimizer complexity are proved.

**Dependencies and story role:** M16–M18 and M23–M27. The evidence supporting the connected argument is organized by what each method actually establishes.

**Conceptual connection:** Reproducibility makes specific formulas inspectable, while the probability and complexity theorems support claims beyond the finite examples.

**Source pointers:** [Verification guide](../verification/README.md); [Scientific account](../science/README.md); [Reconstruction, §8](../science/reconstruction.md).

### M29: Attribution, security scope and boundaries

**Phase:** Narrative/innovation.

**Central question:** What does the established result add, and which broader conclusions remain outside it?

**Understanding target:** Identify the inherited noise-statistical and matrix-recovery ingredients and the connection established for this affine-lattice Gaussian model. Distinguish the permitted-key FE conclusion from the separately checked direct tensor-assumption conclusion. State the measurement, degree and parameter boundaries, the prior-source access limits, and the absence of a practical attack-cost claim. Keep ordinary LWE and the source's degree-one reduction outside the claimed consequence.

**Dependencies and story role:** M11–M14 and M26–M28. The complete argument is placed in its scientific and cryptographic context.

**Conceptual connection:** The result concerns additional correlated short-preimage key material; its scope is determined by the stated experiment and parameter regime.

**Source pointers:** [Interpretation](../science/interpretation.md); [Sources and related work](../references/RELATED_WORK.md); [Model, §5](../science/model.md); [Main theorem, §6](../science/attack.md).

### M30: Final synthesis—covariance, geometry and finite distinction

**Phase:** Narrative/innovation.

**Central question:** Why does the whole argument give an efficient distinction despite the deliberately large encryption noise?

**Understanding target:** Present the complete chain: legal equal-output keys expose integer noise; normalized cross-covariance yields an exact hidden Gram; its kernel removes nuisance terms; joint geometry separates the two projected cases; finite-bit reconstruction and integer rounding implement the test. State the resulting security conclusion together with its assumptions, resources, probability guarantees and boundaries.

**Dependencies and story role:** M14 and M26–M29, with the component arguments integrated through their dependencies. This is the final synthesis of the scientific contribution.

**Conceptual connection:** Statistical normalization, algebraic integrality, uniform measurement geometry and encoded computation jointly explain why large numerical noise fails to protect this particular many-key regime.

**Source pointers:** [Main theorem](../science/attack.md); [Interpretation](../science/interpretation.md); [Parameters](../science/parameters.md); [Source-to-project bridge](BRIDGE.md).
