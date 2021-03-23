import pandas as pd
from random import randint
import datetime


def scrape_data(num_samples: int, keyword: str) -> pd.DataFrame:
    check_inputs(num_samples, keyword)
    urls = generate_urls(num_samples)
    result = []

    for url in urls:
        resp = collect_html(url)
        soup = make_soup(resp)
        result = extract_data(soup, result)
        sleep(randint(1, 5))

    df = pd.DataFrame(result)
    df = process_data(df)
    return df