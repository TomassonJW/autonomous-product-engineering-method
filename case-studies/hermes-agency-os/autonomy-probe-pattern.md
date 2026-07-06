# Autonomy Probe Pattern

An autonomy probe is a small controlled run that tests whether a worker can operate safely before giving it broader responsibility.

## Probe Design

Define:

- mission;
- allowed files or systems;
- maximum cycles;
- expected artifact;
- quality gates;
- stop conditions;
- report format.

## What The Probe Measures

- Does the worker understand scope?
- Does it avoid forbidden files?
- Does it produce useful artifacts?
- Does it report skipped checks?
- Does it stop when blocked?
- Does it avoid false success?

## Probe Result

Classify:

- ready for larger run;
- ready with narrower scope;
- needs wrapper improvement;
- unsafe for autonomy.

## Why It Matters

A probe is cheaper than discovering during a long run that the worker cannot respect scope, costs, or status truth.
