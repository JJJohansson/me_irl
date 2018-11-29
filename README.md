# me_irl
Fetching data from Reddit's[https://www.reddit.com/] me_irl subreddit[https://www.reddit.com/r/me_irl/] submissions.

Phase one:
- fetch new submissions every 5 minutes (execute script every 5 minutes with linux cron jobs)
- save new submissions to sqlite database
- data saved: weekday, time, upvote amount and submission id (id used as primary key)

Phase two: (in progress..)
- update the upvote of every saved submission

Phase three: (in progress..)
- check if there are correlations between time/weekday and the amount of upvotes
