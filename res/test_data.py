"""Testing how well the scrape is going
Author: Maris Sala
Date: 23 Dec 2021
"""

import json
import glob
import pandas as pd
from icecream import ic

import ujson as json
import pandas as pd


def main(test_data):
    include_these = ["10_2020", "09_2020","11_2020","12_2020","02_2021","04_2021","05_2021","06_2021","07_2021","08_2021","09_2021","10_2021","11_2021","12_2021"]
    include_these = ["02_2021"]
    test_data_files = f"{test_data}finnish_tweets_*"
    files = glob.glob(test_data_files)
    files.sort()

    empty_files = []
    for file in files:
        if any(date in file for date in include_these):
            ic(file)

            lines = {"entry_nr":[], "entry":[]}
            i = 0
            created_at = []
            with open(file) as f:
                for line in f:
                    lines["entry_nr"].append(i)
                    lines["entry"].append(line)
                    i+=1
            for i in range(0, len(lines["entry"])):
                try:
                    entry0 = json.loads(lines["entry"][i])
                    created_at.append(entry0["created_at"])
                except:
                    ic("failed row", i)
                    pass
        
            ic(max(created_at), min(created_at))
            ic("Length of entries")
            length = len(lines["entry"])
            del lines
            ic(length)
            if length == 0:
                empty_files.append(file)
            ic("--------------------------------------------------")
    ic(empty_files)

if __name__ == '__main__':
    root_path = "/home/commando/marislab/NORDIS-nordic-Twitter-data-specs/"
    test_data = "/home/commando/marislab/test_data/"
    
    main(test_data)
