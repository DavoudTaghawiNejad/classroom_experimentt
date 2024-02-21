import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def fill_none_with_avg(lst):
    """
    This function takes a list and replaces any series of None values with the average
    of the last non-None value before the series and the first non-None value after the series.
    If the series of Nones is at the start or end, they remain unchanged.
    """
    # Copy the list to avoid modifying the original list
    filled_lst = lst.copy()
    i = 0
    while i < len(filled_lst):
        if filled_lst[i] is None:
            start = i
            # Find the end of the series of Nones
            while i < len(filled_lst) and filled_lst[i] is None:
                i += 1
            end = i
            # Calculate average if possible
            if start > 0 and end < len(filled_lst):
                # Both neighbours are numbers
                avg = (filled_lst[start - 1] + filled_lst[end]) / 2
                for j in range(start, end):
                    filled_lst[j] = avg
            # No action required if None series is at the start or end
        i += 1
    return filled_lst

def plot(quantities, prices):
    window_size = 15  # Define the window size for the moving average
    quantities_ma = np.convolve(quantities, np.ones(window_size)/window_size, mode='valid')

    try:
        prices_ma = np.convolve(prices, np.ones(window_size)/window_size, mode='valid')
    except TypeError:
        prices_ma = None

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=list(range(len(quantities))), y=quantities, name="Quantities"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=list(range(len(prices))), y=prices, name="Prices"),
        secondary_y=True,
    )

        # Add moving average traces
    fig.add_trace(
        go.Scatter(x=list(range(window_size-1, len(quantities))), y=quantities_ma, name="Quantities MA", line=dict(color='black', dash='dash')),
        secondary_y=False,
    )
    if prices_ma is not None:
        fig.add_trace(
            go.Scatter(x=list(range(window_size-1, len(prices))), y=prices_ma, name="Prices MA", line=dict(color='black', dash='dash')),
            secondary_y=True,
        )


    # Add figure title
    fig.update_layout(
        title_text="Quantities and Prices"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Quantities</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Prices</b>", secondary_y=True)

    fig.show()

