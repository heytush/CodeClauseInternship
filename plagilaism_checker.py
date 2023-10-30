import difflib

def check_plagiarism(text1, text2):
    # Split the text into lines for comparison
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    # Initialize the Differ class from difflib
    d = difflib.Differ()

    # Compare the two texts and compute the difference
    diff = list(d.compare(lines1, lines2))

    # Calculate the similarity score (percentage of common lines)
    common_lines = sum(1 for line in diff if line[0] == ' ')
    total_lines = max(len(lines1), len(lines2))
    similarity = common_lines / total_lines * 100

    return similarity

if __name__ == "__main__":
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    similarity = check_plagiarism(text1, text2)

    print(f"Similarity Score: {similarity:.2f}%")
