import os

# Tests use in-memory SQLite and mocked providers; pin these before app settings load
# so a developer's local .env cannot change test behavior.
os.environ.setdefault("DATABASE_URL", "sqlite://")
os.environ.setdefault("AUTH_SECRET_KEY", "test-secret-key")
os.environ.setdefault("LLM_BASE_URL", "")
os.environ.setdefault("LLM_API_KEY", "")
os.environ.setdefault("LLM_MODEL", "")
os.environ.setdefault("IMAGE_PROVIDER", "")
os.environ.setdefault("IMAGE_API_KEY", "")
os.environ.setdefault("VIDEO_PROVIDER", "")
os.environ.setdefault("VIDEO_API_KEY", "")
