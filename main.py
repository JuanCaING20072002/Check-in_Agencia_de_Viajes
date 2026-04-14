"""Application entry point."""
import os

from app import create_app

if __name__ == "__main__":
    app = create_app()
    
    # Get host and port from environment
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    
    app.run(host=host, port=port, debug=debug)
