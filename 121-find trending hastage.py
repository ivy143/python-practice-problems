# Find trending hashtags problem
def find_trending_hashtags(hashtags, k):
    from collections import Counter
    if k <= 0:
        return []

    # Count the frequency of each hashtag
    hashtag_counts = Counter(hashtags)

    # Get the k most common hashtags
    trending = hashtag_counts.most_common(k)

    # Extract just the hashtags from the (hashtag, count) tuples
    return [hashtag for hashtag, count in trending]
# Example usage
hashtags = ["#fun", "#sun", "#fun", "#beach", "#sun", "#travel", "#fun", "#travel"]
k = 2
result = find_trending_hashtags(hashtags, k)
print("Trending hashtags:", result)  # Output: Trending hashtags: ['#fun', '#sun']