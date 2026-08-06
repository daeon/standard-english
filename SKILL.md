---
name: standard-english
description: >-
  Select and apply an explicit language standard, controlled-language profile,
  normative keyword system, terminology policy, accessibility writing profile,
  or formal documentation guide. Use for standards selection, controlled
  technical English, requirements language, regulated or safety-sensitive
  wording, terminology governance, localization-ready content, and
  conformance-oriented review. Do not use for ordinary grammar correction,
  casual messages, creative writing, or routine copyediting unless the user
  requests a named standard or formal profile.
---

# Standard English

Route standards-sensitive writing, rewriting, review, and audit tasks to the smallest useful profile stack. Preserve meaning before improving style. Do not force a standard onto work that is adequately governed by the requested channel, repository, publication, or supplied house style.

Invocation: mention `standard-english`, choose it from `/skills`, or let the harness select it for explicit standards selection, controlled language, requirements language, safety or legal wording, terminology governance, accessibility-sensitive content, localization-ready source content, or conformance-oriented review.

## Default posture

Make routine routing decisions automatically. Ask for a choice only when unresolved alternatives materially change meaning, obligations, safety, normative force, or compliance scope.

A valid routing result can be:

```text
No external profile required — use the conventions of the requested channel,
repository, publication, or supplied house style.
```

## Core rule

Select standards from the task and governing sources, not from the user's vocabulary alone.

Use this sequence:

```text
need for explicit profile → governing sources → task classification →
profile fit → conflict elimination → material-risk gates → evidence strength →
permitted claim → output mode
```

Load `./references/routing-algorithm.md` for the full decision process and `./references/selection-matrix.md` for task classification.

## Profile stack

Keep roles distinct:

1. **Governing source** — law, regulation, contract, publication policy, or supplied organization rules. It overrides lower-level profiles and does not count toward the stack limit.
2. **Document or content profile** — the main standard for the communication outcome or information product.
3. **Language constraint** — at most one controlled-language, normative-keyword, or terminology profile.
4. **Delivery overlay** — at most one accessibility, localization, or channel profile.

Use no more than three selected profiles besides governing sources unless the task spans independent risks. Explain every extra profile. Do not stack profiles merely because they are related.

## No-profile gate

Before selecting a standard, ask internally whether an explicit profile materially improves at least one of these outcomes:

- correctness or preservation of obligations;
- safety or legal interpretation;
- requirements quality or normative consistency;
- terminology governance;
- accessibility or localization readiness;
- conformance-oriented review;
- consistency with a required publication or organization framework.

If not, use native channel or house conventions and stop routing.

## Independent assessments

Never collapse these into one score:

- **Profile fit** — which profile best matches the task.
- **Routing confidence** — how clearly one profile dominates.
- **Material risk** — whether unresolved choices can change meaning or consequence.
- **Evidence strength** — what authoritative material is available.
- **Claim level** — what alignment or conformance language is permitted.

Weak evidence limits the claim; it does not make a less suitable profile a better fit.

## Confirmation and escalation

Use the independent gates in `./references/risk-and-escalation.md`.

Ask the user to choose only when two or more materially different routes remain plausible. High consequence alone does not require routing confirmation. Do not ask merely because several profiles could offer minor improvements.

When a domain decision is unresolved, preserve the source meaning, label the decision, and identify the responsible reviewer. Do not invent hazard severity, legal effect, thresholds, definitions, warnings, guarantees, or acceptance criteria.

## Confidence model

Use qualitative routing confidence only when useful:

- **High** — one route clearly dominates and no routing gate applies.
- **Medium** — one route is best but a secondary route is plausible; state the assumption and proceed unless the difference is material.
- **Low** — missing information could change obligations, safety, normative interpretation, or compliance scope; recommend ranked routes and request a choice.

Do not expose numeric pseudo-precision.

## Workflow

1. Determine whether an explicit profile is useful. If not, use the no-profile result.
2. Identify governing sources and their precedence.
3. Classify purpose, audience, document type, normative force, consequence, domain, channel, localization, and supplied authority.
4. Select candidates from `./references/standards-catalog.md`.
5. Eliminate redundant, incompatible, unavailable-for-the-requested-claim, jurisdictionally inappropriate, or unnecessarily restrictive candidates.
6. Choose one document/content profile, zero or one language constraint, and zero or one delivery overlay.
7. Apply routing, evidence, domain-decision, and human-review gates independently.
8. Select the output mode from `./references/output-contract.md`.
9. Execute while preserving facts, conditions, exceptions, thresholds, actors, permissions, prohibitions, sequence, terminology, and normative force.
10. Report unresolved ambiguity, terminology gaps, conflicts, evidence limits, and required reviewer roles.

## Normative-language rule

Use one normative keyword system unless a governing source explicitly requires another:

- Internet and interoperability specifications: RFC 2119 and RFC 8174 with defined uppercase `MUST`, `SHOULD`, and `MAY`.
- ISO-like standards and formal specifications: the applicable ISO/IEC drafting rules using `shall`, `should`, `may`, and `can` with distinct meanings.

Do not silently convert between systems. Flag mixed systems unless the document explicitly defines precedence.

## Source and compliance boundary

The structured registry in `./data/standards-catalog.yaml` records source authority, edition, lifecycle, role, access, scope, exclusions, and conformance prerequisites. The generated `./references/standards-catalog.md` is a routing aid, not authoritative standard text.

Therefore:

- apply publicly known principles and user-provided rules as a profile;
- use supplied authoritative clauses, approved checklists, termbases, schemas, and organization policy when available;
- do not reproduce substantial copyrighted standard text;
- do not claim `compliant`, `certified`, `passed`, or `conformant` without the required authoritative material, assessment scope, validation process, and human roles;
- prefer `edited using`, `aligned with`, `checked against the supplied profile`, or `candidate violations` when evidence is limited;
- require qualified human review for safety, legal, regulated, or other high-consequence content.

## Special conformance boundaries

- **CAN-ASC-3.1:2025:** textual inspection alone cannot establish conformance. Intended-audience involvement, evaluation, and testing are part of the conformance workflow.
- **ASD-STE100:** do not claim conformance without the applicable issue, dictionary decisions, approved project terminology, and an appropriate checking process.
- **WCAG:** a wording review cannot establish page-level WCAG conformance; implementation, interaction, semantics, technology support, and human evaluation also matter.
- **ISO 24495-3:** use for plain science communication to varied audiences, not as a research-reporting, journal-style, or methodology standard.
- **ISO 18587:** use only for full human post-editing of machine-translation output, not generic AI rewriting.

## Glossary authority

Treat a supplied glossary, termbase, schema, API definition, UI string catalog, or product taxonomy as authoritative unless it conflicts with a higher-order legal, safety, or contractual source.

For each concept:

- use one preferred term where practical;
- preserve exact product, API, command, field, and UI labels;
- record deprecated, forbidden, or ambiguous synonyms;
- do not invent acronym expansions;
- flag new terms instead of silently normalizing them.

## Rewrite discipline

- Preserve facts, conditions, exceptions, thresholds, actors, permissions, prohibitions, and sequence.
- Separate instructions from explanations.
- Use one primary action per procedural step when the selected profile calls for it.
- Replace vague modifiers with measurable criteria only when evidence exists.
- Keep examples visibly non-normative unless the source says otherwise.
- Retain necessary technical terms and define them for the audience instead of deleting them.
- For repository work, edit requested files in place when tools permit, validate the result, and summarize material changes rather than returning only a proposed rewrite.

## Audit discipline

Classify each finding as exactly one of:

1. **confirmed issue** — directly supported by supplied authoritative material;
2. **candidate issue** — likely under the selected profile but requires authoritative verification;
3. **content ambiguity** — source meaning is unclear;
4. **domain decision** — a subject-matter expert must decide;
5. **preference** — optional style improvement, not a violation.

Do not inflate preferences into compliance failures.

## Required output

Always identify the selected route, preserve source meaning, state evidence limits when material, and surface unresolved ambiguity. Use the smallest output mode that satisfies the request.

## Failure modes

- Forcing an external standard onto ordinary writing.
- Selecting a profile because its text is available rather than because it fits the task.
- Treating process standards, interchange formats, accessibility requirements, and editorial guides as peer writing styles.
- Selecting ASD-STE100 for all technical writing.
- Applying plain language to requirements without preserving obligation strength.
- Combining RFC `MUST` with ISO `shall` without defined precedence.
- Claiming formal compliance from memory or public summaries.
- Treating readability scores, sentence length, or automated checks as proof of clarity or accessibility.
- Removing legal, safety, scientific, or technical nuance to make text shorter.
- Asking the user to choose when differences are immaterial.
- Failing to escalate an unresolved material domain decision.
