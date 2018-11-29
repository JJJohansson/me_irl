# me_irl
Fetching data from [Reddit's](https://www.reddit.com/) [me_irl subreddit](https://www.reddit.com/r/me_irl/) submissions.

Phase one: (completed)
- Fetch new submissions every 5 minutes. The script will be set up running on Raspberry Pi 3 Model B+. The script itself will be set to run every 5 minutes with Linux cron job.
- Save new submissions to SQLite database.
- Data saved: weekday, time, upvote amount and submission id (id used as primary key)

Phase two: (in progress..)
- Update the upvote of every saved submission.

Phase three: (in progress..)
- Analyze the data with Python and create a heatmap to see if there are correlations between time/weekday and the total amount of upvotes the submission received.

Technologies used:
- Python
- Python Reddit API Wrapper (PRAW)
- Python seaborn.heatmap or matplotlib
- SQLite
- Raspberry Pi 3 Model B+
- Raspbian OS
- Linux Cron jobs
