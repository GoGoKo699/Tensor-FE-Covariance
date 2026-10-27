# Scientific account

The repository separates the model, statistical inference, measurement geometry, finite computation and parameter instantiation so each dependency can be checked independently.

| Read | Question answered |
|---|---|
| [Model](model.md) | What information is available, and why are all queried functions legal? |
| [Noise covariance](noise_covariance.md) | How can wide integer noise reveal an exact hidden Gram matrix? |
| [Gaussian measurements](gaussian_measurements.md) | Why does the actual affine-lattice sampler supply the joint geometry? |
| [Reconstruction](reconstruction.md) | How is the decision made in polynomial bit complexity? |
| [Parameters](parameters.md) | Do all hypotheses coexist in a published admissible regime? |
| [Main theorem](attack.md) | How do the components combine, and what is the total error? |
| [Interpretation](interpretation.md) | Which security conclusions and limits follow? |
| [Sources and related work](../references/RELATED_WORK.md) | What is inherited, compared and newly established? |

For a first pass, read the model, main theorem and interpretation. For a proof audit, follow the table from covariance through parameters, then check the theorem's interface and probability ledger.

For a conceptual introduction, use the [project bridge](../learning/BRIDGE.md). The [learning route](../learning/README.md) connects the selected Peikert anchor and the project's 30 milestones to these authoritative statements and proofs.

[Verification](../verification/README.md) contains small reproducible checks of specified algebraic identities. They support inspection of the proofs and do not replace the statistical or complexity arguments.

