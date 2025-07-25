# Billboard Hot 100 to Spotify Playlist Creator

This Python script allows you to scrape the Billboard Hot 100 chart for a specific date and then automatically create a private Spotify playlist containing those songs.

## ✨ Features

* **Date-Specific Chart Scraping**: Fetches the Billboard Hot 100 chart for any given date.
* **Spotify Integration**: Utilizes the Spotify Web API to search for songs and create playlists.
* **Private Playlists**: Creates a new private playlist on your Spotify account.
* **Token Caching**: Caches your Spotify authentication token to avoid re-authorization on subsequent runs (for a set period).

## ⚙️ How It Works

1.  **User Input**: Prompts the user to enter a date in `YYYY-MM-DD` format.
2.  **Web Scraping**: Uses `requests` to fetch the HTML content of the Billboard Hot 100 chart page for the specified date. `BeautifulSoup` then parses this HTML to extract the titles of the top 100 songs.
3.  **Spotify Authentication**: Authenticates with your Spotify account using the Authorization Code Flow. This requires you to set up a Spotify Developer application and provide your credentials.
4.  **Song Search**: For each song title scraped from Billboard, the script searches Spotify for the corresponding track, prioritizing results from the specified year.
5.  **Playlist Creation**: Creates a new private playlist on your Spotify account with a name indicating the chart date.
6.  **Add Songs to Playlist**: Adds all found Spotify track URIs to the newly created playlist.

## 🚀 Setup and Installation

### Prerequisites

Before you begin, ensure you have:

* **Python 3.x** installed.
    * If `python` or `pip` commands are not recognized, ensure Python is correctly added to your system's PATH. On Windows, it's often best to use `py -m pip` if `pip` alone fails.
* A **Spotify Account**.
* A **Spotify Developer Application**:
    1.  Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
    2.  Log in with your Spotify account.
    3.  Click "Create an app".
    4.  Fill in the details (App name, Description).
    5.  Once created, you will see your **Client ID** and **Client Secret**. Keep these safe!
    6.  Click "Edit Settings" for your app.
    7.  Under "Redirect URIs", **add `http://127.0.0.1:9090`** (this exact URI is used in the script for local authentication).
    8.  Click "Save".

### Installation Steps

1.  **Clone this repository** (or download the `main.py` file):
    ```bash
    git clone [https://github.com/your-username/billboard-spotify-playlist.git](https://github.com/your-username/billboard-spotify-playlist.git)
    cd billboard-spotify-playlist
    ```
    (Replace `your-username` with your actual GitHub username if you clone/fork it)

2.  **Install the required Python libraries**:
    ```bash
    pip install requests beautifulsoup4 spotipy
    ```
    or, if `pip` is not in your PATH:
    ```bash
    py -m pip install requests beautifulsoup4 spotipy
    ```

3.  **Configure your Spotify API Credentials**:
    Open the `main.py` file and replace the placeholder values with your actual Spotify Client ID, Client Secret, and Spotify Display Name:

    ```python
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="[http://127.0.0.1:9090](http://127.0.0.1:9090)",
            client_id="YOUR CLIENT ID",           # <--- REPLACE THIS
            client_secret="YOUR CLIENT SECRET",   # <--- REPLACE THIS
            show_dialog=True,
            cache_path="token.txt",
            username="YOUR SPOTIFY USERNAME",     # <--- REPLACE THIS (e.g., "Shasi")
        )
    )
    ```

## 🚀 Usage

1.  **Run the script** from your terminal:
    ```bash
    python main.py
    ```
    or
    ```bash
    py main.py
    ```

2.  **Enter the date** for the Billboard Hot 100 chart you want to scrape when prompted (e.g., `2025-07-25`).

3.  **Follow the Spotify Authorization Prompt**:
    * A browser window will open, asking you to log in to Spotify and authorize your application.
    * After successful authorization, your browser will be redirected to `http://127.0.0.1:9090`.
    * **Crucially, copy the *entire URL* from your browser's address bar** (it will include `?code=...`).
    * **Paste this full URL back into your terminal** when the script prompts "Enter the URL you were redirected to:".
    * Press Enter.

4.  The script will then proceed to search for songs and create your playlist. Check your Spotify account for the newly created playlist!

## ⚠️ Important Notes & Troubleshooting

* **Redirect URI Deprecation**: Spotify is deprecating HTTP Redirect URIs. While `http://127.0.0.1:9090` works for local development, for any public-facing application, you should use `https` and a proper domain.
* **Billboard Website Structure Changes**: Web scraping relies on the structure of the target website. If Billboard.com changes its HTML structure (e.g., class names, tag hierarchy), the `soup.select(selector="ul li ul li h3.c-title")` line might need to be updated. If the script stops finding songs, this is the first place to check.
* **Songs Not Found**: Not all songs from the Billboard chart may be available on Spotify, or the search query might not perfectly match. The script will print a message for any skipped songs. This is normal behavior.
* **Token Cache**: An `token.txt` file will be created in your script's directory to cache your authentication token. This prevents you from having to re-authorize every time you run the script (until the token expires).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
