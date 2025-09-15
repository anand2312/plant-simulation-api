# API Layer

FastAPI backend that exposes simulation engine functionality over HTTP.

## Key Responsibilities
- **Endpoints**: Control simulation (start/stop/pause)
- **Data Transfer**: Bridge between simulation and frontend
- **WebSockets**: Real-time simulation state updates

## Development Commands
- `uv run fastapi dev src/api/server.py` - Run dev server
- `uv run ruff check` - Lint code
- `uv run ruff format` - Format code
- `uv sync` - Sync dependencies

## Project Structure
- `src/` - Main API source code
- `tests/` - Test files
- `pyproject.toml` - uv project config

## Dependencies
Managed by uv in pyproject.toml. Key dependencies:
- fastapi - Web framework
- uvicorn - ASGI server
- Imports simulation logic from ../sim/