import sqlite3

conn = sqlite3.connect('Youtube_video.db')
cur = conn.cursor()

cur.execute('''
    create table if not exists videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_videos():
    # Selecting element from the db
    cur.execute(""" 
    SELECT * FROM videos
    """)

    for row in cur.fetchall():
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(videoID, name, time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, videoID))
    conn.commit()

def delete_video(videoID):
    cur.execute("DELETE FROM videos WHERE id = ?", (videoID,)) # The comma must be given because tuples can not hold single values
    conn.commit()


def main():
    while True:
        print("Youtube manager with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice Index")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter Video Name")
            time = input("Enter Video Time")

            add_video(name, time)

        elif choice == '3':
            videoID = input("Enter video ID: ")
            name = input("Enter Video Name")
            time = input("Enter Video Time")

            update_video(videoID, name, time)

        elif choice == '4':
            videoID = input("Enter video ID: ")
            delete_video(videoID)

        elif choice == '5':
            break

        else:
            print("Invlid choice")


    conn.close()


if __name__ == "__main__":
    main()
