import os

import pandas as pd
from habanero import Crossref
from tqdm.notebook import tqdm_notebook

from .scopusUtils import log


def by_reference_title(download_folder_directory: str | None = None) -> None:
    """
    Search for DOI (Digital Object Identifier) information based on references in CSV files.

    Args:
        download_folder_directory (str, optional): Path to the download folder. If provided, changes the current
            working directory to this path. If None, checks if the current working directory ends with 'Download',
            if not, sets the current working directory to 'Download'. Defaults to None.

    Returns:
        None

    Description:
        This function searches for DOI information in CSV files within specified folders. It reads CSV files,
        processes the 'References' column, queries the Crossref API to get DOI information for each reference,
        and adds a new column 'References DOI' to the CSV files containing DOI information. The processed files
        are saved with a 'DOI_' prefix in the same folder.

    Note:
        The Crossref API (crossref-python) is used to retrieve DOI information. Ensure you have appropriate
        access and rate limits are respected when using the API.

    Args Examples:
        >>> by_reference_title()  # Searches for DOI information in the 'Download' folder.
        >>> by_reference_title('custom_folder')  # Searches for DOI information in the 'custom_folder' directory.

    Usage:
        - Call this function to process CSV files within specified folders and retrieve DOI information
          for the references mentioned in the 'References' column of the CSV files.
        - The processed CSV files are saved in the same folder with a 'DOI_' prefix.

    Raises:
        This function does not raise any specific exceptions.

    See Also:
        - Crossref API documentation: https://github.com/fabiobatalha/crossrefapi

    Example:
        >>> by_reference_title('Data/ResearchPapers')  # Processes CSV files in 'Data/ResearchPapers' folder.
        >>> by_reference_title()  # Processes CSV files in the 'Download' folder.

    """
    if download_folder_directory:
        os.chdir(download_folder_directory)
    elif os.getcwd().endswith('Download'):
        pass
    else:
        os.chdir('Download')

    searched_queries = [dr for dr in os.listdir() if os.path.isdir(dr)]
    cross_reference = Crossref()

    for reference_folder in searched_queries:
        log(f'Searching "{reference_folder}" folder')

        for reference_file in os.listdir(reference_folder):
            query_df = pd.read_csv(f"{reference_folder}\\{reference_file}",
                                   low_memory=False).dropna(
                subset='References')
            query_df_values = query_df.loc[:, ['References']].values
            column_values = []

            for references in tqdm_notebook(query_df_values):
                row_reference = []

                for reference in tqdm_notebook(references[0].split(';')):
                    row_reference.append(cross_reference.works(query=reference, limit=1)[
                        'message']['items'][0]['DOI'])
                column_values.append('; '.join(row_reference))

            query_df['References DOI'] = column_values
            query_df.to_csv(f"{reference_folder}\\DOI_{reference_file}")
            del query_df
            log(f'Closed "{reference_file}"')

    return None


def by_article_doi(download_folder_directory: str | None = None) -> None:
    """
    Search for DOI (Digital Object Identifier) information for articles based on their DOIs mentioned in CSV files.

    Args:
        download_folder_directory (str, optional): Path to the download folder. If provided, changes the current
            working directory to this path. If None, checks if the current working directory ends with 'Download',
            if not, sets the current working directory to 'Download'. Defaults to None.

    Returns:
        None

    Description:
        This function processes CSV files within specified folders, extracts DOIs from the 'DOI' column, queries the
        Crossref API to get reference DOIs for each article, and adds new columns 'References DOI all', 'Actual number
        of references', 'Found references', and 'Unfound references' to the CSV files containing DOI information. The
        processed files are saved with a 'DOI_search_' prefix in the same folder.

    Note:
        The Crossref API (crossref-python) is used to retrieve DOI information. Ensure you have appropriate
        access and rate limits are respected when using the API.

    Args Examples:
        >>> by_article_doi()  # Searches for DOI information in the 'Download' folder.
        >>> by_article_doi('custom_folder')  # Searches for DOI information in the 'custom_folder' directory.

    Usage:
        - Call this function to process CSV files within specified folders, extract DOIs, and retrieve DOI
          information for the articles mentioned in the 'DOI' column of the CSV files.
        - The processed CSV files are saved in the same folder with a 'DOI_search_' prefix.

    Raises:
        This function does not raise any specific exceptions.

    See Also:
        - Crossref API documentation: https://github.com/fabiobatalha/crossrefapi

    Example:
        >>> by_article_doi('Data/ResearchPapers')  # Processes CSV files in 'Data/ResearchPapers' folder.
        >>> by_article_doi()  # Processes CSV files in the 'Download' folder.

    """
    if download_folder_directory:
        os.chdir(download_folder_directory)
    elif os.getcwd().endswith('Download'):
        pass
    else:
        os.chdir('Download')

    searched_queries = [dr for dr in os.listdir() if os.path.isdir(dr)]
    cross_reference = Crossref()

    for query_folder in searched_queries:
        log(f'Searching "{query_folder}" folder')
        query_files = os.listdir(query_folder)
        query_files = [file for file in query_files if f'DOI_search_{file}' not in query_files and not file.startswith(
            'DOI_search_')]

        for query_file in query_files:
            query_df = pd.read_csv(
                f"{query_folder}\\{query_file}", low_memory=False).dropna(subset='DOI')
            query_df_dois = [doi_str for doi_str in query_df.loc[:, [
                'DOI']].astype(str).values.reshape(-1).tolist()]

            log(f'Processing "{query_file}"')

            references_column_values = []
            actual_number_of_references_column = []
            number_of_found_references_column = []
            number_of_unfound_references_column = []

            for doi in tqdm_notebook(query_df_dois):
                try:
                    article_references = cross_reference.works(
                        ids=doi)['message']['reference']
                except:
                    references_column_values.append(None)
                    actual_number_of_references_column.append(None)
                    number_of_found_references_column.append(None)
                    number_of_unfound_references_column.append(None)
                else:
                    result_LIST = [reference_doi['DOI']
                                   for reference_doi in article_references if reference_doi.get('DOI')]

                    references_column_values.append('; '.join(result_LIST))
                    actual_number_of_references_column.append(
                        len(article_references))
                    number_of_found_references_column.append(len(result_LIST))
                    number_of_unfound_references_column.append(
                        len(article_references) - len(result_LIST))

            query_df['References DOI all'] = references_column_values
            query_df['Actual number of references'] = actual_number_of_references_column
            query_df['Found references'] = number_of_found_references_column
            query_df['Unfound references'] = number_of_unfound_references_column

            query_df.to_csv(f"{query_folder}\\DOI_search_{query_file}")
            del query_df
            log(f'Processing "{query_file}" has finished')
            log(f'Article not found: {number_of_unfound_references_column.count(None)}')
            log(f'Unfound references: {sum([number for number in number_of_unfound_references_column if number])}')

    return None
