from manga_scrape import manga_parser
from anime_scrape import anime_parser
import webbrowser, os

def main ():
    anime_list = anime_parser()
    manga_list = manga_parser()

    # writes the 2 lists into an html file
    file = open('daily.html', encoding='utf-8', mode='w')

    wrapper = """<html>
    <head></head>
        <body>
            <div style="display: table;">
                <div>
                    <p>%s</p>
                </div>

                <div>
                    <p>%s</p>
                </div>
            <div>
        </body>
    </html>"""

    content = wrapper %(''.join(anime_list), '<br>'.join(manga_list))

    # print('\n'.join(anime_list))
    # print('\n')
    # print('\n'.join(manga_list))

    file.write(content)
    file.close()

    # opens the new html file after script execution
    webbrowser.open('file://' + os.path.realpath('daily.html'))

if __name__ == "__main__":
    main()