from fastapi import HTTPException
from fastapi import APIRouter
import validators
import app.process_video as process_video
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, validator
import os

router = APIRouter(
    prefix="/dashcam",
    tags=["Dashcam Geojson"],
    responses={404: {"description": "Not found"}},
)

# * Model for the request body


class DashcamVideo(BaseModel):
    video_link: str
    machine_learning_stride: int = 1

    @validator("video_link", pre=True, always=True)
    def check_recording_link(cls, recording_link):
        assert recording_link != '', "Recording Link cannot be empty."
        return recording_link


@router.get("/")
async def read_root():
    return {"Dashcam Endpoint"}


@router.post("/machinelearning")
async def read_root(dashcamVideo: DashcamVideo):
    modelInput = dashcamVideo.dict()
    if validators.url(modelInput['video_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Video URL is not valid.")

    output_video_codec_compressed_path = process_video.get_video_for_processing(
        modelInput['video_link'], modelInput['machine_learning_stride'])

    # Checking if the output video file exists
    if not os.path.exists(output_video_codec_compressed_path):
        raise HTTPException(
            status_code=404, detail="Output video not found.")

    def iterfile():
        with open(output_video_codec_compressed_path, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="video/mp4")
