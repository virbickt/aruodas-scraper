import pytest

### Check inputs
# Check the case when both the inputs are of the right type
def check_both_inputs_correct(input1: int, input2: str) -> None:
    check_inputs(12, "vilnius")


# Check the case when only the second input is of the right type
def check_int_input_correct(input1: int, input2: str) -> None:
    check_inputs("12", "vilnius")


# Check the case when only the first input is of the right type
def check_str_input_correct(input1: int, input2: str) -> None:
    check_inputs(12, 12)


# Check the case when neither of the inputs are of the right type
def check_neither_input_correct(input1: int, input2: str) -> None:
    check_inputs("12", 12)


### Generate links
#Check the case when there's less than 27 num_samples requested
def generate_urls_single_page() -> Str:
    assert generate_urls(27) == 'https://www.aruodas.lt/butu-nuoma/vilniuje/'

def check_for_enough_search_results() -> None:
    num_samples = 4000
    num_pages = -(-num_samples // 27)
    max_pages = 16

    message = """You have requested to generate {num_samples} samples. In order to generate this number of samples,
                      {num_pages} pages of search results would have to be scraped. However, there are only {max_pages} pages
                      available given the criteria you selected. Please enter a number no larger than {max_samples} and 
                      run the program again.
                      """.format(num_samples=num_samples, num_pages=num_pages, max_pages=max_pages,
                                 max_samples=max_pages * 27))
    assert message = """You have requested to generate 4000 samples. In order to generate this number of samples,
                  149 pages of search results would have to be scraped. However, there are only 16 pages
                  available given the criteria you selected. Please enter a number no larger than 432 and 
                  run the program again."""

#Check the case when there's more than 27 num_samples requested and multiple pages are required
def generate_urls_multiple_pages() -> list:
    assert generate_urls(28) == ['https://www.aruodas.lt/butu-nuoma/vilniuje/',
                                 'https://www.aruodas.lt/butu-nuoma/vilniuje/puslapis/2']


### Collect htmls
def check_response_type() -> None:
    urls = ['https://www.aruodas.lt/butu-nuoma/vilniuje/',
            'https://www.aruodas.lt/butu-nuoma/vilniuje/puslapis/2']
    collected_htmls = collect_html(urls)
    assert type(collected_htmls) == requests.models.Response


def check_how_is_the_soup() -> None:
    resp = collect_html(urls)
    soup = make_soup(resp)
    assert type(soup) == bs4.BeautifulSoup


### Extraction
def check_listings() -> None:
    soup = make_soup(resp)
    listings = soup.select("tr.list-row")
    assert type(listings) == list


def check_extracted_data() -> None:
    soup = make_soup(resp)
    listings = soup.select("tr.list-row")
    extracted_data = extract_data(listings)
    assert type(extracted_data) == pandas.core.frame.DataFrame


def check_extracted_data_shape() -> None:
    soup = make_soup(resp)
    listings = soup.select("tr.list-row")
    extracted_data = extract_data(listings)
    assert extracted_data.shape[1] == 7

def test_maximum_page() -> None:
    maximum_page = find_maximum_page()
    assert maximum_page == 16