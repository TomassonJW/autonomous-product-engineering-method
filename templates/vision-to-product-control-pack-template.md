# Vision-to-Product Control Pack Template

Use this compact artifact for a small or medium project. Split sections into dedicated sources of truth when they gain different owners, sensitivity, review gates, or update rhythms.

## 1. Control Metadata

- Project:
- Control Pack version:
- Active method movement: Understand / Diverge / Stabilize / Build / Observe
- Product owner:
- Engineering owner:
- Acceptance owner:
- Active Foundation Freeze version:
- Last reviewed:
- Next mandatory review event:

## 2. Raw Vision

Preserve the original words.

> `<initial user vision>`

## 3. Active Interpretation

### Reformulated Intent

### Desired Future State

### Primary Problem

### Active Product Interpretation

### Rejected Or Deferred Interpretations

| Interpretation | Disposition | Evidence And Reason |
| --- | --- | --- |
|  |  |  |

### North Star

> `<enduring product purpose>`

### Non-Goals

-

## 4. Three Profiling Views

Collect only information needed for the declared project purpose.

### Sponsor Profile

- Goals:
- Decision authority:
- Declared preferences:
- Constraints:
- Success evidence:
- Corrections or refusals to preserve:

### Audience Profile

| Audience | Job | Context | Capability Level | Accessibility Need | Main Risk |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

### Situational Profile

- Existing workflow:
- Existing product or workaround:
- Organization and operating context:
- Technical environment:
- Market or domain constraints:
- Regulatory context:
- Timing and resources:

## 5. Signal And Inference Register

| ID | Status | Statement | Sources | Counter-Evidence | Product Consequence | Risk If Wrong | Owner | Review Trigger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INF-001 | FACT / SIGNAL / HYPOTHESIS / STRONG DEDUCTION / UNKNOWN / DECISION / CONSTRAINT / HUMAN GATE |  |  |  |  |  |  |  |

### User Corrections

| Record | Correction | Superseded Statement | Date | Consequence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 6. Adaptive Question Budget

| Question | Decision It Can Change | Why It Cannot Be Inferred Safely | Status |
| --- | --- | --- | --- |
|  |  |  |  |

Interview exit evidence:

- [ ] Active interpretation is explicit.
- [ ] Main audience and outcome are usable.
- [ ] Major contradictions are resolved or owned.
- [ ] Data and external actions have preliminary risk classes.
- [ ] Another question is unlikely to change the next bounded step.

## 7. Challenge Record

- Strongest counter-hypothesis:
- Simpler competing workflow:
- Broader system interpretation:
- Evidence that would invalidate the active interpretation:
- Likely technically-complete-but-unusable outcome:
- Hidden operating or compliance burden:
- Decision owner:
- Challenge result: pass / fail / decision needed

## 8. Product Cartography

### Domain Atlas

| Domain | Purpose | Inside | Outside | Owner | Data Class | Main Risk |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Capability Atlas

| Capability | Domain | Actor And Outcome | Inputs And Outputs | Journey | Safety Zone | Maturity | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

### Module Map

| Module | Capabilities Realized | Data Owned | Public Contracts | Forbidden Dependencies | Test Boundary | Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Object And State Catalog

| Object | Owning Domain | States | Valid Transitions | Transition Permission | Invariant | Retention |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Cross-Domain Compositions

| Composition | Trigger | Capabilities | Contracts | Partial Failure | Final User Truth | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### UI Surface Map

| Surface | Experience Or Control Plane | Actor | Main Job | Truth Exposed | Advanced Path | Accessibility Risk |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Permission And Autonomy Map

| Action | Requester | Approver | Executor | Autonomy Level | Data Class | External Effect | Rollback | Audit Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## 9. Exploration And Curation

### Exploration Passes

| Lens Or Pass | New Domains | New Objects Or Invariants | New Threats | New Journeys | Decision Impact |
| --- | --- | --- | --- | --- | --- |
| Expected product |  |  |  |  |  |
| Simpler competitor |  |  |  |  |  |
| Broader system |  |  |  |  |  |

### Curation Decisions

| Candidate | Disposition | Merge Or Split Target | Evidence | Decision Owner |
| --- | --- | --- | --- | --- |
|  | active / foundation-candidate / incubator / deferred / merged / split / rejected / superseded |  |  |  |

### Saturation Result

- Two independent exploration passes reviewed:
- Net-new P0 domain found:
- Net-new shared object or invariant found:
- Net-new red action or material threat found:
- Unresolved contradiction blocking stabilization:
- Saturated for current decision: yes / no
- Evidence:

## 10. Foundation Freeze Candidate

- Candidate version:
- North Star and vision version:
- Domains included:
- Core capabilities and compositions:
- Shared objects, states, and invariants:
- Experience and Control Plane principles:
- Permissions and autonomy policy:
- Data, privacy, and security policy:
- Accepted ADRs and contracts:
- Excluded, deferred, and incubated concepts:
- Known risks and unknowns:

### Falsification Verticals

| Vertical | Risky Assumption Tested | Real Boundaries Crossed | Result | Evidence | Foundation Consequence |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

### Freeze Gate

| Requirement | Pass / Fail / Decision Needed | Evidence | Owner |
| --- | --- | --- | --- |
| Curated maps |  |  |  |
| Shared objects and states |  |  |  |
| Versioned contracts |  |  |  |
| P0 falsification verticals |  |  |  |
| Alternatives and rejected decisions |  |  |  |
| Security and privacy review |  |  |  |
| Change and rollback strategy |  |  |  |
| Product acceptance |  |  |  |
| Engineering acceptance |  |  |  |

## 11. Roadmap And Build Mission Portfolio

### Horizons

| Horizon | Outcome | Included Verticals | Explicitly Excluded | Exit Evidence |
| --- | --- | --- | --- | --- |
| P0 foundation |  |  |  |  |
| First usable release |  |  |  |  |
| Operational release |  |  |  |  |
| Incubator |  |  |  |  |

### Mission Portfolio

| Mission | Vertical | Dependencies | Workspace And Ownership | Inputs | Outputs | Safety | Budget And Timeout | Tests | Reviewer | Integration Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

### Execution DAG

```text
<mission dependency graph>
```

## 12. Security, Privacy, And Compliance

### Data Map

| Data | Purpose | Source | Class | Recipient Or Processor | Location | Retention | Deletion | Access | Incident Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

### Threats And Abuse Cases

| Threat Or Abuse Case | Asset | Actor | Impact | Control | Residual Risk | Gate Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Legal And Organizational Review

- Product context: private / internal / public or commercial
- Controller and processors, if applicable:
- Purposes and lawful bases, if applicable:
- User rights and preference controls:
- Retention and deletion policy:
- Transfer and vendor review:
- Accessibility obligations:
- Moderation or abuse obligations:
- DPIA or qualified legal review needed:
- Explicit statement: this artifact is not a compliance certificate.

## 13. Integration And Acceptance

### Integration Evidence

| Mission | Patch Or Commit | Foundation Version | Contracts | Tests | Real Integration State | Risks | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

### Evidence States

- Specified:
- Implemented:
- Unit-tested:
- Fixture-integrated:
- Integrated:
- End-to-end verified:
- User-validated:
- Release-ready:
- Released:
- Operationally validated:

### Independent Acceptance

- Builder:
- Reviewer:
- Integration owner:
- Acceptance owner:
- Publisher or deployer:
- Result: accepted / accepted-with-reservations / rejected / decision-needed
- Evidence:
- Reservations and owners:

## 14. Completeness Estimate

| Dimension | Weight | Level 0-5 | Evidence | Confidence | Next Legitimate Progress Event |
| --- | --- | --- | --- | --- | --- |
| Conceptual coverage |  |  |  |  |  |
| Domain coherence |  |  |  |  |  |
| Inference maturity |  |  |  |  |  |
| Foundation readiness |  |  |  |  |  |
| Contract coverage |  |  |  |  |  |
| Integrated P0 verticals |  |  |  |  |  |
| UX and accessibility |  |  |  |  |  |
| Security and privacy |  |  |  |  |  |
| Tests and real integration |  |  |  |  |  |
| Deployment and operation |  |  |  |  |  |
| Human and user validation |  |  |  |  |  |
| Compliance review |  |  |  |  |  |
| Rollback capability |  |  |  |  |  |

- Weighted estimate:
- Confidence:
- Unknowns:
- Realism warning:

## 15. External Action Gate

- Exact action:
- Target and environment:
- Human approval reference:
- Reviewed payload or change set:
- Data minimization and basis:
- Dry-run evidence:
- Rollback or compensation:
- Redacted logs:
- Executable perimeter check:
- Result verification:
- Final authorization: granted / denied / expired

## 16. Learning And Foundation Evolution

| Signal, Feedback, Incident, Or Metric | Source | Competing Explanations | Inference Updated | Capability Or Change Candidate | Decision |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

### Foundation Change Proposal

- Trigger and evidence:
- Contracts, domains, journeys, and workers affected:
- Alternatives:
- Compatibility and migration impact:
- Tests:
- Rollback:
- Decision owner:
- Target foundation version:

## 17. Current Truth And Next Action

- Current verified state:
- What is simulated or fixture-only:
- What remains unknown:
- Blocking decision:
- Highest-value unblocked next outcome:
- Action that is explicitly not authorized:
