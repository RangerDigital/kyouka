import keyboard
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse


tags_metadata = [
    {
        "name": "Track",
        "description": "Controls currently playing track.",
    },
    {
        "name": "Volume",
        "description": "Controls global system volume."
    }
]

app = FastAPI(title="Kyouka", openapi_tags=tags_metadata)
app.mount("/dist", StaticFiles(directory="dist"), name="dist")


@app.get("/", include_in_schema=False)
def root():
    return FileResponse("dist/index.html")


@app.post("/track/play", tags=["Track"])
def play_track():
    keyboard.press("play/pause")

    return {"status": "success"}


@app.post("/track/next", tags=["Track"])
def next_track():
    keyboard.press("next track")
    keyboard.press_and_release("shift+n")

    return {"status": "success"}


@app.post("/track/previous", tags=["Track"])
def previous_track():
    keyboard.press("previous track")

    return {"status": "success"}


@app.post("/volume/up", tags=["Volume"])
def volume_up():
    keyboard.press("volume up")

    return {"status": "success"}


@app.post("/volume/mute", tags=["Volume"])
def volume_mute():
    keyboard.press("volume mute")

    return {"status": "success"}


@app.post("/volume/down", tags=["Volume"])
def down():
    keyboard.press("volume down")

    return {"status": "success"}


def get_ip():
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 1))
    return s.getsockname()[0]


if __name__ == "__main__":
    import uvicorn

    print("Kyouka running at:")
    print(" - Local:   http://localhost:7070/")
    print(f" - Network: http://{get_ip()}:7070/")

    uvicorn.run(app, host="0.0.0.0", port=7070, log_level="warning")
