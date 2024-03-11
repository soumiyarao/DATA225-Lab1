import pandas as pd
import constants
import db_manager
import ast

def get_dataset(file_name, nrows=None, low_memory=False):
    file = f'{constants.DATA_SET_PATH}/{file_name}.{constants.DATA_SET_EXTENSION}'
    # For windows use \\ as filepath delimeter
    #file = f'{constants.DATA_SET_PATH}\\{file_name}.{constants.DATA_SET_EXTENSION}'
    df = pd.read_csv(filepath_or_buffer=file, nrows=nrows, low_memory=low_memory)
    return df

def remove_duplicates(df, headers=None):
    df_processed = None
    if headers == None:
        df_processed = df.drop_duplicates()
        return df_processed
    
    for header in headers:
        df_processed = df.drop_duplicates(subset=[header])
    return df_processed

def remove_nullrows(df, headers=None):
    df_processed = None
    if headers == None:
        df_processed = df.dropna()
        return df_processed
    
    for header in headers:
        df_processed = df.dropna(subset=[header])
    return df_processed

def clean_df(df, headers=None):
    df_processed = None
    df_processed = remove_duplicates(df, headers)
    df_processed = remove_nullrows(df_processed, headers)
    return df_processed

def prepare_parent_and_connecting_data(df, column_name):
    column1 = constants.HEADER_TMDB_ID
    column2 = f'{column_name}_id'
    corr_column1 = constants.HEADER_ID
    corr_column2 = constants.HEADER_ID
     
    # Initialize a dictionary to store unique values for each key
    connecting_table_data = {}
    connecting_table_data[column1] = []
    connecting_table_data[column2] = []
    
    parent_table_data = {}
    
    # Iterate over each row in the DataFrame
    for _, row in df.iterrows():
        try:
            # Load JSON data from the specified column
            json_object = ast.literal_eval(row[column_name])
            if type(json_object) == dict:
                json_array = [json_object]
            elif type(json_object) == list:
                json_array = json_object
            else:
                print(f'Unsupported json object found: {type(json_object)} in column {column_name}')
        except SyntaxError as e:
            # Handle syntax errors
            # print(f"Ubale to extract json data from {column_name}")
            # print("SyntaxError:", e)
            pass
        except ValueError as e:
            # Handle value errors
            # print(f"Ubale to extract json data from {column_name}")
            # print("ValueError:", e)
            pass
        except Exception as e:
            # Handle other types of exceptions
            # print(f"Ubale to extract json data from {column_name}")
            # print("An error occurred:", e)
            pass
       
        # Iterate over each JSON object in the array
        for json_obj in json_array:
            try:
                # Check if the specified key exists in the JSON object
                if corr_column2 in json_obj:
                # If the key exists, append its value to the list
                    connecting_table_data[column1].append(row[corr_column1])
                    connecting_table_data[column2].append(json_obj[corr_column2])
            except Exception as e:
                print("Error adding entries in connecting_table_data", e)
                
            for key, value in json_obj.items():
                # If the key already exists in the dictionary and the value is not already present in the list,
                # append the value to its corresponding list
                if key in parent_table_data:
                    parent_table_data[key].append(value)
                # If the key does not exist in the dictionary, create a new list for the key and append the value
                else:
                    parent_table_data[key] = [value]

    return parent_table_data, connecting_table_data
    
def prepare_movie_metadata_parent_table(df, host, user, password, database):
    table_name = constants.MOVIES_METADATA_TABLE
    headers = constants.movies_meta_data_headers
         
    create_table_query = f"""
        CREATE TABLE movie_metadata (
        {constants.HEADER_TMDB_ID} INT PRIMARY KEY,
        title VARCHAR(255)
    )
    """
    
    insert_table_query = f"""
            INSERT INTO Movie_Metadata 
            ({constants.HEADER_TMDB_ID}, title) 
            VALUES (%s, %s)
        """
    
    db_manager.create_insert_table(df, host, user, password, database, table_name, create_table_query, headers, insert_table_query)
    
def prepare_parent_and_connecting_tables(df, column_name, host, user, password, database):
    parent_table_data, connecting_table_data = prepare_parent_and_connecting_data(df, column_name)
    parent_table_data = pd.DataFrame(parent_table_data)
    parent_table_data = clean_df(parent_table_data, [constants.HEADER_ID])
    connecting_table_data = pd.DataFrame(connecting_table_data)
    
    parent_table_name = column_name
    header_list = [constants.HEADER_ID,'name'] 
    create_table_query = f"""
        CREATE TABLE {parent_table_name} (
        {parent_table_name}_id INT PRIMARY KEY,
        name VARCHAR(255)
    )
    """
    
    insert_table_query = f"""
        INSERT INTO {parent_table_name} 
        ({parent_table_name}_id, name) 
        VALUES (%s, %s)
    """
    db_manager.create_insert_table(parent_table_data, host, user, password, database, parent_table_name, create_table_query, header_list, insert_table_query)
    
    connecting_table_name = f'movie_{column_name}'
    header_list = [constants.HEADER_TMDB_ID,f'{column_name}_id']
         
    create_table_query = f"""
        CREATE TABLE {connecting_table_name} (
        {constants.HEADER_TMDB_ID} INT,
        {column_name}_id INT,
        Foreign key({constants.HEADER_TMDB_ID}) references {constants.MOVIES_METADATA_TABLE}({constants.HEADER_TMDB_ID}),
        Foreign key({column_name}_id) references {parent_table_name}({column_name}_id),
        Primary Key({constants.HEADER_TMDB_ID}, {column_name}_id)
    )
    """
    
    insert_table_query = f"""
        INSERT INTO {connecting_table_name} 
        ({constants.HEADER_TMDB_ID}, {column_name}_id)
        VALUES (%s, %s)
    """
    
    db_manager.create_insert_table(connecting_table_data, host, user, password, database, connecting_table_name, create_table_query, header_list, insert_table_query)