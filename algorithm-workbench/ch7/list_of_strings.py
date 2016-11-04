# Assume the names variable references a list of strings. Write code that
# determines whether 'Ruby' is in the names list. If it is,
# display the message 'Hello, Ruby'. Otherwise, display 'No Ruby'

def main():
    languages = ['Ruby', 'Swift', 'Python', 'C#', 'C++']
    Find(languages)

def Find(languages):
    for language in languages:
        if language.title() == 'Ruby':
            print('Awesome, Get Ready To Ride The Rails, Mr.', language)
        elif language.title() == 'Python':
            print('Clean and lethal, Mr.', language)
        elif language.title() == 'Swift':
            print('Moveover Droid, Mr.', language, 'is here.')

main()
