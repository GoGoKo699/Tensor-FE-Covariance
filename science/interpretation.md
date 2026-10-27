# Interpretation, boundaries, and open directions

## The established conclusion

The [main theorem](attack.md) gives a classical polynomial-time distinguisher for a specified degree-two family of the Cini–Lai–Ünal–Woo construction. It uses valid monomial functional keys and polynomially many known-zero encryptions. The two challenge messages are $0$ and $e_1$; every queried function evaluates to zero on both. The distinguishing gap is $1-\operatorname{negl}(\lambda)$.

The same mechanism distinguishes the corresponding direct secret-key tensor-preimage assumption experiments in [the model](model.md). That implication is established from their explicit distributions, not inferred merely from a failure of the construction.

## Why the mechanism works

The shared key material makes different output noises correlated. Those correlations are useful even though the encryption noise is very wide.

1. **Normalize the observations.** Dividing by the known encryption variance yields bounded standardized moments controlled by dimensions and short-key sizes.
2. **Recover a discrete invariant.** Subtract the known covariance contributions and round to the exact integer Gram $H_s^{\mathsf T}H_s$.
3. **Remove its image.** The Gram identifies the mixed nuisance kernel without revealing a particular factor $H_s$. Add the known auxiliary-key kernel and project.
4. **Test a rank-one explanation.** Zero-message data become measurements of $ee^{\mathsf T}$. The other challenge retains a transverse term. Joint restricted isometry makes that term uniformly incompatible with every rank-one explanation.
5. **Keep the algorithm finite.** Rational projection, bounded convex feasibility, integer rounding and an exact residual test establish polynomial bit complexity.

The proof of geometry precedes the key-dependent projection. Conditioning on that projection and pretending the remaining measurements are independent Gaussian matrices would be an invalid shortcut.

## What the large noise changes

Large noise increases the absolute size of each observed integer. It does not, in this family, force the normalized covariance estimator to use a number of samples proportional to that size. Similarly, the convex feasibility algorithm depends logarithmically on its outer radius, and integer rounding needs only constant absolute accuracy in the recovered matrix.

These facts do not say that arbitrarily large noise is harmless to every attack. The present argument relies on fixed, known noise laws, bounded standardized moments, polynomial short-key width, exact integer structure, and a suitable number of measurements. Changing those assumptions requires a new analysis.

## What the result does not establish

| Possible inference | Actual boundary |
|---|---|
| Ordinary LWE is easy | The proof uses additional correlated preimage key material and supplies no ordinary-LWE solver |
| Every parameter choice is covered | The number of columns must dominate the mixed nuisance dimension up to logarithmic factors |
| Any number of keys suffices | The theorem uses $\Theta(k^2)$ valid keys |
| Higher degrees follow automatically | The worked geometry and recovery theorem are degree two |
| A practical cryptanalytic tool has been built | The algorithm has a polynomial-time existence proof with conservative constants; no full implementation or timing claim is supplied |
| Different polynomial supports alone imply efficient distinction | Efficient hidden-Gram learning and uniform reconstruction are necessary parts of this proof |
| The entire proposed route to obfuscation is ruled out | Only the stated tensor-assumption regime and FE family are concluded here |
| The target's degree-one reduction is contradicted | The target's degree-one claim is separate and is not attacked by this result |

## Relationship to earlier work

Noise statistics, multiple-key attacks and nuclear-norm recovery all have substantial prior literature. The source preprint itself discusses different error-image manifolds. [Related work](../references/RELATED_WORK.md) identifies these antecedents and the verified parameter distinctions.

The new scientific content asserted here is the complete covariance-to-kernel-to-reconstruction argument for this affine-lattice Gaussian model and a compatible parameter family. This is a research proof recorded in a repository, not an external peer-review verdict. Source access limitations for two earlier full papers are stated in the comparison, so no exhaustive priority claim is made.

## Questions left open

The theorem suggests several precise questions, without supplying their answers:

- Can the measurement requirement be reduced enough to cover substantially larger secret-randomizer dimensions?
- Can the sample bound and optimization constants be improved to make finite parameter evaluation informative?
- Which unequal encryption widths preserve an efficient normalized Gram-learning procedure?
- Does a higher-degree analogue admit an equally controlled finite-bit reconstruction step?
- Can the same hidden-Gram principle yield a general lower bound for a broader, explicitly defined class of correlated-key FE schemes?

These are extensions beyond the theorem proved here. The explicit family and current proof stand independently of them.

