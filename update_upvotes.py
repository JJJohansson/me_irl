#!/usr/bin/python3
'''
    steps:

     - loop through table rows
     - get the submission by it's id
     - get the submission upvotes
     - update the upvotes of each submission
'''
import praw, sqlite3, datetime, os.path

def update():
    # OAuth information
    reddit = praw.Reddit(client_id='xxxxxx',
                         client_secret='xxxxxx',
                         user_agent='upvote_analyzer by /u/datamies',
                         username='datamies',
                         password='xxxxxx')

    updated_rows = 0
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    try:
        path = '/home/pi/exec/reddit/me_irl'
        conn = sqlite3.connect(path)
        print('\n*** Database connection opened ***\n')
        c = conn.cursor()
    except Exception as e:
        print(e)


    try:
        c = conn.execute("SELECT id from me_irl")
        for row in c:
            submission = reddit.submission(row[0])
            upvotes = submission.ups
            c = conn.execute('UPDATE me_irl SET upvotes = ? WHERE id= ?', (upvotes, row[0]))
            conn.commit()
            print('UPDATE me_irl SET upvotes = {} WHERE id = {}'.format(upvotes, row[0]))
            updated_rows += 1
    except Exception as e:
        print(e)

    finally:
        c.close()
        conn.close()
        print('\n*** Database connection closed ***')
        print(updated_rows,'new row(s) updated.')
        print('*** Program closing.. ***')
        save_log(updated_rows, timestamp)


# everytime the script is run, log the number of rows inserted and the timestamp
def save_log(updated_rows, timestamp):
    save_path = '/home/pi/exec/reddit'
    file_name = os.path.join(save_path, 'log.txt')
    try:
        with open(file_name, 'a') as log_file:
            log_file.write('['+timestamp+']: '+str(updated_rows)+' row(s) updated\n')
    except Exception as e:
        with open(file_name, 'a') as log_file:
            log_file.write('['+timestamp+']: Error: ' + str(e) + '\n')


def main():
    update()

if __name__ == '__main__':
    main()
