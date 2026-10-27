# Finite-bit reconstruction and decision

## Scope

This note proves the deterministic reconstruction step used after exact recovery of the hidden noise Gram matrix. It gives a polynomial-time Turing algorithm under an explicit joint restricted-isometry hypothesis. The proof accounts for rational projection, convex feasibility, objective accuracy, and the final decision. Its running time depends polynomially on the **bit length** of the encryption-noise scale.

The statistical recovery of the integer Gram matrix is treated in [noise_covariance.md](noise_covariance.md). The random-matrix argument establishing the restricted-isometry hypothesis is in [gaussian_measurements.md](gaussian_measurements.md), with parameter conditions in [parameters.md](parameters.md). Those probabilistic statements are separate from this deterministic result. In particular, this note does not replace the projected key matrices by independent Gaussian matrices.

The application is the degree-two construction of Cini, Lai, Ünal, and Woo [CLÜW26]. Their correctness calculation supplies an integer quadratic error term, a hidden bilinear term, and a known linear error term. The algebraic model below records precisely the information needed by the decoder.

## 1. Algebraic model and encoding

Let $`m,L\ge1`$. Let $`\mathrm{Sym}_m`$ denote the real symmetric $`m\times m`$ matrices, equipped with the Frobenius inner product and norm. For public integer matrices $`K_1,\ldots,K_L\in\mathbb Z^{m\times m}`$, define

```math
\mathcal K(X)_\ell=\langle K_\ell,X\rangle_F,
\qquad X\in\mathrm{Sym}_m.
\qquad\text{(1)}
```

The matrices $`K_\ell`$ need not be symmetric. Their symmetric parts define the same map on $`\mathrm{Sym}_m`$.

Let

```math
H_s\in\mathbb Z^{d_s\times L},\qquad
C\in\mathbb Z^{d_c\times L},\qquad
J\in\mathbb Z^{m\times L}.
```

In the notation of [the observation model](model.md), $`d_s=nm`$ and $`d_c=\widetilde m`$; the algebraic result permits arbitrary nuisance dimensions. Only $`C`$ and the exact integer Gram matrix

```math
G=H_s^{\mathsf T}H_s
\qquad\text{(2)}
```

are available to the decoder. Neither $`H_s`$ nor $`J`$ is needed as input.

The observation is an integer vector of one of the forms

```math
\begin{aligned}
z_0&=\mathcal K(ee^{\mathsf T})+H_s^{\mathsf T}u+C^{\mathsf T}v,\\
z_1&=\mathcal K(ee^{\mathsf T})+H_s^{\mathsf T}u+C^{\mathsf T}v-J^{\mathsf T}e,
\end{aligned}
\qquad\text{(3)}
```

where $`e\in\mathbb Z^m`$, while $`u,v`$ may be arbitrary real vectors consistent with an integer observation. No distributional property of $`u,v`$ is used in this note. A public integer $`R_0\ge1`$ bounds

```math
\|e\|_2^2\le R_0.
\qquad\text{(4)}
```

All supplied integers and rationals use binary encoding. Write $`B`$ for the total input encoding length, including $`K_\ell,C,G,z`$, the rational scale below, and $`R_0`$. An algorithm polynomial in $`B,m,L,d_c`$ may have a large polynomial exponent; no practical resource estimate is asserted here.

### Joint restricted isometry

The decoder receives a positive rational scale $`a`$. Assume that, for every symmetric $`X`$ of rank at most $`10`$ and all $`u,v,w`$,

```math
\begin{aligned}
(1-\delta)\bigl(\|X\|_F^2+2\|u\|_2^2+\|v\|_2^2+2\|w\|_2^2\bigr)
&\le
\left\|a\bigl(\mathcal K(X)+H_s^{\mathsf T}u+C^{\mathsf T}v+J^{\mathsf T}w\bigr)\right\|_2^2\\
&\le
(1+\delta)\bigl(\|X\|_F^2+2\|u\|_2^2+\|v\|_2^2+2\|w\|_2^2\bigr),
\end{aligned}
\qquad\text{(5)}
```

with $`\delta\le1/100`$. If $`m<10`$, the rank bound simply includes all symmetric matrices of the relevant ranks. The factors two correspond to adding two disjoint Gaussian preimage blocks in each mixed term.

Hypothesis (5) is an analytic promise. The decoder is not required to verify it or recover the hidden matrices.

### Rational normalization

In the Gaussian preimage application the natural scale is

```math
a_* = \frac{\sqrt{2\pi}}{\sigma\sqrt L}.
\qquad\text{(6)}
```

The algorithm never needs this irrational number exactly. If the unrounded joint RIP holds at scale $`a_*`$ with distortion at most $`1/200`$, choose a positive rational $`a`$ satisfying

```math
\left|a/a_*-1\right|\le 1/1000.
\qquad\text{(7)}
```

Then (5) holds with distortion at most $`1/100`$, because

```math
0.995(0.999)^2>0.99,
\qquad
1.005(1.001)^2<1.01.
```

For rational public $`\sigma>0`$, certified square-root and constant approximations construct such an $`a`$ with polynomial encoding length and time. Integer widths are sufficient for the parameter family in [parameters.md](parameters.md). More generally, a width supplied by certified polynomial-time rational intervals is sufficient. Approximation is only at the public normalization step; the subsequent projection and comparisons can use exact rational arithmetic.

## 2. The deterministic decision theorem

**Theorem 1.** Under (2), (4), and (5), there is a deterministic algorithm, polynomial in the binary input size and the dimensions, with the following properties.

1. On any observation $`z_0`$ in (3), it reconstructs $`ee^{\mathsf T}`$ exactly and outputs $`0`$.
2. On any observation $`z_1`$ in (3) with $`e\ne0`$, it outputs $`1`$.
3. It terminates in polynomial time on every encoded input, including inputs outside the promises. It makes no claim about its answer on such inputs.

The algorithm uses only $`K_\ell,C,G,z,a,R_0`$. After bounded convex reconstruction, it rounds the entries to integers, rejects if the resulting matrix has rank greater than one, and otherwise checks a rational squared residual against $`1/16`$. Rank is tested by exact integer arithmetic. It does not compute an approximate eigenvector, assume an eigenvalue gap, or solve exact semidefinite feasibility on arbitrary instances.

The exception $`e=0`$ in the second conclusion is necessary: in that case the two displayed forms coincide for the same nuisance vectors.

The proof occupies Sections 3–8. A probability statement for the cryptographic application follows in Section 9.

## 3. Exact rational removal of the nuisance subspace

Form the public integer matrix

```math
Q_G=G+C^{\mathsf T}C.
\qquad\text{(8)}
```

When (2) holds,

```math
\ker Q_G=\ker H_s\cap\ker C,
\qquad\text{(9)}
```

because $`x^{\mathsf T}Q_G x=\|H_s x\|_2^2+\|C x\|_2^2`$. Let $`\Pi`$ be the orthogonal projector onto this kernel.

The projector is rational and can be computed exactly. Choose a maximal independent set of rows of $`Q_G`$, forming an integer matrix $`V`$. Then

```math
\Pi=I-V^{\mathsf T}(VV^{\mathsf T})^{-1}V.
\qquad\text{(10)}
```

For $`Q_G=0`$, use $`\Pi=I`$. Fraction-free elimination finds $`V`$ and the inverse in polynomial bit complexity. If entries of $`Q_G`$ have at most $`b_Q`$ bits, entries of $`VV^{\mathsf T}`$ have $`O(b_Q+\log L)`$ bits, and Hadamard bounds its determinant and cofactors by integers with $`O(L(b_Q+\log L))`$ bits. Formula (10) therefore has polynomial numerator and denominator lengths. Small nonzero singular values cause no unbounded-precision issue: a rational matrix of bounded bit length has determinant/minor bounds of exactly the size accounted for here.

This step requires the **exact** recovered integer $`G`$. Thresholding the eigenvalues of an approximate covariance matrix is a different algorithm and is not used.

Define the rational map and data

```math
\mathcal A(X)=a\Pi\mathcal K(X),
\qquad b=a\Pi z.
\qquad\text{(11)}
```

The projector's range is orthogonal to $`\mathrm{im}H_s^{\mathsf T}+\mathrm{im}C^{\mathsf T}`$. Consequently,

```math
\|a\Pi[\mathcal K(X)+J^{\mathsf T}w]\|_2
=\inf_{u,v}\|a[\mathcal K(X)+H_s^{\mathsf T}u+C^{\mathsf T}v+J^{\mathsf T}w]\|_2.
\qquad\text{(12)}
```

Applying (5) uniformly before this infimum gives two facts.

**Projected RIP.** For every symmetric $`X`$ of rank at most $`10`$,

```math
0.99\|X\|_F^2\le\|\mathcal A(X)\|_2^2\le1.01\|X\|_F^2.
\qquad\text{(13)}
```

**Alternative-branch separation.** For every symmetric matrix $`Y`$ of rank at most one, an observation from the second line of (3) satisfies

```math
\begin{aligned}
\|\mathcal A(Y)-b\|_2^2
&\ge0.99\bigl(\|Y-ee^{\mathsf T}\|_F^2+2\|e\|_2^2\bigr)\\
&\ge1.98\|e\|_2^2.
\end{aligned}
\qquad\text{(14)}
```

Here $`\mathrm{rank}(Y-ee^{\mathsf T})\le2`$. If the integer vector $`e`$ is nonzero, the squared residual exceeds one. This soundness statement holds for every rank-one candidate, independently of how it was produced.

An explicit bound for the unrestricted operator norm will be useful. Set

```math
K_{\max}=\max_{\ell,i,j}|(K_\ell)_{ij}|,
\qquad M=1+\lceil a m L K_{\max}\rceil.
\qquad\text{(15)}
```

Then $`M\ge1`$ is an encoded integer and

```math
\|\mathcal A\|_{F\to2}\le a m\sqrt L K_{\max}\le M.
\qquad\text{(16)}
```

This global norm bound is derived from the input, not from low-rank RIP.

## 4. A robust nuclear-norm lemma

The following proof is a quantitative form of the usual nuclear-norm tangent-space argument [RFP10]. It applies within the symmetric matrix space.

**Lemma 2.** Suppose (13) holds. Let $`X_0\in\mathrm{Sym}_m`$ have rank at most one. If a symmetric $`\widehat X`$ satisfies

```math
\|\mathcal A(\widehat X-X_0)\|_2\le\eta,
\qquad
\|\widehat X\|_*\le\|X_0\|_*+\varepsilon,
\qquad\text{(17)}
```

then

```math
\|\widehat X-X_0\|_F\le3.1\eta+2\varepsilon.
\qquad\text{(18)}
```

**Proof.** Write $`H=\widehat X-X_0`$. If $`X_0\ne0`$, let $`P_0`$ project onto its one-dimensional image and put

```math
H_c=(I-P_0)H(I-P_0),\qquad H_0=H-H_c.
```

Then $`\mathrm{rank}H_0\le2`$, and $`H_0,H_c`$ are Frobenius-orthogonal. The nuclear norm is additive between $`X_0`$ and $`H_c`$. The triangle inequality and (17) give

```math
\|H_c\|_*\le\|H_0\|_*+\varepsilon
\le\sqrt2\|H_0\|_F+\varepsilon.
\qquad\text{(19)}
```

For $`X_0=0`$, take $`P_0=0`$, $`H_0=0`$; the same inequality holds.

Split the eigenvalues of $`H_c`$, in decreasing absolute value, into blocks of at most eight. Let $`H_1,H_2,\ldots`$ be the associated symmetric matrices. The standard block estimate is

```math
\sum_{j\ge2}\|H_j\|_F
\le\frac{\|H_c\|_*}{\sqrt8}
\le\frac12\|H_0\|_F+\frac\varepsilon{\sqrt8}.
\qquad\text{(20)}
```

To check the first inequality, every absolute eigenvalue in block $`j`$ is at most the average absolute eigenvalue of the preceding full block; sum the resulting estimates.

Set $`T=H_0+H_1`$. It has rank at most ten and satisfies $`\|H_0\|_F\le\|T\|_F`$. The triangle inequality, (13), and (20) imply

```math
\|\mathcal A(H)\|_2
\ge\left(\sqrt{0.99}-\tfrac12\sqrt{1.01}\right)\|T\|_F
-\sqrt{1.01}\frac\varepsilon{\sqrt8}.
\qquad\text{(21)}
```

Also $`\|H\|_F\le1.5\|T\|_F+\varepsilon/\sqrt8`$. The coefficient in parentheses in (21) exceeds $`0.49`$. Substitution yields (18), with deliberately loose constants. ∎

No matrix decomposition in this proof has to be computed by the decoder. It is an analysis of any matrix meeting (17).

## 5. Bounded semidefinite feasibility with an explicit interior ball

An unconditional claim that every rational SDP can be solved exactly in polynomial time would be insufficient here. Small feasible regions and boundary-only feasible points require care. The decoder uses only a bounded feasibility primitive with an explicit interior-ball guarantee on the branch where reconstruction must succeed.

Fix

```math
\eta=\varepsilon=\frac1{10000},
\qquad R=2(R_0+1),
\qquad
r=\min\left\{\frac\varepsilon{64m},\frac\eta{16M}\right\}.
\qquad\text{(22)}
```

For a rational level $`t\in[0,R]`$, define

```math
\mathcal F_t=\left\{(U,V)\in\mathrm{Sym}_m^2:
U,V\succeq0,\quad
\mathrm{tr}(U+V)\le t,\quad
\|\mathcal A(U-V)-b\|_2\le\eta
\right\}.
\qquad\text{(23)}
```

This is a convex semidefinite/second-order-cone feasibility problem. Use upper-triangular entries as rational coordinates; the dimension is

```math
n_{\rm var}=m(m+1).
```

If $`x`$ is the coordinate vector of $`(U,V)`$, then

```math
\|x\|_2^2\le\|U\|_F^2+\|V\|_F^2\le2\|x\|_2^2.
\qquad\text{(24)}
```

### Outer radius

Every point of $`\mathcal F_t`$ has coordinate norm at most $`R`$. Indeed, a positive-semidefinite matrix has Frobenius norm at most its trace, so

```math
\sqrt{\|U\|_F^2+\|V\|_F^2}
\le\mathrm{tr}U+\mathrm{tr}V\le t\le R.
\qquad\text{(25)}
```

### Interior radius on a zero-branch input

Suppose $`b=\mathcal A(X_0)`$ with $`X_0=ee^{\mathsf T}`$, and write $`S=\mathrm{tr}X_0=\|e\|_2^2\le R_0`$. For every

```math
t\ge S+\varepsilon/2,
\qquad\text{(26)}
```

the set $`\mathcal F_t`$ contains a coordinate Euclidean ball of radius $`r`$. Its center is the analytically specified, possibly unknown point

```math
U_0=X_0+\gamma I,\qquad V_0=\gamma I,
\qquad\gamma=\frac\varepsilon{8m}.
\qquad\text{(27)}
```

At this center the residual is zero, both PSD constraints have eigenvalue margin at least $`\gamma`$, and the trace is $`S+\varepsilon/4`$.

A coordinate perturbation of norm at most $`r`$ changes the product Frobenius norm by at most $`\sqrt2r`$. Therefore each PSD block remains positive definite: its operator perturbation is at most $`\sqrt2r<\gamma/2`$. The trace changes by at most $`2\sqrt m\,r\le\varepsilon/32`$. The difference $`U-V`$ changes in Frobenius norm by at most $`2r`$, so the residual changes by at most $`2Mr\le\eta/8`$. All constraints in (23) retain slack. This proves the claimed ball inclusion.

The center in (27) need not be known. The ellipsoid feasibility guarantee uses the known lower bound $`r`$ and the known outer radius $`R`$; it does not need the position of an interior ball.

### Exact rational separation

There is a polynomial-time strong separation oracle for (23).

- A trace violation gives the corresponding rational linear inequality.
- If $`U`$ or $`V`$ is not PSD, rational symmetric elimination produces a rational vector $`v`$ with $`v^{\mathsf T}Uv<0`$, or the analogous inequality for $`V`$. The linear functional $`W\mapsto v^{\mathsf T}Wv`$ separates the query from the feasible set.
- For a violated residual constraint, let $`f(U,V)=\|\mathcal A(U-V)-b\|_2^2`$. Its value and gradient at a rational query are rational. Convexity gives

```math
\langle\nabla f(x),y-x\rangle\le\eta^2-f(x)<0
\quad\text{for every feasible }y,
\qquad\text{(28)}
```

The gradient therefore provides a separating hyperplane. If the gradient vanishes while $`f(x)>\eta^2`$, the residual constraint is infeasible everywhere, and the oracle can report that directly.

PSD testing here needs neither floating-point eigenvalues nor a condition-number promise. A constructive rational test repeatedly takes a positive diagonal pivot and its Schur complement. A negative diagonal gives an immediate negative quadratic witness. If all remaining diagonal entries vanish but an off-diagonal entry is nonzero, a two-coordinate vector gives such a witness. Lifting a witness through a Schur complement preserves rationality. The entries and witnesses are ratios of bounded-size minors, so their bit lengths are polynomial in the matrix size and query encoding length.

### The bounded feasibility primitive

Use the rational, rounded ellipsoid method with the preceding strong separation oracle. Given $`t`$, it returns either

1. a rational point of $`\mathcal F_t`$, verified by the exact oracle; or
2. the conclusion that $`\mathcal F_t`$ contains no Euclidean ball of radius $`r`$.

The second outcome is **not** asserted to mean that $`\mathcal F_t`$ is empty. All sets encountered are contained in the radius-$`R`$ ball. Apply [GLS88, Theorem 3.2.1] with a rational volume threshold

```math
\nu=(r/n_{\rm var})^{n_{\rm var}}.
```

Its rounded ellipsoid algorithm either accepts an oracle query or encloses the feasible set in an ellipsoid of volume less than $`\nu`$. Supply the exact strong oracle above as its separation oracle: it reports membership only after verifying membership in $`\mathcal F_t`$, so the accepted query is exactly feasible, even though the general GLS interface permits approximate membership. A radius-$`r`$ Euclidean ball contains an axis-aligned cube of side $`2r/n_{\rm var}`$; its volume is therefore greater than $`\nu`$. The second GLS outcome certifies the required absence of such a ball.

The binary length of $`\nu`$ is polynomial in $`n_{\rm var}`$ and the encoding length of $`r`$. The volume-decrease argument gives a number of oracle calls polynomial in $`n_{\rm var}`$ and $`\log(R/r)`$. Rounded ellipsoid updates keep query encodings polynomial; together with the rational oracle this is a Turing-model polynomial bound. The role of interior radii and PSD separation is also discussed in [Lovász, Section 3.2].

For clarity, the method does not demand a hidden lower bound on the smallest eigenvalue of an arbitrary SDP optimum. The explicit padding (27) supplies all conditioning needed for completeness at the levels (26). A feasible set at a smaller level may be thin or empty; either behavior is harmless to the algorithm below.

## 6. Objective control by bisection

On input $`b`$, run the feasibility primitive at level $`R`$. If it returns no point, output $`1`$. Otherwise save its point, set $`\ell=0`$, $`h=R`$, and repeat until $`h-\ell\le\varepsilon/2`$:

1. Set $`t=(\ell+h)/2`$.
2. If a feasible point is returned at level $`t`$, set $`h=t`$ and save that point.
3. Otherwise set $`\ell=t`$.

Return $`\widehat X=U-V`$ from the saved point.

This procedure uses $`O(1+\log(R/\varepsilon))`$ feasibility calls. On a zero-branch input, $`R>S+\varepsilon/2`$, so the first call succeeds. Every failed call must have level strictly less than $`S+\varepsilon/2`$, by the ball guarantee. Thus throughout bisection $`\ell\le S+\varepsilon/2`$, and the final successful level obeys

```math
h\le S+\varepsilon.
\qquad\text{(29)}
```

Consequently the output satisfies

```math
\|\mathcal A(\widehat X)-b\|_2\le\eta,
\qquad
\|\widehat X\|_*\le\mathrm{tr}(U+V)\le\|X_0\|_*+\varepsilon.
\qquad\text{(30)}
```

The nuclear-norm inequality follows from $`U,V\succeq0`$ and the triangle inequality. Lemma 2 gives

```math
\|\widehat X-ee^{\mathsf T}\|_F
\le\frac{5.1}{10000}
=0.00051<\frac12.
\qquad\text{(31)}
```

This is the precise objective guarantee needed for decoding. The algorithm need not approximate the optimum of every arbitrary SDP instance. On an alternative-branch input, any output or failure is acceptable subject to the final residual check.

## 7. Exact integer rounding and the rank-one residual test

The integer-error model permits a particularly simple final step. Given the rational symmetric matrix $`\widehat X`$ from Section 6, round each entry to its nearest integer, using any fixed rule at exact ties:

```math
Y_{ij}=\mathrm{round}(\widehat X_{ij}).
\qquad\text{(32)}
```

The result is symmetric and integral. Compute its rank by exact fraction-free elimination. If $`\mathrm{rank}Y>1`$, output $`1`$ immediately. Otherwise output $`0`$ exactly when

```math
\|\mathcal A(Y)-b\|_2^2\le1/16.
\qquad\text{(33)}
```

Every operation in this step is rational or integer arithmetic. In particular, the rank comparison has no floating-point threshold. The squared residual in (33) is rational and is compared exactly.

On a zero-branch input, $`ee^{\mathsf T}`$ is an integer matrix, and (31) implies that every entry of $`\widehat X`$ is strictly less than $`1/2`$ away from the corresponding entry of $`ee^{\mathsf T}`$. Thus

```math
Y=ee^{\mathsf T},
\qquad
\mathrm{rank}Y\le1,
\qquad
\|\mathcal A(Y)-b\|_2=0.
\qquad\text{(34)}
```

This proves exact reconstruction and acceptance, including $`e=0`$.

On an alternative-branch input with $`e\ne0`$, there are three possible paths. Failure of the initial feasibility call outputs $`1`$. A rounded matrix of rank greater than one also outputs $`1`$. In the remaining case, $`Y`$ is symmetric and has rank at most one, so the uniform bound (14) gives

```math
\|\mathcal A(Y)-b\|_2^2
\ge1.98\|e\|_2^2\ge1.98>1/16.
\qquad\text{(35)}
```

The residual test therefore outputs $`1`$. This proves the correctness conclusions of Theorem 1. The test never infers soundness from approximate rank: it checks exact rank after rounding and then uses a separate uniform separation bound.

## 8. Bit complexity and absence of a hidden precision assumption

The preceding construction uses the following finite computations.

| Step | Required information | Bit-complexity control |
|---|---|---|
| Nuisance projection | Exact integer $`G,C`$ | Rational elimination and determinant bounds; polynomial numerator and denominator lengths |
| Normalization | Positive rational $`a`$ satisfying the prescribed constant relative precision | Polynomial-time certified approximation of public parameters |
| Feasibility oracle | Rational query $`(U,V)`$ | Exact traces, Schur complements, and quadratic residuals |
| Ellipsoid feasibility | Known $`R,r`$ and the oracle | Polynomial in dimensions, coefficient lengths, and $`\log(R/r)`$ |
| Objective search | Interval $`[0,R]`$, accuracy $`\varepsilon`$ | $`O(\log(R/\varepsilon))`$ feasibility calls |
| Integer reconstruction and decision | Rational $`\widehat X`$ | Exact entry rounding, fraction-free rank test, rational squared-residual comparison |

All calls are capped by the stated polynomial bounds, including on malformed or out-of-promise inputs. The algorithm may reject such an input immediately. In particular, an invalid Gram input can be rejected by an exact symmetry/PSD check, although passing that check is not a certificate that the statistically recovered Gram is correct.

From (22),

```math
\log(R/r)=O\bigl(\log(R_0+1)+\log m+\log(M+1)\bigr).
\qquad\text{(36)}
```

Every quantity on the right has polynomial input encoding length. The rational projected coefficients may have large denominators, but those denominators also have polynomial bit length. Rounding a polynomial-length rational changes its bit length by at most a polynomial amount. Fraction-free elimination on the rounded integer matrix and the final rational residual calculation therefore have polynomial bit complexity as well.

For an integer encryption width $`\chi_e`$, take $`R_0=\lceil m\chi_e^2\rceil`$ on the Gaussian norm event. Then

```math
\log R_0=O(\log m+\log\chi_e).
\qquad\text{(37)}
```

Thus the reconstruction algorithm has no factor polynomial in the **value** of $`\chi_e`$. Its dependence on that scale is polynomial in $`\log\chi_e`$, together with the bit lengths of the actual observed integers. In the FE application the raw observations are bounded by the modulus after the correct balanced lift, so their lengths are controlled by $`\log q`$.

This is a polynomial-time existence proof using the rounded ellipsoid method. It does not establish that a particular floating-point SDP package will meet the tolerances or that the resulting polynomial is practical.

## 9. Failure probabilities in the cryptographic application

Theorem 1 is deterministic once its promises hold. There is no additional numerical failure probability to hide in the security bound.

For experiment $`i\in\{0,1\}`$, let $`\beta_i`$ upper-bound the probability that at least one required event fails:

- the key/preimage distribution and joint RIP event used to justify (5);
- exact recovery of $`G=H_s^{\mathsf T}H_s`$, including the learning theorem's key-bound and sampling events;
- correct integer lifting of all training and challenge observations;
- the challenge norm bound $`\|e\|_2^2\le R_0`$.

A union bound is sufficient; independence between these events is not required. The statistical statement in [noise_covariance.md](noise_covariance.md) gives explicit contributions for exact Gram recovery and lifting. If that statement already includes a key-bound event, it should be counted once in $`\beta_i`$.

Let $`D_{\rm rec}`$ denote the decoder and let

```math
\theta_1=\Pr_1[e=0].
```

Then

```math
\Pr_0[D_{\rm rec}=0]\ge1-\beta_0,
\qquad
\Pr_1[D_{\rm rec}=0]\le\beta_1+\theta_1,
\qquad\text{(38)}
```

and the distinguishing gap is at least

```math
1-\beta_0-\beta_1-\theta_1.
\qquad\text{(39)}
```

For independent coordinates $`e_j\leftarrow D_{\mathbb Z,\chi_e}`$, with weights proportional to $`e^{-\pi x^2/\chi_e^2}`$,

```math
\theta_1=\rho_{\chi_e}(\mathbb Z)^{-m}\le\chi_e^{-m}
\quad(\chi_e\ge1),
\qquad\text{(40)}
```

where the inequality follows from Poisson summation. The standard norm bound, also stated as Lemma 3 of [CLÜW26], gives

```math
\Pr[\|e\|_2>\chi_e\sqrt m]\le2^{-m}.
\qquad\text{(41)}
```

Thus $`R_0=\lceil m\chi_e^2\rceil`$ contributes at most $`2^{-m}`$ to each relevant norm-failure budget. In the wide-noise parameter family, (40) is negligible as well. Choosing inverse-exponential statistical error budgets increases the number of median-of-means blocks only polynomially; this is separate from, and does not alter, the finite-bit reconstruction argument.

## 10. Interpretation and limits

The conclusion depends on joint RIP before projection and exact integer Gram recovery. It does not follow merely from having many projected quadratic equations. It also does not follow from a generic assertion that convex programs are efficient: the proof explicitly supplies the bounded level sets, separation oracle, interior-ball radius, objective guarantee, and final exact rational test.

The width of the encryption Gaussian can make an observation very large as a real number while leaving its binary representation polynomially long. The decoder uses that representation and a constant separation from the alternative rank-one image. Its residual and objective tolerances are fixed rational constants. The explicitly proved interior radius depends on the dimension and the encoded measurement coefficients, and the outer radius enters the running time only logarithmically.

The theorem is specific to the stated degree-two algebraic model. It does not assert that the joint RIP holds when the nuisance dimension approaches the number of available key coordinates, nor that raising the secret-randomizer dimension preserves the attack.

## References

- **[CLÜW26]** Valerio Cini, Russell W. F. Lai, Akın Ünal, and Ivy K. Y. Woo. *Lattice-based Secret-Key Functional Encryption for Constant-Degree Polynomials*. Cryptology ePrint Archive, Report 2026/1977. [Canonical record](https://eprint.iacr.org/2026/1977); [PDF mirror](https://eprint.iacr.asia/2026/1977.pdf). Relevant locations: Figure 5, the degree-two specialization of the correctness calculation in Appendix C.1, and Lemma 3.
- **[RFP10]** Benjamin Recht, Maryam Fazel, and Pablo A. Parrilo. *Guaranteed Minimum-Rank Solutions of Linear Matrix Equations via Nuclear Norm Minimization*. SIAM Review 52(3), 471–501, 2010. [Author-hosted PDF](https://www.mit.edu/~parrilo/pubs/files/RechtFazelParrilo-GuaranteedMinimumRankSolutionsOfLinearMatrixEquationsViaNuclearNormMinimization-SIAM.pdf). The tangent decomposition and restricted-isometry approach are standard; Lemma 2 above provides the particular approximate-reconstruction constants used here.
- **[GLS88]** Martin Grötschel, László Lovász, and Alexander Schrijver. *Geometric Algorithms and Combinatorial Optimization*. Springer, 1988. [Author-hosted PDF](https://www.zib.de/userpage/groetschel/pubnew/paper/groetschellovaszschrijver1988.pdf). Theorem 3.2.1 and its proof give the rounded central-cut ellipsoid algorithm with a small-volume alternative, including finite-bit rounding and oracle-polynomial running time. Chapters 3–4 develop the accompanying separation-oracle framework.
- **[Lovász]** László Lovász. *Semidefinite Programs and Combinatorial Optimization*, lecture notes, Section 3.2. [PDF](https://sites.math.washington.edu/~thomas/teaching/m514_web/Lovasz_semidef.pdf). Used for the standard PSD-separation and interior-radius context; the exact rational oracle and explicit padding needed here are given in Section 5 above.
