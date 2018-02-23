import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

def import_df(location):
    """
    Import data as Pandas DF
    Input location label from dict
    """

    df = pd.read_csv("filename.csv", sep='\t', 
                    names = [   "id",
                                "locat"
                                "full_topics", 
                                "full_topics_pos", 
                                "full_topics_neg", 
                                "hash_count", 
                                "hash_count_pos", 
                                "hash_count_neg"])

    #Drop rows from other location then desired
    df[df.locat != location]:

def plots(df):
    """
    Plots that goes into the paper!!
    """
    
def all_plots(df):
    """
    Plotting all the general plots.
    Takes neighbourhood filtered dataframe as input
    Documentation for plot formating: https://plot.ly/python/subplots/
    """
    
    #Defining plots + inputs
    trace1 = go.Bar(x = x[0:50], y = y[0:50], marker = dict(colorscale = 'jet', color = y[0:50]), text = "Word Counts")
    trace1 = go.Bar(x=[1, 2], y=[1, 2])
    trace2 = Bar(x=[1, 2], y=[1, 2])
    trace3 = go.Scatter(x=[1, 2], y=[1, 2])
    trace4 = go.Scatter(x=[1, 2], y=[1, 2])
    trace5 = go.Scatter(x=[1, 2], y=[1, 2])
    trace6 = go.Scatter(x=[1, 2], y=[1, 2])



    
    #Assigning names for plots + layout
    fig = tools.make_subplots(rows=3, cols=2),
                          subplot_titles=(  'First Subplot',
                                            'Second Subplot',
                                            'Third Subplot',
                                            '4 subplot',
                                            '5 subplot',
                                            '6 suplot',)

    #Append plots to fig
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    fig.append_trace(trace3, 2, 1)
    fig.append_trace(trace4, 1, 1)
    fig.append_trace(trace5, 1, 2)
    fig.append_trace(trace6, 2, 1)

    fig['layout'].update(showlegend=False, title='Plots of Neighourhood:' + "location")
