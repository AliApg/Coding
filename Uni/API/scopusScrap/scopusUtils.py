import os
import time
from datetime import datetime
from typing import List, Literal

import geonamescache
import pandas as pd
import spacy
from fuzzywuzzy.fuzz import WRatio, token_set_ratio
from IPython.display import HTML, display
from tqdm.notebook import tqdm_notebook


def log(message: str, length: int = 50):
    """
    Formats and logs a message along with the current date and time.

    Parameters:
        message (str): The message to be logged.
        length (int, optional): The total length of the log entry.
                               Defaults to 50 characters if not provided.

    Returns:
        None

    Example:
        >>> log("Processing completed successfully")
        'Processing completed successfully           2023-10-18 15:30:45'
    """
    message += ' '*(length-len(message))
    print(f'{message} \t{datetime.now()}'.rsplit(".", 1)[0])


def time_formatter(start_time: float) -> str:
    """
    Calculates the elapsed time since a specified start time and
    returns a formatted string representing the elapsed time in hours, minutes, and seconds.

    Parameters:
        start_time (float): The start time, represented as a float value returned by time.time().

    Returns:
        str: A string representing the elapsed time in the format 'HHh MMm SSs'.

    Example:
        >>> start_time = time.time()
        >>> time.sleep(5)  # Simulating a task that takes 5 seconds
        >>> elapsed_time = time_formatter(start_time)
        >>> print(f"Operation completed in {elapsed_time}")
        'Operation completed in 00h 00m 05s'
    """
    elapsed_time_seconds = time.time() - start_time

    hours = int(elapsed_time_seconds // 3600)
    minutes = int((elapsed_time_seconds % 3600) // 60)
    seconds = int(elapsed_time_seconds % 60)

    return f'{hours:02}h {minutes:02}m {seconds:02}s'


def query_formatter(input_str: str) -> str:
    """
    Format a search query string for use in Scopus API requests.

    This function takes an input search query string and performs formatting to make it
    suitable for use in Scopus API requests. It converts the input string to lowercase,
    replaces specific characters, and ensures proper use of boolean operators.

    Args:
        input_str (str): The input search query string to be formatted.

    Returns:
        str: The formatted search query string.

    Example:
        >>> formatted_query = query_formatter('machine learning AND neural networks')
        >>> print(formatted_query)
        'machine+learning+neural+networks'

    Notes:
        - The function converts the input query to lowercase to ensure case-insensitive
          searching.
        - It replaces 'and', 'or', 'not', '+', '-', and '~' with the appropriate boolean
          operators ('AND', 'OR', 'NOT') for Scopus API queries.
        - Multiple spaces are replaced with a single space, and the query is joined
          using '+' to represent spaces in the final formatted query.

    See Also:
        - For Scopus API usage, you can use the formatted query as a parameter in API
          requests to retrieve specific data.
    """
    output_str = input_str.lower()

    replace_chars = {
        ' and ': ' ',
        ' or ': ' ',
        ' not ': ' ',
        ' + ': ' AND ',
        ' - ': ' NOT ',
        ' ~ ': ' OR ',
    }

    for key, value in replace_chars.items():
        output_str = output_str.replace(key, value)

    return "+".join(output_str.split())


def color_code(condition: bool, message: str):
    """
    Display a message with specified color in Jupyter Notebook based on a given condition.

    Args:
        condition (bool): A boolean condition. If True, the message will be displayed in green; if False, in red.
        message (str): The message to be displayed.

    Returns:
        None: This function does not return any value; it displays the formatted message in the specified color.

    Example:
        >>> color_code(True, "Condition is met!")
        # Displays "Condition is met!" in green color.
        >>> color_code(False, "Condition not satisfied.")
        # Displays "Condition not satisfied." in red color.
    """
    color = "green" if condition else "red"
    html_code = f'<div style="color: {color}; font-weight: bold;">{message}</div>'
    display(HTML(html_code))


def analyze_dataset(subset_columns: List[str], download_folder_directory: str | None = None,
                    missing_values_handling: Literal['all', 'any'] = 'all', verbose: bool = False, show_stat: bool = True) -> float:
    """
    Analyze datasets in subfolders and calculate the percentage of missing values in specified columns.

    Args:
        subset_columns (List[str]): A list of column names to check for missing values.
        download_folder_directory (str | None): Path to the directory containing the datasets.
            If None, defaults to 'Download' folder in the current working directory.
        missing_values_handling (Literal['all', 'any']): Determines how missing values are handled.
            - 'all': Drops rows only if all specified columns have missing values.
            - 'any': Drops rows if any of the specified columns have missing values. (Default is 'all').
        verbose (bool): If True, displays detailed information about each file processed. Default is False.
        show_stat (bool): If True, displays the summary statistics after analyzing the datasets. Default is True.

    Returns:
        float: The percentage of missing values in the specified columns across all datasets.

    Raises:
        ValueError: If any file is not a CSV or encounters other parsing errors.

    Example:
        >>> analyze_dataset(['Column1', 'Column2'], missing_values_handling='any')
        # Analyzes datasets in subfolders, checks for missing values in 'Column1' and 'Column2',
        # and displays the percentage of missing values in those columns across all datasets.
    """
    if download_folder_directory:
        os.chdir(download_folder_directory)
    elif not os.getcwd().endswith('Download'):
        os.chdir('Download')

    try:
        all_data_size = columns_without_data = 0
        for folder in os.listdir():
            if os.path.isdir(folder):
                for file in os.listdir(folder):
                    if file.endswith('.csv'):
                        df = pd.read_csv(
                            f'{folder}\\{file}', usecols=subset_columns, low_memory=False)

                        total_rows, rows_after_drop = df.shape[0], df.dropna(
                            how=missing_values_handling).shape[0]
                        # how=missing_values_handling, subset=subset_columns).shape[0]
                        without_columns = total_rows - rows_after_drop

                        all_data_size += total_rows
                        columns_without_data += without_columns

                        if verbose:
                            ok = not without_columns
                            color_code(
                                ok, f'"{file: >40}" Total Rows: {total_rows}, \tRows with Missing Values: {without_columns}')

        percent = (columns_without_data / all_data_size) * 100
        if show_stat:
            print(f'Out of {all_data_size:,} rows, {columns_without_data:,} of them have \
missing values in at least one of the specified columns. {percent:.4f}%')

    except pd.errors.ParserError as e:
        raise ValueError(f'Make sure all files are CSV.\n{e}') from e

    return percent


def convert_csv_to_bibtex(csv_file: str, output_file: str, bib_id: str = 'EID') -> None:
    """
    Read a CSV file containing bibliographic identifiers (e.g., EID) and other fields,
    and convert it to BibTeX entries. Write the BibTeX entries to a .bib file.

    Args:
        csv_file (str): Path to the input CSV file.
        output_file (str): Path to (name of) the output .bib file.
        bib_id (str, optional): Column name containing bibliographic identifiers. Default is 'EID'.

    Returns:
        None

    Example:
        >>> convert_csv_to_bibtex("scopus_test.csv", "output.bib")
        # Reads the input CSV file, generates BibTeX entries using 'EID' as identifiers,
        # and writes them to the output .bib file.
    """
    # Read the CSV file into a pandas DataFrame and drop rows with missing bibliographic identifiers
    df = pd.read_csv(csv_file, low_memory=False).dropna(subset=[bib_id])

    # Function to convert DataFrame row to BibTeX entry
    def convert_to_bibtex(row):
        bibtex_entry = "@article{"
        bibtex_entry += f"{row[bib_id]},\n"

        # Add other fields from the CSV file as BibTeX fields
        for column, value in row.items():
            if column != bib_id and not pd.isna(value):
                bibtex_entry += f"{column} = {{{value}}},\n"

        bibtex_entry = bibtex_entry.rstrip(",\n")
        bibtex_entry += "\n}\n"
        return bibtex_entry

    # Apply the conversion function to each row in the DataFrame
    bibtex_entries = df.apply(convert_to_bibtex, axis=1)

    # Write the BibTeX entries to the output .bib file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(bibtex_entries))

    log(f'"{csv_file}" converted to BibTeX ({output_file})')


def get_bib_file_row_count(file_path: str) -> int:
    """
    Get the number of BibTeX entries in a .bib file.

    Args:
        file_path (str): Path to the .bib file.

    Returns:
        int: Number of BibTeX entries in the file.

    Example:
        >>> get_bib_file_row_count("output.bib")
        # Returns the number of BibTeX entries in the specified .bib file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return sum(bool(line.strip().startswith("@")) for line in lines)


def merge_csv_to_bib_per_folder(input_folder: str, bib_id: str = 'EID') -> None:
    """
    Merge all CSV files in separate folders to individual BibTeX .bib files within each folder.

    Args:
        input_folder (str): Path to the folder containing folders with CSV files.
        bib_id (str): Column name containing unique identifiers (Default is 'EID').

    Returns:
        None

    Example:
        >>> merge_csv_to_bib_per_folder("input_folder")
        # Merges all CSV files in separate folders within 'input_folder',
        # generates BibTeX entries, and writes them to .bib files in respective folders.
    """
    # valid_columns = ['abbrev_source_title', 'abstract', 'address',
    #                  'affiliation', 'affiliations', 'art_number',
    #                  'author', 'author_keywords', 'chemicals_cas',
    #                  'coden', 'correspondence_address1', 'document_type',
    #                  'doi', 'editor', 'funding_details', 'funding_text\xa01',
    #                  'funding_text\xa02', 'funding_text\xa03', 'isbn', 'issn',
    #                  'journal', 'keywords', 'language', 'note', 'number',
    #                  'page_count', 'pages', 'publisher', 'pubmed_id',
    #                  'references', 'source', 'source_title', 'sponsors',
    #                  'title', 'tradenames', 'url', 'volume', 'year']

    convert_map = {"Authors": "author",
                   "Source title": "journal",
                   "Link": "url",
                   "Index Keywords": "keywords",
                   "Abbreviated Source Title": "abbrev_source_title",
                   "Document Type": "type"}

    # Traverse through each folder in the input directory
    for folder in os.listdir(input_folder):
        folder_path = os.path.join(input_folder, folder)

        # Check if the item in the folder is a directory
        if os.path.isdir(folder_path):
            all_bibtex_entries = []
            # Flag to check if any CSV files are found in the folder
            csv_files_found = False

            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)

                # Check if the item is a CSV file
                if file.endswith('.csv'):
                    csv_files_found = True
                    try:
                        # Read the CSV file into a pandas DataFrame and drop rows with missing bib_id
                        df = pd.read_csv(file_path, low_memory=False).dropna(
                            subset=[bib_id])

                        # Function to convert DataFrame row to BibTeX entry
                        def convert_to_bibtex(row):
                            # if not pd.isna(row['Authors']):
                            bibtex_entry = "@" + \
                                row['Document Type'].upper().split()[
                                    0] + "{"
                            # bibtex_entry += f"{row['Authors'].replace(',',' ').replace('.',' ').split()[0]}{row['Year']},\n"
                            bibtex_entry += f"{row[bib_id]},\n"
                            # bibtex_entry += f"{row[bib_id].replace('.', '').replace('-', '')},\n"

                            # Add other fields from the CSV file as BibTeX fields
                            for column, value in row.items():
                                if column != bib_id and not pd.isna(value):
                                    if convert_map.get(column):
                                        column = convert_map.get(column)
                                    column = column.lower().replace(' ', '_').replace('(s)', '')
                                    # if column in valid_columns:
                                    bibtex_entry += f"{column} = {{{value.replace('.','').replace(';',',')}}},\n" if column == 'author' else f"{column} = {{{value}}},\n"

                            access = '' if pd.isna(
                                row['Open Access']) else f"; {row['Open Access'].replace(';', ',')}"
                            bibtex_entry += '' if pd.isna(
                                row['Cited by']) else f"note = {{Cited by: {row['Cited by']}{access}}}"
                            # bibtex_entry = bibtex_entry.rstrip(",\n")
                            bibtex_entry += "\n}\n"
                            return bibtex_entry

                        # Apply the conversion function to each row in the DataFrame
                        bibtex_entries = df.apply(convert_to_bibtex, axis=1)
                        all_bibtex_entries.extend(bibtex_entries)

                    except pd.errors.ParserError as e:
                        raise ValueError(
                            f'Make sure all files are CSV.\n{e}') from e

            # If CSV files are found in the folder, write BibTeX entries to .bib file
            if csv_files_found:
                output_file = os.path.join(folder_path, f"{folder}.bib")
                if os.path.exists(output_file):
                    os.remove(output_file)
                    log(f'Existing "{output_file}" deleted', length=100)

                while None in all_bibtex_entries:
                    all_bibtex_entries.remove(None)
                with open(output_file, "w", encoding="utf-8") as file:
                    file.write("\n".join(all_bibtex_entries))
                log(
                    f'Merged CSV files from "{folder_path}" to BibTeX ({output_file})', length=100)
            else:
                log(f'No CSV files found in "{folder_path}"', length=100)
            print()


def get_authors_name_id():

    # if os.getcwd().endswith('Download'):
    #     pass
    # else:
    #     os.chdir('Download')

    os.chdir(r'D:\Coding\Uni\API\Download')

    all_author_name = []
    all_author_id = []

    try:
        for folder in os.listdir():
            if os.path.isdir(folder):
                for file in os.listdir(folder):
                    if file.endswith('.csv'):
                        df = pd.read_csv(f'{folder}\\{file}', usecols=[
                                         'Author full names'], low_memory=False).dropna()

                        for author_full_names in df.values:
                            for author_name_id in author_full_names[0].split(';'):

                                author_name, author_id = author_name_id[:-1].strip().rsplit(
                                    ' (', 1)
                                all_author_name.append(author_name)
                                all_author_id.append(author_id)
        return pd.DataFrame({'Author': all_author_name, 'ID': all_author_id})
    except pd.errors.ParserError as e:
        raise ValueError(f'Make sure all files are CSV.\n{e}') from e


def check_author_unique_id(similarity: int = 75):

    raw_data = get_authors_name_id()
    cleaned_data = raw_data.drop_duplicates()
    del raw_data

    cleaned_ids = cleaned_data.ID
    author_ids = cleaned_ids[cleaned_ids.duplicated(
        keep=False)].drop_duplicates().values

    names_similarity = []
    for author_id in tqdm_notebook(author_ids):
        first, *authors = [name.replace('.', ' ').replace('-', ' ').replace(
            ',', ' ') for name in cleaned_data[cleaned_data.ID == author_id].Author.values]

        for author in authors:
            value = max(WRatio(first, author),
                        token_set_ratio(first, author))
            if value < similarity:
                names_similarity.append((first, author, value))

    return pd.DataFrame(names_similarity, columns=('Name 1', 'Name 2', 'Similarity'))


def load_geonames_data():
    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries()
    cities = gc.get_cities()
    city_names = [city['name'] for city in cities.values()]
    country_names = [country['name'] for country in countries.values()]
    return city_names, country_names


def tag_location(entity, cities, countries):
    if entity.label_ == 'GPE':
        if entity.text in countries:
            return "Country"
        if entity.text in cities:
            return "City"
    elif entity.label_ != 'ORG':
        return None
    return "ORG"


def get_country_city_org():

    # if os.getcwd().endswith('Download'):
    #     pass
    # else:
    #     os.chdir('Download')

    os.chdir(r'D:\Coding\Uni\API\Download')
    nlp = spacy.load('en_core_web_sm')
    cities, countries = load_geonames_data()

    for folder in os.listdir():
        if os.path.isdir(folder):
            for file in os.listdir(folder):
                if file.endswith('.csv'):
                    affiliation_df = pd.read_csv(f'{folder}\\{file}', usecols=[
                        'EID', 'Affiliations'], low_memory=False).dropna()
                    document_affiliation = []

                    for affiliation in affiliation_df['Affiliations']:
                        cell_affiliation = []

                        for each_affiliation in affiliation.split(';'):
                            each_affiliation_list = []
                            document = nlp(each_affiliation)

                            for entity in document.ents:

                                if entity_label := tag_location(
                                        entity, cities, countries):
                                    each_affiliation_list.append(
                                        (entity.text, entity_label))

                            cell_affiliation.append(each_affiliation_list)
                        document_affiliation.append(cell_affiliation)

                    affiliation_df['Tagged Affiliations'] = document_affiliation
                    affiliation_df = affiliation_df.drop(
                        ['Affiliations'], axis=1)

                    left = pd.read_csv(f'{folder}\\{file}', low_memory=False)

                    merged = pd.merge(left, affiliation_df, how='left')
                    merged.to_csv(f'{folder}\\tagged_{file}.csv', index=False)

                    del left, merged
                    # return affiliation_df


def get_document_types():  # Temp function

    # if os.getcwd().endswith('Download'):
    #     pass
    # else:
    #     os.chdir('Download')

    os.chdir(r'D:\Coding\Uni\API\Download')

    type_set = set()

    try:
        for folder in os.listdir():
            if os.path.isdir(folder):
                for file in os.listdir(folder):
                    if file.endswith('.csv'):
                        df = pd.read_csv(f'{folder}\\{file}', usecols=[
                                         'Document Type'], low_memory=False).dropna().drop_duplicates().values
                        for type_ in df:
                            type_set.add(type_[0])

        return type_set
    except pd.errors.ParserError as e:
        raise ValueError(f'Make sure all files are CSV.\n{e}') from e
