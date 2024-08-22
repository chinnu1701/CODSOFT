import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Mock data: user-item ratings with realistic usernames and movie titles
data = {
    'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie', 'David', 'David', 'David'],
    'Item': ['Inception', 'The Matrix', 'Titanic', 'Inception', 'Titanic', 'The Matrix', 'Titanic', 'Inception', 'The Matrix', 'Titanic'],
    'Rating': [5, 4, 3, 5, 2, 4, 3, 2, 4, 5]
}

df = pd.DataFrame(data)

# Create a user-item matrix
user_item_matrix = df.pivot_table(index='User', columns='Item', values='Rating').fillna(0)

# Calculate user similarity matrix
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def get_recommendations(user, user_item_matrix, user_similarity_df):
    similar_users = user_similarity_df[user].sort_values(ascending=False).index[1:]  # Exclude the user themselves
    recommendations = pd.Series(dtype="float64")

    for similar_user in similar_users:
        # Get items that similar_user has rated but the target user hasn't
        similar_user_ratings = user_item_matrix.loc[similar_user]
        user_ratings = user_item_matrix.loc[user]
        
        # Concatenate the recommendations
        recommendations = pd.concat([recommendations, similar_user_ratings[user_ratings == 0]])
    
    # Aggregate and sort recommendations
    recommendations = recommendations.groupby(recommendations.index).mean()
    recommendations = recommendations.sort_values(ascending=False)
    return recommendations

# Interactive part: Continuously ask the user for their input
def interactive_recommendation_system():
    while True:
        user_name = input("Enter your username (or type 'quit' to exit): ")
        
        if user_name.lower() == 'quit':
            print("Exiting the recommendation system. Goodbye!")
            break
        
        if user_name not in user_item_matrix.index:
            print(f"Username '{user_name}' not found in the dataset. Please try again.")
            continue

        recommendations = get_recommendations(user_name, user_item_matrix, user_similarity_df)
        
        if not recommendations.empty:
            print(f"\nRecommendations for {user_name}:")
            print(recommendations)
        else:
            print(f"\nNo recommendations available for {user_name}. It might be that all items have been rated.")

# Run the interactive recommendation system
interactive_recommendation_system()
