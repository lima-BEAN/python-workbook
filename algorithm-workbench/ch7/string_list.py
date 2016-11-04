# Write a statement that creates a list with the following strings:
# 'Einstein', 'Newton', 'Copernicus', and 'Kepler'

def main():
    count = 0
    greats = ['Tesla', 'Einstein', 'Newton', 'Copernicus', 'Kepler']
    for great in greats:
        count += 1
        print(str(count) + ': ' + great)

main()
