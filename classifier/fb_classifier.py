import facebook as fb
import requests
import argparse
from textblob import TextBlob


FLAGS = None

def sentiment_analysis(post):

    # Here's where the magic happens
    tb_msg = TextBlob(post)
    # print str(posts)
    score = tb_msg.sentiment.polarity
    print score
    if score > 0:
            print 'positive'
    elif score == 0:
            print 'neutral'
    else:
            print 'negative'



def connect(access_token, user):
    graph = fb.GraphAPI(access_token)
    profile = graph.get_object(user)

    return graph, profile


def main():

    # access_token = FLAGS.access_token
    # user = FLAGS.profile

    access_token = 'EAACEdEose0cBAO2zappZBcTe1ZAbhznFQDZAIkM3oEMXsR3HZBAwmMF5y1JSJaov1ZAKZAZB2HjnBjQmfz7PzlH2ZCEmdriq9D27ol1Jo2ZADeMv1D5dZBxWVzCcM1V802DQhYEYPbueZAEoTBwLCggZBSCamVnYm8ZAkuk1ooZBKZChknTf2Hm1IodTVBdPmmK6Vl4wmFFevMDKwukigZDZD'
    user ='920538008066818'

    graph, profile = connect(access_token, user)
    
    posts = graph.get_connections(profile['id'], 'posts')


    #Let's grab all the posts and analyze them!
    while True:
        try:
            for post in posts['data']:
              print post['message']
              sentiment_analysis(post['message']) 
              posts= requests.get(posts['paging']['next']).json()

        except KeyError:
            break
            


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Simple Facebook Sentiment Analysis Script')
    # parser.add_argument('--access_token', type=str, required=True, default='', help='Your Facebook API Access Token: https://developers.facebook.com/docs/graph-api/overview')
    # parser.add_argument('--profile', type=str, required=True, default='', help='The profile name to retrieve the posts from')
    # FLAGS = parser.parse_args()
    main()

