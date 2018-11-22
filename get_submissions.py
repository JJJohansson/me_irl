#!/usr/bin/python3
'''
    GET 100 NEWEST SUBMISSIONS FROM ME_IRL SUBREDDIT.
    SAVE THE SUBMISSIONS INTO THE DATABASE.
    USE THE SUBMISSION ID AS THE PRIMARY KEY.
    IF THE SUBMISSION HAS ALREADY BEEN SAVED, IGNORE IT.

    DATA TO BE SAVED:
    - id
    - weekday
    - time of the day
    - number of upvotes
'''

import praw, datetime, sqlite3, os.path

def reddit():
    # OAuth information
    reddit = praw.Reddit(client_id='xxxxxx',
                         client_secret='xxxxxx',
                         user_agent='upvote_analyzer by /u/datamies',
                         username='datamies',
                         password='xxxxxx')

    sub_reddit = 'me_irl'
    new_rows = 0
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    try:
        # open database connection
        path = '/home/pi/exec/reddit/me_irl'
        conn = sqlite3.connect(path)
        print('*** database connection opened ***')
        c = conn.cursor()

        # loop through 50 newest submissions
        for submission in reddit.subreddit(sub_reddit).new(limit=50):
            id = submission.id
            time = get_date(submission)
            upvotes = submission.ups

            try:
                # insert statement
                c.execute("INSERT INTO me_irl (id, weekday, time, upvotes) VALUES (?, ?, ?, ?)",
                            (id, time['weekday'], time['time'], upvotes))
                conn.commit()
            except Exception as e:
                # if the row is already saved, pass and try the next one
                pass
            else:
                # if the row is not in the database, the earlier commit and this print statement is executed
                print('INSERT INTO me_irl (id, weekday, time, upvotes) VALUES ({}, {}, {}, {})'.format(id, time['weekday'], time['time'], upvotes))
                new_rows += 1
    # catch exception if the database connection doesn't work
    except Exception as e:
        print(e)

    finally:
        # close database connection
        c.close()
        conn.close()
        print('*** database connection closed ***')
        print(new_rows,'new row(s) inserted.')
        save_log(new_rows, timestamp)


# format the submission timestamp
def get_date(submission):
    time = submission.created_utc
    return {'weekday':datetime.datetime.fromtimestamp(time).strftime('%w'),
            'time':datetime.datetime.fromtimestamp(time).strftime('%H:%M')}

# everytime the script is run, log the number of rows inserted and the timestamp
def save_log(new_rows, timestamp):
    save_path = '/home/pi/exec/reddit'
    file_name = os.path.join(save_path, 'log.txt')
    try:
        with open(file_name, 'a') as log_file:
            log_file.write('['+timestamp+']: '+str(new_rows)+' row(s) inserted\n')
    except Exception as e:
        with open(file_name, 'a') as log_file:
            log_file.write('['+timestamp+']: Error: ' + str(e) + '\n')


def main():
    reddit()

if __name__ == '__main__':
    main()
