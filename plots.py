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

    #Drop rows from other locations then desired
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
    
    #Defining plots + inputs Jet = Awesome looking plots. color = defines the ammount of colors to use.
    #Adjust [0:50] depending on ammounts of top topics/hashes to include in barplot.
    trace1 = go.Bar(x = x[0:50], y = y[0:50], marker = dict(colorscale = 'jet', color = y[0:50]), text = "Word Counts")
    trace2 = go.Bar(x = x[0:50], y = y[0:50], marker = dict(colorscale = 'jet', color = y[0:50]), text = "Word Counts")
    trace3 = go.Bar(x = x[0:50], y = y[0:50], marker = dict(colorscale = 'jet', color = y[0:50]), text = "Word Counts")
    trace4 = go.Bar(x = x[0:50], y = y[0:50], marker = dict(colorscale = 'jet', color = y[0:50]), text = "Word Counts")
    trace5 = go.Bar(x = x[0:50], y = y[0:50], marker = dict(colorscale = 'jet', color = y[0:50]), text = "Word Counts")
    trace6 = go.Bar(x = x[0:50], y = y[0:50], marker = dict(colorscale = 'jet', color = y[0:50]), text = "Word Counts")

    #Assigning tiles for plots + layout structure for subplots
    fig = tools.make_subplots(rows=3, cols=2),
                          subplot_titles=(  'Overall Topic Frequency Count',
                                            'Most Frequent #Hashtag Count',
                                            'Positive Sentiment Frequency Count',
                                            'Negative Sentiment Frequency Count',
                                            'Positive Sentiment Most Frequent Hashtag Count',
                                            'Negative Sentiment Most Frequent Hashtag Count',)
    
    #Append plots to fig. fig = variable holding all the subplots, in order to print out one complete plot in the end.
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    fig.append_trace(trace3, 2, 1)
    fig.append_trace(trace4, 2, 2)
    fig.append_trace(trace5, 3, 1)
    fig.append_trace(trace6, 3, 2)

    #Setting overall title for plots
    fig['layout'].update(showlegend=False, title='Plots of Neighourhood:' + "location")

    #Export plot
    py.iplot(fig, filename='plots.png')