# From noisy functional outputs to an exact hidden kernel

Suppose encrypted records are accompanied by keys that reveal selected products of their coordinates. The permitted products can be identical for two records, yet the ciphertext and key arithmetic may expose more structure than those final products. This project asks whether repeated encryptions of a known record reveal a fixed relation among the keys, and whether that relation helps distinguish a fresh encrypted record.

The answer in the stated parameter regime has three stages: learn a hidden Gram matrix from covariance, remove the nuisance subspace it identifies, and test whether the remaining measurements have a rank-one explanation. This page develops that connection. [Peikert's survey](ANCHOR.md) supplies the lattice and Gaussian background; the linked scientific pages contain the exact statements and proofs.

## 1. The information the experiment permits

A functional-encryption key for a function $f$ permits the holder to compute $f(x)$ from an encryption of $x$. In the experiment studied here, the adversary declares two challenge messages and known training messages before setup. It can obtain keys only for functions that agree on the two challenge messages.

Choose $x_0=0$ and $x_1=e_1$, where $e_1$ is the first standard basis vector in the $k$-dimensional message space. Request the monomials $x_i x_j$ with $i\le j$, omitting $x_1^2$. Every requested function is zero on both messages. For example, when $k=3$, the five allowed products are $x_1x_2$, $x_1x_3$, $x_2^2$, $x_2x_3$ and $x_3^2$. This small example illustrates legality; the theorem uses a growing dimension family.

The adversary also receives polynomially many honest encryptions of the known zero message. It uses the same functional keys across these observations. That fixed key material is what makes cross-covariance informative. No decryption oracle or hidden setup matrix is supplied. [Model §4](../science/model.md#4-legal-selective-message-access) specifies the access and query count.

## 2. A permitted product exposes an integer noise

For a key indexed by $\ell$, the public ciphertext/key arithmetic produces the authorized product plus $p^2z_\ell$ modulo $q$. Here $p$ is a small scaling integer, $q$ is the ciphertext modulus, and $z_\ell$ is an integer noise. The factor is $p^2$ because the mixed quadratic expansion supplies one factor of $p$ and its preimage relation supplies another.

Every queried product is known to be zero on the training and challenge messages. When the correctness bound guarantees that the intermediate integer has not wrapped modulo $q$, the balanced representative of the observable residue, divided by $p^2$, is exactly $z_\ell$. The [model derivation](../science/model.md#3-ciphertexts-and-the-observable-integer-noise) proves this identity and charges the probability of an unsuccessful lift separately.

Collect the $L$ noises from one ciphertext into a column vector $z$. The complete observation equation is

```math
z=\mathcal K(ee^{\mathsf T})+C^{\mathsf T}\widetilde e
  -H_s^{\mathsf T}(s\otimes e)-bJ^{\mathsf T}e.
```

The known quadratic measurement map is

```math
\mathcal K(X)_\ell=\langle K_\ell,X\rangle_F.
```

The symbols have distinct roles:

| Object | Role |
|---|---|
| $e\in\mathbb Z^m$ | Fresh primary encryption error |
| $s\in\mathbb Z^n$, $\widetilde e\in\mathbb Z^{\widetilde m}$ | Fresh randomizer and auxiliary error |
| $K_\ell$, $C$ | Known quadratic and auxiliary functional-key coefficients |
| $H_s$ | Fixed hidden coefficients of the randomizer–error products |
| $J$ | Fixed hidden coefficients associated with the first message coordinate |
| $b\in\{0,1\}$ | Zero for training; the challenge message is $be_1$ |

The sampled matrix $K_\ell$ need not be symmetric. The identity $\langle K_\ell,ee^{\mathsf T}\rangle_F=e^{\mathsf T}K_\ell e$ still holds. The vector $e_1$ naming a message and the fresh error vector $e$ are different objects.

## 3. Covariance reveals a fixed relation

For training messages, $b=0$. Condition on all key material and vary only the fresh encryption randomness. Its coordinates are independent, centered discrete Gaussians of common variance $v=v_\chi$. The quadratic term has known mean $v\,\mathrm{tr}(K_\ell)$ and a covariance $C_K$ computable from the known $K_\ell$, $v$, and the exact fourth moment.

The auxiliary linear term contributes $vC^{\mathsf T}C$. For the hidden bilinear term, independence gives

```math
\mathbb E[s_a e_i s_b e_j]
=v^2\,\mathbf1_{a=b}\mathbf1_{i=j}.
```

Its covariance is therefore $v^2H_s^{\mathsf T}H_s$. Cross terms vanish because a remaining independent factor has mean zero. Combining the terms gives

```math
\mathrm{Cov}(z)=C_K+vC^{\mathsf T}C+v^2G,
\qquad G=H_s^{\mathsf T}H_s.
```

The unknown $G$ is a Gram matrix: its entries are inner products between hidden key columns. Those entries are integers. The exact formula for $C_K$ in [Noise covariance §1](../science/noise_covariance.md#1-exact-covariance) includes the discrete fourth-moment correction. Using a continuous-Gaussian approximation without an error bound would invalidate the exact subtraction.

This calculation uses independence of encryption coordinates. It makes no independence assumption about coordinates within a fixed functional-key column. It is also performed in the unwrapped integer model, with the lifting failure handled by a coupling bound rather than by conditioning the noise distribution.

## 4. Wide noise and precise learning can coexist

The raw covariance grows with the encryption width. The estimator first forms

```math
Y_\ell=z_\ell/v-\mathrm{tr}(K_\ell).
```

Then $\mathbb E[Y_\ell Y_j]$ is a known normalized term plus $G_{\ell j}$. The standardized encryption coordinates have bounded moments independent of their width. Consequently, the variance of each covariance estimator is polynomially bounded in the dimensions and a bound on the short-key entries. The sample count depends on those quantities; it does not grow polynomially in the numerical value of a possibly enormous encryption width.

The proof uses block averages and a median of those averages. It budgets error from sampling, finite arithmetic and known-term subtraction, each at most $1/8$. The resulting error is at most $3/8$ per entry. Rounding to the nearest integer recovers $G$ exactly, simultaneously over all its entries, except with the stated small failure probability.

There is still a precision cost. Exact discrete moments must be approximated accurately enough, and input integers must be represented. The dual theta formulas in [Noise covariance §6](../science/noise_covariance.md#6-computing-discrete-moments-with-polynomially-many-bits) give a cost polynomial in the required number of bits and $\log\chi$. Normalization controls the sample count; certified arithmetic controls the bit cost. Both are needed.

## 5. A worked projection example

For any real vector $a$,

```math
a^{\mathsf T}Ga=\|H_sa\|_2^2.
```

Thus $\ker G=\ker H_s$. Learning the Gram matrix gives the hidden kernel even when the hidden matrix itself remains unknown. Taking the orthogonal projector $P$ onto $\ker G\cap\ker C$ removes both nuisance terms:

```math
Pz=P\mathcal K(ee^{\mathsf T})-bPJ^{\mathsf T}e.
```

Here is a complete two-coordinate example of that operation. Suppose covariance subtraction and rounding have produced

```math
G=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad C=0.
```

The kernel consists of vectors proportional to $(1,-1)^{\mathsf T}$, so

```math
P=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
```

Let the quadratic signal be $q_{\star}=(4,1)^{\mathsf T}$ and subtract the nuisance term $3(1,1)^{\mathsf T}$. The observed vector is $z=q_{\star}-3(1,1)^{\mathsf T}=(1,-2)^{\mathsf T}$. Direct multiplication gives

```math
Pz=\begin{pmatrix}3/2\\-3/2\end{pmatrix}
=Pq_{\star}.
```

The hidden nuisance has disappeared. The projection has also discarded one signal direction: this example retains only the difference between the two signal coordinates. That loss explains why cancellation alone is insufficient. The full theorem needs enough remaining measurements to determine the relevant low-rank matrix. This toy calculation illustrates the kernel operation, not the full sampler, parameter family or recovery theorem.

Because $G$ and $C$ are exact integer matrices, a rational basis for their row span gives an exact rational projector. The method does not need to infer a kernel by thresholding numerically small eigenvalues. [Main theorem §2](../science/attack.md#2-recover-the-nuisance-kernel) gives the construction.

## 6. Why enough useful measurements survive

For $b=0$, the projected observation has a rank-one positive-semidefinite explanation, namely $X_0=ee^{\mathsf T}$. A matrix of this form has only order $m$ degrees of freedom, although it occupies an $m$ by $m$ array. That low-rank structure makes recovery from fewer than $m^2$ measurements plausible. It does not by itself prove recovery.

The measurement matrices and the learned projector come from the same correlated keys. The proof therefore starts before projection. It proves a simultaneous restricted-isometry bound for the joint operator

```math
\mathcal M(X,u,v,w)
=\mathcal K(X)+H_s^{\mathsf T}u+C^{\mathsf T}v+J^{\mathsf T}w,
```

on rank-at-most-ten symmetric $X$ and arbitrary nuisance vectors. Restricted isometry means that the measured norm stays within a controlled factor of the appropriate input norm. The weights on the mixed blocks account for their sums of two full-column coordinates.

The [Gaussian measurement proof](../science/gaussian_measurements.md) establishes this bound for the actual ideal affine-lattice extension, using smoothing, moment estimates, concentration and a uniform covering argument. Different columns are independent conditional on the setup; coordinates within a column may remain dependent. Passing from the ideal extension to actual exposed keys costs the source theorem's statistical-distance error.

The uniform joint bound can then be minimized over nuisance vectors, which is exactly what orthogonal projection does. At a computable rational scale $a$, the surviving operator $\mathcal A(X)=aP\mathcal K(X)$ has the restricted isometry required for recovery. Under the other challenge message, the extra $PJ^{\mathsf T}e$ contribution remains separated from every rank-one explanation when $e\ne0$. Both conclusions use the same joint geometry, so no new independence is assumed after learning $P$.

## 7. From approximate recovery to an exact decision

A real-valued optimization argument is not yet a polynomial-time algorithm on encoded inputs. The [reconstruction proof](../science/reconstruction.md) specifies rational data, an encoded radius, a bounded convex feasibility problem, exact separating tests, a certified interior-ball radius and a finite-bit ellipsoid procedure.

The convex formulation represents a symmetric matrix as $X=U-V$ with $U,V$ positive semidefinite. Minimizing $\mathrm{tr}(U)+\mathrm{tr}(V)$ controls the nuclear norm, the sum of singular values. The measurement constraint allows a fixed small error. Restricted isometry connects that objective and feasibility to closeness to the true rank-one matrix in the zero branch.

With the stated tolerances $\eta=\varepsilon=10^{-4}$, the proof obtains

```math
\|\widehat X-ee^{\mathsf T}\|_F
\le3.1\eta+2\varepsilon=0.00051<\frac12.
```

Every entry of $ee^{\mathsf T}$ is an integer, and entrywise error is no larger than Frobenius error. Nearest-integer rounding therefore recovers the entire matrix exactly. For example,

```math
\begin{pmatrix}4.0002&1.9999\\1.9999&1.0001\end{pmatrix}
\quad\longmapsto\quad
\begin{pmatrix}4&2\\2&1\end{pmatrix}
=\begin{pmatrix}2\\1\end{pmatrix}
 \begin{pmatrix}2&1\end{pmatrix}.
```

This example shows the rounding operation. The theorem supplies the error bound for its own input distribution. A fixed absolute error below $1/2$ is enough even when the integer entries are very large; their bit lengths still enter the computation cost.

The final decision checks the rounded matrix's rank and its exact rational residual. A zero-branch observation passes with the proved probability. In the other branch, the geometric separation makes every rank-at-most-one candidate fail when $e\ne0$, regardless of how the optimizer behaves on that branch. The event $e=0$ is bounded separately. This avoids treating a numerical optimizer's output or failure as a security argument.

## 8. The dimensions and resources must fit together

The mechanism needs many more key measurements than effective nuisance degrees of freedom, with room for concentration. It also needs polynomial short-key width, common encryption widths, smoothing, correct integer lifts and polynomial input bit lengths. A list of individually plausible assumptions would leave open whether any permitted family satisfies all of them.

[Parameters](../science/parameters.md) supplies an explicit family. With $k=\lambda^2$, the number of selected monomial keys is $\Theta(\lambda^4)$, while the effective nuisance dimension is $\Theta(\lambda^3\log^2\lambda)$. The measurement surplus eventually absorbs the logarithmic factors in the geometry theorem. The short-key width is polynomial in $\lambda$, while the modulus and encryption width may have superpolynomial numerical size and still have polynomial bit length.

The full accounting includes the training samples, key queries, moment precision, exact linear algebra, convex feasibility and the final decision. Its conclusion is asymptotic polynomial time, not a practical cost estimate. The parameter page also checks the target's numerical safeguards and ciphertext compactness. The ordinary-LWE hardness rows remain assumptions; this argument does not prove or refute them.

## 9. Assemble the conclusion and its boundary

The [main theorem](../science/attack.md) combines the ideal-output approximation, setup and key-tail events, integer lifting, Gram estimation, measurement geometry and challenge norm bound. A union bound combines their failure probabilities without asserting independence. It yields a distinguishing gap $1-\mathrm{negl}(\lambda)$ for the specified degree-two FE family and the corresponding direct tensor-preimage assumption experiment.

The general lesson is that increasing fresh noise does not automatically hide a fixed algebraic covariance pattern. In this construction, normalized observations reveal an integer kernel, and the remaining low-rank structure supplies a decision rule. Applying that reasoning elsewhere requires checking the actual access model, moment law, geometry and encoded resource costs again.

Earlier work already studies noise-based FE attacks, many-key observations and structured distinctions; low-rank matrix recovery and finite convex optimization also have established sources. [Related work](../references/RELATED_WORK.md) separates those ingredients from this project's connection and records the limits of the literature inspection. The scope does not extend to every parameter choice, every polynomial degree, ordinary LWE, or practical timings.

For reproducible local calculations, run `python3 verification/run_all.py` from the repository root. The four checks cover the exact covariance identity, modular quadratic expansion, dual theta formulas and integer rounding examples. They do not implement the full cryptosystem or the ellipsoid decoder and do not replace the probability and complexity proofs.

[Learning route](README.md) · [Anchor](ANCHOR.md) · [Milestones](MILESTONES.md) · [Scientific index](../science/README.md)
