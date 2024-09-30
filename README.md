# NORDIS - Nordic Twitter data specifics
Description of the specifics of the Nordic Twitter datasets collected for various projects in NORDIS.
The data used is gathered by DATALAB and in collaboration with the [HOPE project](https://hope-project.dk/#/). HOPE project has been collecting data for Danish, Norwegian, and Swedish since early 2020. DATALAB is collecting the Finnish tweets for the same time range with a similar approach to match the datasets as closely as possible.

<a href=https://nordishub.eu/>NORDIS website</a>

## The scraping process
DATALAB utilizes the codes made by CHCAA for scraping Finnish Twitter as that is used for scraping the HOPE Scandinavian tweets. For more info, contact Peter Bjerregaard Vahlstrup.

We have the researcher academic access to Twitter and use their API for the scraping. This includes using an API access token and key.
The tweets are recorded in separate files based on the months.

## Structure of this repository
    .
    ├── res                                 # Resources for the Finnish scrape
    │   ├── finnish_query_tracking.md       # Overview on how the Finnish scrape is developing
    │   ├── test_data.py                    # Quick script that shows how many tweets have been scraped per month
    │   ├── M8_FI.txt                       # List of generated finnish keywords
    ├── HOPE-and-scrape-specs.md            # Specifications for the HOPE and Finnish scrapes
    └── README.md                           # Main information for this repository

This repository does not include the API key and token, nor the actual call made to receive the tweets.
