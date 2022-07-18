import json, requests
from bs4 import BeautifulSoup


# Gets the summary data for the given episode
def get_episode_summary(ep):
    # Scrapes the website data
    ep_url = f"https://spongebob.fandom.com/wiki/{ep}"
    web_scrape = requests.get(ep_url)
    soup = BeautifulSoup(web_scrape.text, "html.parser")

    # Gets the synopsis of the episode
    headers = soup.find_all("h2")
    for header in headers:
        if header.text == "Synopsis":
            summary = ""
            elem = header.nextSibling
            # Builds the summary from text elements
            while elem.name != "h2":
                if elem.name == "p":
                    summary += elem.text
                elem = elem.nextSibling
            # Returns the completed episode summary
            return summary[:-1]
    
    # Throws an error if no summary was found
    raise Exception(f"No synopsis was found on the SpongeBob wiki for {ep}.")


# Returns a list of episode dict data for each episode in the given season
def get_season_data(n):
    # Scrapes the list of seasons website
    output = []
    sb_season_scrape = requests.get(f"https://spongebob.fandom.com/wiki/Season_{n}")
    soup = BeautifulSoup(sb_season_scrape.text, "html.parser")

    # Gets a list of episodes and a list of episode descriptions
    episode_list = soup.find_all("tr", class_="general-header")[1:]

    # Iterates through the episodes and creates a JSON entry for each one
    for episode in episode_list:
        # Gets the episode summary data
        td_entry = episode.findChild("td", style="text-align:left")
        ep_title = td_entry.findChild("a")["title"]
        if ep_title == "Knock Knock, Who's There?":
            summary = get_episode_summary("Knock_Knock,_Who%27s_There%3F")
        else:
            summary = get_episode_summary(ep_title)
        
        # Adds the data to the output
        output.append({
            "prompt": ep_title,
            "completion": summary
        })

    # Returns the list of dictionaries
    return output


# The main program
def main():
    # Gets the JSON data for each episode
    episode_data = []
    for i in range(1, 13):
        episode_data += get_season_data(i)
    
    # Writes the output to a JSONL file
    with open("spongebob-data.jsonl", "w", encoding="utf-8") as f:
        for data in episode_data:
            json.dump(data, f, ensure_ascii=False)
            f.write("\n")


# Runs the main program
if __name__ == "__main__":
    main()
