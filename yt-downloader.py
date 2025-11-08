import yt_dlp

url = input("Enter the YouTube video URL: ")

options ={
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best','merge_output_format': 'mp4','outtmpl': '%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])
