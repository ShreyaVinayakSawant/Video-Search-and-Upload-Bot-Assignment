from insta_downloader import download_instagram_video
from tiktok_downloader import download_tiktok_video
from directory_monitor import start_monitoring
import asyncio

async def main():
    FLIC_TOKEN = "flic_22cbebc37ab0f97a4aca73193bb5dd3d564a94a9a38f2cd20b1a0a293f72f34e"

    # Download videos from Instagram and TikTok
    download_instagram_video("https://www.instagram.com/reels/DDZVNCfzPJY/", "videos")
    download_tiktok_video("https://www.tiktok.com/@username/video/<video_id>", "videos/tiktok_video.mp4")

    # Start monitoring the videos directory for new .mp4 files
    start_monitoring("videos/", FLIC_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())