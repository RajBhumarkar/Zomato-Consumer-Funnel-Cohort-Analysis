import pandas as pd


def cleaning(file_path):
    df = pd.read_csv(file_path)

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df = df.drop_duplicates()
    df = df.dropna(subset=['user_id', 'event', 'channel'])

    df['month'] = df['timestamp'].dt.to_period('M')
    df['week'] = df['timestamp'].dt.to_period('W')
    df['date'] = df['timestamp'].dt.date

    return df


def summary(df):
    summary_df = df.groupby('session_id').agg(
        {
            'user_id':'first',
            'timestamp':['min','max'],
            'event' : lambda x: list(x),
            'device':'first',
            'city':'first',
            'channel':'first',
            'cuisine_category':'first',
            'revenue':'max'
        }
    ).reset_index()
    summary_df.columns = ['session_id','user_id','session_start','session_end','event_sequence','device','city','channel','cuisine_category','revenue']
    

    summary_df['month'] = summary_df['session_end'].dt.to_period('M')
    summary_df['week'] = summary_df['session_end'].dt.to_period('W')
    summary_df['date'] = summary_df['session_end'].dt.date

    
    summary_df['session_duration'] = (summary_df['session_end'] - summary_df['session_start']).dt.total_seconds()/60
    
    return summary_df


def purchase_period(summary_df):
    purchase = summary_df[summary_df['revenue']>0].copy()

    customer_acquired_date = purchase.groupby('user_id')['month'].min().reset_index()
    customer_acquired_date.columns = ['user_id','a_month']
    combined_df = purchase.merge(customer_acquired_date,on='user_id')
    
    combined_df['period'] = (
    combined_df['month'] - combined_df['a_month']
    ).apply(lambda x: x.n)

    return combined_df
