"""This script houses functions used to download raw data from third party 
sources to disk."""

import os

import requests
from bs4 import BeautifulSoup
import pandas as pd

def download_several_years_of_mock_draft_data(year_start, year_end, format, league_size):
    """Downloads several year of mock draft statistics from 
    fantasyfootballcalculator.com.
    
    Args:
        year_start (int): First year to collect mock draft data for.
        year_end (int): Last year to collect mock draft data for.
        format (str): Format of the league for the mock draft.
        league_size (int): The size of the league that the mock draft happened
        in.
    """
    for y in range(year_start, year_end + 1):
        download_mock_draft_data(y, format, league_size)


def download_mock_draft_data(year, format, league_size):
    """Download mock draft data for one year, a specific league type and league
    size.

    Args:
        year (int): Year to collect mock draft data for.
        format (str): Format of the league for the mock draft.
        league_size (int): The size of the league that the mock draft happened
        in.   
    """
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


def download_nflverse_data(asset_name, year_start, year_end):
    """Downloads a dataset from nflverse for a set of years.
    
    Args:
        asset_name (str): The name of the type of data to download from nflverse.
        year_start (int): First year to collect data for.
        year_end (int): Last year to collect data for.
    """

    for y in range(year_start, year_end + 1):
        _download_nflverse_data(asset_name, y)


def _download_nflverse_data(asset_name, year):
    """Downloads a specific asset from nflverse's github repo for a given year.
    
    Args:
        asset_name (str): The name of the type of data to download from nflverse.
        year (int): Year to collect data for.
    """

    filename = f'{asset_name}_{year}.parquet'
    asset_url = '/'.join([
        'https:', '', 'github.com', 'nflverse', 'nflverse-data',
        'releases', 'download', asset_name, filename
    ])
    response = requests.get(asset_url)
    
    with open(os.path.join('data', 'snap_counts', filename), 'wb') as f:
        f.write(response.content)
    