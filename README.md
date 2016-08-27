/u/WhatWhatWhatBot
======================
This is my first Reddit bot. I created it to practice Python and using the Reddit API with PRAW.

This bot that scans Reddit comments in a particular subreddit as they come in. It looks for certain phrases or slang that are synonymous with "what" and makes a reply.

This bot is built using PRAW (Python Reddit API Wrapper).

This is just a fun little project I did, and it might not be perfect or complete because I'm only getting started. It serves as a stepping stone for more complex bots.


What it does
------------
On Reddit, repliers sometimes reply with "what" to comments which almost always provides no feedback to the comment and is often used in a sarcastic tone. When the bot see a reply with "what" or something similar like "wot" or "wat" it will reply to that comment with a uppercased comment of the same comment.


How it works
------------
This bot makes use of PRAW's comment_stream to continuously pull comments over and over in a loop every 15 seconds. It scans each one using the list "phrases".

The bot's login details (username/password) are stored in a config file which is not included in this repository.

What you can do with this code
------------------------------
This bot is open-source, I have not included the username and password for the reddit account in the code. Instead I put it into a .ini file which the bot reads when logging in.

If you were to run this bot on your computer, here's what you would do:
- **Install Python, pip, and PRAW**
- Edit the config.ini.dist and remove the .dist. Add a reddit username and password as well as the subreddit you would like to scan in in the placeholders.
- Run the bot using this command from the directory you put it into:
    <code>python WhatBot.py</code>
