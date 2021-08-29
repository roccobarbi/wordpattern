from dictionaries import dictionary
import sys


class KnownLetter:
    def __init__(self, letter, position):
        self.letter = letter
        self.position = position

    def is_here(self, word):
        if len(word) >= self.position + 1 and word[self.position] == self.letter:
            return True
        return False


def parse_arguments(arguments):
    configuration = {
        "language": ""
    }
    return configuration


def generate_pattern(pattern, config, wordlist):
    # translate
    return ""


def lookup_pattern(pattern, config, wordlist):
    # translate
    pass


def main():
    arguments = sys.argv[1:]
    config = parse_arguments(arguments)
    wordlist = dictionary.get_dictionary(config["language"])
    if wordlist is None:
        sys.exit(1)
    pattern = generate_pattern(config)  # Generate a pattern in the right format
    return lookup_pattern(pattern, config, wordlist)


if __name__ == "__main__":
    main()
