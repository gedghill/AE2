#Everything in this file was copied and pasted from google colab. All code works in colab. Test & debug code here.
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Handle missing values (if any) using Forward fill
df_transposed.fillna(method='ffill', inplace=True)

# Scale the data
x = StandardScaler().fit_transform(df_transposed)

# Apply PCA with 2 components
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)

# Create a new DataFrame with the principal components
# preserve the ticker index

principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])

principalDf['coin'] = df_transposed.reset_index()['Ticker']

# Display the new DataFrame
principalDf

# Print the explained variance ratio
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# Display the new DataFrame
principalDf

#Conduct K-means clustering
from sklearn.cluster import KMeans

# Apply KMeans clustering with 4 clusters, drop Coin column to make dataset more readable by k-means algorithm
kmeans = KMeans(n_clusters=4, random_state=0)
principalDf['cluster'] = kmeans.fit_predict(principalDf.drop('coin', axis=1))

# Display the DataFrame with cluster assignments
principalDf.sort_values(by='cluster')
# prompt: write code to add back the coin column after clustering

# Assuming your code is already executed and principalDf is defined

# Move the 'coin' column to the beginning of the DataFrame
cols = principalDf.columns.tolist()
cols = cols[-1:] + cols[:-1]
principalDf = principalDf[cols]

# Display the DataFrame with cluster assignments and the coin column at the beginning
principalDf.sort_values(by='cluster')
import plotly.express as px

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

# Show the plot
fig.show()