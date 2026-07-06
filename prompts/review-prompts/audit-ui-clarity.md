# Audit UI Clarity

## Purpose

Review whether an interface is clear, dual-plane, and premium in behavior.

## When To Use

Use before accepting UX/UI work or calling a product slice premium.

## Expected Output

Findings on clarity, journey quality, dual UI separation, truth status, and next fixes.

## Prompt

```text
Audit this UI or UX plan for clarity.

Material:
<paste screen description, screenshot notes, design, or route>

Check:
1. Is the primary action obvious?
2. Can a beginner proceed without jargon?
3. Can an expert access deeper control?
4. Are Experience Plane and Control Plane separate?
5. Are mock, inferred, real, and unknown data labeled?
6. Are errors understandable?
7. Are red actions approval-gated?
8. Is the journey testable end to end?
9. Is the UI actually useful, or only scaffolded?

Constraints:
- Findings first.
- Do not treat visual polish as product quality.
- Recommend concrete UX fixes.

Safety boundaries:
- Flag any UI that lets users publish, delete, spend, expose, or send without approval.

Next step:
Return a minimal fix plan and a UI gate result.
```
