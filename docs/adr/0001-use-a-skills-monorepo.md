# Use a skills monorepo

We will keep Adam's reusable Codex skills in one private repository, `adam-codex-skills`, instead of scattering them directly under `~/.codex/skills` or creating one repository per skill. This keeps version control, review, shared scripts, and cross-skill evolution in one place while still allowing local Codex discovery through symlinks.

## Considered Options

- Store skills directly in `~/.codex/skills`: fastest locally, but weak versioning and hard to sync.
- Create one repo per skill: clean isolation, but too much management overhead for personal workflow skills.
- Use one monorepo: best fit for related AI workflow assets, shared scripts, and gradual expansion.

## Consequences

- Local install should use `scripts/link-skills.sh` to symlink skills into Codex.
- Skills should stay lean; durable project context belongs in repo docs, not inside every skill.
