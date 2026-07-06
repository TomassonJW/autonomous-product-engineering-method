# Risk Register

| Risk | Severity | Likelihood | Mitigation |
| --- | --- | --- | --- |
| Agent underbuilds an ambitious request | High | High | Deductive profiling and ambition scale |
| Agent overbuilds a simple request | Medium | Medium | First useful slice and challenge gate |
| Fake premium UX | High | Medium | Dual UI, Truth, and Journey Gates |
| Secret exposure | Critical | Medium | .gitignore, secret scan, no-secret rules |
| Public release with private content | Critical | Low | Safe GitHub workflow and public-safety scan |
| Cost explosion | High | Medium | Cost gate, budget policy, quota-aware execution |
| Worker false success | High | High | Supervisor pattern and evidence-based final report |
| Documentation too abstract | Medium | Medium | Examples, templates, and operational checks |
| Prompt grants unsafe authority | High | Medium | Safety boundaries in each prompt |
| Capability mesh becomes over-engineered | Medium | Medium | Require operational purpose for each relation |
| Challenge gate becomes bureaucratic | Medium | Medium | Scale challenge level to task risk |
| Human approvals are unclear | High | Medium | Green/orange/red action model |

## Open Risk

The method still needs validation across several real repositories and agent tools. Until then, some guidance may be incomplete or too idealized.
