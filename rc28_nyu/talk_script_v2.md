# A Matthew Effect in Occupational Skill Content

## Updated talk script

### Title slide

Good morning, and thank you for being here.

This paper asks a simple question: when occupations change their skill content, does that change narrow occupational inequality, or reproduce it?

The usual expectation is optimistic. Technological change raises the demand for cognitive skills, and lower-status occupations may face the strongest pressure to upskill. That suggests some degree of convergence.

What we find is different. Skill change is not simply more intense at one end of the hierarchy. It is directional. Socio-cognitive skills tend to move upward, while sensory-physical skills tend to move downward.

The result is a Matthew effect in the content of occupations themselves.

### The Puzzle

Let me begin with the puzzle.

Recent evidence from job postings suggests that lower-status jobs are changing rapidly. Their advertised skill requirements may diversify more, or move farther from their previous profile.

But pressure to change does not tell us what change is ultimately realized. A job can change a great deal without becoming more cognitively intensive. And a new requirement can appear without moving that occupation closer to the top of the skill hierarchy.

So our question is not only *how much* occupations change. It is: *which skills move, and in which status direction?*

### From Upskilling Pressure to Realized Change

Our starting point is that occupations do not change in isolation.

They sit in a relational structure defined by task similarity, shared training, and productive complementarities. Those relationships shape which skill changes are feasible.

But feasibility and direction are different things. Similarity may tell us whether a skill can appear in a nearby occupation. It does not tell us whether that skill will move toward an occupation above or below its current holders.

That distinction takes us from upskilling pressure to realized, directional change.

### Two Different Objects: Demand Signals vs. Realized, Directional Change

This is where our study differs from recent work using job advertisements.

Those studies examine employer demand signals. They ask how much an occupation's advertised skill vector changes, or how diverse its requested skills become. These are important outcomes, but they are properties of one occupation at a time.

We study a different object. Using O*NET, we examine realized occupational requirements and organize the analysis around directed pairs of occupations.

For a particular skill, one occupation is the reference holder and another is the potential adopter or abandoner. We then ask whether the target ranks above or below the reference occupation.

So the key quantity is not simply change. It is the signed status gap between two occupations involved in a diffusion opportunity.

### Demand Signals vs. Realized Change: Schematic

The schematic makes the distinction concrete.

On the left, we can ask how much the skill profile of a single occupation changes. Its own status may predict the magnitude or diversity of that change.

On the right, we ask a relational question. When a specific skill is present in one occupation and later appears in another, where does the second occupation sit relative to the first?

We are not claiming to observe a skill being directly transmitted from one exact occupation to another. These are structured diffusion opportunities, not traced acts of transmission.

The empirical question is whether millions of these directed comparisons reveal a systematic status gradient, and whether that gradient differs by skill type.

### The Architecture We Build Upon

To classify skills, we combine two established insights.

The first is polarization. Skills cluster into a socio-cognitive domain associated with higher education and wages, and a sensory-physical domain associated with lower education and wages.

The second is nestedness. Skills do not form a flat list. Some are broad and provide scaffolding for other, more specialized capabilities.

Crossing domain with this position in the skill architecture lets us distinguish general socio-cognitive, specialized socio-cognitive, and sensory-physical skills.

The question is whether these classes follow the same pathways through the occupational structure. Our argument is that they do not.

## I. Directional Skill Diffusion

### Two Elementary Events

We focus on two elementary events: adoption and abandonment.

In an adoption opportunity, the source occupation already holds a skill and the target does not. We observe whether the target acquires it.

In an abandonment opportunity, both occupations initially hold the skill. We observe whether the target subsequently drops it.

Again, source and target identify the direction of the comparison. They do not imply that we observe direct transfer.

For each opportunity, we ask how the event hazard varies with baseline profile distance, the signed status gap, and the class of the skill.

### Theory: Directed Assortative Mixing

The first part of the argument is assortative mixing: occupational change should be more likely among occupations with similar skill profiles.

That gives us symmetric proximity. A nurse and a physician, for example, share more relevant tasks and training than a nurse and an unrelated occupation.

But proximity alone has no arrow. The nurse's probability of adopting a requirement held by physicians need not mirror the physician's probability of adopting a requirement held by nurses.

Our theoretical claim is that status gives this relational proximity a direction.

For socio-cognitive skills, adoption should be more likely above current holders, while abandonment should be more likely below them. For sensory-physical skills, the pattern should reverse.

If adoption and abandonment point in those same directions, small dyadic asymmetries can accumulate into a durable Matthew effect.

### Mechanisms Behind the Directional Gap

Several mechanisms could generate this asymmetry.

Occupations may emulate those above them, but differ in their capacity to realize that emulation. Complex requirements may be allocated to positions that already have complementary skills. Credentials can protect certain requirements once they become attached to higher-status occupations. And identical content may be recognized and rewarded differently depending on who performs it.

These are plausible channels, not mechanisms we separately identify here.

The empirical implication they share is narrower: conditional on occupational proximity, relative status should still predict the direction of skill change.

## II. Data and Methods

### Data

We combine O*NET observations from 2015 and 2024 with occupational wages from the BLS, as well as measures of education and cognitive task content.

The analytic universe contains 741 occupations and 160 skill requirements.

This produces roughly 40 million directed diffusion opportunities: 21.5 million for adoption and 18.6 million for abandonment.

The scale matters because the events themselves are sparse. We are looking for a systematic directional pattern across a very large relational risk set.

### Measures I: Diffusion Events

The unit is a directed occupation-occupation-skill triple.

For adoption, the source holds the skill in 2015 and the target does not. The outcome is whether the target crosses the RCA threshold by 2024.

For abandonment, both occupations hold the skill in 2015. The outcome is whether the target falls below that threshold by 2024.

Occupational status is the first principal component of wages, education, and cognitive task content.

We define the gap as target status minus source status. A positive gap means movement toward a higher-status target; a negative gap means movement toward a lower-status target.

That sign is the central information that a conventional distance measure discards.

### Measures I: Identification Strategy

Three features of the design are important.

First, we control for baseline skill-profile distance. This separates directional status sorting from ordinary relatedness between occupations.

Second, skill fixed effects absorb the fact that some requirements are intrinsically more likely to appear or disappear.

Third, we estimate complementary specifications with source and skill fixed effects, and with target and skill fixed effects.

Because the status gap is constructed from endpoint status, source and target fixed effects cannot both be included while identifying that gap. Agreement across the two strategies therefore matters.

Finally, uncertainty is clustered by source, target, and skill to reflect the network structure of the data.

### Measures II: Skill Classes

Here are the three skill classes produced by crossing domain and nestedness.

We identify 49 general socio-cognitive skills: broad capabilities that tend to provide scaffolding for other skills.

We identify 48 specialized socio-cognitive skills: narrower requirements that depend more heavily on that scaffolding.

And we identify 63 sensory-physical skills.

This classification lets us test whether direction differs only between cognitive and physical content, or also within the socio-cognitive domain.

### Directional Gravity Model

The model is a directional gravity-hazard model with a complementary log-log link.

The equation contains four substantive pieces: fixed effects for occupational endpoints and skills; an upward status-gap slope; a downward status-gap slope; and baseline profile distance.

Splitting the gap at zero is crucial. A model using only absolute status distance can tell us that two occupations are far apart. It cannot tell us which one ranks higher.

We estimate the model separately for adoption and abandonment, and for each skill class.

The test is straightforward: after accounting for proximity and fixed propensities, does the sign of the gap still organize skill change?

## III. Descriptive Patterns

### Adoption and Abandonment Gradients

Before turning to the model, consider the descriptive patterns.

The first result is familiar and reassuring: profile distance matters. Adoption becomes less likely as occupations become less similar. Abandonment becomes more likely as their profiles diverge.

So skill change is relationally local. Occupational proximity creates the channel through which change can occur.

But these panels only establish the symmetric part of the story. The next question is what happens once we place an arrow on that channel.

### Status-Gap Gradients and Flow Networks

Here the directional asymmetry becomes visible.

For both general and specialized socio-cognitive skills, adoption rises as the target moves above the source in status. For sensory-physical skills, adoption is more likely toward lower-status targets.

Abandonment reinforces rather than cancels this pattern. Lower-status occupations are more likely to shed socio-cognitive requirements, while higher-status occupations are more likely to shed sensory-physical ones.

The network visualizations express the same result as a flow structure: cognitive content is channeled upward, and physical content downward.

### Descriptive Result

The descriptive result can therefore be stated in two sentences.

Occupational similarity determines where skill change is feasible.

Relative status determines the direction that feasible change is more likely to take, and that direction reverses across skill domains.

The remaining question is whether this survives controls for occupations' and skills' stable propensities.

## IV. Gravity Model Results

### Fixed-Effects Gravity Estimates

These are the fixed-effects estimates.

Focus first on the signs and their consistency across specifications. The socio-cognitive coefficients indicate upward adoption and downward abandonment. The sensory-physical coefficients indicate downward adoption and upward abandonment.

In other words, the two types of event work together. Cognitive content is both added disproportionately above and removed disproportionately below. Physical content follows the mirror image.

And the pattern appears under both endpoint strategies.

### What the Model Shows

The model establishes three points.

First, direction matters beyond profile similarity. Similar occupations are not equally likely to change in both status directions.

Second, the pattern is not driven only by unusually dynamic source occupations, unusually receptive target occupations, or highly diffusible skills.

Third, adoption and abandonment compound. They do not represent offsetting forms of occupational adjustment.

That is the micro-level result. But a Matthew effect is ultimately a claim about the occupational structure as a whole. So we next ask whether these dyadic estimates reproduce the macro-level gradient.

### From Dyads to Occupational Stratification I

In this exercise, we aggregate the predicted dyadic events and compare the implied distribution of skill change across occupational status with the observed distribution.

For socio-cognitive skills, the directional model recovers the upward gradient in the data.

The important comparison is with the null models. A distance-only model remains close to flat. A model that knows the magnitude of the status gap but ignores its direction also fails to reproduce the observed pattern.

So relatedness and hierarchy are both necessary, but hierarchy must be signed.

### From Dyads to Occupational Stratification II

For sensory-physical skills, we see the mirror image.

The observed distribution slopes toward the bottom of the occupational hierarchy, and the directional model follows it. Once again, the direction-blind alternatives miss the gradient.

This is the bridge from local change to stratification: repeated, status-directed events reorganize the skill content of occupations in a way that preserves the cognitive-physical divide.

### Threats to Inference

We target four main threats.

To address a mechanical artifact in RCA, we freeze the denominator and re-estimate the results using raw importance scores.

To address stable occupation or skill propensities, we use the fixed-effects strategies and a within-stratum permutation test.

We vary the RCA threshold, status measure, and skill taxonomy to test dependence on measurement choices.

And we replicate the pattern across sub-periods to ensure that it is not produced by one exceptional episode.

The magnitudes move, as we should expect, but the directional asymmetry remains.

### Why This Matters

This matters because occupations are not fixed bundles of tasks. They are moving targets, and what they become is itself sorted by status.

The result is not simply that high-status occupations contain more cognitive skills at one point in time. It is that the process of occupational change tends to reproduce that concentration.

Socio-cognitive content accumulates above. Sensory-physical content accumulates below. And models that remove direction also remove our ability to explain those gradients.

Occupational inequality is therefore reproduced not only through wages, credentials, or the sorting of workers, but through changes in the content of occupations themselves.

### Implications: AI and a Compounding Barrier

This has an important implication for the current wave of technological change.

AI may raise productivity in cognitively intensive work while substituting for well-specified routine and physical tasks. But the capacity to move into the skills that complement new technologies is not evenly distributed across occupations.

Our results suggest a compounding barrier. Workers in physical-intensive occupations may be concentrated in content that is more exposed to substitution, while the occupational pathways toward socio-cognitive content are themselves status-sorted.

This is not a direct estimate of AI displacement. It is a claim about adjustment capacity: exposure and the ability to reach new skill destinations may be unequally distributed.

That makes the architecture of skill diffusion central to understanding who can adapt.

### Limitations

There are four limits to keep in view.

First, the analysis is at the occupational level. We do not observe the firms, workers, or organizational decisions behind each change.

Second, the design is observational. Shared shocks may influence multiple occupations, although a common shock alone would not explain why direction reverses between cognitive and physical skills.

Third, the evidence comes from the United States. Credentialing, unions, training systems, and wage-setting institutions may alter the magnitude of these patterns elsewhere.

Finally, we identify the directional regularity shared by several mechanisms. We do not adjudicate which mechanism produces it.

These limitations define the next research questions; they do not erase the directional pattern we document.

### Conclusion

Let me close with three points.

First, occupational skill change is not generalized cognitive upgrading. It is a status-sorted process.

Second, adoption and abandonment work together: socio-cognitive skills move upward, while sensory-physical skills move downward.

Third, these local asymmetries scale into occupational stratification. Occupations already rich in cognitive content are positioned to accumulate more, while physical content becomes increasingly concentrated below.

So the central message is this: occupations are not fixed bundles of tasks. They change. But the direction of that change is structured by status, and that process can reproduce inequality even in a period of widespread technological transformation.

Thank you.
