# imports
import datetime as dt
import json

import pandas as pd
from glob2 import glob


class CleanJSON:
    def __init__(self):
        self.datetime_format = '%Y.%m.%dT%H:%M:%S'
        self.data_frame = pd.DataFrame()
        self.fail_counter = 0

    def get_paths(self):
        self.paths = glob('data/*')

    def clean_json_file(self, json_data):
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
        self.get_paths()
        for path in self.paths:
            with open(path, 'r') as f_obj:
                try:
                    data = json.load(f_obj)
                except json.decoder.JSONDecodeError:
                    self.fail_counter += 1
            self.clean_json_file(data)

    def to_csv(self):
        self.data_frame.to_csv('../data/master.csv')
