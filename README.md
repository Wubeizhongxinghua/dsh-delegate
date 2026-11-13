# dsh-delegate

A Codex skill that delegates bounded analysis to DeepSeek through your local dsh installation and compatible configured plugins. Default: `deepseek-flash`, reasoning effort `max`.

## Setup

1. Install dsh and Python 3; configure the plugins you need in a dsh profile.
2. Copy `skill` to `~/.codex/skills/dsh-delegate`.
3. Set `DEEPSEEK_API_KEY` in the environment, or save your own key in `~/.config/codex-dsh/api-key` with permissions `600`. Configure any plugin credentials separately. Never commit or paste keys into chat.
4. The source profile defaults to `desktop`; set `DSH_DELEGATE_SOURCE_PROFILE` to use another profile. Invoke `$dsh-delegate` in Codex.

The helper creates a separate headless profile under `DSH_HOME` from the source profile. Plugin support depends on compatibility, required services, and permissions; check startup warnings. Tasks and session logs may include sensitive data. Requests consume your API quota.

---

使用本机 dsh 和兼容的已配置插件，将可核验的分析子任务交给 DeepSeek。默认模型为 `deepseek-flash`，推理强度为 `max`。

## 配置

1. 安装 dsh 和 Python 3，并在 dsh 配置中安装所需插件。
2. 将 `skill` 文件夹复制到 `~/.codex/skills/dsh-delegate`。
3. 设置环境变量 `DEEPSEEK_API_KEY`，或将自己的密钥保存在 `~/.config/codex-dsh/api-key` 并设置权限为 `600`。插件所需的凭据需另行配置。不要提交密钥或将密钥粘贴到聊天中。
4. 默认使用 `desktop` 作为插件来源；可通过 `DSH_DELEGATE_SOURCE_PROFILE` 指定其他配置。在 Codex 中输入 `$dsh-delegate` 即可。

工具会在 `DSH_HOME` 下创建独立的无界面配置。插件是否可用取决于版本兼容性、依赖服务和权限，请留意启动提示。任务和会话日志可能包含敏感信息；请求会消耗你的 API 额度。
