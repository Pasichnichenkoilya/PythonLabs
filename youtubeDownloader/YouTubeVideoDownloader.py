from pytube import YouTube

class YouTubeVideoDownloader:

    def download(self, url, path = None):
        youtube = YouTube(url)

        if not self.is_available(url):
            print('The url is wrong or video is unavailable')
            return ''
        
        video = youtube.streams.filter(mime_type='video/mp4').get_highest_resolution()
        
        if path is not None:
            return video.download(output_path=path)

        return video.download()
    

    def is_available(self, url):
        youtube = YouTube(url)

        try:
            youtube.check_availability()
        except:
            return False
        
        return True


    def get_available_resolutions(url):
        youtube = YouTube(url)
        resolutions = []
        streams = []
        
        # getting unique reolutions
        for stream in youtube.streams.filter(type="video"):
            resolution = f"{stream.resolution}"
            if resolution not in resolutions:
                resolutions.append(resolution)
                streams.append(stream)

        # sorting resolutions desc
        for i in range(len(resolutions)):
            for j in range(len(resolutions)):
                if streams[i].itag > streams[j].itag:
                    streams[i], streams[j] = streams[j], streams[i]
