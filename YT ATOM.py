import requests

BASE_YOUTUBE_URL = ""
YOUTUBE_API_KEY = ""  # Do NOT hard-code real keys in production
BASE_NOTION_URL = ""
NOTION_API_KEY = ""
NOTION_DB_ID = ""

def get_video_details(video_ids):
    videos_statistics = []

    # YouTube API allows up to 50 IDs per request
    max_ids_per_request = 50
    # Split video IDs into chunks of 50
    video_id_chunks = [
        video_ids[i:i + max_ids_per_request]
        for i in range(0, len(video_ids), max_ids_per_request)
    ]

    for chunk in video_id_chunks:
        ids = ",".join(chunk)

        url = f"{BASE_YOUTUBE_URL}/videos"
        params = {
            "key": YOUTUBE_API_KEY,
            "id": ids,
            "part": "snippet,statistics"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            items = response.json().get("items", [])

            for item in items:
                videos_statistics.append({
                    "id": item["id"],
                    "title": item["snippet"]["title"],
                    "views": int(item["statistics"].get("viewCount", 0)),
                    "likes": int(item["statistics"].get("likeCount", 0)),
                    "comments": int(item["statistics"].get("commentCount", 0))
                })
        else:
            print("Error:", response.status_code, response.text)

    return videos_statistics


# Example usage
# print(get_video_details(["cJbvcH0JNGA"]))

query_notion_database()