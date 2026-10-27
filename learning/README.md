# Learning route

The central question is how repeated encryptions can reveal a fixed relation among functional keys even when every authorized function has the same value on the two challenge messages. The answer connects three objects: the covariance of observable noise, the kernel of a hidden integer Gram matrix, and a rank-one explanation of a fresh observation.

The selected educational anchor is **Chris Peikert, _A Decade of Lattice Cryptography_ (2016)**. Its relevant sections supply the lattice, Gaussian and LWE foundations. The local bridge supplies the functional-encryption experiment and the statistical and matrix-recovery steps particular to this project.

## Reading routes

| Purpose | Route |
|---|---|
| Understand the complete idea | Read the [project bridge](BRIDGE.md), including the projection example, then the [main theorem](../science/attack.md) and [interpretation](../science/interpretation.md). |
| Connect existing lattice knowledge to this project | Use the [anchor and notation map](ANCHOR.md), then follow its source-to-project table. |
| Build the background systematically | Follow M01–M14 in the [30-milestone map](MILESTONES.md), consulting the indicated anchor sections and local explanations as needed. |
| Follow the argument from observations to its security consequence | Follow M15–M30 in the [same map](MILESTONES.md), with the scientific pages as the authoritative statements and proofs. |
| Audit a technical step | Go directly to the [scientific index](../science/README.md). |
| Inspect a reproducible calculation | Run the four checks in [Verification](../verification/README.md). |

The map allocates **14 milestones to background and preliminaries** and **16 to the narrative and contribution**. The background must connect modular arithmetic, probability, lattice sampling, functional-encryption access and low-rank recovery. The narrative then follows the actual proof interfaces from legal observations to exact covariance recovery, correlated measurement geometry, finite computation and the final parameter regime. M14 and M30 integrate their respective phases.

The map describes shared scientific understanding targets. It does not require reading the entire survey or every technical lemma in order to understand the result. Research citations beyond Peikert remain available in [Related work](../references/RELATED_WORK.md) for attribution and proof dependencies.

## The distinction to retain

The result is a classical polynomial-time argument for a specified degree-two family of one tensor functional-encryption construction. Its many-key and known-message access, smoothing, width and dimension assumptions are part of the statement. The proofs establish an asymptotic distinguishing gap; the small verification scripts check selected identities and examples. The repository does not provide a full cryptosystem implementation or practical attack timings.

[Repository overview](../README.md) · [Anchor](ANCHOR.md) · [Project bridge](BRIDGE.md) · [Milestones](MILESTONES.md)
