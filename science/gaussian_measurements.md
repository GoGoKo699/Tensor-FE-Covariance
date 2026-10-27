# Gaussian cosets and joint restricted isometry

## Scope and main statement

This note proves the probability estimate used for the quadratic tensor measurements. Its input is a spherical discrete Gaussian on an affine lattice. Its conclusion is a restricted-isometry statement for a low-rank symmetric matrix together with arbitrary linear nuisance coordinates. The affine cosets may differ between measurement rows. Independence is required across rows, conditional on the setup; independence of coordinates within a row is not required.

All constants below are deliberately conservative. In particular, the logarithmic overhead in the measurement count is convenient rather than optimized.

Let

```math
\mathcal V=\mathrm{Sym}_m(\mathbb R)\oplus\mathbb R^{d_0},
\qquad
\|(X,z)\|_{\mathcal V}^2=\|X\|_F^2+\|z\|_2^2,
```

and put

```math
D=\frac{m(m+1)}2+d_0,
\qquad \kappa=r(m+1)+d_0.
```

**Theorem 1 (joint restricted isometry).** Suppose that

- $1\le r\le m$, $0<\delta\le 1/2$, and $0<\varepsilon\le\delta/24$;
- $\Lambda\subset\mathbb R^N$ is a full-rank lattice and $\sigma/\sqrt2\ge\eta_\varepsilon(\Lambda)$;
- $\iota:\mathcal V\longrightarrow\mathbb R^N$ is a fixed linear isometry;
- $W_1,\ldots,W_L$ are independent, with
  $W_\ell\sim D_{\Lambda+c_\ell,\sigma}$, for arbitrary fixed cosets $c_\ell$.

Define the normalized linear map

```math
[\mathcal A(X,z)]_\ell
=\frac{\sqrt{2\pi}}{\sigma\sqrt L}
  \langle W_\ell,\iota(X,z)\rangle.
\\qquad\\text{(1)}
```

Then the probability that there exists a pair with $\mathrm{rank}(X)\le r$ for which

```math
(1-\delta)(\|X\|_F^2+\|z\|_2^2)
\le \|\mathcal A(X,z)\|_2^2
\le (1+\delta)(\|X\|_F^2+\|z\|_2^2)
\\qquad\\text{(2)}
```

fails is at most

```math
e^{-L}
+2\exp\!\left(
\kappa\log\frac{1000rLD}{\delta}
-\frac{\delta^2L}{2^{15}}
\right).
\\qquad\\text{(3)}
```

In particular, the sufficient condition

```math
L\ge 2^{16}\delta^{-2}
\kappa\log\frac{1000rLD}{\delta}
\\qquad\\text{(4)}
```

gives failure probability at most

```math
3\exp\!\left(-\frac{\delta^2L}{2^{16}}\right).
\\qquad\\text{(5)}
```

Since $\kappa\le 2rm+d_0$, this has the form
$L\ge C\delta^{-2}(rm+d_0)\log(\mathrm{poly}(m,d_0,L,r)/\delta)$.
The appearance of $L$ inside the logarithm is explicit; (4) is a sufficient inequality, not an assertion that its constants are small.

The same result holds conditionally on any shared setup variable for which these hypotheses hold. Thus the cosets and the lattice may depend on the setup. They must be fixed after conditioning, with the rows independent under that conditioning.

Sections 1–5 prove the theorem. Section 6 gives the exact tensor-coordinate embedding. Section 7 checks the smoothing hypothesis for the full tensor preimage lattice, including its auxiliary block. Section 8 records the deterministic consequence for a learned projection.

## 1. Conventions and Poisson summation

For $\sigma>0$, define

```math
\rho_\sigma(x)=e^{-\pi\|x\|_2^2/\sigma^2},
\qquad
\rho_\sigma(S)=\sum_{x\in S}\rho_\sigma(x).
```

The distribution $D_{\Lambda+c,\sigma}$ assigns mass
$\rho_\sigma(x)/\rho_\sigma(\Lambda+c)$ to $x\in\Lambda+c$.
The Gaussian is centered at the origin; the support, rather than the center of the Gaussian weight, is shifted. Its mean need not be zero.

Write

```math
\Lambda^*=\{y\in\mathbb R^N:\langle y,x\rangle\in\mathbb Z
\text{ for every }x\in\Lambda\}.
```

We use the smoothing convention

```math
\eta_\varepsilon(\Lambda)
=\inf\left\{s>0:
\sum_{0\ne y\in\Lambda^*}e^{-\pi s^2\|y\|_2^2}
\le\varepsilon\right\}.
\\qquad\\text{(6)}
```

Poisson summation for the Gaussian gives

```math
\rho_\sigma(\Lambda+c)
=\frac{\sigma^N}{\det\Lambda}\,f_\sigma(c),
\qquad
f_\sigma(c)=
\sum_{y\in\Lambda^*}
e^{-\pi\sigma^2\|y\|_2^2}e^{2\pi i\langle y,c\rangle}.
\\qquad\\text{(7)}
```

The series and its derivatives converge absolutely. Terms indexed by $y$ and $-y$ show that $f_\sigma(c)$ is real. It is positive because the left-hand side of (7) is positive.

The smoothing hypothesis implies

```math
\sum_{0\ne y\in\Lambda^*}
e^{-\pi\sigma^2\|y\|_2^2/2}\le\varepsilon.
\\qquad\\text{(8)}
```

In particular, uniformly for every real $c$,

```math
1-\varepsilon\le f_\sigma(c)\le1+\varepsilon.
\\qquad\\text{(9)}
```

The extra factor $\sqrt2$ in the smoothing hypothesis will control derivatives of (7), not merely its value.

## 2. Uniform mean, second moment, and tails

**Lemma 2 (affine-coset Gaussian bounds).** Let $0<\varepsilon\le1/4$, let $\sigma/\sqrt2\ge\eta_\varepsilon(\Lambda)$, and let $W\sim D_{\Lambda+c,\sigma}$. Then, uniformly in $c$,

```math
\|\mathbb EW\|_2\le\sigma\varepsilon,
\\qquad\\text{(10)}
```

```math
\left\|\frac{2\pi}{\sigma^2}\mathbb E[WW^{\mathsf T}]-I_N\right\|_{\rm op}
\le3\varepsilon,
\\qquad\\text{(11)}
```

and

```math
\left\|\frac{2\pi}{\sigma^2}\mathrm{Cov}(W)-I_N\right\|_{\rm op}
\le5\varepsilon.
\\qquad\\text{(12)}
```

If $Y=\sqrt{2\pi}\,W/\sigma$, then every vector $a\in\mathbb R^N$ satisfies

```math
\mathbb E e^{t\langle Y,a\rangle}
\le \frac{1+\varepsilon}{1-\varepsilon}
e^{t^2\|a\|_2^2/2}
\quad(t\in\mathbb R),
\\qquad\\text{(13)}
```

and, for $u\ge0$ and $a\ne0$,

```math
\Pr\{ |\langle Y,a\rangle|\ge u\|a\|_2\}
\le4e^{-u^2/2}.
\\qquad\\text{(14)}
```

These are bounds for the uncentered random variable. No exact-zero-mean assumption is implicit.

**Proof.** Completing the square yields the exact identity

```math
\mathbb E e^{\langle\theta,W\rangle}
=e^{\sigma^2\|\theta\|_2^2/(4\pi)}
\frac{\rho_\sigma(\Lambda+c-\sigma^2\theta/(2\pi))}
     {\rho_\sigma(\Lambda+c)}
=e^{\sigma^2\|\theta\|_2^2/(4\pi)}
\frac{f_\sigma(c-\sigma^2\theta/(2\pi))}{f_\sigma(c)}.
\\qquad\\text{(15)}
```

Equation (13) follows from (9) after substituting
$\theta=t\sqrt{2\pi}\,a/\sigma$.
Chernoff's inequality, optimized at $t=u/\|a\|_2$ for the upper tail and its negative for the lower tail, gives

```math
\Pr\{|\langle Y,a\rangle|\ge u\|a\|_2\}
\le 2\frac{1+\varepsilon}{1-\varepsilon}e^{-u^2/2}
\le4e^{-u^2/2}.
```

For the derivatives, the elementary bounds

```math
\sup_{t\ge0}t e^{-\pi\sigma^2t^2/2}
=\frac1{\sigma\sqrt{\pi e}},
\qquad
\sup_{t\ge0}t^2 e^{-\pi\sigma^2t^2/2}
=\frac2{\pi e\sigma^2}
```

and (8) imply

```math
\|\nabla f_\sigma(c)\|_2
\le\frac{2\sqrt{\pi/e}}\sigma\varepsilon
\le\frac{3\varepsilon}\sigma,
\\qquad\\text{(16)}
```

```math
\|\nabla^2 f_\sigma(c)\|_{\rm op}
\le\frac{8\pi}{e\sigma^2}\varepsilon
\le\frac{10\varepsilon}{\sigma^2}.
\\qquad\\text{(17)}
```

For example, (17) follows by bounding the operator norm of each rank-one term $yy^{\mathsf T}$ by $\|y\|_2^2$, retaining half its Gaussian exponent for (8).

Differentiating (15) at $\theta=0$ gives

```math
\mathbb EW=-\frac{\sigma^2}{2\pi}
\frac{\nabla f_\sigma(c)}{f_\sigma(c)},
\\qquad\\text{(18)}
```

```math
\mathbb E[WW^{\mathsf T}]
=\frac{\sigma^2}{2\pi}I_N
+\frac{\sigma^4}{4\pi^2}
  \frac{\nabla^2 f_\sigma(c)}{f_\sigma(c)}.
\\qquad\\text{(19)}
```

The second equation concerns the raw second moment, so there is no squared-gradient term in it. Equations (9), (16), and (18) give

```math
\|\mathbb EW\|_2
\le\frac{3\sigma\varepsilon}{2\pi(1-\varepsilon)}
\le\frac{2}{\pi}\sigma\varepsilon
\le\sigma\varepsilon.
```

Similarly, (17) and (19) bound the left-hand side of (11) by

```math
\frac{5\varepsilon}{\pi(1-\varepsilon)}
\le\frac{20}{3\pi}\varepsilon<3\varepsilon.
```

Subtracting the mean outer product changes the normalized second moment by at most $2\pi\varepsilon^2$. Since $\varepsilon\le1/4$, this proves (12). ∎

The moment-generating-function method for discrete Gaussian cosets is established in the lattice literature; see Micciancio–Peikert [MP12]. The derivative estimates and constants above are included so that the later near-isotropy step does not rest on an unstated centering assumption.

## 3. Concentration for one fixed structured vector

**Lemma 3 (independent, nonidentically distributed rows).** Let $Y_\ell=\sqrt{2\pi}\,W_\ell/\sigma$ under the hypotheses of Theorem 1. For any fixed unit vector $v\in\mathcal V$, put

```math
Z_\ell=\langle Y_\ell,\iota v\rangle.
```

Then

```math
\left|\frac1L\sum_{\ell=1}^L\mathbb EZ_\ell^2-1\right|
\le3\varepsilon,
\\qquad\\text{(20)}
```

and, for $0<t\le1$,

```math
\Pr\left\{
\left|\frac1L\sum_{\ell=1}^L
(Z_\ell^2-\mathbb EZ_\ell^2)\right|\ge t
\right\}
\le2e^{-Lt^2/264}.
\\qquad\\text{(21)}
```

In particular, when $\varepsilon\le\delta/24$,

```math
\Pr\{ |\|\mathcal Av\|_2^2-1|>\delta/4\}
\le2\exp\left(-\frac{\delta^2L}{2^{15}}\right).
\\qquad\\text{(22)}
```

**Proof.** Equation (20) follows from (11) and the isometry of $\iota$. To derive the concentration bound explicitly, (14) implies, for integers $p\ge1$,

```math
\mathbb E|Z_\ell|^{2p}
=\int_0^\infty 2p u^{2p-1}
  \Pr\{|Z_\ell|>u\}\,du
\le4\,2^p p!.
\\qquad\\text{(23)}
```

Let $X_\ell=Z_\ell^2-\mathbb EZ_\ell^2$. Jensen's inequality and
$|a-b|^p\le2^{p-1}(|a|^p+|b|^p)$ give

```math
\mathbb E|X_\ell|^p\le4\,4^p p!
\quad(p\ge2).
\\qquad\\text{(24)}
```

Consequently, for $|u|<1/4$, expansion of the exponential, using $\mathbb EX_\ell=0$, gives

```math
\mathbb E e^{uX_\ell}
\le1+\frac{64u^2}{1-4|u|}
\le\exp\left(\frac{64u^2}{1-4|u|}\right).
\\qquad\\text{(25)}
```

Independence multiplies these bounds over $\ell$. Chernoff's inequality with
$u=t/(128+4t)$ proves an upper-tail bound
$\exp[-Lt^2/(256+8t)]$; replacing $X_\ell$ by $-X_\ell$ gives the other tail. This proves (21). Identical distributions were never used.

For (22), the deterministic bias is at most $\delta/8$. Apply (21) with $t=\delta/8$; its exponent denominator is $264\cdot64=16896<2^{15}$. ∎

## 4. A net for low-rank symmetric matrices with nuisance coordinates

Write

```math
\mathcal S_r=
\{(X,z)\in\mathcal V:
\mathrm{rank}(X)\le r,\ \|X\|_F^2+\|z\|_2^2=1\}.
```

**Lemma 4 (covering number).** For $0<\eta\le1$, there is an $\eta$-net
$\mathcal N\subset\mathcal S_r$ in the $\mathcal V$-norm with

```math
|\mathcal N|\le
\left(\frac{9\sqrt r}{\eta}\right)^{r(m+1)+d_0}.
\\qquad\\text{(26)}
```

**Proof.** Every member of $\mathcal S_r$ has a representation

```math
X=U\mathrm{diag}(a)U^{\mathsf T},
\quad U^{\mathsf T}U=I_r,
\quad \|a\|_2^2+\|z\|_2^2=1.
```

Zero eigenvalues pad matrices of rank less than $r$. A maximal $h$-separated subset of the Stiefel manifold in Frobenius norm is an $h$-net. Disjoint ambient Euclidean balls of radius $h/2$, all inside a ball of radius $\sqrt r+h/2$ in $\mathbb R^{mr}$, show that this net has at most
$(1+2\sqrt r/h)^{mr}$ members. Its centers remain on the Stiefel manifold.

The same volume argument gives an $h$-net of the unit sphere in $\mathbb R^{r+d_0}$, with centers on that sphere and at most $(1+2/h)^{r+d_0}$ members. Approximate $U$ and $(a,z)$ by these nets. For a fixed orthonormal $U$, the map
$(a,z)\mapsto(U\mathrm{diag}(a)U^{\mathsf T},z)$ is an isometry. Changing $U$ to $\widehat U$ changes the matrix by at most

```math
\|(U-\widehat U)\mathrm{diag}(\widehat a)U^{\mathsf T}\|_F
+\|\widehat U\mathrm{diag}(\widehat a)
        (U-\widehat U)^{\mathsf T}\|_F
\le2h,
```

because $\|\widehat a\|_\infty\le1$. The total error is at most $3h$. Choose $h=\eta/3$. All net points are still in $\mathcal S_r$, and

```math
(1+6\sqrt r/\eta)^{mr}(1+6/\eta)^{r+d_0}
\le(9\sqrt r/\eta)^{r(m+1)+d_0}.
```

This proves (26). ∎

## 5. Extending the net estimate without an independence assumption after projection

Choose an orthonormal basis $e_1,\ldots,e_D$ of $\mathcal V$. The matrix entries of $\mathcal A$ in this basis are
$L^{-1/2}\langle Y_\ell,\iota e_j\rangle$. Each coordinate obeys (14), regardless of dependencies among coordinates.

Set

```math
B=\sqrt{2\bigl(L+\log(4LD)\bigr)}.
\\qquad\\text{(27)}
```

A union bound gives

```math
\Pr\{\max_{\ell,j}|\langle Y_\ell,\iota e_j\rangle|>B\}
\le4LD e^{-B^2/2}=e^{-L}.
\\qquad\\text{(28)}
```

On the complementary event,

```math
\|\mathcal A\|_{\rm op}
\le\|\mathcal A\|_F\le B\sqrt D.
\\qquad\\text{(29)}
```

Here the operator acts on the **whole** space $\mathcal V$. The bound is crude but prevents a circular restricted-norm argument when passing from a net to all low-rank matrices.

Use Lemma 4 with

```math
\eta=\frac{\delta}{16B\sqrt D}.
\\qquad\\text{(30)}
```

For $L,D,r\ge1$,

```math
144\sqrt r\,B\sqrt D\le1000rLD.
```

For example, $L+\log(4LD)\le5LD$ gives this inequality immediately. Thus

```math
|\mathcal N|\le
\left(\frac{1000rLD}{\delta}\right)^\kappa.
\\qquad\\text{(31)}
```

By (22) and a union bound, outside an event of probability

```math
2\exp\left(\kappa\log\frac{1000rLD}{\delta}
-\frac{\delta^2L}{2^{15}}\right),
```

all $v_0\in\mathcal N$ satisfy
$|\|\mathcal Av_0\|_2^2-1|\le\delta/4$.
On this event and (29), any $v\in\mathcal S_r$ has a net point $v_0$ such that

```math
\bigl|\|\mathcal Av\|_2-1\bigr|
\le \bigl|\|\mathcal Av_0\|_2-1\bigr|
     +\|\mathcal A\|_{\rm op}\|v-v_0\|_{\mathcal V}
\le\frac\delta4+\frac\delta{16}
=\frac{5\delta}{16}.
\\qquad\\text{(32)}
```

Squaring (32), and using $\delta\le1/2$, gives
$|\|\mathcal Av\|_2^2-1|\le\delta$.
Homogeneity proves (2) for all structured vectors, including zero. Combining the two exceptional probabilities proves (3). Condition (4) makes the entropy term no more than half the negative exponent; (5) follows. This completes the proof of Theorem 1. ∎

The net method is related to the matrix-RIP arguments of Recht–Fazel–Parrilo [RFP10] and Candès–Plan [CP11]. The proof above supplies the extension needed here: arbitrary nuisance coordinates, nonidentical affine-coset rows, and coordinates that may be dependent within a row.

## 6. Exact embedding of the tensor coefficients

In the notation of [the observation model](model.md), $\widetilde K=C$, $F_{01}=F_L$, $F_{10}=F_R$, and the matrix $H_1$ below is the message-cross matrix called $J$ there. The symbol $\iota$ remains reserved for the isometric embedding.

Fix $h=k+n$. For one key column, order its coordinates as

```math
W_\ell=
\bigl(\mathrm{vec}(K_\ell),\ \widetilde K_\ell,
\ \mathrm{vec}(F_{01,\ell}),
\ \mathrm{vec}(F_{10,\ell})\bigr),
```

where

```math
K_\ell\in\mathbb R^{m\times m},\quad
\widetilde K_\ell\in\mathbb R^{\widetilde m},\quad
F_{01,\ell}\in\mathbb R^{h\times m},\quad
F_{10,\ell}\in\mathbb R^{m\times h}.
```

The vectorization order is fixed consistently. A different tensor-order convention is a permutation of coordinates and does not change the Gaussian norm.

For $a\in[h]$ and $i\in[m]$, define

```math
H_{a,i,\ell}=(F_{01,\ell})_{a,i}+(F_{10,\ell})_{i,a}.
\\qquad\\text{(33)}
```

Let $H_s\in\mathbb R^{nm\times L}$ select the rows with $a=k+j$, $j\in[n]$, and let $H_1\in\mathbb R^{m\times L}$ select $a=1$. These two sets of coordinates are disjoint.

For $u\in\mathbb R^{n\times m}$, $v\in\mathbb R^{\widetilde m}$, and $w\in\mathbb R^m$, define $C(u,w)\in\mathbb R^{h\times m}$ by

```math
C(u,w)_{a,i}=
\begin{cases}
w_i,&a=1,\\
u_{j,i},&a=k+j,\ j\in[n],\\
0,&\text{otherwise}.
\end{cases}
```

Then the coefficient vector of

```math
\langle K_\ell,X\rangle_F
+\langle H_{s,\ell},u\rangle
+\langle\widetilde K_\ell,v\rangle
+\langle H_{1,\ell},w\rangle
```

inside the full $W_\ell$ space is exactly

```math
\bigl(\mathrm{vec}X,\ v,
\mathrm{vec}(C(u,w)),\mathrm{vec}(C(u,w)^{\mathsf T})\bigr).
\\qquad\\text{(34)}
```

Its squared norm is

```math
\|X\|_F^2+2\|u\|_2^2+\|v\|_2^2+2\|w\|_2^2.
\\qquad\\text{(35)}
```

There is no factor-of-two adjustment to the $X$ block: for a symmetric $X$, its full vectorization has squared norm $\|X\|_F^2$. In particular, off-diagonal entries occur twice in that Frobenius norm exactly as they do in the two distinct coordinates of $K_\ell$.

Apply Theorem 1 with

```math
d_0=nm+\widetilde m+m,
\qquad
z=(\sqrt2\,u,v,\sqrt2\,w).
```

The isometry $\iota$ sends this rescaled tuple to (34). Consequently, with

```math
\tau=\sigma\sqrt{\frac L{2\pi}},
\quad
\mathcal M(X,u,v,w)
=K_{\rm key}^{\mathsf T}\mathrm{vec}X
+H_s^{\mathsf T}u+\widetilde K^{\mathsf T}v+H_1^{\mathsf T}w,
```

the conclusion is

```math
(1-\delta)(\|X\|_F^2+2\|u\|_2^2+\|v\|_2^2+2\|w\|_2^2)
\le\tau^{-2}\|\mathcal M(X,u,v,w)\|_2^2
```

```math
\le(1+\delta)(\|X\|_F^2+2\|u\|_2^2+\|v\|_2^2+2\|w\|_2^2),
\\qquad\\text{(36)}
```

uniformly for symmetric $X$ of rank at most $r$ and all nuisance vectors. Equation (36) is the normalization used by the reconstruction argument.

## 7. Checking smoothing for the full preimage lattice

This section separates two facts that should not be conflated: a short full-rank set need not be a basis of the entire lattice, and appending an auxiliary block can introduce long preimage coordinates. Neither fact invalidates the required smoothing bound.

### 7.1 A Gram–Schmidt smoothing bound

**Lemma 5.** If a full-rank lattice $\Gamma\subset\mathbb R^N$ has a basis whose Gram–Schmidt vectors have lengths at most $b$, then

```math
\eta_\varepsilon(\Gamma)
\le b\sqrt{\frac{\log(4N(1+1/\varepsilon))}{\pi}}
\quad(\varepsilon>0).
\\qquad\\text{(37)}
```

**Proof.** For any lattice basis with Gram–Schmidt lengths $b_i$, writing its norm in triangular Gram–Schmidt coordinates and summing one integer coordinate at a time gives

```math
\rho_t(\Gamma)\le\prod_{i=1}^N\rho_{t/b_i}(\mathbb Z).
\\qquad\\text{(38)}
```

At each step, a shifted one-dimensional Gaussian mass is bounded by its mass at zero. This last fact follows immediately from one-dimensional Poisson summation: the Fourier coefficients of the periodized Gaussian are nonnegative, so replacing each cosine by 1 gives its maximum.

The dual basis, in reverse order, has Gram–Schmidt lengths $1/b_N,\ldots,1/b_1$. This follows from the defining biorthogonality relations: after removing the preceding reverse-dual span, the remaining vector is the original Gram–Schmidt direction divided by its squared length. Applying (38) to the dual gives

```math
\rho_{1/s}(\Gamma^*)
\le\prod_{i=1}^N\rho_{b_i/s}(\mathbb Z)
\le\left(\frac{1+a}{1-a}\right)^N,
\quad a=e^{-\pi(s/b)^2},
\\qquad\\text{(39)}
```

because $\sum_{j\ge1}a^{j^2}\le a/(1-a)$.
For the value of $s$ in (37),
$a=\varepsilon/[4N(1+\varepsilon)]<1/4$. Therefore

```math
N\log\frac{1+a}{1-a}
\le4Na=\frac{\varepsilon}{1+\varepsilon}
\le\log(1+\varepsilon).
```

Thus $\rho_{1/s}(\Gamma^*)\le1+\varepsilon$, which is the smoothing condition. ∎

If $\Gamma\subseteq\Lambda$ are full-rank lattices, then
$\Lambda^*\subseteq\Gamma^*$, so

```math
\eta_\varepsilon(\Lambda)\le\eta_\varepsilon(\Gamma).
\\qquad\\text{(40)}
```

In particular, a short linearly independent set in $\Lambda$ may be used as a basis of its generated sublattice; it need not be a basis of $\Lambda$.

### 7.2 Appending the auxiliary block

**Lemma 6.** Let $E_0\in\mathbb Z_q^{a\times N_0}$ be surjective as a map $\mathbb Z_q^{N_0}\to\mathbb Z_q^a$. Suppose $\Lambda_q^\perp(E_0)$ contains a linearly independent set of $N_0$ vectors, each of Euclidean norm at most $b$. For arbitrary $B\in\mathbb Z_q^{a\times t}$, set

```math
\Lambda=\Lambda_q^\perp([E_0\ B])\subset\mathbb Z^{N_0+t}.
```

Then, with $N=N_0+t$ and $\bar b=\max(b,1)$,

```math
\eta_\varepsilon(\Lambda)
\le\bar b\sqrt{\frac{\log(4N(1+1/\varepsilon))}{\pi}}.
\\qquad\\text{(41)}
```

**Proof.** Let $T$ have the short independent vectors as columns. Surjectivity gives an integer matrix $R$ with
$E_0R=-B\pmod q$. The columns of

```math
\widehat T=
\begin{pmatrix}T&R\\0&I_t\end{pmatrix}
\\qquad\\text{(42)}
```

are independent vectors in $\Lambda$. They generate a full-rank sublattice $\Gamma\subseteq\Lambda$.

Order the columns as displayed. The first $N_0$ Gram–Schmidt lengths are at most $b$, because an orthogonal projection cannot increase a column norm. These columns span $\mathbb R^{N_0}\oplus0$. Hence, after projecting out their span, each later column $(R_j,e_j)$ is exactly $(0,e_j)$. The later Gram–Schmidt lengths are all 1. Apply Lemma 5 to $\Gamma$, then (40). No upper bound on the coordinates of $R$ is needed. ∎

### 7.3 Application to the tensor sampler

For degree two, after a harmless block permutation,

```math
E_0(A)=
\begin{pmatrix}
A\otimes A&0&0\\
A\otimes I_m&pI_{hm}&0\\
I_m\otimes A&0&pI_{mh}
\end{pmatrix}.
\\qquad\\text{(43)}
```

If $A\in\mathbb F_q^{h\times m}$ has row rank $h$ and $p\ne0$ in $\mathbb F_q$, then $E_0(A)$ is surjective. Indeed, $A\otimes A$ is surjective onto the top block, and the two invertible $pI$ blocks can then set the lower blocks arbitrarily.

The full sampler lattice is the kernel lattice of $[E_0(A)\ \widetilde A]$, up to a coordinate permutation. Theorem 1 of Cini–Lai–Ünal–Woo [CLUW26] supplies, on its high-probability setup event, a full-rank set for the unextended kernel with column norms at most

```math
b=2(s\sqrt m)^2.
\\qquad\\text{(44)}
```

It is sufficient for the present note to impose the explicit width condition

```math
\sigma\ge
\sqrt2\max(b,1)
\sqrt{\frac{\log(4N(1+1/\varepsilon))}{\pi}},
\qquad N=m^2+2hm+\widetilde m.
\\qquad\\text{(45)}
```

Lemma 6 then gives precisely $\sigma/\sqrt2\ge\eta_\varepsilon(\Lambda)$.

Table 1 of [CLUW26] uses a width above the tensor short-set bound by a factor $\omega(\sqrt{\log m})$, with an additional message-size factor. When all dimensions are polynomial in the security parameter and $m$ is at least that parameter, this permits negligible $\varepsilon$ in (45). This asymptotic statement does not replace (45) when explicit numerical widths are used; a concrete instantiation should check (45) directly.

There is also a setup-distribution issue. Existence of the short set in (44) is a property of $A$, even though the procedure demonstrating it uses a trapdoor. If that property fails with probability $\alpha$ under the trapdoor setup, and its $A$-marginal is within statistical distance $\beta$ of uniform, it fails with probability at most $\alpha+\beta$ under uniform $A$. For uniform $A$, row-rank failure is at most $(q^h-1)q^{-m}$, by a union bound over nonzero left-kernel vectors. The paper's wide-matrix regime makes this negligible. The auxiliary matrix $\widetilde A$ may be arbitrary for Lemma 6.

### 7.4 Column independence and statistical transfer

Theorem 2, Eq.18 of [CLUW26] gives an ideal spherical Gaussian law for the matrix containing $K,\widetilde K,F$. Conditional on the setup matrices, a constraint of the form

```math
E W=V
```

separates by columns, and

```math
e^{-\pi\|W\|_F^2/\sigma^2}
=\prod_{\ell=1}^L e^{-\pi\|W_\ell\|_2^2/\sigma^2}.
```

Its normalizing sum also factors. Thus the columns are independent affine-coset Gaussians, even when the target columns $V_\ell$ differ. This is the source of row independence in the measurement theorem.

The published statistical-closeness statement concerns the output marginal $(A,\widetilde A,K,\widetilde K)$. The hidden $F$ in its ideal law is a valid auxiliary variable for the proof. One need not assert statistical closeness of an unexposed implementation-specific $F$: any resulting event or algorithm on the actual output marginal transfers by statistical distance and data processing. If the setup is good except with probability $\alpha_{\rm good}$, and the output sampler differs from the ideal marginal by $\alpha_{\rm samp}$, the failure probability in the application is at most

```math
\alpha_{\rm good}+\alpha_{\rm samp}
+3e^{-\delta^2L/2^{16}}
\\qquad\\text{(46)}
```

under (4). Smoothing error enters the deterministic second-moment bias; it is not additionally counted as a per-row statistical-distance loss.

## 8. What the theorem implies after learning a nuisance projection

This consequence is deterministic and therefore preserves arbitrary correlations among the coefficient blocks and the learned projection.

Let $P$ be the orthogonal projector onto

```math
\ker H_s\cap\ker\widetilde K\subseteq\mathbb R^L,
```

and define

```math
\mathcal A_P(X)=\tau^{-1}P K_{\rm key}^{\mathsf T}\mathrm{vec}X.
```

The distance to the nuisance span is

```math
\|\mathcal A_P(X)\|_2
=\tau^{-1}\inf_{u,v}
\|\mathcal M(X,u,v,0)\|_2.
\\qquad\\text{(47)}
```

The lower bound in (36), uniform over all $u,v$, and the upper bound with $u=v=0$, show that $\mathcal A_P$ has the same rank-$r$ RIP constants.

Likewise, if $X_0$ has rank one and $X'$ has rank at most one, then $\mathrm{rank}(X'-X_0)\le2$. For $r\ge2$, (36) gives

```math
\left\|\mathcal A_P(X'-X_0)+\tau^{-1}P H_1^{\mathsf T}e\right\|_2
\ge\sqrt{2(1-\delta)}\,\|e\|_2.
\\qquad\\text{(48)}
```

This is the quantitative separation used by the reconstruction test. The proof makes no assertion that entries of $PK_{\rm key}^{\mathsf T}$ are independent or Gaussian.

## References and attribution

- **[CLUW26]** Valerio Cini, Russell W. F. Lai, Akin Ünal, and Ivy K. Y. Woo. *Lattice-based Secret-Key Functional Encryption for Constant-Degree Polynomials*. Cryptology ePrint Archive, Report 2026/1977. [Primary paper](https://eprint.iacr.asia/2026/1977.pdf). The relevant inputs are the tensor short-set construction in Theorem 1, the sampler law in Theorem 2/Eq.18, and Table 1. The Gaussian and RIP arguments in this note are deductions from those inputs.
- **[MP12]** Daniele Micciancio and Chris Peikert. *Trapdoors for Lattices: Simpler, Tighter, Faster, Smaller*. EUROCRYPT 2012; ePrint 2011/501. [Author version](https://web.eecs.umich.edu/~cpeikert/pubs/efftrap.pdf). This is prior work for the Gaussian-coset moment-generating-function and subgaussian framework; the needed bounds are proved explicitly here.
- **[RFP10]** Benjamin Recht, Maryam Fazel, and Pablo A. Parrilo. *Guaranteed Minimum-Rank Solutions of Linear Matrix Equations via Nuclear Norm Minimization*. SIAM Review 52(3), 2010. [Author version](https://web.mit.edu/parrilo/www/pubs/files/RechtFazelParrilo-GuaranteedMinimumRankSolutionsOfLinearMatrixEquationsViaNuclearNormMinimization-SIAM.pdf). This is prior work for matrix restricted isometry and nuclear-norm recovery.
- **[CP11]** Emmanuel J. Candès and Yaniv Plan. *Tight Oracle Inequalities for Low-Rank Matrix Recovery from a Minimal Number of Noisy Random Measurements*. IEEE Transactions on Information Theory 57(4), 2011; preprint titled *Tight Oracle Bounds for Low-Rank Matrix Recovery from a Minimal Number of Random Measurements*. [Primary preprint](https://arxiv.org/abs/1001.0339). Its concentration-to-RIP covering argument is a useful comparator; Theorem 1 above retains a logarithmic overhead to give a direct proof for the nuisance-augmented affine-coset model.
