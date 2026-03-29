def save_entry(entry):
    # append entry to file (does NOT overwrite old data)
    with open("diary.txt", "a") as f:
        f.write(entry + "\n")   # newline is mandatory

def show_all_entries():
    try:
        with open("diary.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No entries yet.")

# Main program
new_entry = input('Write your diary entry: ')
save_entry(new_entry)

print('\n--- All Diary Entries ---')
show_all_entries()