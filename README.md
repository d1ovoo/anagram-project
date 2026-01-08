# Real-Time Anagram Generator with Dictionary API
A fun little Python project I built that plays with words and coding.

It takes any word you give it, finds all the possible anagrams, filters out the ones that aren’t real English words using the Dictionary API, and even lets you look up definitions interactively.

What It Does

Checks your input to make sure it’s only letters (and up to 8 characters)

Shows how many theoretical anagrams your word could have

Lists all the valid English anagrams

Lets you pick an anagram and see its definition

It’s a small project, but a great way to explore Python, combinatorics, and APIs—all while having a bit of word-game fun.

How to Use It

Make sure you have Python 3 installed.

Install the required library:

pip install requests

Run the script:

python anagram_generator.py

Follow the prompts:

Enter a word

See all valid anagrams

Optionally, look up definitions

Example

Enter a word up to 8 characters: moon
There are 2 real anagrams of said word which are: mono, moon

Do you want to know what any of these words mean? (y/n): y
Definitions for 'mono':

(noun) mononucleosis, an infectious disease

Why I Built This

I wanted a project that was small but fun, combining Python, APIs, and language. It’s a neat way to practice coding while exploring words—and it turned out to be a lot of fun!

License

This project is open-source and available under the MIT License.
