import re

def count_frequency(text, n):
    """
    Counts the frequency of words in the given text, removing punctuation and non-alphabetic characters.
    Writes the top n most common words to "word_count_report.txt" and prints them.

    Args:
        text (str): The input text to analyze.
        n (int): The number of most common words to print.

    Returns:
        None

    """
    words = text.split()  # Automatically handles multiple spaces/newlines
    word_count = {}

    for word in words:
        cleaned_word = re.sub(r'[^a-zA-Z]', '', word).lower()  # Remove non-alphabetic chars
        if cleaned_word:  # Ignore empty strings after cleaning
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    total_words = sum(word_count.values())

    # Sort words by frequency (descending), then alphabetically (ascending)
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    # Save to file and print report
    with open("word_count_report.txt", "w") as f:
        report = f"Word Count Report\nTotal words: {total_words}\n"
        report += f"Top {n} words:\n" + "\n".join(f"{word} - {count} times" for word, count in sorted_words[:n])

        f.write(report)  # Write report to file
        print(report)  # Print report


def get_input(file_path="sample.txt"):
    """
    Reads text from a file if it exists. If the file is missing, prompts the user
    to enter text manually and saves it to the file.

    Args:
        file_path (str): The file path to read/write. Default is "sample.txt".

    Returns:
        str: The retrieved or user-inputted text.
    """
    try:
        with open(file_path, "r") as file:
            return file.read().strip()  # Read and remove extra spaces/newlines
    except FileNotFoundError:
        print("Enter multiple lines (Press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if not line:  # Stop on empty input
                break
            lines.append(line)

        content = "\n".join(lines)
        with open(file_path, "w") as file:
            file.write(content)
        return content


if __name__ == '__main__':
    content = get_input()
    if content: # Only process if content exists
        num = 5
        try:
            num = int(input("'top common words' to display (e.g., top 3, top 10, etc.)  "))
        except ValueError:
            print("Invalid number. Displaying info with default 5 words...")
        if num <= 0:
            print("Invalid number. Displaying info with default 5 words...")
            num = 5
        count_frequency(content, num)
