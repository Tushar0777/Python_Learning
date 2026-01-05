import sqlite3

connect=sqlite3.connect("crud.db")

cursor=connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL 
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,length):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?) ",(name,length))
    connect.commit()

def update_video(name,length,video_id):
    cursor.execute("UPDATE videos SET name= ? , time = ? WHERE id = ? ",(name,length,video_id))
    connect.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ? ",(video_id,))
    connect.commit()


def main():

    while True:
        print("\n youtube manager app with db ")
        print(" 1. List Videos ")
        print(" 2. Add Videos ")
        print(" 3. Update Videos ")
        print(" 4. Delete Videos ")
        print(" 5. Exit ")
        choice =input("Enter the choice ")

        if choice=="1":
            list_videos()
        elif choice=="2":
            name=input("Enter video name ")
            length=input("Enter video length ")
            add_video(name,length)
        elif choice=="3":
            list_videos()
            video_id=input("\n Select the id of video you want to update ")
            name=input("Enter the name of updated video ")
            length=input(f"Enter the length of {name}")
            update_video(name,length,video_id)

        elif choice=="4":
            list_videos()
            video_id=input("\n Select the id of video you want to Delete ")
            delete_video(video_id)

        elif choice=="5":
            break

        else:
            print("invalid choice ")

    connect.close()

if __name__=="__main__":
    main()