
# takes as input a string like: 4 This quiet , introspective and entertaining independent is worth seeking .
# and returns a list like: [4, ['This','quiet','introspective','and','entertaining','independent','is','worth','seeking','.']]

def process_review(inputReview) :
    pass

# opens the file indicated by filename reads in each line, and then called process_review on that line.
# should return a list of all reviews generated by process_review

def process_all_reviews(filename) :
    pass

# takes as input a review of the type generated by process_review and, for each word in the review,
# adds the score for the review to the word's score, and increments the count of occurrences, on inserts
# it into the wordScore dictionary if this is the first time it's appeared.

def add_review_to_score(review, wordScore) :
    pass

# creates a wordScore dictionary, opens the file indicated by filename, reads in each line, and adds each
# review to the wordScore dictionary using add_review_to_score. Returns the wordScore  dictionary.

def add_all_reviews(filename) :
    pass

# takes as input a string representing a review (like "It was really great"),  splits it and computes a predicted
# score by  looking up the average score for each word and averaging those.

def score_review(review, wordScore) :
    pass

# add your six reviews here. Which ones do well with your classifier? Which ones do poorly? Why do you think that is?