import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates and set index column to 'date')
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data by filtering out days when page views were in the top 2.5% or bottom 2.5%
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
  # Copy data frame for the plot
  df_bar = df.copy()

  # Draw line plot
  fig, ax = plt.subplots(figsize=(15, 5))
  ax.plot(df_bar.index, df_bar["value"], color="red", linewidth=1)

  # Set title and labels
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  ax.set_xlabel("Date")
  ax.set_ylabel("Page Views")

  # Save image and return fig (don't change this part)
  fig.savefig("line_plot.png")
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar["Year"] = df_bar.index.year
  df_bar["Month"] = df_bar.index.strftime("%B")

  # Group by Year and Month, then calculate the average daily page views
  df_grouped = (
      df_bar.groupby(["Year", "Month"])["value"].mean().unstack(level=1)
  )

  # Reorder months correctly
  month_order = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
  ]
  df_grouped = df_grouped[month_order]

  # Draw bar plot
  fig = df_grouped.plot(kind="bar", figsize=(15, 8), legend=True).figure
  plt.xlabel("Years")
  plt.ylabel("Average Page Views")
  plt.legend(title="Months", loc="upper left")
  plt.xticks(rotation=0)

  # Save image and return fig (don't change this part)
  fig.savefig("bar_plot.png")
  return fig


def draw_box_plot():
  # Prepare data for box plots
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box["year"] = df_box["date"].dt.year
  df_box["month"] = df_box["date"].dt.strftime("%b")
  df_box["month_num"] = df_box["date"].dt.month

  # Sort by month number to ensure correct chronological order in the plot
  df_box = df_box.sort_values("month_num")

  # Draw box plots using Seaborn
  fig, axes = plt.subplots(1, 2, figsize=(20, 6))

  # Year-wise Box Plot (Trend)
  sns.boxplot(
      x="year", y="value", data=df_box, ax=axes[0], hue="year", legend=False
  )
  axes[0].set_title("Year-wise Box Plot (Trend)")
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")

  # Month-wise Box Plot (Seasonality)
  month_order_short = [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
  ]
  sns.boxplot(
      x="month",
      y="value",
      data=df_box,
      order=month_order_short,
      ax=axes[1],
      hue="month",
      legend=False,
  )
  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")

  # Save image and return fig (don't change this part)
  fig.savefig("box_plot.png")
  return fig