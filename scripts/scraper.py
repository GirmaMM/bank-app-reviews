from google_play_scraper import reviews_all, Sort
import pandas as pd
import numpy as np

class AppReviewsScraper:
    def __init__(self, app_ids):
        """
        Initialize the scraper with a dictionary of app names and their corresponding IDs.
        """
        self.app_ids = app_ids

    def fetch_reviews(self, app_id):
        """
        Fetch reviews for a given app ID.
        """
        return reviews_all(
            app_id,
            sleep_milliseconds=0,  
            lang='en',  
            country='us',  
            sort=Sort.NEWEST
        )

    def get_reviews_dataframe(self):
        """
        Retrieve reviews for all apps and compile them into a single DataFrame.
        """
        dataframes = []
        for name, app_id in self.app_ids.items():
            reviews = self.fetch_reviews(app_id)
            df = pd.DataFrame(np.array(reviews), columns=['review'])
            df = df.join(pd.DataFrame(df.pop('review').tolist()))
            df['App'] = name  # Add an identifier column
            dataframes.append(df)

        return pd.concat(dataframes, ignore_index=True)