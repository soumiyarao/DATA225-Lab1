import constants
import db_manager
import data_processing
import numpy as np
    
# main function
def main():
    
    # Read Dataset
    df_movie_metadata = data_processing.get_dataset(file_name=constants.MOVIES_METADATA) #, nrows=30)
    df_movie_metadata['id'] = df_movie_metadata['id'].apply(data_processing.replace_non_integer)
    df_movie_metadata = data_processing.clean_df(df_movie_metadata, headers=constants.movies_meta_data_headers)
    df_movie_metadata['id'] = df_movie_metadata['id'].astype(int)
    df_movie_metadata = df_movie_metadata.replace(np.nan, None)
    #df_movie_metadata.info()
    
    df_keywords = data_processing.get_dataset(file_name=constants.KEYWORDS) #, nrows=30)
    df_keywords = data_processing.clean_df(df_keywords, ['id'])
    
    df_links = data_processing.get_dataset(file_name=constants.LINKS) #, nrows=30)
    df_links = data_processing.clean_df(df_links, ['movieId'])
    df_links['tmdbId'] = df_links['tmdbId'].apply(data_processing.replace_non_integer)
    df_links = df_links.replace(np.nan, None)
    
    df_ratings = data_processing.get_dataset(file_name=constants.RATINGS) #, nrows=30)
    df_ratings = df_ratings.replace(np.nan, None)

    
    db_credentilas = db_manager.get_db_credentials() 
    host=db_credentilas['host']
    user=db_credentilas['user']
    password=db_credentilas['password']

    db_manager.create_database(host, user,password, constants.DATABASE_NAME)
    
    data_processing.prepare_movie_metadata_parent_table(df_movie_metadata, host, user, password, constants.DATABASE_NAME)
    for header in constants.primary_table_headers:
        data_processing.prepare_parent_and_connecting_tables(df_movie_metadata, header, host, user, password, constants.DATABASE_NAME)
        
    for header in constants.keywords_table_headers:
        data_processing.prepare_parent_and_connecting_tables(df_keywords, header, host, user, password, constants.DATABASE_NAME)
    
    data_processing.prepare_links_table(df_links, host, user, password, constants.DATABASE_NAME) 
    
    data_processing.prepare_ratings_table(df_ratings, host, user, password, constants.DATABASE_NAME)
  
    
# call main function
if __name__=="__main__": 
	main()
 