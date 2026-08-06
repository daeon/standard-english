# Standard English

`standard-english` is an AI-agent skill that selects and applies the most appropriate language standard or style profile for a writing task.

It routes by audience, document type, normative force, consequence, domain, channel, localization needs, and available authoritative evidence. It can combine a small set of complementary profiles without blending incompatible rules.

## What it covers

- Plain language: ISO 24495 family and CAN-ASC-3.1
- Controlled technical English: ASD-STE100
- Product and software information: IEC/IEEE 82079-1 and ISO/IEC/IEEE 26514
- Requirements: ISO/IEC/IEEE 29148, RFC 2119/8174, and ISO-style normative language
- Terminology: ISO 704 and TBX
- Accessibility: WCAG and W3C COGA guidance
- Legal, scientific, safety, localization, and public-sector communication
- Google, Microsoft, GOV.UK, and Canada.ca editorial guidance

## Core behavior

The skill automatically selects a profile when the task is clear and low-risk. It recommends ranked alternatives and asks for confirmation only when the choice could materially change legal obligations, safety meaning, normative force, technical nuance, or compliance scope.

It does not claim formal compliance from model memory or public summaries. Formal audits require the applicable authoritative standard, approved checklist, glossary, and appropriate human review.

## Layout

```text
.
├── SKILL.md
├── references/
│   ├── output-contract.md
│   ├── selection-matrix.md
│   └── standards-catalog.md
├── scripts/
│   └── validate.py
└── .github/workflows/
    └── validate.yml
```

## Use

Invoke the skill by name:

```text
Use standard-english to rewrite this deployment guide. Select the best language profile, preserve all technical meaning, and report unresolved ambiguity.
```

For routing only:

```text
Use standard-english to recommend the best language standards for this API specification. Explain material alternatives and ask only if the choice changes normative meaning.
```

## Validate

```bash
python3 scripts/validate.py
```

## License

MIT
