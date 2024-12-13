import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

cursor.execute(
    """ 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )             
"""
)


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name, time))
    con.commit()


def update_video(videoId, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, videoId),
    )
    con.commit()


def delete_video(videoId):
    cursor.execute("DELETE FROM videos WHERE id = ?", (videoId,))

    con.commit()


def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit app")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            videoId = input("Enter Video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(videoId, name, time)
        elif choice == "4":
            videoId = input("Enter Video ID to delete: ")
            delete_video(videoId)
        elif choice == "5":
            break
        else:
            print("Invalid Choice ")

    con.close()


if __name__ == "__main__":
    main()
