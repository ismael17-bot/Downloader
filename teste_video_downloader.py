from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)

        stream = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}")

        stream.download()

        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

video_url = input("Enter the YouTube video URL: ")

download_video(video_url)