from youtube_transcript_api import YouTubeTranscriptApi
import re

# Function to extract the video ID from a YouTube URL
def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

# Ask user for the YouTube link
youtube_url = input("Enter the YouTube video URL: ")

# Extract video ID
video_id = extract_video_id(youtube_url)

if not video_id:
    print("Invalid YouTube URL.")
else:
    try:
        # Fetch transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Save transcript to file
        with open("video_transcript.txt", "w", encoding="utf-8") as file:
            for entry in transcript:
                file.write(entry['text'] + '\n')

        print("Transcript saved successfully to 'video_transcript.txt'.")

    except Exception as e:
        print("Error while retrieving transcript:", e)