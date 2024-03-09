import pandas as pd

DATA_SET_PATH = 'res'
DATA_SET_EXTENSION = 'csv'
MOVIES_METADATA = 'Movies_Metadata'

def get_dataset(name):
    file = f'{DATA_SET_PATH}/{name}.{DATA_SET_EXTENSION}'
    df = pd.read_csv(file, low_memory=False)
    return df
    
# main function
def main(): 
    # Read Dataset
    df_movie_metadata = get_dataset(MOVIES_METADATA)
    df_movie_metadata.info()
    
# call main function
if __name__=="__main__": 
	main()
 