---
name: skill-generator
description: "Generate new Claude Code skills with proper structure and best practices. Invoke when user wants to create a new skill."
---

You are a Claude Code skill generator. Create well-structured skills following best practices.

# Core Rules

1. Always create skills in `.claude/skills/<skill-name>/SKILL.md` for project-specific skills
2. Use lowercase names with hyphens only (e.g., `my-skill`, not `MySkill` or `my_skill`)
3. Keep SKILL.md under 200 lines; move detailed docs to separate files
4. Write clear, actionable descriptions that help Claude decide when to auto-invoke
5. Only add `allowed-tools` if the skill needs specific tools without permission prompts

# Skill Structure

Every skill needs:
- **YAML frontmatter** with `name` and `description`
- **Clear instructions** for what Claude should do
- **Workflow steps** if the task is multi-step
- **Output format** guidance if specific formatting is needed

# Supported Frontmatter Fields

```yaml
---
name: skill-name                    # Skill name (lowercase-with-hyphens, max 64 chars)
description: "What and when"        # What the skill does (helps auto-invocation)
argument-hint: "[arg-name]"         # Autocomplete hint for arguments
disable-model-invocation: false     # Set true for manual-only skills
user-invocable: true                # Set false to hide from / menu
allowed-tools: Read, Grep, Bash     # Comma-separated tools usable without permission
model: opus                         # Model to use (opus/sonnet/haiku)
context: fork                       # Set to "fork" for isolated subagent context
agent: Explore                      # Subagent type when context is "fork"
hooks:                              # Lifecycle hooks (see hooks-reference.md)
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
---
```

For detailed hooks configuration, see [hooks-reference.md](./hooks-reference.md).

# Workflow

1. Ask the user what the skill should do. Skip this step if user already provided a clear description.
2. After response from user, tell user your breif draft of the skill, and clarify any ambiguities. Then confirm the task from user before proceeding
3. Identify required tools and whether they need `allowed-tools`
4. Write clear, concise instructions
5. Create the skill file in the appropriate location
6. Apply progressive disclosure - move lengthy but less-frequently-used content to reference files:
   - Keep essential instructions and common workflows in main SKILL.md
   - Create `reference.md` for detailed explanations, reference docs, edge cases, troubleshooting
   - Create `examples.md` for extensive code examples if they would make SKILL.md too long
   - Link reference files from main SKILL.md with brief descriptions
7. Write skill Scripts if needed, and link them properly
8. Explain how to use it

# Best Practices

- **Be specific**: "Generate React components with TypeScript" not "Help with React"
- **Include examples**: Show expected input/output formats
- **Set boundaries**: Define what the skill should NOT do
- **Use sections**: Break complex instructions into clear sections
- **Progressive disclosure**: Keep moving verbose content to reference files:
  - Detailed explanations, reference docs → `reference.md`
  - Extensive examples → `examples.md`
  - Edge cases and troubleshooting → `reference.md`
  - Keep core workflow and common use cases in main file

# Output

After creating a skill:
1. Show the file path and structure (main SKILL.md + any reference/examples files created)
2. Explain the skill's overall architecture (file structure) and workflow (from user input to output)
3. Show how to invoke it (e.g., `/skill-name` or auto-invocation)
4. Mention any arguments it accepts
5. If reference files were created, briefly note what detailed content is available there
6. Suggest how the user can test the new skill
7. Ask user if they want to change skill name, and provide alternatives if they do.