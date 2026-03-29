def add_score(name, score):
    try:
        with open("scores.txt", "a") as f:
            f.write(f"{name}: {score}\n")
        print(f"Added -> {name}: {score}")
    except Exception as e:
        print(f"Error while writing: {e}")


def read_scores():
    try:
        with open("scores.txt", "r") as f:
            content = f.read()
            if content.strip() == "":
                print("No scores recorded yet.")
            else:
                print(content.strip())
    except FileNotFoundError:
        print("No scores file found yet.")


def find_student(name):
    try:
        with open("scores.txt", "r") as f:
            found = False
            for line in f:
                # strict match instead of lazy 'if name in line'
                student, score = line.strip().split(": ")
                if student.lower() == name.lower():
                    print(f"{student}: {score}")
                    found = True
                    break

            if not found:
                print("Student not found")

    except FileNotFoundError:
        print("No scores file found yet.")


# ---- Test ----
add_score('Rahul', 90)
add_score('Anita', 85)
add_score('John', 72)

print("\n--- All Scores ---")
read_scores()

print("\n--- Search ---")
find_student('Anita')
find_student('Sara')