# Selection Matrix

Classify only the dimensions that can change routing. Use the matrix as structured judgment, not a compliance calculator.

## 1. Intended outcome

| Outcome | Routing implication |
|---|---|
| explain or educate | prioritize audience understanding and concept sequence |
| instruct or troubleshoot | prioritize task completion, prerequisites, feedback, recovery, and action order |
| specify requirements | preserve normative force, atomicity, conditions, actors, feasibility, and verifiability |
| warn or protect | preserve hazard, consequence, avoidance action, urgency, and approved severity |
| establish rights or duties | preserve legal effect, jurisdiction, definitions, exceptions, and remedies |
| communicate science | preserve evidence strength, uncertainty, methods, limitations, and causal boundaries |
| localize or translate | control terminology, ambiguity, units, locale, and review workflow |
| label an interface | prioritize brevity, exact behavior, consistency, accessibility, and product terminology |
| govern terminology | distinguish concepts, preferred terms, definitions, synonyms, and deprecated terms |
| perform conformance-oriented review | identify governing edition, evidence basis, scope, and permitted claim |

## 2. Audience

Classify the least-expert intended audience who must act correctly:

- general public or customer;
- software developer;
- operator or technician;
- engineer or architect;
- regulator or auditor;
- lawyer or contracting party;
- scientist or specialist;
- translator or multilingual reader;
- cognitively diverse or accessibility-sensitive audience.

Record only material characteristics: domain knowledge, language proficiency, reading conditions, urgency, device or channel, and cost of misunderstanding.

## 3. Document type

| Document type | Strong candidates |
|---|---|
| public notice, form, policy explanation | ISO 24495-1; CAN-ASC-3.1 in Canadian accessibility contexts; delivery overlay when digital |
| maintenance or operating procedure | IEC/IEEE 82079-1; ASD-STE100 when controlled language is justified; applicable safety framework |
| software help, tutorial, CLI, or API guide | ISO/IEC/IEEE 26514 plus a developer editorial guide; accessibility overlay when web-based |
| PRD, SRS, acceptance criteria, protocol | ISO/IEC/IEEE 29148 plus one normative-keyword system |
| formal standard or specification | governing publication rules or ISO/IEC Directives Part 2 |
| RFC or interoperability protocol | RFC 2119 and RFC 8174 when explicitly invoked |
| contract, privacy notice, legal explanation | ISO 24495-2 plus jurisdiction-specific legal review |
| public science communication | ISO 24495-3 plus any field-specific factual review |
| scientific journal or academic paper | publication and discipline reporting rules; ISO 24495-3 is not the governing profile |
| warning or safety manual | applicable ANSI, ISO, IEC, regulatory, or organization safety framework |
| terminology list or ontology | ISO 704; TBX only when machine exchange matters |
| full human post-editing of MT output | ISO 18587 plus terminology and source-content profiles |
| UI strings and error messages | product or Microsoft-style UI conventions plus accessibility and terminology overlays |
| casual message, routine copyedit, commit message | normally no external profile required |

## 4. Normative force

Determine whether each statement:

- describes a fact;
- recommends behavior;
- permits behavior;
- imposes a requirement;
- prohibits behavior;
- declares capability or possibility;
- defines a term;
- gives a non-normative example.

When normative force exists, select one governing keyword system.

### RFC system

Use for Internet and interoperability specifications that explicitly define RFC 2119/8174 usage:

- MUST / MUST NOT;
- SHOULD / SHOULD NOT;
- MAY.

### ISO-style system

Use for standards-like documents governed by the applicable ISO/IEC drafting rules:

- shall: requirement;
- should: recommendation;
- may: permission;
- can: possibility or capability.

Do not infer normative meaning from ordinary lowercase words unless the document defines it.

## 5. Consequence

| Consequence | Safeguard |
|---|---|
| low | execute automatically |
| moderate | execute and state material assumptions |
| high | preserve technical precision; surface domain decisions; identify reviewer role |
| critical | preserve source meaning; apply domain and human-review gates; ask about routing only when materially ambiguous |

Consequence does not decide the profile and does not automatically change a rewrite into an audit.

## 6. Domain overlays

Check whether a distinct domain risk justifies an overlay:

- aerospace, defence, maintenance, multilingual operations;
- software information for users;
- product instructions;
- requirements engineering;
- public administration in Canada;
- digital accessibility;
- legal communication;
- public science communication;
- safety communication;
- terminology and localization.

Do not select a domain merely because the content mentions related vocabulary.

## 7. Channel

Account for printed manual, PDF, responsive web, mobile UI, terminal, API reference, chatbot, email, notification, spoken script, or translation source. Channel affects navigation, length, warning visibility, step structure, link wording, and accessibility, but channel alone rarely determines a formal standard.

## 8. Localization

Check:

- whether English is source content for translation;
- whether readers are non-native speakers;
- whether machine translation is expected;
- whether a termbase exists;
- whether locale, units, dates, and regulatory terms are controlled.

Add terminology or localization support only when it protects a real requirement. Do not erase culturally or legally necessary distinctions.

## 9. Evidence available

Classify evidence independently from fit:

- full authoritative standard and required validation process;
- relevant licensed or authoritative clauses;
- approved organization checklist, policy, or glossary;
- current public official guidance;
- public summaries or model knowledge only.

Evidence controls claim strength and audit certainty, not conceptual profile fit.

## Fit evaluation

Evaluate candidates qualitatively:

| Factor | Question |
|---|---|
| direct outcome match | Does this profile govern the actual communication outcome? |
| document/domain match | Does it govern this information product or professional context? |
| consequence protection | Does it protect the highest-cost plausible misunderstanding? |
| audience/channel fit | Does it serve the people and delivery conditions? |
| distinct role | Does it add a non-duplicative function to the stack? |
| unnecessary restriction | Would it make the content mechanical, incomplete, or less precise without compensating value? |
| conflict | Does it contradict a governing source or selected normative system? If yes, eliminate it. |

## Tie-breaking

1. Apply mandatory governing sources.
2. Prefer the profile closest to the document and outcome.
3. Prefer the route that protects the highest-cost failure.
4. Prefer the smaller compatible stack.
5. Use a general plain-language profile only when it adds audience value.
6. Ask for a choice only when remaining differences are material.
