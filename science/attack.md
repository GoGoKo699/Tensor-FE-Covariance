# From learned covariance to a distinguisher

The result combines exact recovery of a hidden integer Gram matrix with stable recovery of a rank-one matrix. Its security consequence is specific to the [quadratic experiment](model.md) and the dimension and width hypotheses below.

## 1. Main theorem

**Theorem (quadratic tensor-FE distinguisher).** Consider the degree-two construction of [CLÜW26](../references/RELATED_WORK.md#cluw26), with the selective-message interface in its Figure 1. Let

```math
L=\frac{k(k+1)}2-1,\qquad
d_0=nm+\widetilde m+m,\qquad
N_{\rm col}=m^2+\widetilde m+2(k+n+1)m.
```

Assume the following properties, all of which hold for the explicit asymptotic family in [Parameters](parameters.md).

1. The actual setup output is negligibly close to the corresponding marginal of the full spherical affine-lattice Gaussian extension described by the target's Theorem 2. Conditional on the setup matrices, its complete columns are independent.
2. Outside a negligible setup event, the common column lattice $\Lambda$ satisfies $\sigma/\sqrt2\ge\eta_{\epsilon}(\Lambda)$ for negligible $\epsilon$.
3. For a sufficiently large absolute constant $C$, the number of queried columns satisfies

```math
L\ge C\big[(10m+d_0)\log(2N_{\rm col}L)+\lambda\big].
```

4. The dimensions and $\sigma$ are polynomially bounded in $\lambda$. The width $\sigma$ is a rational input or admits polynomial-time certified interval approximation, so the measurement normalization can be computed to the required relative precision. The common encryption width satisfies $\chi\ge1$, with $\log\chi$ polynomially bounded; $m\ge\lambda$. The prescribed discrete Gaussian moments are computable to polynomial-bit precision.
5. The published correctness bounds give negligible failure of the balanced integer lift for every polynomial number of observations used here. All modulus and input bit lengths are polynomially bounded. A public encoded radius $R_0$ bounds the challenge $\|e\|_2^2$ except with negligible probability, with $\log R_0$ polynomially bounded.

Here $N_{\rm col}$ bounds the full preimage-column dimension, including the extra row used by the direct assumption experiment. It also dominates the structured-domain dimension $D=m(m+1)/2+d_0$ in [Gaussian measurements](gaussian_measurements.md), so the displayed measurement condition suffices for that theorem.

There is a classical probabilistic polynomial-time adversary making $L$ valid functional-key queries and polynomially many known-zero encryption observations such that

```math
\left|\Pr[\mathcal D(\mathrm{Enc}(0))=0]
      -\Pr[\mathcal D(\mathrm{Enc}(e_1))=0]\right|
 =1-\mathrm{negl}(\lambda).
```

The keys are the distinct monomials $x_ix_j$ with $i\le j$, excluding $x_1^2$. Every requested function has output zero on both messages. The success probability of guessing a uniformly random challenge bit is therefore $1-\mathrm{negl}(\lambda)$ as well. The adversary uses honest ciphertexts and the published functional keys; it never receives the hidden encryption matrices.

The theorem is an asymptotic polynomial-time statement. Its statistical and convex-optimization costs are included in the proof; it is not a claim that the resulting polynomial is small at practical parameters.

## 2. Recover the nuisance kernel

Use the notation of [Model](model.md). For zero training messages, the observed integer noise is

```math
z=\mathcal K(ee^{\mathsf T})+C^{\mathsf T}\widetilde e
      -H_s^{\mathsf T}(s\otimes e).
```

Let $v=v_\chi$ and $\mu_4=\mathbb E[e_i^4]$. For each pair of exposed columns, [Noise covariance](noise_covariance.md) proves the exact identity

```math
\mathrm{Cov}(z)=C_K+vC^{\mathsf T}C+v^2H_s^{\mathsf T}H_s,
```

with a completely known matrix $C_K$. The known mean is $v\mathrm{tr}(K_\ell)$ in coordinate $\ell$.

The estimator normalizes by $v$ before taking products. Its variance is bounded by a polynomial in the dimensions and a public high-probability bound on the short-key entries. It therefore estimates

```math
G=H_s^{\mathsf T}H_s
```

to entrywise error below $1/2$ using polynomially many training observations, even if $\chi$ is superpolynomial. Rounding recovers $G$ exactly with failure at most $2^{-\lambda}$, in addition to the setup, short-key-tail, and lifting errors. The number of training messages is chosen from public parameter bounds before setup, as the selective game requires.

Since $G$ is a real positive-semidefinite Gram matrix,

```math
\ker G=\ker H_s.
```

Exact rational linear algebra computes the orthogonal projector

```math
P:\mathbb R^L\longrightarrow\ker H_s\cap\ker C
```

from the public matrices $G,C$. For example, choose a rational full-row-rank basis $Q$ of the row span of $[G;C]$ and set

```math
P=I_L-Q^{\mathsf T}(QQ^{\mathsf T})^{-1}Q.
```

If that row span is zero, set $P=I_L$. The entries have polynomial bit length by determinant bounds for rational linear algebra. This construction does not estimate small eigenvalues numerically.

## 3. Joint geometry before projection

Let $J$ be the first-message mixed block. Define the full linear measurement operator

```math
\mathcal M(X,u,v,w)
 =\mathcal K(X)+H_s^{\mathsf T}u+C^{\mathsf T}v+J^{\mathsf T}w,
```

where $X$ is symmetric, $u\in\mathbb R^{nm}$, $v\in\mathbb R^{\widetilde m}$, and $w\in\mathbb R^m$. The relevant norm is

```math
\|(X,u,v,w)\|_\diamond^2
 =\|X\|_F^2+2\|u\|_2^2+\|v\|_2^2+2\|w\|_2^2.
```

Each mixed block is the sum of two distinct coordinates of the complete preimage column, which explains the factors of two. The four groups occupy disjoint coordinates. The [Gaussian measurement theorem](gaussian_measurements.md) proves, with negligible failure, that for all such tuples with $\mathrm{rank}X\le10$,

```math
(1-\delta_0)\|(X,u,v,w)\|_\diamond^2
\le \alpha^{-2}\|\mathcal M(X,u,v,w)\|_2^2
\le (1+\delta_0)\|(X,u,v,w)\|_\diamond^2,
\qquad \delta_0=\frac1{200},
```

where $\alpha=\sigma\sqrt{L/(2\pi)}$. The statement is simultaneous over the full structured set, so it remains valid for the projector subsequently computed from the same key material.

Choose a positive rational $a$ with $|a\alpha-1|\le1/1000$. As proved in [Reconstruction](reconstruction.md), the same joint bounds then hold at scale $a$ with distortion $\delta=1/100$. This requires only constant relative precision in the public normalization; all subsequent inputs and operations are rational. Put

```math
\mathcal A(X)=aP\mathcal K(X).
```

Orthogonal projection gives

```math
\|\mathcal A(X)\|_2
 =\inf_{u,v}\|a\mathcal M(X,u,v,0)\|_2.
```

The joint lower bound and the choice $u=v=0$ for the upper bound imply ordinary rank-10 restricted isometry of $\mathcal A$. This argument retains the dependence between $P$ and $K$. It does not replace the projected matrices by fresh Gaussian matrices.

## 4. Separate the challenge cases

Normalize the projected challenge noise as $y=aPz^*$. In case zero,

```math
y=\mathcal A(ee^{\mathsf T}).
```

The [reconstruction theorem](reconstruction.md) recovers $ee^{\mathsf T}$ exactly in polynomial bit complexity. Approximate nuclear-norm minimization achieves Frobenius error below $1/2$, and entrywise integer rounding therefore returns the exact matrix. Its final normalized residual is zero.

In case one,

```math
y=\mathcal A(ee^{\mathsf T})-aPJ^{\mathsf T}e.
```

For every symmetric matrix $Y$ of rank at most one, apply joint restricted isometry to $X=Y-ee^{\mathsf T}$, which has rank at most two. Taking the infimum over the nuisance vectors yields

```math
\|\mathcal A(Y)-y\|_2
\ge\sqrt{2(1-\delta)}\,\|e\|_2.
```

If $e\ne0$, it is an integer vector with norm at least one, so this residual is larger than one. Consequently **every** rank-one candidate fails the final test in case one, regardless of the behavior of the convex optimizer. An infeasible or unsuccessful optimization run is also rejected.

The exceptional event has probability

```math
\Pr[e=0]=\rho_\chi(\mathbb Z)^{-m}
\le (1+2e^{-\pi})^{-m},
```

using $\chi\ge1$. It is negligible for $m\ge\lambda$.

## 5. Algorithm and resource accounting

The distinguisher performs these operations in order:

1. Declare the zero training messages and challenge pair $(0,e_1)$, then request the fixed list of legal monomial keys.
2. Extract the integer noise vectors and estimate their normalized covariance with a median-of-means estimator.
3. Subtract the known covariance terms, round the hidden Gram, and construct the exact rational projector. Reject if consistency checks fail.
4. Choose the certified rational scale $a$, form the rational projected challenge data, and supply the public norm bound $R_0$.
5. Run the bounded, weak-feasibility convex procedure from [Reconstruction](reconstruction.md), round its output entrywise to integers, reject if the rounded matrix has rank greater than one, and accept case zero only if its exact rational squared residual is at most $1/16$.

The sample bound is explicit in [Noise covariance](noise_covariance.md). Arithmetic on ciphertexts costs polynomial time in $\log q$. Forming Gram entries and the projector costs polynomial time in $L$ and the entry bit lengths. The convex problem has polynomial dimension, a known outer radius with bit length $O(\log\chi+\log m)$, and fixed rational absolute tolerances. Its separation tests, integer rounding, exact rank test and final residual check use polynomial-bit rational arithmetic. The constant-relative-accuracy rational scale has polynomial encoding length. No runtime proportional to the numerical value of $\chi$ is used.

Let $\nu_{\rm setup},\nu_{\rm lift},\nu_{\rm key},\nu_{\rm iso},\nu_{\rm norm}$ denote the total setup-replacement, lifting, key-tail, joint-isometry, and challenge-norm failure probabilities in either experiment. Each is negligible in the stated family, including the polynomial union bounds. The two error probabilities are bounded respectively by

```math
\begin{aligned}
\Pr[\text{reject case zero}]
&\le\nu_{\rm setup}+\nu_{\rm lift}+\nu_{\rm key}+\nu_{\rm iso}+\nu_{\rm norm}+2^{-\lambda},\\
\Pr[\text{accept case one}]
&\le\nu_{\rm setup}+\nu_{\rm lift}+\nu_{\rm key}+\nu_{\rm iso}+\nu_{\rm norm}+2^{-\lambda}
  +\rho_\chi(\mathbb Z)^{-m}.
\end{aligned}
```

Adding these bounds proves the theorem. The bounds use a conservative accounting in which a Gram-learning failure may cause either decision; they do not assume the learner detects every failed estimate.

## 6. Consequence for the underlying assumption

Use all $k^2$ exposed columns in the direct assumption experiment described in [Model, Section 5](model.md#5-direct-tensor-assumption-interpretation). With all specified messages equal to zero, the two experiments again differ by the extra mixed block $J^{\mathsf T}e$. The same learner and decision rule apply, with the Gaussian theorem verified separately for the two setup lattices. This gives advantage $1-\mathrm{negl}(\lambda)$ against the degree-two secret-key tensor-preimage assumption in the stated parameter family.

The proof requires no algorithm for ordinary LWE and makes no claim to invalidate its hardness. The distinction is the additional, correlated short-preimage key material and the repeated known-message observations supplied by this construction. The [interpretation](interpretation.md) explains the parameter boundary and the role of large encryption noise.
