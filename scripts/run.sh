
#!/bin/bash
# Run the FastAPI app locally

uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload