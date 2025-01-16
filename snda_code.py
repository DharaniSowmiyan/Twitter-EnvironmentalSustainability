import pandas as pd

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_csv("C:/Users/dhara/Downloads/bert_sentiment_results.csv")


# Sample list of dates
dates = [
    "09-Aug-23", "20-Oct-23", "08-Nov-19", "19-May-19", "03-Aug-24",
    "09-Nov-24", "30-Nov-20", "31-May-24", "15-Oct-18", "10-Nov-18",
    "09-Sep-24", "29-Mar-24", "09-Nov-24", "08-Jul-23", "19-Aug-24",
    "09-Sep-24", "09-Sep-24", "09-Jun-24", "08-Mar-22", "09-Nov-24",
    "16-Jul-23", "09-Sep-24", "07-Jul-19", "07-May-18", "09-Sep-24",
    "06-Feb-19", "09-Oct-24", "09-Sep-24", "09-Sep-24", "14-Sep-24",
    "01-Mar-19", "14-Oct-20", "09-Mar-21", "09-May-21", "19-Mar-23",
    "29-Aug-22", "21-Mar-21", "18-Mar-23", "11-Dec-19", "09-Oct-24",
    "27-Sep-19", "08-Nov-19", "06-Jul-19", "09-Sep-24", "09-Sep-24",
    "16-Nov-19", "09-Nov-24", "09-Sep-24", "29-Jan-19", "05-Jan-21",
    "20-Jun-22", "24-Jun-22", "15-Aug-23", "30-Apr-21", "31-Jul-19",
    "27-Mar-21", "03-Aug-23", "03-Feb-22", "08-Aug-22", "05-Oct-21",
    "24-Jun-19", "06-May-18", "17-Dec-22", "14-Oct-22", "13-Oct-22",
    "03-Sep-22", "15-Aug-22", "22-Jun-22", "22-May-23", "12-Feb-22",
    "12-Nov-18", "24-Jun-22", "24-Jul-21", "18-Oct-22", "12-Jan-22",
    "20-Jun-22", "11-Jul-22", "17-Oct-18", "16-Jun-19", "09-Oct-18",
    "13-Oct-22", "18-May-22", "13-Sep-24", "09-Dec-24", "13-Sep-24",
    "29-May-24", "02-Jun-21", "09-Jan-19", "02-Jan-21", "20-Jan-20",
    "20-Jan-20", "20-Jan-20", "20-Jan-20", "02-Aug-20", "20-Mar-20",
    "22-Dec-19", "02-Feb-19", "10-Jun-18", "03-Dec-19", "23-Jul-23",
    "08-Nov-21", "28-Jun-23", "07-Feb-23", "09-Sep-24", "03-Oct-21",
    "29-Nov-20", "23-Sep-23", "15-Aug-23", "09-Aug-23", "25-Jun-24",
    "19-May-19", "14-Sep-24", "06-Feb-23", "22-Apr-23", "09-Nov-24",
    "19-Aug-24", "22-Apr-20", "25-Nov-23", "26-Feb-24", "14-Sep-24",
    "09-Dec-24", "26-Apr-24", "15-Sep-24", "05-Dec-24", "09-Dec-24",
    "09-Sep-24", "09-Aug-24", "09-Nov-24", "11-Aug-23", "08-Jun-21",
    "01-May-23", "09-Aug-23", "30-Dec-20", "10-Nov-18", "06-Jul-20",
    "22-Sep-21", "12-Jul-23", "14-Sep-24", "13-Jun-24", "11-Mar-21",
    "01-Sep-24", "01-Sep-24", "01-Mar-23", "09-Sep-23", "18-May-19",
    "23-Sep-19", "17-Mar-19", "13-Oct-20", "25-Sep-20", "13-Oct-19",
    "04-May-20", "09-Aug-20", "01-Oct-23", "20-Nov-20", "Sep-10-2010",
    "07-Jun-20", "Sep-10-2010", "29-07-2020", "Jun-12-2010", "31-08-2020",
    "02-06-2023", "Sep-12-2010", "25-09-2023", "23-05-2021", "03-03-2022",
    "10-03-2021", "15-08-2019", "21-09-2019", "18-10-2023", "23-08-2020",
    "15-03-2019", "17-06-2021", "Sep-10-2010", "29-11-2019", "01-09-2019",
    "03-09-2022", "14-03-2021", "13-03-2019", "09-02-2022", "03-09-2021",
    "Sep-10-2010"
]


# Function to parse and format dates
def format_date(date):
    date_formats = [
        "%d-%b-%y",  # Example: 09-Aug-23
        "%d-%b-%Y",  # Example: 30-Nov-2020
        "%d-%m-%Y",  # Example: 29-07-2020
    ]
    
    for fmt in date_formats:
        try:
            # Try to parse the date
            parsed_date = pd.to_datetime(date, format=fmt)
            # Return formatted date as DD-MM-YYYY
            return parsed_date.strftime("%d-%m-%Y")
        except (ValueError, TypeError):
            continue  # If parsing fails, try the next format

    return None  # Return None if no formats match

# Apply the function to the list of dates
formatted_dates = [format_date(date) for date in dates]

# Create DataFrame
df = pd.DataFrame(formatted_dates, columns=['Date'])

# Output the DataFrame
print(df)


# Sidebar for filtering
st.sidebar.header("Filter Data")
selected_sentiment = st.sidebar.selectbox("Select Sentiment", options=["POSITIVE", "NEGATIVE", "All"], index=2)
date_range = st.sidebar.slider("Select Date Range", min_value=pd.to_datetime(df['Date']).min(), max_value=pd.to_datetime(df['Date']).max(), value=(pd.to_datetime(df['Date']).min(), pd.to_datetime(df['Date']).max()))

# Filter by sentiment
if selected_sentiment != "All":
    df = df[df["sentiment"] == selected_sentiment]

# Filter by date
df['Date'] = pd.to_datetime(df['Date'])
df_filtered = df[(df['Date'] >= date_range[0]) & (df['Date'] <= date_range[1])]

# Main title
st.title("Climate Change Sentiment Analysis and Engagement Dashboard")

#### 2. Sentiment Over Time (Temporal Dynamics)
st.subheader("Sentiment Over Time")
df_time_series = df_filtered.groupby('Date')['sentiment'].value_counts().unstack().fillna(0)
fig = px.line(df_time_series, x=df_time_series.index, y=df_time_series.columns, labels={'value':'Number of Tweets'})
st.plotly_chart(fig)

#### 3. Retweets and Likes (Engagement Metrics)
st.subheader("Tweet Engagement: Retweets, Likes, and Views")

# Engagement bar chart
engagement_fig = go.Figure(data=[
    go.Bar(name='Retweets', x=df_filtered['Name'], y=df_filtered['Retweets']),
    go.Bar(name='Likes', x=df_filtered['Name'], y=df_filtered['Likes']),
    go.Bar(name='Views', x=df_filtered['Name'], y=df_filtered['Views'])
])
engagement_fig.update_layout(barmode='group', xaxis_tickangle=-45)
st.plotly_chart(engagement_fig)

#### 4. Investigating Social Media Content (Post Body and Influencers)
st.subheader("Posts and Influencers")

# Display Post Body and Sentiment
for i, row in df_filtered.iterrows():
    st.write(f"**{row['Name']}** ({row['Handle']}): *{row['cleaned_post_body']}* - {row['sentiment']}")
    st.write(f"Engagement: Retweets - {row['Retweets']}, Likes - {row['Likes']}, Comments - {row['Comments']}")
    st.markdown(f"[Link to Tweet]({row['Tweet URL']})")
