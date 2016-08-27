import praw             # For reddit API
import sys              # Used for stderr message output
import time             # To make the bot sleep
import threading        # To run second thread that cleans up downvoted posts
import urllib2          # To except HTTPError
import ConfigParser     # Used to read config file (for authentication)

# Reading config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

green_light = True      # Boolean later used to prevent duplicate comments

# From config file for authentication
USERNAME = config.get('Authentication', 'Username')
PASSWORD = config.get('Authentication', 'Password')

USER_AGENT = "WhatWhatWhat by /u/jdeng1234"

def what_scanner(session, phrases):
    print >> sys.stderr, "Scanning comments for phrases..."
    # comments now stores all the comments pulled using comment_stream
    # Change "all" to "subreddit-name" to scan a particular sub
    # limit = None fetches max possible comments (about 1000)
    # See PRAW documentation for verbosity explanation (it is not used here)
    comments = praw.helpers.comment_stream(session, "WhatWhatWhatTest", limit = None, verbosity = 0)

    #for each comment
    #todo: check if comments is empty
    for comment in comments:
        for phrase in phrases:
            print >> sys.stderr, "Searching for '" + phrase + "' in " + "'" + comment.body + "'"
            green_light = True
            # If phrase found in comment
            if phrase in comment.body:
                print >> sys.stderr, "'" + phrase + "'" + " found!..."
                for reply in comment.replies:
                    if reply.author.name == USERNAME:
                        print >> sys.stderr, "Already replied"
                        green_light = False
                        break

                if green_light == True:
                    print >> sys.stderr, "'what' found and no existing comment from me..."
                    post_what_comment(comment)
                    print >> sys.stderr, "posted 'whated comment"
                    break

def post_what_comment(comment):
    try:
        print >> sys.stderr, "Posting comment"
        comment.reply("test")
        print >> sys.stderr, "comment posted"

     # If reddit returns error (when bot tries to post in unauthorized sub)
    except urllib2.HTTPError as e:
        print >> sys.stderr, "Got HTTPError from reddit:" + e.code
        if e.code == 403:
            print >> sys.stderr, "Posting in restricted subreddit."
        print >> sys.stderr, "Nothing to see here. Moving on."

    # To catch any other exception
    except Exception as e:
        print >> sys.stderr, "Got some non-HTTPError exception."

def main():
    # r is reddit object
    r = praw.Reddit(USER_AGENT)
    r.login(USERNAME, PASSWORD, disable_warning=True)
    print("Logged in successfully")

    what_phrases = ("what","wut","wat","wot")

    while(True):
        print >> sys.stderr, "Initializing bot..."
        what_scanner(r, what_phrases)

        print >> sys.stderr, "Taking 15 second break..."
        time.sleep(3)
        print >> sys.stderr, "I'm back!"

if __name__ == '__main__':
    main()
