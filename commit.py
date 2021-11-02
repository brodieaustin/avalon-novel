import os
from datetime import datetime

def main():

    today = datetime.today().strftime('%m/%d/%Y')

    commands = [
        'git add index.markdown',
        'git commit -m "progress for {}. {} words."',
        'git push origin gh-pages'
    ]

    fh = open('./index.markdown', 'r')
    content = fh.read()
    fh.close()

    words = content.split()
    wc = len(words)

    print(wc)

    for c in commands:
        if '{}' in c:
            c = c.format(today, wc)

        os.system(c)

if __name__ == '__main__':
    main()
