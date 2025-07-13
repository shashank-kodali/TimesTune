 Full Description (for README or documentation)
This project automates the creation of a Spotify playlist based on the Billboard Hot 100 chart for any given date. It uses web scraping (via BeautifulSoup) to extract song titles from the Billboard website and integrates with the Spotify API to search for matching tracks and build a playlist in the user's Spotify account.

Key Features:

Prompts the user for a specific date (YYYY-MM-DD)

Scrapes Billboard’s Hot 100 chart for that date

Searches for each song on Spotify

Creates and populates a new playlist on the user’s Spotify profile

🧱 Technologies Used

->Python
->BeautifulSoup (for scraping)
->Requests
->Spotify Web API via spotipy
