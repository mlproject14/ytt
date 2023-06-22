import streamlit as st
import pytube

def download_youtube_video(url):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        st.success("Download completed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit app
def main():
    st.title("YouTube Video Downloader")
    st.write("Enter the YouTube video URL and click the 'Download' button to download the video.")

    # Input field for the YouTube URL
    url = st.text_input("Enter YouTube URL")

    # Download button
    if st.button("Download"):
        if url:
            st.write("Downloading...")
            download_youtube_video(url)
        else:
            st.warning("Please enter a valid YouTube URL.")

# Run the app
if __name__ == "__main__":
    main()
