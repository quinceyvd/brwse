import typer
from rich import print
from bs4 import BeautifulSoup
from datetime import datetime
import requests

app = typer.Typer()
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent" : USER_AGENT}
@app.command()
def google(query: str):
    # Fetch and parse data from Google
    urlQuery = query.replace(" ", "+")
    search = requests.get(f'https://www.google.com/search?q={urlQuery}', headers=headers)
    search = search.text
    soup = BeautifulSoup(search, 'html.parser')

    sources = []
    links = []
    titles = []
    previews = []
    results = soup.find(attrs={'id':'rso'})
    sourcesList = [result for result in results.find_all(attrs={'class':'VuuXrf'})]
    
    # Append sources
    for result1, result2 in zip(sourcesList[::2], sourcesList[1::2]):
        sources.append(result1.get_text())
     
    # Append links    
    for result in results.find_all(attrs={'jsname':'UWckNb'}):
        links.append(result.attrs['href'])

    # Append titles
    for result in results.find_all(attrs={'class':'LC20lb'}):
        titles.append(result.get_text())

    # Append previews
    for result in results.find_all(attrs={'class':'VwiC3b yXK7lf lyLwlc yDYNvb W8l4ac lEBKkf'}):
        previews.append(result.get_text())
    
    # Print results to terminal
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f'[bright_yellow][{timestamp}][/bright_yellow] - Searched [bold]Google[/bold] for [bright_yellow]{query}[/bright_yellow]\n')
    for index, value in enumerate(sources):
        print(f'{sources[index]}\n[link={links[index]}][bold][blue]{titles[index]}[/blue][/bold][/link]\n{previews[index]}\n')

@app.command()
def duck(query: str):
    print(f'[red]DuckDuckGo is currently not yet supported. Please use [bold]Google[/bold] instead.\nSearch query: [bold]{query}[/bold][/red]')
    # query = query.replace(" ", "+")
    # search = requests.get(f'https://duckduckgo.com/?q={query}')
    # search = search.text
    # soup = BeautifulSoup(search, 'html.parser')
    # print(f'Searched DuckDuckGo for {query}')
    # print(soup.get_text())

if __name__ == "__main__":
    app()