# Risk and Escalation

Apply four gates independently. Do not use one vague “high-risk” gate for every decision.

## 1. Routing gate

Ask the user to choose only when two or more plausible routes would materially change:

- legal rights, duties, consent, liability, or regulatory interpretation;
- safety meaning, hazard severity, prohibited action, or emergency action;
- normative force or requirement interpretation;
- necessary scientific or technical nuance;
- jurisdictional or formal compliance scope.

Use this format:

```text
Recommended: <route A> — <reason>.
Alternative: <route B> — <when it is better>.
Material difference: <what changes>.
Choose A or B before the final rewrite or audit.
```

Do not ask when differences are merely stylistic, when a governing source fixes the route, or when one candidate clearly dominates.

## 2. Evidence gate

Trigger when the user requests compliance, conformance, certification, a pass/fail result, or a clause-level audit without enough authoritative material.

Response:

- identify the best-fit profile;
- state which authoritative edition or clauses are missing;
- limit the result to profile-informed editing or candidate findings;
- request or locate authoritative material only when needed for the requested claim.

Do not select a weaker but available profile as a substitute.

## 3. Domain-decision gate

Trigger when rewriting would require an unsupported decision about:

- hazard classification or signal word;
- legal effect, jurisdiction, rights, remedies, or consent;
- security control strength or threat acceptance;
- requirement threshold, actor, exception, or verification method;
- scientific causal claim, uncertainty, or generalizability;
- approved terminology or product behavior.

Response:

- preserve the original meaning;
- label the unresolved decision;
- offer a non-normative placeholder or sample only when useful;
- name the responsible role, such as safety engineer, legal counsel, security owner, requirements owner, scientist, terminologist, accessibility specialist, or product owner.

Do not ask the user to choose a writing style when the real blocker is a domain decision.

## 4. Human-review gate

Require qualified human review for final use when content can materially affect:

- injury, emergency response, or product safety;
- legal rights, consent, liability, or regulated obligations;
- security exposure, data loss, or critical operations;
- clinical or public-health decisions;
- formal certification or contractual acceptance.

High consequence does not automatically require routing confirmation. It requires the correct review role and a clear limitation statement.

## Consequence bands

| Band | Typical effect | Default response |
|---|---|---|
| Low | cosmetic or preference | route and execute automatically |
| Moderate | confusion, support cost, failed task | execute; state material assumptions |
| High | outage, data loss, financial impact, security exposure | preserve precision; surface domain decisions; require appropriate review |
| Critical | injury, legal rights, regulated compliance, emergency response | preserve source meaning; apply domain and human-review gates; use routing gate only if routes remain materially ambiguous |

## Common mistakes

- Asking for profile confirmation merely because content is critical.
- Giving a full audit when the user requested only a rewrite.
- Converting a missing domain decision into invented wording.
- Treating human review as a substitute for identifying concrete unresolved issues.
- Using “consult a professional” without naming the relevant role or decision.
