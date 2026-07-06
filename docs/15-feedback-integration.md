# Feedback Integration

Users can give feedback in ordinary language. The system must translate feedback into the right layer without turning every comment into a full vision rewrite.

## Feedback Flow

1. Reformulate the feedback.
2. Classify impact level.
3. Identify affected layers.
4. State what should change.
5. State what must not change.
6. Propose tasks.
7. Propose tests.
8. Update documentation if needed.
9. Execute only when the scope is clear.

## Impact Levels

- **Copy or visual polish**: small UI or wording changes.
- **Journey clarity**: affects workflow, navigation, or information hierarchy.
- **Capability behavior**: changes what the product can do.
- **Architecture**: changes system structure or shared contracts.
- **Vision**: changes product direction, users, or ambition level.
- **Safety**: changes permissions, external effects, or risk class.

## Example

Feedback:

> "It is too technical."

Possible affected layers:

- Experience Plane copy;
- navigation;
- default settings;
- advanced disclosure;
- onboarding;
- examples.

Usually not affected:

- core architecture;
- capability graph;
- worker runtime.

## Feedback Contract

A good response to feedback says:

- "I understand this as..."
- "This affects..."
- "This does not require changing..."
- "The smallest useful update is..."
- "The test should prove..."

## Avoid Overreaction

Do not rebuild the product vision for every comment.

Do not implement vague feedback blindly.

Do not hide uncertainty behind confident design language.
