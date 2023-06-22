import streamlit as st
import pytube
import os

def download_youtube_video(url):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        return video.title
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit app
def main():
    st.title("YouTube Video Downloader")
    st.write("Enter the YouTube video URL and click the 'Download' button to get the download link.")

    # Input field for the YouTube URL
    url = st.text_input("Enter YouTube URL")

    # Download button
    if st.button("Download"):
        if url:
            st.write("Downloading...")
            filename = download_youtube_video(url)
            if filename:
                file_path = os.path.join(os.getcwd(), filename + ".mp4")
                st.success("Download completed successfully!")
                st.write("Click the link below to download:")
                st.markdown(f"[Download {filename}](./{filename}.mp4)")
        else:
            st.warning("Please enter a valid YouTube URL.")

# Run the app
if __name__ == "__main__":
    main()
