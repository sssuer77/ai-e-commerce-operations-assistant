import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // 关闭 Next.js 自动生成的 AGENTS.md / CLAUDE.md，保持仓库根目录说明唯一。
  agentRules: false,
  // 本地开发时允许通过 127.0.0.1 访问 HMR 与静态资源。
  allowedDevOrigins: ["127.0.0.1", "localhost"],
};

export default nextConfig;
