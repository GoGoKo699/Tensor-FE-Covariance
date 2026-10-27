# Recovering an integer Gram matrix from noise covariance

The [model](model.md) gives a vector of integer noises for each known-zero encryption:

```math
z_\ell=e^{\mathsf T}K_\ell e+\widetilde e^{\mathsf T}C_\ell
 -(s\otimes e)^{\mathsf T}(H_s)_\ell.
```

Keys are fixed across observations. The three fresh vectors have independent coordinates with law $`D_{\mathbb Z,\chi}`$, where $`\chi\ge1`$. This page proves an exact covariance identity and a finite-sample, finite-precision recovery statement. Large encryption noise is accounted for through its bit length.

## 1. Exact covariance

Write $`v=\mathbb E[e_i^2]`$ and $`\mu_4=\mathbb E[e_i^4]`$. Symmetry gives zero odd moments. The mean is

```math
\mathbb E z_\ell=v\,\mathrm{tr}K_\ell.
```

For possibly nonsymmetric $`K_\ell`$, separate diagonal and off-diagonal terms:

```math
e^{\mathsf T}K_\ell e
=\sum_i(K_\ell)_{ii}e_i^2
 +\sum_{i<j}\big((K_\ell)_{ij}+(K_\ell)_{ji}\big)e_i e_j.
```

Independence and parity make different centered terms in this expansion uncorrelated. The known quadratic covariance is

```math
\begin{aligned}
(C_K)_{\ell j}
={}&(\mu_4-v^2)\sum_i(K_\ell)_{ii}(K_j)_{ii}\\
&+v^2\sum_{i<t}
\big((K_\ell)_{it}+(K_\ell)_{ti}\big)
\big((K_j)_{it}+(K_j)_{ti}\big).
\end{aligned}
```

The linear auxiliary term has covariance $`vC^{\mathsf T}C`$. The bilinear term has covariance $`v^2H_s^{\mathsf T}H_s`$, since

```math
\mathbb E[s_a e_i s_b e_j]=v^2\,\mathbf1_{a=b}\mathbf1_{i=j}.
```

All cross-covariances vanish. In a quadratic–bilinear product, the remaining $`s_a`$ has mean zero. Products involving the independent centered $`\widetilde e`$ vanish as well. These calculations condition on all keys and require no independence between coordinates within a key column. Thus

```math
\boxed{\mathrm{Cov}(z)=C_K+vC^{\mathsf T}C+v^2G,\qquad
G=H_s^{\mathsf T}H_s\in\mathbb Z^{L\times L}.}
```

The discrete fourth moment is essential. Replacing it silently by the continuous Gaussian value $`3v^2`$ would change the known subtraction.

## 2. Uniform standardized moments

Let $`Z\sim D_{\mathbb Z,\chi}`$. The Gaussian mass of a shifted integer lattice is maximal at the unshifted lattice, by Poisson summation and positivity of its Fourier coefficients. Completing the square gives

```math
\mathbb E e^{tZ}\le e^{\chi^2t^2/(4\pi)},\qquad
\Pr(|Z|\ge u)\le2e^{-\pi u^2/\chi^2}.
```

Integrating this tail gives, for every integer $`p\ge1`$,

```math
\mathbb E|Z|^{2p}\le2p!\,(\chi^2/\pi)^p.
```

For a lower variance bound, there are at least $`\lfloor\chi\rfloor\ge\chi/2`$ positive integers in $`[\chi,2\chi]`$. Each contributes at least $`\chi^2e^{-4\pi}`$ to the unnormalized second moment; include the negative integers too. Monotonicity of the Gaussian on the positive half-line gives $`\rho_\chi(\mathbb Z)\le1+\chi\le2\chi`$. Hence

```math
v\ge a_0\chi^2,\qquad a_0=\tfrac12e^{-4\pi}.
```

This conservative constant also covers $`1\le\chi<2`$. For $`\xi=Z/\sqrt v`$,

```math
\mathbb E\xi^2=1,\qquad
\mathbb E|\xi|^{2p}\le\frac{2p!}{(\pi a_0)^p}.
```

Put $`M_8=48/(\pi a_0)^4`$. Then $`\mathbb E|\xi|^8\le M_8`$. Hölder's inequality bounds the lower even moments by corresponding powers of $`M_8`$. These are absolute constants independent of $`\chi`$.

## 3. A public fourth-moment bound

Suppose every relevant coordinate of the complete key extension has absolute value at most a public $`B\ge1`$. In particular,

```math
|(K_\ell)_{ij}|\le B,\quad |C_{a,\ell}|\le B,\quad
|(H_s)_{a,i,\ell}|\le2B.
```

Section 5 supplies this event with negligible failure. Normalize and center each coordinate:

```math
Y_\ell=\frac{z_\ell}{v}-\mathrm{tr}K_\ell.
```

It is a sum of at most

```math
t_0=m+\frac{m(m-1)}2+\widetilde m+nm
```

terms of four types: $`\xi_i^2-1`$, $`\xi_i\xi_j`$ with $`i\ne j`$, an auxiliary standardized coordinate, and $`\xi_{s,a}\xi_{e,i}`$. Every coefficient has absolute value at most

```math
b_0=2B\max\{1,a_0^{-1/2}\}.
```

For the auxiliary term this uses $`v^{-1/2}\le a_0^{-1/2}`$. Every basis term has fourth moment at most $`16M_8`$: a centered square satisfies $`\mathbb E(\xi^2-1)^4\le8(\mathbb E\xi^8+1)\le16M_8`$; products of independent coordinates satisfy $`(\mathbb E\xi^4)^2\le\mathbb E\xi^8`$.

The deterministic inequality $`|\sum_{i=1}^t a_i|^4\le t^3\sum_i|a_i|^4`$ gives

```math
\mathbb E|Y_\ell|^4\le V,\qquad V=16M_8(t_0b_0)^4.
```

Consequently

```math
\mathrm{Var}(Y_\ell Y_j)
\le\mathbb E[Y_\ell^2Y_j^2]\le V.
```

No independence across functional-key coordinates is needed. Independence is used across fresh encryptions.

## 4. Median-of-means estimation and exact rounding

Choose block size and odd block count

```math
b_{\rm samp}=\lceil256V\rceil,\qquad
g\ge8\big(\lambda\log2+\log(2L^2)\big),\qquad Q=b_{\rm samp}g,
```

rounding $`g`$ upward to an odd integer. Certified larger integer bounds are equally suitable.

For every pair $`(\ell,j)`$, average $`Y_\ell Y_j`$ in each block, then take the median of the $`g`$ averages. Chebyshev's inequality makes one block's error exceed $`1/8`$ with probability at most $`1/4`$. Hoeffding's inequality on the independent bad-block indicators makes the median fail with probability at most $`e^{-g/8}`$. Union over at most $`L^2`$ pairs gives simultaneous error at most $`1/8`$ with failure at most $`2^{-\lambda}/2`$.

Let $`\widehat\Sigma`$ be this estimate. The known normalized covariance is

```math
\begin{aligned}
N_{\ell j}
={}&(\mu_4/v^2-1)\sum_i(K_\ell)_{ii}(K_j)_{ii}\\
&+\sum_{i<t}
\big((K_\ell)_{it}+(K_\ell)_{ti}\big)
\big((K_j)_{it}+(K_j)_{ti}\big)\\
&+\frac1v(C^{\mathsf T}C)_{\ell j}.
\end{aligned}
```

The identity says $`\mathbb E[Y_\ell Y_j]=N_{\ell j}+G_{\ell j}`$. Allocate another $`1/8`$ to finite arithmetic in the observations and another $`1/8`$ to the known subtraction. Every entry of $`\widehat\Sigma-\widehat N`$ is then within $`3/8`$ of the integer $`G_{\ell j}`$. Nearest-integer rounding recovers $`G`$ exactly.

The same observations estimate every entry; $`Q`$ is not multiplied by $`L^2`$. Processing costs polynomial time in $`Q,L`$ and the input bit lengths. Since $`t_0,B`$ are polynomial in the security parameter in the stated family, $`Q`$ is polynomial too. Its schedule depends only on public parameters and can be declared before setup, as the selective-message experiment requires.

## 5. Key tails and correct integer lifts

Let $`N_{\rm col}`$ be the full dimension of one extended preimage column. Under the smoothing hypothesis in [Gaussian measurements](gaussian_measurements.md), the affine-coset moment-generating function gives

```math
\Pr(|W_i|>B)\le4e^{-\pi B^2/\sigma^2}.
```

One deliberately loose public integer choice is

```math
B=\left\lceil\sigma\big(\lambda+\lceil\log_2(8N_{\rm col}L)\rceil+1\big)\right\rceil.
```

The union bound over all coordinates of the selected columns is at most $`4N_{\rm col}L e^{-\pi B^2/\sigma^2}`$, hence negligible. This $`B`$ is polynomial in the dimensions, $`\sigma`$ and $`\lambda`$. It bounds the hidden mixed coordinates before the two blocks are added.

The covariance identity concerns the unwrapped integer $`z`$. [Parameters](parameters.md) uses the target's correctness estimate to bound the probability that any of the $`Q+1`$ observations wraps modulo $`q`$. Couple the observed experiment to the unwrapped experiment and add this probability. **Do not condition the moment calculation on successful lifting:** conditioning would generally change its moments. The unwrapped calculation and a separate coupling bound avoid that error.

## 6. Computing discrete moments with polynomially many bits

The estimator needs $`\nu=1/v`$ and $`\kappa_4=\mu_4/v^2`$. It does not enumerate all integers of magnitude $`\chi`$.

For $`\chi\ge1`$, use the dual theta sums

```math
S_j(\chi)=\sum_{t\in\mathbb Z}t^j e^{-\pi\chi^2t^2},
\qquad j=0,2,4.
```

Poisson summation and differentiation give

```math
\begin{aligned}
v&=\frac{\chi^2}{2\pi}-\chi^4\frac{S_2}{S_0},\\
\mu_4&=\frac{3\chi^4}{4\pi^2}
 -\frac{3\chi^6}{\pi}\frac{S_2}{S_0}
 +\chi^8\frac{S_4}{S_0}.
\end{aligned}
```

The dual summands decay at least as fast as a polynomial times $`e^{-\pi t^2}`$. To obtain $`P`$ absolute bits in these moments, truncate at $`|t|=O(\sqrt{P+\log(2+\chi)})`$, with a sufficiently large absolute constant and a Gaussian integral bound for the tail. Evaluate the remaining elementary functions with certified rational intervals. If an exponent already certifies a contribution smaller than the tolerance, omit that term using the bound. Its numerical magnitude does not cause a long loop. The bound $`v\ge a_0\chi^2`$ controls division and cancellation. Thus $`\nu,\kappa_4`$ can be computed to any polynomial number of bits in time polynomial in $`P+\log(2+\chi)`$.

For explicit precision accounting, use the unconditional public bound $`Z_{\max}=q`$ on the magnitude of every extracted integer observation, and set

```math
U=Z_{\max}/(a_0\chi^2)+mB.
```

Both $`Z_{\max}`$ and $`U`$ have polynomial bit length. Their numerical values need not be polynomially bounded; only their logarithms enter the precision cost below, and neither enters the sample bound $`Q`$. Compute $`\widehat\nu`$ with

```math
|\widehat\nu-\nu|
\le\min\left\{
\frac1{64(Z_{\max}+1)(U+1)},
\frac1{64(1+(m+\widetilde m)B^2)}
\right\}.
```

Then $`|\widehat Y_\ell-Y_\ell|\le1/[64(U+1)]`$, so each product changes by less than $`1/8`$. Block averages and medians preserve this bound. Also compute $`\widehat\kappa_4`$ to error at most $`1/[64(1+(m+\widetilde m)B^2)]`$. The diagonal and auxiliary Gram coefficients are bounded by $`mB^2`$ and $`\widetilde mB^2`$, so the known subtraction changes by less than $`1/8`$. The off-diagonal subtraction and the trace are exact integers.

All precisions require polynomially many bits in $`\log Z_{\max},\log\chi`$ and the dimensions. No sampling or arithmetic step has cost proportional to the numerical width $`\chi`$.

## 7. Output and evidence boundary

The output is the exact integer matrix $`G=H_s^{\mathsf T}H_s`$ except with the stated statistical, key-tail, setup-replacement and lift errors. It determines the nuisance kernel through $`\ker G=\ker H_s`$; it need not determine $`H_s`$ itself.

[The exact finite-law check](../verification/check_covariance_identity.py) verifies the identity and Gram subtraction by enumerating independent centered ternary variables. It tests the algebra, including nonsymmetric $`K`$ and the fourth-moment correction. It does not validate Gaussian sampling, concentration, or the full construction. Those claims are proved above and in the linked notes.

Continue with [the joint measurement geometry](gaussian_measurements.md) or [the complete theorem](attack.md).

