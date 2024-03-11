import pandas as pd
import constants
import db_manager
import data_processing

# main function
def main():
    
    # Read Dataset
    df_movie_metadata = data_processing.get_dataset(file_name=constants.MOVIES_METADATA) #, nrows=30)
    df_movie_metadata = data_processing.clean_df(df_movie_metadata, headers=constants.movies_meta_data_headers)
    #df_movie_metadata.info()
    
    db_credentilas = db_manager.get_db_credentials()
    host=db_credentilas['host']
    user=db_credentilas['user']
    password=db_credentilas['password']

    db_manager.create_database(host, user,password, constants.DATABASE_NAME)
    
    data_processing.prepare_movie_metadata_parent_table(df_movie_metadata, host, user, password, constants.DATABASE_NAME)
    #data_processing.prepare_parent_and_connecting_tables(df_movie_metadata, constants.HEADER_GENRES, host, user, password, constants.DATABASE_NAME)
    #data_processing.prepare_parent_and_connecting_tables(df_movie_metadata, constants.HEADE_PRODUCTION_COMPANIES, host, user, password, constants.DATABASE_NAME)
    for header in constants.primary_table_headers:
        data_processing.prepare_parent_and_connecting_tables(df_movie_metadata, header, host, user, password, constants.DATABASE_NAME)
    
# call main function
if __name__=="__main__": 
	main()
 