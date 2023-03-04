from pytube import YouTube

class YouTubeVideoDownloader:

    def download(self, url):
        youtube = YouTube(url)

        if not self.is_available(url):
            print('The url is wrong or video is unavailable')
            return ''
        
        video = youtube.streams.filter(mime_type='video/mp4').get_highest_resolution()
        
        return video.download()


    def is_available(self, url):
        youtube = YouTube(url)

        try:
            youtube.check_availability()
        except:
            return False
        
        return True
