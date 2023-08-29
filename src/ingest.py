import requests
from bs4 import BeautifulSoup
import pandas as pd

def download_several_years_of_adp(year_start, year_end, format, league_size):

    for y in range(year_start, year_end + 1):
        download_adp(y, format, league_size)


def download_adp(year, format, league_size):
    url = f'https://fantasyfootballcalculator.com/adp/{format}/{league_size}-team/all/{year}'
    html = requests.get(url).text.encode( )
    soup = BeautifulSoup(html, 'html.parser')
    raw_table = (
        soup
        .find('table', class_='table adp')
        .find_all('tr')
    )
    table = [
        [element.text for element in row.find_all('td')] 
        for row in raw_table
    ][1:]

    df = pd.DataFrame(table).drop(10, axis=1)
    df.columns = [
        'rank', 'pick', 'player', 'position', 'team',  'overall', 
        'standard_deviation', 'highest_pick', 'lowest_pick', 'times_drafted'
    ]
    df['year'] = year
    df.to_parquet(f'data/average_draft_pick/adp_{year}.parquet')