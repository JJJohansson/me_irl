import sqlite3, datetime, os.path

def me_irl():
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    choices =   ['[1] CREATE',
                '[2] SELECT *',
                '[3] DELETE ALL DATA',
                '[4] QUIT\n']


    while True:
        for choice in choices:
            print(choice)
        choice = int(input('Select one: '))

        if choice == 1:
            try:
                conn = sqlite3.connect('me_irl')
                print('\n*** Database connection opened ***\n')
                c = conn.cursor()
                conn.execute('''CREATE TABLE ME_IRL
                            (id TEXT PRIMARY KEY,
                            weekday INT NOT NULL,
                            time TEXT NOT NULL,
                            upvotes INT NOT NULL)''')

            except Exception as e:
                print('\n*** ERROR:',e,'***\n')

            finally:
                c.close()
                conn.close()
                print('\n*** Database connection closed ***')

        elif choice == 2:
            try:
                conn = sqlite3.connect('me_irl')
                print('\n*** Database connection opened ***\n')
                c = conn.cursor()
                row_count = 0
                c = conn.execute("SELECT id, weekday, time, upvotes from me_irl")
                print("+--------+---------+-----------------+")
                print("| id     | weekday | time  | upvotes |")
                print("+--------+---------+-----------------+")

                for row in c:
                    if row[3] < 10:
                        print("| {} | {}       | {} | {}       |".format(row[0],row[1],row[2],row[3],))
                        row_count += 1
                    else:
                        print("| {} | {}       | {} | {}      |".format(row[0],row[1],row[2],row[3],))
                        row_count += 1

                print("+--------+---------+-----------------+")
                print('\n*** '+str(row_count)+' row(s) in set ***\n')

            except Exception as e:
                print(e)

            finally:
                c.close()
                conn.close()
                print('*** Database connection closed ***')

        elif choice == 3:
            while True:
                confirm = input("Are you sure? (y/n): ")
                if confirm == 'y':
                    try:
                        conn = sqlite3.connect('me_irl')
                        print('\n*** Database connection opened ***\n')
                        c = conn.cursor()
                        c.execute("DELETE FROM me_irl")
                        conn.commit()
                        print('\n*** Data deleted ***\n')
                        save_log(timestamp)

                    except Exception as e:
                        print(e)

                    finally:
                        c.close()
                        conn.close()
                        print('\n*** Database connection closed ***')
                elif confirm == 'n':
                    print('\n')
                    break
                else:
                    print('\n*** Wrong input ***\n')
                    pass

        elif choice == 4:
            print('*** Program closing.. ***')
            break


        else:
            print('\n'+'*** Invalid choice! ***'+'\n')


# save an entry to the log if data is deleted
def save_log(timestamp):
    try:
        with open('log.txt', 'a') as log_file:
            log_file.write('['+timestamp+']: '+'Deleted all data\n')
    except Exception as e:
        with open(file_name, 'a') as log_file:
            log_file.write('['+timestamp+']: Error: ' + str(e) + '\n')


def main():
    me_irl()

if __name__ == '__main__':
    main()
