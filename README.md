# Standard English

[![Validate](https://github.com/daeon/standard-english/actions/workflows/validate.yml/badge.svg)](https://github.com/daeon/standard-english/actions/workflows/validate.yml)

`standard-english` is an AI-agent skill for selecting and applying explicit language standards, controlled-language profiles, normative keyword systems, terminology policies, accessibility requirements, and formal documentation guides.

It uses a deterministic routing model:

```text
need for explicit profile → governing sources → task classification →
profile fit → conflict elimination → material-risk gates → evidence strength →
permitted claim → output mode
```

Profile fit, material risk, evidence strength, and claim level are assessed independently. A missing standard does not make a less suitable style guide a better fit; it limits what the agent may apply or claim.

## What it covers

- Plain language: ISO 24495 family and CAN-ASC-3.1
- Controlled technical English: ASD-STE100
- Product and software information: IEC/IEEE 82079-1 and ISO/IEC/IEEE 26514
- Requirements: ISO/IEC/IEEE 29148, RFC 2119/8174, and ISO/IEC drafting rules
- Terminology: ISO 704 and TBX
- Accessibility: WCAG and W3C COGA guidance
- Legal, scientific, safety, localization, and public-sector communication
- Google, Microsoft, GOV.UK, and Canada.ca editorial guidance

## Non-goals

This skill is not:

- a general-purpose grammar checker for every message;
- a legal, safety, scientific, or accessibility certification engine;
- a substitute for authoritative standards, audience testing, implementation testing, or subject-matter review;
- a reason to force ASD-STE100 or plain-language rules onto all technical writing;
- a source of invented requirements, hazard severity, legal effect, definitions, thresholds, or guarantees.

A valid result is **no external profile required** when native channel, repository, publication, or supplied house conventions are sufficient.

## Architecture

```text
.
├── SKILL.md
├── data/
│   └── standards-catalog.yaml      # versioned source of truth
├── references/
│   ├── routing-algorithm.md
│   ├── risk-and-escalation.md
│   ├── selection-matrix.md
│   ├── standards-catalog.md        # generated
│   └── output-contract.md
├── tests/
│   ├── routing-cases.yaml
│   ├── conflict-cases.yaml
│   └── claim-boundary-cases.yaml
├── scripts/
│   ├── render_catalog.py
│   └── validate.py
└── .github/workflows/
    └── validate.yml
```

## Install

Copy or clone this repository into the skills directory supported by your agent harness. The skill follows the Agent Skills package structure with `SKILL.md` at the repository root.

For a local skills directory:

```bash
git clone https://github.com/daeon/standard-english.git standard-english
```

Then register or select `standard-english` using your agent's skill mechanism. In ChatGPT or Codex environments that support skills, mention the skill by name or select it from the available skills UI.

To update an installed clone:

```bash
git -C standard-english pull --ff-only
```

## Use

### Rewrite

```text
Use standard-english to rewrite this deployment guide. Select the smallest
useful profile stack, preserve all technical meaning, and report unresolved
ambiguity.
```

### Route only

```text
Use standard-english to recommend the best language standards for this API
specification. Explain material alternatives and ask only if the choice changes
normative meaning.
```

### Repository edit

```text
Use standard-english to update these documentation files in place. Validate the
result and summarize material changes.
```

## Worked example

### Input

```text
Audit this wire-protocol specification. The introduction defines MUST, SHOULD,
and MAY using RFC 2119 and RFC 8174, but several requirements use shall.
```

### Routing

```text
Governing source: the specification's explicit RFC 2119/8174 definition
Document profile: ISO/IEC/IEEE 29148:2018-informed requirements review
Language constraint: RFC 2119 and RFC 8174
Rejected profile: ISO/IEC drafting rules, because mixing shall with defined RFC
keywords creates conflicting normative systems
```

### Expected behavior

The audit flags mixed normative systems, preserves requirement meaning, proposes RFC-consistent wording, and does not claim ISO/IEC/IEEE 29148 conformance unless the applicable authoritative material and assessment process are available.

## Source registry

`data/standards-catalog.yaml` records for each source:

- designation and edition;
- authority and profile role;
- lifecycle status;
- official source and access model;
- intended scope and exclusions;
- conformance prerequisites;
- last verification date.

The human-readable `references/standards-catalog.md` is generated from the registry:

```bash
python3 scripts/render_catalog.py
```

Do not edit the generated catalog directly.

## Freshness policy

The validator warns when a source verification date is older than the configured freshness window. Before formal or high-consequence work, verify the current edition, amendments, errata, governing jurisdiction, and organization-specific adoption.

Draft revisions are recorded as lifecycle notes but are not treated as governing published editions unless the project explicitly adopts them.

## Behavioral tests

The repository includes routing, conflict, and claim-boundary fixtures. They are structured benchmarks for evaluating agent behavior across model versions; static validation checks their integrity and registry references.

The fixtures cover ordinary no-profile tasks, requirements language, controlled technical English, legal and safety escalation, WCAG and CAN-ASC claim boundaries, terminology formats, machine-translation post-editing, and adversarial profile conflicts.

## Validate

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
```

Validation checks:

- real YAML frontmatter parsing and activation boundaries;
- required files and local links;
- registry schema, unique IDs, roles, HTTPS official sources, and freshness;
- synchronization of generated Markdown;
- behavioral fixture structure and profile references;
- stale repository-name leaks.

## Compliance boundary

Formal audits require the applicable authoritative standard, approved organization rules and terminology, a defined assessment scope, the required validation process, and appropriate human review.

Use precise claim language such as:

- `edited using an ISO 24495-1-informed profile`;
- `checked against the supplied clauses within the stated scope`;
- `candidate WCAG language-related issues`.

Do not claim `compliant`, `certified`, `passed`, or `fully conformant` when the evidence and required process do not support the claim.

## License

MIT
