# Output Contract

Choose the smallest output that satisfies the request. High consequence strengthens safeguards and review notes; it does not automatically change the requested mode.

## Shared route header

For standards-sensitive tasks, identify:

```markdown
**Route:** <no external profile required | selected profile stack>
**Routing confidence:** High | Medium | Low
**Evidence basis:** <authoritative material | supplied clauses/checklist | official public guidance | profile-level knowledge>
**Claim level:** <permitted claim>
```

Omit fields that add no trust value for a simple low-risk task.

## Route only

```markdown
## Recommended route

**Governing source:** <if any>
**Document/content profile:** <profile or none>
**Language constraint:** <zero or one>
**Delivery overlay:** <zero or one>
**Routing confidence:** High | Medium | Low

**Why:** <task-specific reason>
**Material trade-off:** <what the route protects and constrains>

## Alternative

<Only when meaningfully different.>

## Decision required

<Only when the routing gate applies.>
```

## Rewrite

Return the usable revision first.

```markdown
## Revised content

<finished text>

## Applied route

- Governing source: ...
- Document/content profile: ...
- Language constraint: ...
- Delivery overlay: ...
- Evidence and claim limit: ...

## Review notes

- Material assumptions: ...
- Unresolved ambiguities or domain decisions: ...
- Terminology gaps: ...
- Human reviewer role: ...
```

Do not clutter a simple rewrite with empty sections.

## Audit

```markdown
## Audit summary

- Selected route: ...
- Evidence basis: full authoritative material | supplied clauses | organization checklist | official public guidance | profile-level review only
- Assessment scope: ...
- Overall result: ...
- Claim: not assessed | candidate alignment only | checked against supplied material | conformance assessment performed within stated scope

## Findings

| ID | Severity | Classification | Location | Finding | Evidence/rule | Proposed correction | Confidence |
|---|---|---|---|---|---|---|---|

## Unresolved decisions

- <decision and responsible role>

## Human review

- <role and reason>
```

### Severity

- **Critical** — likely change to safety, legal obligation, security, or essential normative meaning.
- **Major** — likely ambiguity, incorrect action, failed task, inconsistent requirement, or inaccessible path.
- **Moderate** — significant clarity, terminology, structure, or localization issue.
- **Minor** — low-cost consistency or editorial issue.
- **Suggestion** — preference, not a violation.

### Classification

Use exactly one:

- confirmed issue;
- candidate issue;
- content ambiguity;
- domain decision;
- preference.

## Rewrite plus audit

Return:

1. revised content;
2. selected route and evidence basis;
3. compact table of material changes;
4. unresolved decisions and required reviewer roles.

Group similar minor edits.

## Repository edit

When repository tools are available and the user asks to implement changes:

1. edit files on a branch;
2. keep generated files synchronized with their source data;
3. run or extend validation;
4. summarize material changes and validation results;
5. open a pull request unless the user explicitly requested a direct commit to the default branch.

Do not return only a proposed patch when the requested edits can be performed.

## Profile builder

```markdown
# <Profile name>

## Scope

- Intended content:
- Audience:
- Exclusions:
- Governing sources:
- Source precedence:

## Required rules

1. ...

## Terminology

| Concept | Preferred | Allowed | Forbidden/deprecated | Definition/source |

## Normative language

- System:
- Defined keywords:
- Examples:

## Structure

- ...

## Accessibility and localization

- ...

## Safety, legal, and domain escalation

- ...

## Evidence and claims

- ...

## Positive examples

- ...

## Negative examples

- ...

## Validation checklist

- ...
```

## Claims language

| Evidence available | Permitted claim |
|---|---|
| public principles or model knowledge only | “edited using an <X>-informed profile” |
| current official public guidance | “reviewed against current public <X> guidance” |
| supplied organization checklist or glossary | “checked against the supplied <X> checklist/glossary” |
| supplied authoritative clauses | “checked against the supplied clauses within the stated scope” |
| full authoritative material plus required validation and human roles | “conformance assessment performed within the stated scope” |
| missing authoritative evidence | never say compliant, certified, passed, or fully conformant |

Special limits:

- CAN-ASC-3.1 conformance requires intended-audience involvement and evaluation; text review alone is insufficient.
- WCAG conformance is page-level and cannot be established by wording review alone.
- ASD-STE100 conformance requires the applicable issue, terminology decisions, and checking process.

## Final quality check

Verify:

- meaning, obligations, permissions, prohibitions, conditions, exceptions, and sequence are preserved;
- profiles have distinct roles and are compatible;
- terminology matches supplied authoritative sources;
- normative keywords follow one defined system;
- warnings retain hazard, consequence, and avoidance action;
- claims do not exceed evidence;
- ambiguities and domain decisions remain visible;
- the output is usable in the requested channel;
- repository changes pass available validation.
