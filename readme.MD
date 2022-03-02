## Homework #2 Sentiment analysis

#### Due Fri, March 11, 11:59pm. To turn in, please push all your code to your github repo.

This homework will be graded using specifications grading. To earn a 'C', complete steps 1-4. To earn a B, complete steps 1-6. To earn an 'A', complete steps  1-7.

In this problem, we're interested in developing a tool that can determine whether a movie review is good or bad depending on the words it contains.

For example, a review that says "The film is a breath of fresh air" is positive, while a review that says "this movie made me want to poke my eyes out" is negative.

We're going to use supervised machine learning to solve this problem.

#### The Data

The file movieReviews.txt contains 8529 reviews scraped from RottenTomatoes. Each review has a score from 0 (worst) to 4 (best), along with the review text. The text has had some pre-processing done to separate punctuation from text.

####The approach.

We're going to use a simple averaging strategy here to predict a review's score based on the word in it.
To do this, we'll start with a set of labeled reviews. For each review, we'll do the following:


#### Step 1 - process a review.

To begin, we need a way to store our reviews. Let's keep each review in a list, with two elements: a sublist containing all of the words, and the score for that review.py
For example: 4 This quiet , introspective and entertaining independent is worth seeking .

would be:
<pre>
[4, ['This','quiet','introspective','and','entertaining','independent','is','worth','seeking','.']]
</pre>

Write a function called process_review that takes in one line from movie-reviews.txt and returns a list like this.

#### Step 2. Process all the reviews.

Now we're ready to process all the reviews. Write a function called process_all_reviews that opens movie-reviews.txt, reads each line,
and calls process_review on that line. Store all the reviews in a list called all_reviews.

#### Step 3: Build our wordScore dictionary.
Our goal is to be able to predict how good or bad a particular review is. We'll estimate this by averaging the score for each word in the review.
But to do that, we need to know how good or bad each word is. 

We'll store this in a dictionary called wordScore. It will have as a key the word and as a value a list containing the total score for that word and the number of times it appears. (we can divide those to get an average.)

So how to build this?

Let's start by building a function called add_review_to_score. It should take as input one of the reviews we created in step 1, along with 
our wordScore dictionary, and, for each word in the review, increment the score and the number of times it was seen.

For example, let's say our wordScore dictionary contained:
<pre>
{'This' : [3, 1], 'quiet' : [2,3]}
</pre>
We could read this as: the word 'This' has a total score of 3, and appears once. 'quiet' has a total score of 2, and has appeared 3 times. (so its average is 0.66)

Suppose our next review was [4, ['This','movie','rules']]

After we add it to wordScore, wordScore should be:
<pre>
{'This' : [7, 2], 'quiet' : [2,3], 'movie': [5,1], 'rules' : [5,1]}
</pre>

Note that 'This' was already present, so we added the score for this review to its total (going from 3 to 7) and incremented the number of appearances.
'movie' and 'rules' were not yet in our dictionary, so we added them, along with the score for this review and a count of 1.

#### Step 4: Process all the reviews.

Now we just need to process all the reviews. Write a function called add_all_reviews that creates a new wordScore dictionary and then repeatedly
calls add_review_to_score for each review.

#### Step 5: Predict scores

Now we're ready to use our dictionary to predict the score for a new review. Our formula will be pretty simple: We'll predict that
the score for a review will be the average of the average score for each word in the wordScore dictionary.

So, if wordCount was: 
<pre>
{'This' : [7, 2], 'quiet' : [2,3], 'movie': [5,1], 'rules' : [5,1], 'stinks' : [3,3], 'too' : [7,2]}
</pre>

and we wanted to predict a score for the review: "too quiet. stinks."

We would look up 'too', compute its average score as 3.5, look up quiet, compute its average score as 1.5, and then look up stinks,
and compute its average score as 1. (this is the total score divided by the number of occurrences.)
We would then sum up and average each of these scores. (3.5 + 1.5 + 1) / 3 = 2, so we would predict a score of 2. 

Write a function called score_review. It should take as input a string, such as "this movie is the best", and a wordCount dictionary.
It should split the string and then use the formula above to estimate a score, which the function returns.

If a word is not in the wordCount dictionary, you can ignore it.

Try it out, both with reviews from movie-reviews.txt as well as your own ideas.

#### Step 6: Improving performance

We know from class that not all words are equally useful. We also know that case matters, and that punctuation is can be distracting.
Modify addReviewToScore to:
- throw away punctuation, as well as words beginning with a '. (note that they're already separate characters in the movie-reviews.txt file.)
- convert everything to lower case.
- throw away the following stopwords: he,she,it, they, the, an, a, and, with.

#### Step 7: Experiment.

Now you're ready to try it out. To start, select a few reviews from movie-reviews.txt and use them as input to score_review. How close does your
classifier get to the true value?

Next, construct a set of six reviews. Create three that your classifier does well at, and three that it does poorly at.
Add them to sentiment.py, along with a paragraph discussing why the classifier does well or poorly on them.

