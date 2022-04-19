from pprint import pprint
import requests

from config import oatoken

"""
Get track name, artist
Send api call to search
Get first result ID 
Add to playlist


Important Variables:

OAuth Token
Track name/query
Playlist ID 

"""


class spotify_query:
    def __init__(
        self,
        oatoken: str,
        q: str,
        t: str = "track",
        market: str = "US",
        limit: int = 1,
    ) -> None:
        self.token = "Bearer " + oatoken
        self.q = q.replace(" ", "%20")
        self.t = t
        self.market = market
        self.limit = limit
        self.url = f"https://api.spotify.com/v1/search?q={self.q}&type={self.t}&market={self.market}&limit={self.limit}"

    def fetch_json(self) -> dict:
        response = requests.get(url=self.url, headers={"Authorization": self.token})
        return response.json()


def main():
    song_query = "Back in black"
    sq = spotify_query(oatoken=oatoken, q=song_query)

    data = sq.fetch_json()

    track = data["tracks"]["items"][0]

    pprint(track["id"])


if __name__ == "__main__":
    main()
