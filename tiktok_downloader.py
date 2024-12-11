from TikTokApi import TikTokApi

def download_tiktok_video(post_url, target_file):
    try:
        # Initialize TikTokApi
        api = TikTokApi()

        # Fetch video data
        video_data = api.video(url=post_url).bytes()

        # Write the video to a file
        with open(target_file, "wb") as video_file:
            video_file.write(video_data)

        print(f"TikTok video downloaded to {target_file}")
    except Exception as e:
        print(f"Error downloading TikTok video: {e}")
