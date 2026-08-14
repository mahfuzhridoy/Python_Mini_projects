import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file) # converting to json
    except FileNotFoundError:
        return []
    # finally:
    #     pass

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_video(videos):
    print("\n")
    print("-" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} {video['time']}")
    print("-" * 70)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_video(videos)
    selection = int(input("Which video to update? "))
    if 1<= selection <= len(videos):
        name = input("enter new video name: ")
        time = input("enter new video time: ")

        videos[selection-1] = {'name': name, 'time': time}
        save_data_helper(videos)
        list_video(videos)

    else:
        print("Invalid index!")
    

def delete_video(videos):
    list_video(videos)
    selection = int(input("Enter the video number to delete: "))
    if 1<= selection <= len(videos):
        del videos[selection-1]
        save_data_helper(videos)
        print("Deletion successful! ")
        list_video(videos)
    else:
        print("Invalid index!")  


def main():

    videos = load_data()
    while True:
        print('\n Youtube manager | Choose an option')
        print('1. List a favourite video')
        print('2. Add a youtube video')
        print('3. Update a youtube video details')
        print('4. Delete a video')
        print('5. Exit the app')

        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_video(videos) # define videos variable for taking video list

            case '2':
                add_video(videos) 

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)

            case '5':
                break

            case _: # Default
                print("Invalit option!")


if __name__ == "__main__":
    main()

