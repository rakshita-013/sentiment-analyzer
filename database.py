# SAFE VERSION (NO MongoDB REQUIRED)

reviews = []

def save_review(data):
    reviews.append(data)

def get_all_reviews():
    return reviews