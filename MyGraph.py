import plotly.graph_objects as go


class MyGraph:

    def __init__(self, nodeIds, countAncestors):
        self.fig = go.Figure()
        self.fig.add_trace(go.Bar(x=nodeIds, y=countAncestors))

        xAxisText = []
        for i in nodeIds:
            xAxisText.append(str(i))

        self.fig.update_layout(
            autosize=True,
            xaxis=dict(
                title_text="Node",
                ticktext=xAxisText,
                tickvals=nodeIds,
                tickmode="array",
                titlefont=dict(size=30)
            ),
            yaxis=dict(
                title_text="Repetition",
                titlefont=dict(size=30)
            )
        )

        self.fig.update_xaxes(automargin=True)
        self.fig.update_yaxes(automargin=True)
        self.fig.show()

    def deleteGraph(self):
        self.fig = None
