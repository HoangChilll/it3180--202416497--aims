# Lab 04 discussion

- Prepare releases on main so the release branch is a frozen baseline.
- A tag names an immutable commit; a release branch can advance for hotfixes.
- Release branches do not merge back to main because version bumps and older dependencies may conflict with ongoing development. Cherry-pick the specific fix instead.
- 1.0.0 marks the first stable release after the earlier 0.x lab baselines.
