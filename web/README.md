# Web 工作台

电商运营助手的前端工作台，基于 Next.js 16 App Router、React 19、TypeScript 和 Tailwind CSS 4。

## 本地开发

```bash
npm ci
cp .env.example .env.local
npm run dev
```

环境变量：

- `NEXT_PUBLIC_API_BASE_URL`：浏览器访问的后端地址，本地默认 `http://127.0.0.1:8000`。
- `API_INTERNAL_BASE_URL`：服务端组件与 BFF route handler 转发地址；Docker Compose 中为 `http://api:8000`。

## 构建

```bash
npm run build
npm run start
```

登录 token 只保存在 httpOnly Cookie 中，页面数据由服务端组件读取，前端脚本不直接持有凭证。
