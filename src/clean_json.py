# imports
import datetime as dt
import json

import pandas as pd
from glob2 import glob


class CleanJSON:
    '''
    Build an object to clean .json files
    '''

    def __init__(self):
        '''
        initialize CleanJSON object

        params
        ======
        None

        attrs
        =====
        datetime_format (str): speciic format to convert date text into datetime
            object
        data_frame (pandas.core.frame.DataFrame): empty dataframe to stow launch
            data
        fail_counter (int): counter for stowing the number of failed .json files

        returns
        =======
        None
        '''
        self.datetime_format = '%Y.%m.%dT%H:%M:%S'
        self.data_frame = pd.DataFrame()
        self.fail_counter = 0

    def get_paths(self):
        '''
        glob all .json file paths

        params
        ======
        None

        attrs
        =====
        paths (list): list of all of the file path in the data folder

        returns
        =======
        None
        '''
        self.paths = glob('data/*')

    def clean_json_file(self, json_data):
        '''
        Cleans a .json file and adds it to the pandas dataframe

        params
        ======
        json_data (dict): dictionary of json data

        attrs
        =====
        None

        returns
        =======
        None
        '''
        df = pd.DataFrame()
        date = dt.datetime.strptime(
            json_data['Timestamp'], self.datetime_format).date()

        for shot in json_data['Shots']:
            time = shot['Timestamp']
            ball_df = pd.DataFrame.from_dict(
                shot['BallData'], orient='index').T
            flight_df = pd.DataFrame.from_dict(
                shot['FlightData'], orient='index').T
            temp_df = pd.concat([ball_df, flight_df], axis=1)
            temp_df['club_type'] = shot['ClubType']
            temp_df['club_name'] = shot['ClubName']
            temp_df['date'] = date
            temp_df['time'] = time
        temp_dataframe = pd.concat([df, temp_df])
        self.data_frame = pd.concat([self.data_frame, temp_dataframe])

    def cleaned_paths(self):
        '''
        Cleans all .json files

        params
        ======
        None

        attrs
        =====
        None

        returns
        =======
        None
        '''
        self.get_paths()
        for path in self.paths:
            with open(path, 'r') as f_obj:
                try:
                    data = json.load(f_obj)
                except json.decoder.JSONDecodeError:
                    self.fail_counter += 1
            self.clean_json_file(data)

    def to_csv(self):
        '''
        Converts pandas dataframe to a .csv

        params
        ======
        None

        attrs
        =====
        None

        returns
        =======
        None
        '''
        self.data_frame.to_csv('../data/master.csv')
