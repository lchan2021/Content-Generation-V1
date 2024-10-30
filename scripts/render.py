import ffmpeg

def render_vid():
    input_video = ffmpeg.input('gameplay.mp4')
    input_audio = ffmpeg.input('output.wav')

    (
        ffmpeg
        .output(input_video, input_audio, 'final_output.mp4', vcodec='libx264', acodec='aac', shortest=None)
        .run(overwrite_output=True)
    )

if __name__ == "__main__":
    render_vid() 
