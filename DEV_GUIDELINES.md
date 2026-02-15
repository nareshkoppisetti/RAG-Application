# DEV_GUIDELINES.md
# AI Tooling Usage Rules (Cursor / Aider / CLI Agents)

This repository is production infrastructure.

AI tools are allowed to assist implementation but must respect architecture.

---

## 1. AI Scope of Authority

AI MAY:
- Refactor internal functions
- Improve readability
- Extract helper functions
- Improve chunking logic
- Improve prompt wording
- Add input validation
- Improve error handling

AI MUST NOT:
- Change deployment model
- Modify Dockerfile without explicit instruction
- Introduce persistent storage
- Modify Cloud Run configuration assumptions
- Expose secrets to frontend
- Change API response schema without approval
- Add new infrastructure dependencies

---

## 2. Deployment Safety Rules

Backend runs on Google Cloud Run.

Cloud Run constraints:
- Containers are stateless
- Filesystem is ephemeral
- No disk persistence allowed
- Chroma must run in-memory only

AI must never:
- Add SQLite
- Add local file storage
- Persist Chroma database to disk
- Add background daemons

---

## 3. Vector Store Rules

Chroma must:
- Be built at startup
- Run in memory
- Be attached to app state
- Not write to filesystem

If persistence is needed in future:
- Architecture change must be documented first.

---

## 4. API Contract Rules

The `/chat` endpoint must:
- Accept defined request schema
- Return consistent response format
- Not expose internal system prompts
- Not expose raw retrieved chunks

Breaking API contract requires versioning.

---

## 5. Change Review Policy

Before applying multi-file edits:

AI must:
1. Explain planned changes.
2. Confirm ARCHITECTURE.md compliance.
3. Show diff before applying.

Human must approve infrastructure changes.

---

## 6. Human Authority

Architecture decisions:
- Database changes
- Deployment changes
- Scaling changes
- Authentication layer
- Logging infra

Must be human-approved.

AI is implementation assistant, not system architect.
