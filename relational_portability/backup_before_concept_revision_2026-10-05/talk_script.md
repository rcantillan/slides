# Talk script — The Ties That Open a Community Are Not the Ties That Move It
Speaker notes by slide (English). Target: ~20 minutes for the main deck (slides I–IV); appendix on request.

## I. The Problem and the Argument

Thank you for being here. The paper asks a simple question about diffusion: the people who are best placed to open a community to something new, are they also the people who move the community once it has to decide? Our answer is that it depends on the task, and that you can test it.

## Two Questions About Diffusion

Katz and Lazarsfeld taught us that leadership is specific to a domain. Contemporary work on seeding asks who to approach first. What the strategy leaves implicit is whether the position that makes someone a good point of entry remains valuable as others decide whether to act. That is the question of the paper.

## Two Literatures, One Missing Question

We sit between two literatures. Structural work shows that returns to targeting depend on tie organization. Multiplex work shows that relations are not interchangeable. Both establish that different relations matter. Neither treats the continuity of advantage across tasks as an object of explanation. That continuity is what we study.

## A Diffusion Process Is a Sequence of Tasks

By task we mean a stage of a diffusion process. It is not necessarily something the focal actor does: a lender choosing entry points, a seed set spreading news and a household deciding to borrow are different loci of action. What makes them comparable is that each orders the same population. We distinguish tasks by their place in the process, not by the rankings they produce; otherwise any difference in rankings could be relabeled as a new task. The Rule, Sabetta and Bearman point is only a framing: an opening has consequences when it is tied into what follows.

## Two Households in a Village

Take a village. One household belongs to the schoolteacher; neighbors consult it. The other is visited every day. An organization looking for entry points finds the first household. Whether the second matters more once people must decide to take on a debt depends on what that decision requires. If it requires seeing how others manage repayments, coordinating with them, or relying on them, routine interaction can supply what advice does not.

## Nonportability Needs Three Conditions Together

Panel A: the same actors occupy different positions in different relational domains. Panel B: two tasks weight capacities differently; larger circles mean greater demand. Panel C: an actor who leads in the domain that matters for the first task can trail in the domain that matters for the second. None of the three conditions is enough alone. If everyone stands in the same relative position across domains, nothing changes. If the domains supply equivalent capacities, a change in task demands changes nothing.

## Advantage Is a Match Between a Position and a Task

Relevant position is a property of a match between a relation and a task, not of a household alone. It needs neither a universal centrality measure nor an intrinsically superior layer. x_il is the household's standing in domain l; omega_lr says how much task r draws on the capacity that domain l makes plausible; the sum blends domains by that fit; R_ir is the result. Read the equation left to right as: advantage for a task equals standing in each domain, weighted by how well that domain fits the task.

## When Does Advantage Change? An Exact Identity

In the two-domain case, s indexes how differentiated the domains are and tau how much a task demands the capacity in which domain one specializes. The identity says advantage changes only if domains are differentiated, task demands change, and actors differ in their positions. Because the right side is a product, each of the three null cases returns exactly zero reordering, and they keep a change in a coefficient from being read after the fact as a new function of the relation. A changed score need not change a ranking; the share of pairs that actually exchange places measures how much nonportability there is.

## Three Testable Implications

H1 is closer to a condition than to a contested hypothesis. H2 is a claim about orderings; that they differ because the stages draw on different capacities is an interpretation the data suggest but do not identify. H3 follows because a union network sums relations that supply different capacities. The secondary test was specified, with controls and placebo, in the analysis code before estimating it.

## Setting: Microcredit Entering 75 Karnataka Villages

We use the multiplex data collected by Banerjee and colleagues. A household census and a network survey were fielded in 2006, about six months before the lender entered any village. Borrowing carried repayment obligations, default risk and reputational exposure: a decision for which knowing the program existed was necessary but far from sufficient. Complete data are available for 10,618 households in 49 villages. The lender chose entry points by social role and did not observe the networks, so its relational footprint is an empirical question.

## Same Households, Three Relational Layers

A schematic of what the data contain: the same households, observed in three relational layers (advice and decision, exchange, visiting). Dashed lines link a household across layers. Large nodes mark households that are central in one layer; they are not the same households in every layer. The picture is an illustration, not an estimate.

## Three Relational Domains, One Position Measure

Respondents named households with which they maintained several kinds of relation; following the original authors we combine paired name generators into three undirected domains. Mean degree is 3.2, 4.2 and 5.3, against 7.0 in the union of all relations. A coefficient compares the least and the most central household of a village. The capacities in the table are those each domain makes plausible, not exclusive transmission channels.

## How Position Is Measured

Diffusion centrality is the expected number of times information starting at a household reaches the others through walks of bounded length. A is the adjacency matrix of the domain, q is set to the inverse of its largest eigenvalue so that longer walks count less, T equals the layer's diameter, and the vector of ones means every household starts with one unit. Scores are normalized to zero-one within each village and domain, so coefficients compare the least and the most central household of a village.

## Same Households, Two Tasks

For each outcome we estimate a linear probability model in which the three domains compete, and we estimate both equations jointly so that inference on theta keeps the covariance generated by observing both outcomes for the same households. k indexes the outcome: G is designation, U is uptake. The village intercept means every comparison is within a village; beta is the change in probability associated with moving from the least to the most central household in a domain, because scores are normalized to zero-one within each village. Standard errors are clustered by village; wild-cluster bootstrap with 49 villages.

## The Reversal Estimand

Theta subtracts the entry-stage gap between Visiting and Advice from the adoption-stage gap. If the same relational advantage carried from entry to adoption, the two gaps would be equal and theta would be zero. The two contrasts have opposite signs, so the reversal does not depend on putting probabilities of different base rates on a common scale. Designation is a selection rule applied by the lender, not an act performed by households, so reading it as a task with communicative demands is an interpretation. That is why we add an independent benchmark.

## Triangulation: Three Designs, Three Different Questions

This is how the evidence is organized. The within-BSS comparison is the primary test, and its object is positions. Designation records where an organization began, not how information traveled, so we add an independent benchmark for the informational task: a randomized seeding experiment in the same region. The experiment identifies how the relational position of a seed set affects reach with the village network held fixed. The simulation is a statement about scope, not a test: it shows what the three conditions imply for reach. The studies differ in units and villages. We do not subtract one set of coefficients from the other or test their difference as a common parameter.

## Rival Explanations We Take Seriously

The design is observational. We address four alternatives before the results. General prominence predicts that the same households lead in both tasks; it does not predict that different domains order them for different tasks. Spatial proximity is the one we cannot fully resolve: household coordinates that can be linked to these records are not publicly available, so we use enumeration order as a proxy.

## H1: The Domains Rank Households Differently

H1 would fail only if the domains ranked households nearly identically. The domains are far from independent, which limits how much reordering any change in task demands can produce. What matters is how much reordering the observed correspondence allows, which the simulation takes up.

## H2: Entry and Adoption Privilege Different Relations

Panel A: Advice/Decision centrality strongly characterizes the entry pool; Exchange and Visiting carry little designation signal. Panel B: adoption shows the opposite profile; Visiting predicts take-up and the other two do not. Between the tasks the Advice/Decision coefficient falls by 0.252 and the Visiting coefficient rises by 0.200. Substantively, moving from the 25th to the 75th percentile of Visiting centrality corresponds to 4.3 percentage points of adoption against a base rate of 17.3 percent.

## The Reversal Is Not Fragile

Adjusting the adoption model for designation leaves the Visiting coefficient at 0.174. The reversal is larger when Advice/Decision is represented by the decision generator than by the advice generator, a point we return to in the appendix.

## H3: The Aggregate Network Conceals the Reversal

This is a stronger claim than a contrast in significance, because the two coefficients differ from each other. The negative union coefficient in the joint model should not be over-read: the model also controls for union degree, which is mechanically related to union centrality. The finding does not conflict with Banerjee and colleagues, who showed that the union-network centrality of a village's entry points predicts the village's adoption rate. We ask a different question: which households adopt, within villages.

## What Qualifies the Result

The spatial check is the most consequential qualification. At the most local threshold, which classifies a third of Visiting ties as near, near ties predict adoption and the remaining ties do not. This is what one would expect if routine co-presence lets households observe how neighbors manage their loans, and it is also what one would expect if neighborhoods differed in exposure. We report the secondary test as uninformative. Positional differentiation itself is established directly by H1; what the villages do not provide is enough variation to show that the entry pool's advantage scales with it.

## An Independent Benchmark for the Information Task

Because assignment is random within each village, the experiment identifies how the relational position of the seed set affects realized informational reach. We measure seed exposure relative to its randomization distribution within each village, which removes differences in network size and topology that random assignment did not generate. We read the experiment as supporting the informational side of the argument, not as establishing it. Its Advice domain is the advice generator alone, whereas the BSS composite also includes the decision generator, so the domains are harmonized, not identical.

## Two Tasks, Two Orderings, Not One Estimate

This slide is a reading aid, not a calculation. The experiment is a benchmark for the informational task, not a first stage of the BSS process. Its unit is a village's seed set and its outcome is village-level reach, whereas the BSS models concern households' own positions and adoption. The two point separately to Advice ranking above Visiting when the task is spreading information and to Visiting ranking above Advice/Decision when the task is a household's own take-up of a costly practice.

## When Does Reordering Matter?

The model instantiates the two-domain case of the identity. A factorial design varies the three conditions independently. All three null cases return exactly zero reversal and zero loss, and the program stops if they do not. Varying the reach horizon, attenuation, exposure scale, number of initiators, degree and group structure changes magnitudes but never the ordering. Exhaustive enumeration in smaller networks confirms that the selection heuristic attains the exact optimum. The shaded band is the interquartile range of correspondence across the 75 villages.

## Where the Karnataka Villages Sit

One structural component of the loss, the correspondence between two layers' rankings, can be computed from network data alone, before any outcome is observed. The loss also depends on how differently the layers are specialized, on how much task demands change, and on the redundancy of the network and the selection budget. The synthetic and the observed-network figures are not comparable estimates; part of the gap plausibly reflects the selection budget.

## Relational Advantage Is a Match, Not an Attribute

The argument returns to a question of specificity that the founders of diffusion research posed and later work largely set aside. We add a functional dimension to the structural analysis of how ties are organized. The relations that give an organization purchase on a village need not organize the village's response. The argument should matter most where adoption is consequential: a missed-call promotion is cheap and reversible; group microcredit entails joint liability and financial risk. The same reasoning applies to recruitment into risky collective action and to the uptake of unfamiliar health practices.

## Four Limits

Data recording information receipt, tie-specific resources and later action for the same actors would permit a direct test of the capacities. Without linkable household locations we cannot tell learning from neighbors apart from neighborhood differences in exposure.
