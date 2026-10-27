# The quadratic tensor-FE experiment

This project studies the degree-two construction and secret-key tensor-preimage assumption in Cini, Lai, Ünal and Woo [CLÜW26](../references/RELATED_WORK.md#cluw26). The objective is to distinguish two allowed challenge messages using their functional keys and polynomially many encryptions of a known message. All computation and queries are classical.

The attack uses the arithmetic of the ciphertexts and keys. It requires no decryption oracle, faulty implementation, timing observation, or access to the encryption matrices. The security experiment already supplies the information used below.

## 1. Parameters and conventions

| Symbol | Meaning |
|---|---|
| $\lambda$ | Security parameter |
| $k$ | Number of message coordinates |
| $n$ | Number of fresh secret-randomizer coordinates per encryption |
| $m$ | Number of primary ciphertext/error coordinates |
| $\widetilde m$ | Number of auxiliary ciphertext/error coordinates |
| $h=k+n$ | Number of rows of the hidden primary matrix |
| $q$ | Prime ciphertext modulus |
| $p$ | Small public scaling integer, coprime to $q$ |
| $\chi$ | Common encryption Gaussian width in the parameter family studied here |
| $\sigma$ | Short-preimage Gaussian width |
| $L$ | Number of exposed, distinct functional-key columns |

For a discrete set $S\subseteq\mathbb R^D$, write

```math
\rho_\sigma(S)=\sum_{z\in S}\exp(-\pi\|z\|_2^2/\sigma^2),
\qquad
D_{S,\sigma}(z)=\frac{\exp(-\pi\|z\|_2^2/\sigma^2)}{\rho_\sigma(S)}.
```

Widths use the lattice-cryptography convention: a continuous Gaussian with the same density has variance $\sigma^2/(2\pi)$ in each coordinate. The exact variance of $D_{\mathbb Z,\chi}$ is denoted by $v_\chi$; it is not silently replaced by its continuous value.

Vectors are columns. Tensor indices use the explicitly displayed order; an $m^2$-vector indexed by $(i,j)$ is identified with an $m\times m$ matrix having that entry. Thus $(e\otimes e)^{\mathsf T}\operatorname{vec}(K)=e^{\mathsf T}Ke$. No symmetry of the sampled $K$ is assumed. The inner product on matrices is the Frobenius inner product. For a residue modulo odd $q$, $\operatorname{bal}_q$ denotes its representative in $(-q/2,q/2)$.

## 2. The public key columns and hidden extension

Let $S=[I_k;0_{n\times k}]$. The hidden setup matrices have dimensions

```math
A\in\mathbb Z_q^{h\times m},\quad
\widetilde A_2\in\mathbb Z_q^{h^2\times\widetilde m},\quad
\widetilde A_L\in\mathbb Z_q^{hm\times\widetilde m},\quad
\widetilde A_R\in\mathbb Z_q^{mh\times\widetilde m}.
```

The full short-preimage extension consists of integer matrices

```math
K\in\mathbb Z^{m^2\times k^2},\quad
C\in\mathbb Z^{\widetilde m\times k^2},\quad
F_L\in\mathbb Z^{hm\times k^2},\quad
F_R\in\mathbb Z^{mh\times k^2}
```

satisfying

```math
\begin{aligned}
(A\otimes A)K+\widetilde A_2 C&=S\otimes S,\\
(A\otimes I_m)K+\widetilde A_L C+pF_L&=0,\\
(I_m\otimes A)K+\widetilde A_R C+pF_R&=0
\qquad\pmod q.
\end{aligned}
```

Here $C$ denotes the matrix called $\widetilde K$ in [CLÜW26]. The shorter notation separates it from the individual quadratic matrices $K_\ell$ below. This is the degree-two specialization of the paper's extended tensor matrix, with its two mixed blocks written separately.

Theorem 2 of [CLÜW26] permits analysis in an ideal distribution where the hidden setup matrices are uniform and, conditional on them, each complete column

```math
W_\ell=(\operatorname{vec}K_\ell,C_\ell,(F_L)_\ell,(F_R)_\ell)
```

is a spherical discrete Gaussian on the appropriate affine preimage lattice coset. Different columns are conditionally independent; their affine targets may differ. The actual output distribution of $(A,\widetilde A,K,C)$ is negligibly close to the corresponding marginal of this ideal full extension. The hidden $F_L,F_R$ are analysis variables supplied by that extension; no claim about an implementation-specific hidden witness is required. The model does **not** assert that the coordinates within a column are independent. The required smoothing property is derived from the published trapdoor bound in [Gaussian measurements](gaussian_measurements.md).

## 3. Ciphertexts and the observable integer noise

For a message $x\in\mathbb Z^k$, draw independent

```math
s\leftarrow D_{\mathbb Z^n,\chi},\qquad
e\leftarrow D_{\mathbb Z^m,\chi},\qquad
\widetilde e\leftarrow D_{\mathbb Z^{\widetilde m},\chi},\qquad u=(x;s).
```

The quadratic ciphertext is

```math
\begin{aligned}
c^{\mathsf T}&=u^{\mathsf T}A+pe^{\mathsf T}\pmod q,\\
\widetilde c^{\mathsf T}
&=(u\otimes u)^{\mathsf T}\widetilde A_2
 +p(u\otimes e)^{\mathsf T}\widetilde A_L
 +p(e\otimes u)^{\mathsf T}\widetilde A_R
 +p^2\widetilde e^{\mathsf T}\pmod q.
\end{aligned}
```

For the functional coefficient vector $y$, the key is $(Ky,Cy)$. Multiplying out the ciphertext and using the three preimage equations gives

```math
(c\otimes c)^{\mathsf T}Ky+\widetilde c^{\mathsf T}Cy
 = (x\otimes x)^{\mathsf T}y+p^2z_y\pmod q,
```

where the integer noise is

```math
z_y=(e\otimes e)^{\mathsf T}Ky+\widetilde e^{\mathsf T}Cy
 -(u\otimes e)^{\mathsf T}F_Ly-(e\otimes u)^{\mathsf T}F_Ry.
```

The factor is exactly $p^2$. Each mixed ciphertext term supplies one factor $p$; its preimage relation supplies the second. This is the concrete content of the target's equations (19), (22), and (28)–(30).

The published correctness bound chooses $q$ large enough that the integer on the right lies in the balanced interval except with negligible probability. For keys whose authorized function value is known to be zero, the adversary therefore computes

```math
z_y=\frac{1}{p^2}\operatorname{bal}_q
 \big((c\otimes c)^{\mathsf T}Ky+\widetilde c^{\mathsf T}Cy\big).
```

Malformed lifts are rejected. The analysis couples the actual observations to the unwrapped integer model and charges the negligible probability that any required lift differs. The moment identities are computed in the unwrapped model before this coupling bound. This uses a proved bound on the intermediate integer, rather than inferring it merely from correct output after reduction modulo the message modulus.

## 4. Legal selective-message access

The selective IND-CPA game in Figure 1 of [CLÜW26] allows the adversary to specify polynomially many known plaintexts and two challenge plaintexts before setup. It receives their ciphertexts and can request functional keys whose functions agree on both challenge messages.

Choose every training message to be $0$, and challenge messages

```math
x_0=0,\qquad x_1=e_1.
```

Request the distinct monomial functions

```math
\{x_i x_j:1\le i\le j\le k,\ (i,j)\ne(1,1)\}.
```

There are $L=k(k+1)/2-1$ such functions, and every one evaluates to zero on both challenges. Each has coefficient norm one, so message and function bounds equal to one suffice. Using only upper-triangular monomials avoids counting two representations of the same polynomial as different functional queries.

Restrict all key matrices to these columns and define

```math
H_{a,i,\ell}=(F_L)_{(a,i),\ell}+(F_R)_{(i,a),\ell}.
```

Let $H_s\in\mathbb Z^{nm\times L}$ contain the $n$ secret-randomizer rows, and let $J\in\mathbb Z^{m\times L}$ contain the first message row. The exposed noise vector is then

```math
z=\mathcal K(ee^{\mathsf T})+C^{\mathsf T}\widetilde e
       -H_s^{\mathsf T}(s\otimes e)-bJ^{\mathsf T}e,
\qquad
\mathcal K(X)_\ell=\langle K_\ell,X\rangle_F,
```

for challenge bit $b\in\{0,1\}$. Training observations have $b=0$. Fresh randomness is independent across encryptions, while the key matrices are fixed.

## 5. Direct tensor-assumption interpretation

In Figure 3 of [CLÜW26], the adversary is given all $k^2$ key columns. It may choose all auxiliary messages and the challenge parameter $x^*$ to be zero. In experiment zero, both auxiliary and challenge ciphertexts use the same $n$ secret coordinates. In experiment one, auxiliary ciphertexts use $(0_k;s;0)$ and the challenge uses $(0_k;s;1)$ in a hidden matrix with one extra row.

Consequently both experiments have exactly the displayed observation model: the second experiment has the additional $J^{\mathsf T}e$ term. Its underlying preimage lattice is different, but the same uniform smoothing and concentration bounds apply separately to both distributions. The [parameter family](parameters.md) includes sufficient slack for this extra row. This gives a direct distinguisher for the degree-two assumption as well as the permitted-key FE interpretation.

## 6. Scope of the model

The result uses many fixed functional keys and repeated honest encryptions of a known message. Its Gaussian-width and dimension conditions are explicit in [the main theorem](attack.md). The short-preimage sampler, ciphertext construction, and access experiment come from [CLÜW26]; the covariance-learning and reconstruction argument is developed in the following pages. The conclusion applies to this construction and these parameter families. Increasing the nuisance dimension beyond the stated measurement regime removes the guarantee of this particular argument.

Continue with [exact covariance recovery](noise_covariance.md), or go directly to [the full distinguishing theorem](attack.md).
