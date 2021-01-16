import math
from itertools import count

import plotly.graph_objects as go


class MyGraph:

    def __init__(self, nodeIds, countAncestors):
        self.fig = go.Figure()
        self.fig.add_trace(go.Bar(x=nodeIds, y=countAncestors))

        ITERATIONS = countAncestors[0]
        countAncestors.remove(countAncestors[0])

        ymax = ITERATIONS + math.floor(ITERATIONS * 0.1)

        self.fig.update_layout(
            autosize=True,
            title=dict(
                text="Traverse tree histogram:",
                y=0.99,
                x=0.5,
                xanchor="center",
                yanchor="top",
                font=dict(size=50)
            ),
            xaxis=dict(
                type="category",
                tickvals=nodeIds,
                tickmode="array",
                title=dict(
                    text="Node",
                    standoff=10,
                    font=dict(size=30)
                )
            ),
            yaxis=dict(
                title_text="Repetition",
                range=[0, ymax],
                titlefont=dict(size=30)
            )
        )

        self.fig.update_xaxes(automargin=True)
        self.fig.update_yaxes(automargin=True)
        self.fig.show()

    def deleteGraph(self):
        self.fig = None
