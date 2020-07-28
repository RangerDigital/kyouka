import keyboard
from fastapi import FastAPI


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


@app.post("/track/play", tags=["Track"])
def play_track():
    keyboard.press("play/pause")

    return {"status": "success"}


@app.post("/track/next", tags=["Track"])
def next_track():
    keyboard.press("next track")

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)