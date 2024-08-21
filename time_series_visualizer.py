import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data
q_low = df['value'].quantile(0.025)
q_hi = df['value'].quantile(0.975)
df = df[(df['value'] >= q_low) & (df['value'] <= q_hi)]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()

    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_line.index, df_line['value'], color='blue')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.to_series().dt.strftime('%B')  # Ensure correct month names

    # Group by year and month and calculate average page views
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Reorder columns to match the correct month order
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar_grouped = df_bar_grouped[month_order]  # Reorder columns

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar_grouped.plot(kind='bar', ax=ax)
    ax.set_title('Average Daily Page Views by Month and Year')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=month_order)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))
    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
