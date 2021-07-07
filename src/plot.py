import plotly.express as px


def plot_launch_direction(df, title, legend, out_path):
    '''
    Creates a polar plot of the launch direction and the carry distance

    params
    ======
    df (pandas.core.frame.DataFrame): dataframe containing launch data
    title (str): name of the title
    legend (str): name of the legent
    out_path (str): name of the path to saze the image

    returns
    =======
    None
    '''
    fig = px.scatter_polar(df, r='carry_distance', theta='azimuth', color='azimuth', opacity=0.5,
                           color_continuous_scale='Turbo', width=1600, height=900, range_theta=(0, 180))

    fig.update_layout(
        title=title,
        legend_title=legend,
        font=dict(size=36),
        margin=dict(l=200, r=200, t=200, b=200))

    fig.write_image(f'../img/launch_direction/{out_path}.png')


def plot_offline_distance(df, title, legend, out_path):
    '''
    Creates a scatter plot of the offline distance and the carry distance

    params
    ======
    df: (pandas.core.frame.DataFrame) dataframe containing launch data
    title: (str) name of the title
    legend: (str) name of the legent
    out_path: (str) name of the path to saze the image

    returns
    =======
    None
    '''
    fig = px.scatter(df, x='offline_distance', y='carry_distance', color='offline_distance',
                     opacity=0.5, color_continuous_scale='Turbo', width=1600, height=900)

    fig.update_layout(
        title=title,
        legend_title=legend,
        font=dict(size=36),
        margin=dict(l=200, r=200, t=200, b=200))

    fig.update_xaxes(range=[-200, 200])

    fig.write_image(f'../img/offline_distance/{out_path}.png')


def plot_ball_speed(df, title, legend, out_path):
    '''
    Creates a scatter plot of the ball speed and the carry distance

    params
    ======
    df: (pandas.core.frame.DataFrame) dataframe containing launch data
    title: (str) name of the title
    legend: (str) name of the legent
    out_path: (str) name of the path to saze the image

    returns
    =======
    None
    '''
    fig = px.scatter(df, x='ball_speed', y='carry_distance',
                     opacity=0.5, width=1600, height=900)

    fig.update_layout(
        title=title,
        legend_title=legend,
        font=dict(size=36),
        margin=dict(l=200, r=200, t=200, b=200))

    fig.update_xaxes(range=[0, 100])

    fig.write_image(f'../img/ball_speed/{out_path}.png')


def plot_launch_angle(df, title, legend, out_path):
    '''
    Creates a scatter plot of the carry distance and the launch angle

    params
    ======
    df: (pandas.core.frame.DataFrame) dataframe containing launch data
    title: (str) name of the title
    legend: (str) name of the legent
    out_path: (str) name of the path to saze the image

    returns
    =======
    None
    '''
    fig = px.scatter(df, x='carry_distance', y='launch_angle',
                     opacity=0.5, width=1600, height=900)

    fig.update_layout(
        title=title,
        legend_title=legend,
        font=dict(size=36),
        margin=dict(l=200, r=200, t=200, b=200))

    fig.write_image(f'../img/launch_angle/{out_path}.png')


def plot_max_height(df, title, legend, out_path):
    '''
    Creates a scatter plot of the carry distance and the max height

    params
    ======
    df: (pandas.core.frame.DataFrame) dataframe containing launch data
    title: (str) name of the title
    legend: (str) name of the legent
    out_path: (str) name of the path to saze the image

    returns
    =======
    None
    '''
    fig = px.scatter(df, x='carry_distance', y='max_height',
                     opacity=0.5, width=1600, height=900)

    fig.update_layout(
        title=title,
        legend_title=legend,
        font=dict(size=36),
        margin=dict(l=200, r=200, t=200, b=200))

    fig.write_image(f'../img/max_height/{out_path}.png')


def plot_spin_axis(df, title, legend, out_path):
    '''
    Creates a polar plot of the spin axis and the carry distance

    params
    ======
    df (pandas.core.frame.DataFrame): dataframe containing launch data
    title (str): name of the title
    legend (str): name of the legent
    out_path (str): name of the path to saze the image

    returns
    =======
    None
    '''
    fig = px.scatter_polar(df, r='carry_distance', theta='spin_axis', color='spin_axis', opacity=0.5,
                           color_continuous_scale='Turbo', width=1600, height=900, range_theta=(0, 360))

    fig.update_layout(
        title=title,
        legend_title=legend,
        font=dict(size=36),
        margin=dict(l=200, r=200, t=200, b=200))

    fig.write_image(f'../img/spin_axis/{out_path}.png')
