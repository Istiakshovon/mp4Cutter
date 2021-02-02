from moviepy.editor import *


videoclip = VideoFileClip("video.mp4")
audioclip = AudioFileClip("mp3.mp3")

new_audioclip = CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("new_filename.mp4")

# video = VideoFileClip("video.mp4").subclip(15,200)
# result = CompositeVideoClip([video]) # Overlay text on video
# result.write_videofile("video1.mp4",fps=25) # Many options...

