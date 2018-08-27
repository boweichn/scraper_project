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
            <div style="width: 90vw; height: 15vh; color: red; text-align: center;">
                <h1>Daily Updates</h1>
            </div>
            <div style="width: 90vw; text-align: center;">
                <div style="float: left; width: 45vw; text-align: center;"> 
                    <p>%s</p>
                </div>

                <div style="float: left; width: 45vw; text-align: center;">
                    <p>%s</p>
                </div>
            <div>
        </body>
    </html>"""

    content = wrapper %(''.join(anime_list), ''.join(manga_list))

    # print('\n'.join(anime_list))
    # print('\n')
    # print('\n'.join(manga_list))

    file.write(content)
    file.close()

    # opens the new html file after script execution
    webbrowser.open('file://' + os.path.realpath('daily.html'))

if __name__ == "__main__":
    main()