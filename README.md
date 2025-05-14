# 🎬 YouTube Transcript Saver

A simple Python script to fetch the subtitles (transcript) of a YouTube video and save them to a `.txt` file.  
Works for videos that have captions (either auto-generated or uploaded by the author).

## 📦 Requirements

- Python 3.7+
- [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)

Install the required library:

```commandline
pip install youtube-transcript-api
```

## 🚀 Usage

Run the script:

```commandline
python transcript_saver.py
```

Then enter the URL of the YouTube video when prompted:

```commandline
Enter the YouTube video URL: https://www.youtube.com/watch?v=VIDEO_ID
```

If the video has available subtitles, the script will:

* Extract the transcript
* Save it to a file called `video_transcript.txt` in the current directory

## 🧠 How It Works

1. The script extracts the video ID from the given YouTube link.
2. It uses `youtube-transcript-api` to fetch the transcript.
3. The text is written line by line to a `.txt` file.

## ⚠️ Notes

* Subtitles must be available for the video.
* If there are no captions, the script will throw an error.

## 💡 Example

```text
Enter the YouTube video URL: https://www.youtube.com/watch?v=l6oKriR-RjM
Transcript saved successfully to 'video_transcript.txt'.
```