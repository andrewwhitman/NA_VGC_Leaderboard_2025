import pandas as pd
import urllib.request
import json

def extract_standings(standings_url):
    # load the current NAIC standings
    with urllib.request.urlopen(standings_url) as url:
        data = json.load(url)

    # extract useful standing data
    standings = []
    for v in data:
        record = ''
        for value in v['rounds'].values():
            try:
                record += value['result']
            except TypeError:
                pass
            
        standings.append([v['placing'], v['name'][:-5].title(), v['record']['wins'], v['record']['losses'], v['drop'], record])
        


    # store in df
    standings_df = pd.DataFrame(standings, columns=['placing', 'name', 'wins', 'losses', 'drop', 'record'])
    
    return (standings_df)


# tournament id
url_num = 49

# round prefix
prefix = 'R1_begin' # 'R{x}_{begin/end}'

# load standings
standings_df = extract_standings(f"https://pokedata.ovh/standingsVGC/00001{url_num}/masters/00001{url_num}_Masters.json?")

# save standings
standings_df.to_parquet(f'data/{prefix}_naic25.parquet')
standings_df.to_parquet('data/naic25.parquet')