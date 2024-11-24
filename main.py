import uvicorn

from server.config import app_settings as settings

if __name__ == "__main__":
    uvicorn.run("server.app:gestion_items",
                host="0.0.0.0", port=settings.PORT, reload=settings.DEV)
