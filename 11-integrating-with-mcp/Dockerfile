# 基于官方 Python 镜像，适合大多数生产环境
FROM python:3.10-slim

WORKDIR /app

COPY . /app

# 安装 Python 依赖（自动读取 pyproject.toml 或 setup.py）
RUN pip install --upgrade pip \
    && pip install --no-cache-dir .

ENTRYPOINT ["mcp-server-time"]
