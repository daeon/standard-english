# Routing Algorithm

Use this decision process before applying any language standard or style profile.

## 1. Decide whether an explicit profile is useful

Select **no external profile required** when native channel, repository, publication, or supplied house conventions are sufficient and an explicit profile would not materially improve correctness, safety, normative consistency, terminology, accessibility, localization, or conformance review.

Typical no-profile tasks:

- ordinary grammar and spelling correction;
- casual email, chat, or social copy;
- routine code comments and commit messages;
- creative, persuasive, or brand writing without a formal standard;
- small wording edits already governed by a supplied local style.

Do not use the no-profile route when the user requests a named standard, formal profile, controlled language, normative system, terminology policy, accessibility review, localization-ready source, or conformance-oriented audit.

## 2. Identify governing sources

Apply this precedence unless the task supplies a different binding order:

1. law and regulation;
2. contract, procurement requirement, or certification scheme;
3. governing publication or standards-body rules;
4. approved organization policy, checklist, glossary, schema, or product contract;
5. domain or document standard;
6. accessibility and localization requirements;
7. general plain-language principles;
8. editorial preferences.

A governing source can mandate a profile. Record it separately; it does not consume the profile-stack limit.

## 3. Classify the task

Use `./references/selection-matrix.md` and record only dimensions that affect routing:

```text
outcome → audience → document type → normative force → consequence →
domain → channel → localization → supplied authority
```

Classify the least-expert intended audience who must act correctly. Preserve specialized language where precision requires it.

## 4. Select by fit

Evaluate candidate fit independently from evidence availability.

Prefer a candidate that:

- directly governs the document or communication outcome;
- protects the highest-cost plausible misunderstanding;
- matches the audience and channel;
- controls required normative force or terminology;
- avoids unnecessary restrictions;
- is compatible with governing sources.

Evidence availability never changes which profile is the best conceptual fit. It changes only how fully the profile can be applied or audited and which claim is permitted.

## 5. Assign profile roles

Choose at most:

- one **document or content profile**;
- one **language constraint**;
- one **delivery overlay**.

Profiles with these registry roles are normally not peer writing profiles:

- `governing-framework` — establishes precedence or mandatory rules;
- `document-system` — governs information-product design or lifecycle;
- `content-language-profile` — governs audience-facing wording and structure;
- `controlled-language` — constrains vocabulary and grammar;
- `normative-keyword-system` — defines obligation, recommendation, permission, and capability;
- `terminology-method` — governs concepts, terms, and definitions;
- `interchange-format` — governs machine exchange, not prose style;
- `process-standard` — governs a workflow or professional service;
- `accessibility-requirement` — governs accessibility outcomes and conformance;
- `informative-guidance` — supports decisions but is not automatically normative;
- `editorial-guide` — supplies practical conventions.

## 6. Eliminate conflicts

Eliminate rather than average candidates when:

- a governing source requires another profile;
- normative keyword systems conflict;
- one profile would remove required legal, scientific, safety, or technical nuance;
- a process standard is being misused as a sentence-style guide;
- an interchange format is being treated as a writing standard;
- an accessibility requirement is being reduced to wording alone;
- profiles duplicate the same function without adding independent protection.

Report any conflict that cannot be resolved by precedence.

## 7. Assess routing confidence

Use qualitative confidence:

- **High:** one route clearly dominates.
- **Medium:** one route is best but a secondary route is plausible and not materially different.
- **Low:** missing information leaves materially different routes plausible.

Do not translate scores into percentages.

## 8. Apply material-risk gates

Use `./references/risk-and-escalation.md`. Keep these decisions independent:

- whether the user must choose a route;
- whether authoritative material is needed for the requested claim;
- whether a subject-matter expert must resolve content;
- whether qualified human review is required.

High consequence alone does not require the user to select a profile when the governing route is already clear.

## 9. Assess evidence and claim level

Classify evidence:

1. full authoritative material and required validation process;
2. relevant authoritative clauses or licensed excerpt;
3. approved organization checklist, glossary, or policy;
4. current public official guidance;
5. public summaries or general model knowledge only.

Then choose claim language from `./references/output-contract.md`.

## 10. Select output mode

Match the user's requested outcome:

- route only;
- rewrite;
- audit;
- rewrite plus audit;
- profile builder;
- repository edit.

Consequence affects safeguards and review notes, not automatically the output mode.

## 11. Final invariants

Before returning or committing changes, verify:

- no facts, actors, thresholds, conditions, exceptions, permissions, prohibitions, or sequence were lost;
- one normative system is defined and used consistently;
- terminology follows authoritative sources;
- warnings preserve hazard, consequence, and avoidance action;
- selected profiles have distinct roles and do not conflict;
- claim language matches evidence;
- unresolved domain decisions remain visible;
- requested repository files were validated when tools permit.
