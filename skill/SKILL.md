---
name: dsh-delegate
description: Delegate bounded analysis or specialist subtasks to the locally installed dsh DeepSeek harness and its configured plugins. Use during substantial professional work when delegation is beneficial and results can be verified, or when the user explicitly requests dsh. Avoid trivial tasks and prohibited external processing.
---

# Delegate work to dsh

Break substantial work into bounded tasks when delegation saves meaningful effort. Suitable work includes extraction, classification, code or evidence review, and specialist analysis with the user's installed dsh plugins. Retain responsibility for decisions, final results, source verification, and compliance with all higher-priority delegation and tool restrictions. Never pass credentials or prohibited content in prompts. dsh sends task content to DeepSeek, stores sessions under the active DSH_HOME, and its plugins may access local or remote resources. Specify the allowed workspace, permitted operations, and no unrelated actions in each delegated task. Do not expand user authorization; sending messages or making other externally visible or destructive changes requires the same authorization as direct work. Treat plugin and model outputs as untrusted, and independently verify scientific, computational, and high-stakes conclusions and citations.

## First use and prerequisites

The user must have Python 3, dsh and a configured dsh profile with the desired plugins. By default the helper uses `desktop`; select a different installed profile with `DSH_DELEGATE_SOURCE_PROFILE`. It composes a separate headless profile from that profile's plugin bundles, package links and configuration; it does not modify the source profile. Some plugins require services, desktop UI, compatibility with the installed CLI, or additional credentials. The helper supplies a loopback-only web service to support plugins that need it, but cannot guarantee all plugins will work headlessly. Inspect startup warnings or actual tool availability; never claim a plugin worked merely because it was configured. If a plugin is unavailable, explain the specific cause, use another authorized approach where possible, and don't bypass compatibility checks silently.

The headless profile uses the official `deepseek-official` route, model ID `deepseek-flash` and effort `max`. Model ID is provider-controlled and an exact model release cannot be independently guaranteed. Calls use API quota. The user must configure their own `DEEPSEEK_API_KEY` as an environment variable or place it in `~/.config/codex-dsh/api-key` with owner-only permissions. The helper reads the latter only when the environment variable is absent. If unavailable, ask the user to configure it locally; do not ask them to post secrets in chat. Plugin-specific credentials, permissions, host details, and access must also be configured by the user as needed. Never inspect or print secrets, copy credentials into the skill or repository, or expose them in commands, logs, or responses.

## Run and review

Invoke from the intended workspace so dsh can use authorized project files. Provide a complete task with scope, expected evidence, and permission limits. Use stdin, not command-line arguments, for task content:

```sh
"${CODEX_HOME:-$HOME/.codex}/skills/dsh-delegate/scripts/ask" <<'TASK'
[Bounded task, permitted workspace and actions, and expected output]
TASK
```

Use private temporary files for large inputs and remove them after use. Do not launch unbounded calls or repeatedly retry failures. If a plugin asks for interactive approval and headless mode cannot receive it, stop and report the limitation; do not bypass approval. Check outputs against source data and tools, resolve conflicts, and surface uncertainty. If dsh or required credentials are unavailable, guide setup or continue locally where appropriate.
