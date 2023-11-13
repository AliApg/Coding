import json
from typing import Any, List, Literal, Optional

import requests
from bs4 import BeautifulSoup

from .scopusUtils import query_formatter

# from pybliometrics.scopus.utils import config, constants
# from pybliometrics.scopus import ScopusSearch, AuthorSearch
# from pybliometrics.scopus.exception import ScopusQueryError

# API_KEY = '7f59af901d2d86f78a1fd60c1bf9426a' # ???

# API_KEY = '2486a63b5d616aa4de0576feb95e99a5'
API_KEY = '0a8e79cfa41aeded29d60f49ab30d67c'

# API_KEY = '5227c64c7de74597d4c2c75d6eb5bc16'


def scopus_apis(
    query: Optional[str] = None,
    api_link: Literal[
        'authenticate',
        'abstract_citation_count', 'citation_overview', 'serial_title',
        'serial_title_issn', 'subject_classifications_scidir',
        'subject_classifications_scopus', 'abstract_retrieval_scopus_id',
        'abstract_retrieval_eid', 'abstract_retrieval_doi',
        'abstract_retrieval_pii', 'abstract_retrieval_pubmed_id',
        'abstract_retrieval_pui', 'affiliation_retrieval_affiliation_id',
        'affiliation_retrieval_eid', 'author_retrieval',
        'author_retrieval_author_id', 'author_retrieval_eid',
        'author_retrieval_orcid', 'affiliation_search',
        'author_search', 'scopus_search', 'plumx_metrics'
    ] = 'scopus_search',
    api_key: str = '0a8e79cfa41aeded29d60f49ab30d67c',
    requirement: Optional[str] = None,
    parameters: dict | None = None,
    show_result: bool = True,
    reformat_query: bool = False,
    accept: Literal['image/jpeg', 'application/json', 'text/xml',
                    'application/xml', 'text/html'] = 'application/json'
) -> requests.models.Response:
    """
    Retrieve data from various APIs based on the provided API name or URL.

    Args:
        query (str, None): Additional query parameters for the API request.

        api_link (str): The API name or URL to fetch data from. It should be a string
            representing either a valid API name from the list of available APIs or
            a complete API URL. Default is 'scopus_search'.

        requirement (str, None): Additional requirement for the API request.

        parameters (dict): Filter parameters.

        show_result (bool): Whether to print the API response. Default is True.

        reformat_query (bool): Whether to reform query into the right format.

    Returns:
        requests.Response: The response object from the API request.

    Examples:
        To retrieve data from the Scopus search API, use:
        >>> scopus_apis('scopus_search')

        To retrieve data from a custom API with a specific URL, use:
        >>> scopus_apis('https://customapi.example.com/data')

    Raises:
        ValueError: If the provided `api_link` is not a string or is not a valid
            API name. Also, raises a ValueError if the API requires an argument
            (`requirement`) but it's not provided.

    Notes:
        - The function supports multiple APIs, and you can extend the list of APIs and
          their corresponding URLs in the `APIS` dictionary.
        - Ensure that the provided API name is one of the keys in the `APIS` dictionary
          to fetch data from the correct source.
    """
    APIS = {'authenticate': 'https://api.elsevier.com/authenticate/',
            'abstract_citation_count': 'https://api.elsevier.com/content/abstract/citation-count',

            'citation_overview': 'https://api.elsevier.com/content/abstract/citations',

            'serial_title': 'https://api.elsevier.com/content/serial/title',
            'serial_title_issn': 'https://api.elsevier.com/content/serial/title/issn/{}',

            'subject_classifications_scidir': 'https://api.elsevier.com/content/subject/scidir',
            'subject_classifications_scopus': 'https://api.elsevier.com/content/subject/scopus',

            'abstract_retrieval_scopus_id': 'https://api.elsevier.com/content/abstract/scopus_id/{}',
            'abstract_retrieval_eid': 'https://api.elsevier.com/content/abstract/eid/{}',
            'abstract_retrieval_doi': 'https://api.elsevier.com/content/abstract/doi/{}',
            'abstract_retrieval_pii': 'https://api.elsevier.com/content/abstract/pii/{}',
            'abstract_retrieval_pubmed_id': 'https://api.elsevier.com/content/abstract/pubmed_id/{}',

            'abstract_retrieval_pui': 'https://api.elsevier.com/content/abstract/pui/{}',
            'affiliation_retrieval_affiliation_id': 'https://api.elsevier.com/content/affiliation/affiliation_id/{}',
            'affiliation_retrieval_eid': 'https://api.elsevier.com/content/affiliation/eid/{}',

            'author_retrieval': 'https://api.elsevier.com/content/author',
            'author_retrieval_author_id': 'https://api.elsevier.com/content/author/author_id/{}',
            'author_retrieval_eid': 'https://api.elsevier.com/content/author/eid/{}',
            'author_retrieval_orcid': 'https://api.elsevier.com/content/author/orcid/{}',

            'affiliation_search': 'https://api.elsevier.com/content/search/affiliation',

            'author_search': 'https://api.elsevier.com/content/search/author',

            'scopus_search': 'https://api.elsevier.com/content/search/scopus',

            'plumx_metrics': 'https://api.elsevier.com/analytics/plumx/{}'
            # 'plumx_metrics' : 'https://api.elsevier.com/analytics/plumx/{idType}/{idValue}'
            }

    if query and reformat_query:
        query = query_formatter(query)

    if APIS[api_link][-2:] == '{}' and not requirement:
        raise ValueError('This API needs an argument (requirement).')

    parameters = parameters if parameters else {}

    api_link_str = APIS[api_link].format(
        requirement) if requirement else APIS[api_link]
    query_str = f'?query={query}' if query else ''

    resp = requests.get(api_link_str + query_str,
                        headers={'Accept': accept,
                                 'X-ELS-APIKey': api_key},
                        params=parameters,
                        timeout=300)

    if show_result:
        decorative_lines = f'{"="*(len(api_link)+2)}\n'
        print(f'{decorative_lines} {api_link.upper()} \n{decorative_lines}')

        if accept == 'application/json':
            print(json.dumps(resp.json(),
                             sort_keys=True,
                             indent=4, separators=(',', ': ')))
        else:
            print(resp)

    return resp


def get_abstract(url: str, signed_in: bool,
                 api_key: str = '0a8e79cfa41aeded29d60f49ab30d67c',
                 accept: Literal['image/jpeg', 'application/json', 'text/xml',
                                 'application/xml', 'text/html'] = 'application/json') -> str:
    """
    # Dont use this function
    Retrieve the abstract text from a given URL using web scraping.

    Args:
        url (str): The URL of the webpage containing the abstract.
        signed_in (bool): A boolean indicating whether the user is signed in to access the full abstract content.
        api_key (str, optional): API key for authentication. Defaults to a sample API key.
        accept (Literal['image/jpeg', 'application/json', 'text/xml', 'application/xml', 'text/html'], optional):
            The type of content accepted in the response. Defaults to 'application/json'.

    Returns:
        str: Extracted abstract text from the webpage.

    Description:
        This function performs a GET request to the provided URL, including necessary headers and API key if provided.
        It then parses the HTML content using BeautifulSoup and extracts the abstract text based on the provided HTML
        structure. If the user is signed in, the function looks for the abstract within a specific section; otherwise,
        it uses a different section. The extracted abstract text is returned as a string.

    Note:
        - Ensure that the provided URL contains the necessary HTML structure for abstract extraction.
        - The 'accept' parameter specifies the format of the response. The default value is 'application/json'.

    Args Examples:
        >>> abstract_text = get_abstract('https://example.com/abstract', signed_in=True)
        >>> abstract_text = get_abstract('https://example.com/abstract', signed_in=False, api_key='your_api_key')

    Usage:
        - Call this function with the target URL and sign-in status to extract the abstract text from the webpage.
        - Ensure the appropriate HTML structure for abstract extraction is present on the provided URL.

    Raises:
        This function may raise exceptions related to network issues, timeouts, or incorrect HTML structure.

    See Also:
        - BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/

    Example:
        >>> abstract_text = get_abstract('https://example.com/article123', signed_in=True)
        >>> print(abstract_text)
        "This is the extracted abstract text from the provided URL."

    """
    response = requests.get(url, headers={'Accept': accept,
                                          'X-ELS-APIKey': api_key}, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    text_container = soup.find('section').find('p') if signed_in else soup.find(
        'section', id="abstractSection").find('p')
    extracted_text = text_container.get_text()

    return extracted_text


def get_cited_by(url: str, signed_in: bool,
                 api_key: str = '0a8e79cfa41aeded29d60f49ab30d67c',
                 accept: Literal['image/jpeg', 'application/json', 'text/xml'] = 'application/json') -> list:
    """
    # Dont use this function
    Retrieve information about articles cited by the provided URL using web scraping.

    Args:
        url (str): The URL of the webpage containing the cited by information.
        signed_in (bool): A boolean indicating whether the user is signed in to access the full cited by information.
        api_key (str, optional): API key for authentication. Defaults to a sample API key.
        accept (Literal['image/jpeg', 'application/json', 'text/xml'], optional):
            The type of content accepted in the response. Defaults to 'application/json'.

    Returns:
        list: List of dictionaries containing information about articles cited by the provided URL.

    Description:
        This function performs a GET request to the provided URL, including necessary headers and API key if provided.
        It then parses the HTML content using BeautifulSoup and extracts the cited by information from the table.
        If the user is signed in, the function extracts data from a specific table; otherwise, it uses a different table.
        The extracted information is returned as a list of dictionaries, where each dictionary represents a row of
        cited by data with column names as keys.

    Note:
        - Ensure that the provided URL contains the necessary HTML structure for cited by information extraction.
        - The 'accept' parameter specifies the format of the response. The default value is 'application/json'.

    Args Examples:
        >>> cited_by_info = get_cited_by('https://example.com/article123', signed_in=True)
        >>> cited_by_info = get_cited_by('https://example.com/article123', signed_in=False, api_key='your_api_key')

    Usage:
        - Call this function with the target URL and sign-in status to extract information about articles cited by
          the provided URL.
        - Ensure the appropriate HTML structure for cited by information extraction is present on the provided URL.

    Raises:
        This function may raise exceptions related to network issues, timeouts, or incorrect HTML structure.

    See Also:
        - BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/

    Example:
        >>> cited_by_info = get_cited_by('https://example.com/article123', signed_in=True)
        >>> print(cited_by_info)
        [
            {'Title': 'Article Title 1', 'Authors': 'Author 1', 'Year': '2022', 'Journal': 'Journal Name 1'},
            {'Title': 'Article Title 2', 'Authors': 'Author 2', 'Year': '2021', 'Journal': 'Journal Name 2'},
            ...
        ]

    """
    response = requests.get(url, headers={'Accept': accept,
                                          'X-ELS-APIKey': api_key}, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = []
    rows_raw = soup.find_all("tr", class_="searchArea")

    columns = [
        element.get_text().strip()
        for element in soup.find('table',
                                 id='srchResultsList').find('tr').find_all("th")[1:]
    ] if signed_in else [
        element.get_text()
        for element in soup.find('thead').find_all("th")[1:]
    ]

    for row in rows_raw:

        row_extracted = {key: value.get_text().strip()
                         for key, value in zip(columns, row.find_all('td'))}
        rows.append(row_extracted)

    return rows


def process_search_results(results: List[Any], include_abstract: bool = True, include_cited_by: bool = True,
                           signed_in: bool = True, api_key: str = '0a8e79cfa41aeded29d60f49ab30d67c',
                           accept: Literal['image/jpeg', 'application/json', 'text/xml'] = 'application/json') -> List[List[Any]]:
    """
    # Dont use this function
    Process search results from a Scopus API query and extract abstract and/or cited by information from the results.

    Args:
        results (List[Any]): List of search results obtained from the Scopus API.
        include_abstract (bool): If True, extract abstract information. Defaults to True.
        include_cited_by (bool): If True, extract cited by information. Defaults to True.
        signed_in (bool): A boolean indicating whether the user is signed in to access the full abstract/cited by info.
        api_key (str, optional): API key for authentication. Required if 'signed_in' is True.
        accept (str or List[str], optional): The type of content accepted in the response. Defaults to 'application/json'.

    Returns:
        List[List[Any]]: A list of lists containing extracted data (abstract, cited by info) for each search result entry.

    Description:
        This function processes the search results obtained from the Scopus API. For each search result entry, it checks
        if the entry has 'citedby-count' and, if present, extracts abstract and/or cited by information based on the
        provided arguments. The extracted data is organized into lists and returned as a list of lists.

    Note:
        - Ensure that the API responses contain the necessary fields for abstract and cited by information extraction.
        - The 'accept' parameter specifies the format of the response. Defaults to 'application/json'.
        - If 'signed_in' is True, an 'api_key' must be provided for authentication.

    Args Examples:
        >>> search_results = [...list of Scopus search results...]
        >>> processed_data = process_search_results(search_results, include_abstract=True, include_cited_by=True,
        >>>                                          signed_in=True, api_key='your_api_key')
        >>> processed_data = process_search_results(search_results, include_abstract=False, include_cited_by=True,
        >>>                                          signed_in=False)

    Usage:
        - Call this function with the obtained search results to extract abstract and/or cited by information based on
          the specified parameters.
        - Extracted data is returned as a list of lists, where each inner list contains data for a search result entry.

    Raises:
        ValueError: If 'signed_in' is True but 'api_key' is not provided.

    See Also:
        - Scopus API documentation: https://dev.elsevier.com/sc_apis.html

    Example:
        >>> search_results = [...list of Scopus search results...]
        >>> processed_data = process_search_results(search_results, include_abstract=True, include_cited_by=True,
        >>>                                          signed_in=True, api_key='your_api_key')
        >>> print(processed_data)
        [
            ['Abstract 1', 'Cited by Info 1'],
            ['Abstract 2', 'Cited by Info 2'],
            ...
        ]

    """
    if signed_in and not api_key:
        raise ValueError("API key is required when 'signed_in' is True.")

    processed_data = []

    for page in results:
        page_text = json.loads(page.text.encode('utf-8'))

        for result in page_text["search-results"]["entry"]:
            if result.get("citedby-count"):
                data = []

                for link in result['link']:
                    if link["@ref"] == "scopus" and include_abstract:
                        abstract = get_abstract(
                            link["@href"], signed_in, api_key, accept)
                        data.append(abstract)

                    if link["@ref"] == "scopus-citedby" and include_cited_by:
                        cited_by_info = get_cited_by(
                            link["@href"], signed_in, api_key, accept)
                        data.append(cited_by_info)

                if data:
                    processed_data.append(data)

    return processed_data
