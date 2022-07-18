import requests
from bs4 import BeautifulSoup
import csv

# Returns the name of the episode with punctuation replaced with their URL equivalents
# With corrections to names that have minor differences between IMDB and the SpongebobWiki
def get_url_ep_name(ep):
    if ep == "BubbleStand":
        return "Bubblestand"
    elif ep == "PreHibernation Week":
        return "Prehibernation_Week"
    elif ep == "One Krab's Trash":
        return "One_Krabs_Trash"
    elif ep == "SpongeBob's House Party (Party Pooper Pants)":
        return "Party_Pooper_Pants"
    elif ep == "SpongeBob B.C. (Before Comedy) (Ugh)":
        return "Ugh"
    elif ep == "Mermaidman and Barnacleboy VI: The Motion Picture":
        return "Mermaid_Man_%26_Barnacle_Boy_VI:_The_Motion_Picture"
    elif ep == "Krabs á la Mode":
        return "Krabs_à_la_Mode"
    elif ep == "Bucket, Sweet Bucket":
        return "Bucket_Sweet_Bucket"
    elif ep == "Blackjack":
        return "BlackJack"
    elif ep == "Whatever Happened to SpongeBob? (WhoBob WhatPants)":
        return "What_Ever_Happened_to_SpongeBob%3F"
    elif ep == "The Patty Caper":
        return "Patty_Caper"
    elif ep == "To Squarepants or Not to Squarepants":
        return "To_SquarePants_or_Not_to_SquarePants"
    elif ep == "I Heart Dancing":
        return "I_♥_Dancing"
    elif ep == "Squidward's School for Grown Ups":
        return "Squidward%27s_School_for_Grown-Ups"
    elif ep == "SquarePants Family Vacation":
        return "A_SquarePants_Family_Vacation"
    elif ep == "InSpongeiac":
        return "InSPONGEiac"
    elif ep == "Super Evil Aquatic Villain Team Up Is Go!":
        return "Super_Evil_Aquatic_Villain_Team_Up_is_Go!"
    elif ep == "MermaidPants":
        return "Mermaid_Pants"
    elif ep == "Surf n' Turf":
        return "Surf_N%27_Turf"
    elif ep == "Bubble Town":
        return "Bubbletown"
    else:
        ep = ep.replace("Mermaidman", "Mermaid Man").replace("Barnacleboy", "Barnacle Boy")
        return ep.replace(" ", "_").replace("'", "%27").replace("?", "%3F")


# Gets the transcript data for these episodes
def get_episodes_transcript(eps):
    # Splits the episodes in the bunch
    episodes = eps.split("/")
    output = ""

    # Iterates through the individual episodes
    for ep in episodes:
        # Scrapes the transcript data
        ep_url = f"https://spongebob.fandom.com/wiki/{get_url_ep_name(ep)}/transcript"
        transcript_scrape = requests.get(ep_url)
        soup = BeautifulSoup(transcript_scrape.text, "html.parser")

        # Separates out the transcript
        transcript_lines = soup.find("div", class_="mw-parser-output")
        transcript_lines = transcript_lines.find_all("ul")
        transcript = ""

        # Adds together each section of the transcript text
        for line in transcript_lines:
            transcript += line.text + "\n"
        
        # Adds this episode's transcript to the overall output
        output += transcript
    
    # Returns all the transcripts for these episodes in one string
    return output[:-1]


# Gets the data for each season and outputs it as a list of dictionaries
def get_season_info(n):
    output = []

    # Scrapes the data from IMDB
    imdb_url = f"https://www.imdb.com/title/tt0206512/episodes?season={n}"
    imdb_scrape = requests.get(imdb_url)
    soup = BeautifulSoup(imdb_scrape.text, "html.parser")

    # Merges the episodes
    odd_episodes = soup.find_all("div", class_="list_item odd")
    even_episodes = soup.find_all("div", class_="list_item even")
    episodes = [episode for tup in zip(odd_episodes, even_episodes) for episode in tup]

    # Iterates through the episodes to create a data entry for each and add it to the output list
    for episode in episodes:
        ep_dict = {}

        # Gets the combined transcript for all of the individual episode(s) in this set
        ep_names = episode.findChild("a")["title"]
        rating = float(episode.findChild("span", class_="ipl-rating-star__rating").text)
        transcript = get_episodes_transcript(ep_names)

        # Assigns dictionary values
        ep_dict["season"] = n
        ep_dict["episode"] = ep_names
        ep_dict["transcript"] = transcript
        ep_dict["rating"] = rating

        # Adds the particular dictionary to the output
        output.append(ep_dict)
    
    # Return the list of dictionaries for this season
    return output


# Scrapes the data from IMDB and SpongeBobWiki and writes it to a csv file
def main():
    # Writes the data to a new csv file
    with open("spongebob_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        fields = ["season", "episode", "transcript", "rating"]
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        
        # Iterates through only the first 12 seasons, since Season 13 is still ongoing
        for i in range(1, 13):
            writer.writerows(get_season_info(i))


# Runs the main program if it's not being imported
if __name__ == "__main__":
    main()
