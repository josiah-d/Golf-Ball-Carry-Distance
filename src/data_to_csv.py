# imports
import pandas as pd

from clean_json import CleanJSON

if __name__ == '__main__':
    cj = CleanJSON()
    cj.cleaned_paths()
    cj.to_csv()

    # load data
    file_path = 'data/master.csv'

    df = pd.read_csv(file_path, index_col=0)

    column_order = ['date', 'time', 'BallSpeed_MS', 'Azimuth_DEG', 'LaunchAngle_DEG',
                    'BackSpin_RPM', 'SideSpin_RPM', 'TotalSpin_RPM', 'SpinAxis_DEG',
                    'CarryDistance_M', 'TotalDistance_M', 'OfflineDistance_M',
                    'DistanceToPin_M', 'MaxHeight_M', 'DescentAngle_DEG', 'club_type', 'club_name']
    df = df.reindex(columns=column_order)

    # clean columns
    column_names = ['date', 'time', 'ball_speed', 'azimuth', 'launch_angle',
                    'back_spin', 'side_spin', 'total_spin', 'spin_axis',
                    'carry_distance', 'total_distance', 'offline_distance', 'distance_to_pin',
                    'max_height', 'descent_angle', 'club_type', 'club_name']
    df.columns = column_names

    df.drop('club_name', axis=1, inplace=True)

    df = df.reset_index()
    df.drop('index', axis=1, inplace=True)

    df = df[df['club_type'] != 'Pt']

    # convert to .csv
    df.to_csv('data/master.csv')
