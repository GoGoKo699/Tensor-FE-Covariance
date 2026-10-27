# An explicit parameter family

This page shows that the hypotheses of the [distinguishing theorem](attack.md) hold for an asymptotic degree-two family within the numerical constraints of Table 1 of [CLÜW26](../references/RELATED_WORK.md#cluw26). The ordinary-LWE hardness rows in that table remain assumptions; a numerical parameter choice cannot prove them. The distinguisher itself does not use an ordinary-LWE solver.

All inequalities below hold for sufficiently large integer security parameter $`\lambda`$. Constants and thresholds are not optimized. Logarithms are base two in parameter definitions and natural in analytic tail bounds.

## 1. Choice of parameters

Set

```math
\begin{gathered}
d=2,\qquad k=\lambda^2,\qquad
\ell=\lceil\log_2\lambda\rceil^2,\qquad T=2^\ell,\\
n=\widetilde m=\lambda+\ell^2,\qquad
h_+=k+n+1,\\
m=C_m h_+(\ell+1),\qquad
s=3\lceil\log_2(m+2)\rceil,\\
\sigma=4s^2m(k+1)\lceil\log_2(m+2)\rceil,\\
\chi_s=\chi_e=\chi_{\widetilde e}=\chi
 =\left\lceil T^{1/12}\sqrt{k}\right\rceil,\\
p=2,\qquad r=p^2=4,\qquad \beta_x=\beta_y=1.
\end{gathered}
```

Here $`C_m\ge8`$ is a fixed integer, increased if required by the fixed constant in the chosen admissible trapdoor construction. Choose any prime $`q`$ with

```math
T\le q\le2T.
```

For all sufficiently large $`\lambda`$ such a prime exists and is odd. The family may regard an admissible prime as a public parameter. Alternatively, uniform candidate selection with polynomial-time primality testing constructs one with expected time polynomial in $`\log T`$; this is not a claim that enumerating all integers up to $`T`$ is efficient.

The widths and dimensions other than $`\chi,q`$ are polynomial in $`\lambda`$. The bit lengths of $`\chi`$ and $`q`$ are $`O((\log\lambda)^2)`$. The ceiling defining $`\chi`$ is a twelfth-root computation on a binary integer and requires polynomial bit complexity.

## 2. Feasibility, trapdoors, and smoothing

The degree is constant; $`q`$ is prime and coprime to $`p`$. Since $`\log_2 q\le\ell+1`$,

```math
m\ge C_m h_+\log_2q,\qquad m\ge h_+\log_2T,\qquad m\ge\lambda.
```

Thus the dimensional bounds hold both for $`h=k+n`$ and for the extra-row setup $`h=k+n+1`$ in the direct assumption experiment. The choice $`s=3\lceil\log_2(m+2)\rceil`$ is $`3\omega(\sqrt{\log m})`$.

At degree two, the width row of the target table asks for

```math
\sigma\ge4s^2m\,\sqrt{\omega(\log m)}\,(k+1).
```

Our explicit logarithmic multiplier satisfies this requirement. It also meets the full-extension sampling hypothesis in the target's Theorem 2.

[Gaussian measurements, Section 7](gaussian_measurements.md#7-checking-smoothing-for-the-full-preimage-lattice) derives a short full-rank set for the complete preimage lattice, with maximum Gram–Schmidt length at most

```math
b_{\rm GS}=2s^2m.
```

It is sufficient for the generated sublattice to have this bound; it need not be the entire integer kernel. Adding the auxiliary preimage columns introduces unit Gram–Schmidt lengths, and dual inclusion transfers the smoothing bound to the full lattice.

For full column dimension

```math
N_{\rm col}=m^2+\widetilde m+2h_+m,
```

that proof gives

```math
\eta_\epsilon(\Lambda)
 \le b_{\rm GS}
 \sqrt{\frac{\log(4N_{\rm col}(1+1/\epsilon))}{\pi}}.
```

Choose $`\epsilon=2^{-\lambda}`$. Since
$`\sigma/(\sqrt2 b_{\rm GS})=\sqrt2(k+1)\lceil\log_2(m+2)\rceil`$,
we have $`\sigma/\sqrt2\ge\eta_\epsilon(\Lambda)`$ for sufficiently large $`\lambda`$. Thus both the affine-coset near-isotropy and coordinate tails hold uniformly over the targets used by either experiment. The target's negligible setup/sampling distance is charged separately.

## 3. Integer lifting and correctness

For the degree-two family, a conservative version of the target's correctness quantity, with slack for the extra message row, is

```math
\Gamma_+
=\sigma\left[
8(k+n+1+m)\big(k+1+\chi^2n+\chi^2m\big)
+\chi\widetilde m
\right].
```

This dominates the published Table 1 expression for the FE scheme, and its same derivation covers the direct assumption's extra coordinate. The target's Gaussian norm and key bounds imply $`|z_y|\le\Gamma_+`$ except with negligible probability for the coefficient vectors used here.

Now $`\sigma,m,n,k,\widetilde m`$ are polynomial in $`\lambda`$, while
$`\chi^2=T^{1/6}\mathrm{poly}(\lambda)`$. Therefore

```math
\Gamma_+=T^{1/6}\mathrm{poly}(\lambda),
\qquad
\frac{T}{8(\Gamma_++1)}\longrightarrow\infty.
```

The second limit follows from $`T=2^{\lceil\log_2\lambda\rceil^2}`$ growing faster than every fixed polynomial. Consequently

```math
q\ge 2r(\Gamma_++1)=8(\Gamma_++1).
```

For a zero-output key, $`p^2z_y`$ lies inside the balanced modulus interval on this event. Dividing its balanced lift by $`p^2`$ therefore returns the actual integer $`z_y`$.

There are polynomially many keys and training encryptions. The same bounds and a polynomial union bound make all required lifts correct except with negligible probability. The covariance proof works on the unwrapped distribution and transfers through this coupling; it does not recalculate moments after conditioning on successful lifts.

A public bound for the decoder is

```math
R_0=\lceil m\chi^2\rceil.
```

Indeed, Poisson summation gives $`\rho_{\sqrt2\chi}(\mathbb Z)/\rho_\chi(\mathbb Z)\le\sqrt2`$, because the nonzero dual theta terms decrease when the width increases. Markov's inequality applied to $`\exp(\pi\|e\|_2^2/(2\chi^2))`$ gives

```math
\Pr(\|e\|_2^2>m\chi^2)
\le\left(\sqrt2e^{-\pi/2}\right)^m
<2^{-m}.
```

This negligible norm-tail event is included in the final error ledger. The radius $`R_0`$ is large in numerical value but has polynomial bit length.

## 4. Measurement count

The permitted upper-triangular monomials other than $`x_1^2`$ provide

```math
L=\frac{k(k+1)}2-1=\Theta(\lambda^4).
```

The full nuisance dimension needed for joint restricted isometry is

```math
d_0=nm+\widetilde m+m.
```

As $`\lambda\to\infty`$,

```math
\begin{aligned}
n&=\Theta(\lambda),&
m&=\Theta(\lambda^2(\log\lambda)^2),\\
d_0&=\Theta(\lambda^3(\log\lambda)^2),&
N_{\rm col}&=\mathrm{poly}(\lambda).
\end{aligned}
```

For fixed rank bound ten, the covering exponent
$`\kappa=10(m+1)+d_0`$ is $`\Theta(\lambda^3(\log\lambda)^2)`$, and

```math
\frac{L}{\kappa\log(2LN_{\rm col})}
 =\Theta\left(\frac{\lambda}{(\log\lambda)^3}\right)
 \longrightarrow\infty.
```

Hence the explicit sufficient condition in the Gaussian theorem holds for any fixed distortion, including natural-scale distortion $`1/200`$. Its failure probability is exponentially small in $`L`$ once the inequality holds. Rational normalization enlarges the distortion to at most $`1/100`$, as proved in [Reconstruction](reconstruction.md).

The direct tensor assumption provides all $`k^2`$ columns, so its measurement count is larger. The same argument applies separately to its two setup lattices.

## 5. Noise size, target time, and compactness

The target's large-noise constraint is met exactly:

```math
\chi_s,\chi_e,\chi_{\widetilde e}
 \ge T^{1/(6d)}\sqrt{k}\,\beta_x.
```

The dimensional constraint $`m\ge(k+n)\log T`$ was checked above. The target's ordinary-LWE dimension suggestion $`n=\widetilde m=\lambda+(\log T)^2`$ is our choice, with the declared logarithm convention.

The ordinary-LWE hardness conditions in Table 1 are conjectural baselines of the target construction. This project does not prove time-$`T`$ hardness of those instances. Its algorithm directly exploits the correlated functional-key material and remains an attack regardless of whether those independent hardness conjectures are true.

Ciphertext length obeys

```math
(m+\widetilde m)\log q
 =O(\lambda^2(\log\lambda)^4)
 =O(k(\log k)^4)
 =o(k^{3/2}).
```

Thus the compactness requirement holds, for example with $`\varepsilon=1/4`$ at degree two. The number of ciphertext coordinates grows by a logarithmic factor beyond $`k`$; a prior restriction to a fixed linear number of coordinates should not be silently treated as covering this family.

The learned-Gram sample count is polynomial because $`\sigma`$ and its public tail bound $`B`$ are polynomial. The finite-bit decoder costs polynomial time in the dimensions and $`\log R_0`$. Its total running time is therefore $`\mathrm{poly}(\lambda)`$, which is eventually less than $`T`$, despite $`\chi`$ and $`q`$ being superpolynomial.

## 6. What this family establishes

This is an asymptotic witness that the theorem's hypotheses coexist with the target's published numerical safeguards and compactness criterion. It does not give a small practical attack cost, an optimized threshold for $`\lambda`$, a proof about every permitted parameter choice, or a conclusion about every higher-degree instantiation.

The precise general condition remains the measurement-to-nuisance inequality in [the theorem](attack.md), together with its sampling, smoothing, and bit-complexity hypotheses. This explicit family proves that the covered regime is nonempty.

