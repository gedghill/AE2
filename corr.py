import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from fetch_data import fetch_data

def get_corr_matrix(data):
    # Calculate the correlation matrix for the 'Close' prices of all cryptocurrencies
    correlation_matrix = data.corr()
    # Create the heatmap
    fig = px.imshow(
        correlation_matrix,  # The correlation matrix
        labels=dict(x="Cryptocurrency", y="Cryptocurrency", color="Correlation"),  # Axis labels
        x=correlation_matrix.columns,  # X-axis labels (cryptocurrencies)
        y=correlation_matrix.index,    # Y-axis labels (cryptocurrencies)
        #text_auto=True,  # Display correlation values on the heatmap
        color_continuous_scale='RdBu',  # Color scale
        title="Cryptocurrency Correlation Matrix"  # Title of the plot
    )

    # Update layout for better readability
    fig.update_layout(
        xaxis_title="Cryptocurrency",
        yaxis_title="Cryptocurrency",
        width=800,  # Width of the plot
        height=800,  # Height of the plot
    )

    return fig

def get_selected_corr(data):
     # Calculate the correlation matrix for the 'Close' prices of all cryptocurrencies
    correlation_matrix = data.corr()
    selected_coins = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'WIF-USD']
    selected_correlation_matrix = correlation_matrix[selected_coins]

    fig = px.imshow(
        selected_correlation_matrix,
        labels=dict(color="Correlation"),
        color_continuous_scale='RdBu',
        text_auto=True,
        aspect="auto",
        height = 800,
        title="Selected Cryptocurrency Correlation Matrix"
    )

    return fig

def get_top_4_positive(data, symbol:str):
    # Calculate the correlation matrix for the 'Close' prices of all cryptocurrencies
    correlation_matrix = data.corr()
    # Extract the correlation values for BTC-USD
    btc_correlations = correlation_matrix[f'{symbol}']

    # Sort the correlations in descending order and exclude BTC-USD itself
    sorted_correlations = btc_correlations.drop(f'{symbol}').sort_values(ascending=False)

    # Select the top 4 positively correlated coins
    top_4_positive = sorted_correlations.head(4)
    
    return top_4_positive

def get_top_4_negative(data,symbol:str):
     # Calculate the correlation matrix for the 'Close' prices of all cryptocurrencies
    correlation_matrix = data.corr()
    # Extract the correlation values for BTC-USD
    btc_correlations = correlation_matrix[f'{symbol}']

    # Sort the correlations in descending order and exclude BTC-USD itself
    sorted_correlations = btc_correlations.drop(f'{symbol}').sort_values(ascending=True)

    # Select the top 4 positively correlated coins
    top_4_negative = sorted_correlations.head(4)
    
    return top_4_negative

def get_kmeans_tables(data):
    #Transpose columns and rows so that we have 30 rows and 365 columns
    df_transposed = data.transpose()
    # Handle missing values (if any) using Forward fill
    df_transposed.ffill(inplace=True)

    # Scale the data
    x = StandardScaler().fit_transform(df_transposed)

    # Apply PCA with 2 components
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(x)
    principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
    df_transposed.reset_index()
    # Create a new DataFrame with the principal components
    # preserve the ticker index

    principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])

    principalDf['coin'] = df_transposed.reset_index()['index']
    # Apply KMeans clustering with 4 clusters, drop Coin column to make dataset more readable by k-means algorithm
    kmeans = KMeans(n_clusters=4, random_state=0)
    principalDf['cluster'] = kmeans.fit_predict(principalDf.drop('coin', axis=1))

    # Display the DataFrame with cluster assignments
    principalDf.sort_values(by='cluster')
    # Convert the 'cluster' column to string to ensure discrete coloring
    principalDf['cluster'] = principalDf['cluster'].astype(str)

    # Create an interactive scatter plot
    fig = px.scatter(
        principalDf,
        x='principal component 1',
        y='principal component 2',
        color='cluster',  # Color by cluster (now treated as discrete)
        hover_data=['coin'],  # Show coin name on hover
        title='K-Means Clustering of Cryptocurrencies (2D PCA)'
    )

    # Customize marker size and layout
    fig.update_traces(marker=dict(size=12))
    fig.update_layout(
        xaxis_title='Principal Component 1',
        yaxis_title='Principal Component 2',
        legend_title='Cluster'
    )
    chosen_coins = principalDf.loc[principalDf['coin'].isin(['BTC-USD','ETH-USD', 'BNB-USD','WIF-USD'])]

    # Return k-means result table and 
    return chosen_coins, principalDf, fig