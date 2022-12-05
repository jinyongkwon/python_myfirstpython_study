import plotly.express as px

wide_df = px.data.medals_wide()
print(wide_df)
fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
fig.show()