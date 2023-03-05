from pytube import YouTube

VIDEO_URL = "https://youtu.be/yHsdhrG05Lc"

try:

    yt = YouTube(VIDEO_URL)
    resolutions = []
    streams = []

    for stream in yt.streams.filter(mime_type="video/mp4").order_by('resolution').desc():
        resolution = f"{stream.resolution}"
        if resolution not in resolutions:
            resolutions.append(resolution)
            streams.append(stream)

    print("Choose resolution: ")

    for i in range(len(streams)):
        print(f'{i}: {streams[i].resolution}')

    chosen_res = int(input())

    print(f"Choosen resolution: {streams[chosen_res].resolution}")

    video = yt.streams.get_by_itag(streams[chosen_res].itag)
    video.download()

except Exception as error:
    print(f"An error occurred: {error}")