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
    test_data_files = f"{test_data}finnish_tweets*"
    files = glob.glob(test_data_files)

    empty_files = []
    for file in files:
        ic(file)

        lines = {"entry_nr":[], "entry":[]}
        i = 0
        with open(file) as f:
            for line in f:
                lines["entry_nr"].append(i)
                lines["entry"].append(line)
                i+=1

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