import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot(quantities, prices):
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

