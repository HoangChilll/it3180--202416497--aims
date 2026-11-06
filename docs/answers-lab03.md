# Lab 03 discussion

- Merge base is the best common ancestor of two branches. Git compares each branch with this commit during a merge.
- Shared main and release history should be undone with revert, which adds a traceable inverse commit. Reset rewrites branch history and can discard collaborators work.
- If a PR shows unrelated commits, check its base branch. A bugfix branched from a feature must target that feature first.
- For an unpushed mistake, reset --soft keeps changes staged; reset --mixed keeps them in the working tree. Avoid reset --hard on work you need.
