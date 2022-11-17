import unittest
from gtts import gTTS
import requests
from bs4 import BeautifulSoup
import os
import time


class TestTextToSpeech(unittest.TestCase):
    def test_text_to_speech_from_text(self):
        print('test_text_to_speech')

        text = """

        """

        title = text[:50] \
                    .replace(":", "") \
                    .replace("✎", "") \
                    .replace("", "") \
                    .replace("", "") \
                    .replace("", "") \
                    .replace(" ", "") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace(".", "") \
                    .replace("-", "") \
                    .replace("¶", "") \
                    .replace("", "") \
                    .replace("~", "") \
                    .replace("*", "") \
                    .lower() + ".mp3"

        tts = gTTS(text.replace("", "")
                   .replace("✎", "")
                   .replace(".", "")
                   .replace("_", "")
                   .replace("©", "")
                   .replace("*", "")
                   .replace("-", " ")
                   .replace("✔", "")
                   .replace("•", "")
                   .replace("⇒", "")
                   .replace("¶", "")
                   .replace("↑", "")
                   .replace("/", "")
                   .replace("+", "")
                   .replace("🎉", "")
                   .replace("", "")
                   .replace("", "")
                   .replace("→", "")
                   .replace("~", ""))  # , lang='fr')

        tts.save(title)

    def test_text_url_body(self):
        print('test_text_url_body')

        url_result = "https://sawtooth.hyperledger.org/docs/core/releases/latest/introduction.html"

        html = requests.get(url_result)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        body = ""

        if soup.find("body") is not None:
            body += soup.find("body").text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')\
                .replace('¶', '').replace('©', '')
            print(body)
        else:
            print("no body")

    def test_text_to_speech_from_url_body(self):
        print('test_text_to_speech_from_url')

        url_result = ""

        html = requests.get(url_result)

        time.sleep(3)

        soup = BeautifulSoup(html.content, 'html.parser')

        body = ""

        if soup.find("body") is not None:
            body += soup.find("body").text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')\
                .replace('¶', '').replace('©', '')
            print(body)
        else:
            print("no body")

        title = body[:50] \
                    .replace(":", "") \
                    .replace("✎", "") \
                    .replace("", "") \
                    .replace("", "") \
                    .replace("", "") \
                    .replace(" ", "") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace(".", "") \
                    .replace("-", "") \
                    .replace("¶", "") \
                    .replace("", "") \
                    .replace("~", "") \
                    .replace("*", "") \
                    .lower() + ".mp3"

        tts = gTTS(body.replace("", "")
                   .replace("✎", "")
                   .replace(".", "")
                   .replace("_", "")
                   .replace("©", "")
                   .replace("*", "")
                   .replace("-", " ")
                   .replace("✔", "")
                   .replace("•", "")
                   .replace("⇒", "")
                   .replace("¶", "")
                   .replace("↑", "")
                   .replace("/", "")
                   .replace("+", "")
                   .replace("🎉", "")
                   .replace("", "")
                   .replace("", "")
                   .replace("→", "")
                   .replace("~", ""))  # , lang='fr')

        tts.save(title)

    def test_text_to_speech_from_urls_body(self):
        print('test_text_to_speech_from_urls_body')

        urls_body = [
            {
                "title": "1",
                "url": "https://sawtooth.hyperledger.org/docs/core/releases/latest/introduction.html"
            }
        ]

        for url_body in urls_body:
            html = requests.get(url_body.get("url"))

            time.sleep(3)

            soup = BeautifulSoup(html.content, 'html.parser')

            body = ""

            if soup.find("body") is not None:
                body += soup.find("body").text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')\
                    .replace('¶', '').replace('©', '')
                print(body)
            else:
                print("no body")

            title = url_body.get("title") + "_" + body[:50] \
                        .replace(":", "") \
                        .replace("✎", "") \
                        .replace("", "") \
                        .replace("", "") \
                        .replace("", "") \
                        .replace(" ", "") \
                        .replace("\n", "") \
                        .replace("?", "") \
                        .replace("/", "") \
                        .replace(".", "") \
                        .replace("-", "") \
                        .replace("¶", "") \
                        .replace("", "") \
                        .replace("~", "") \
                        .replace("*", "") \
                        .lower() + ".mp3"

            tts = gTTS(body.replace("", "")
                       .replace("✎", "")
                       .replace(".", "")
                       .replace("_", "")
                       .replace("©", "")
                       .replace("*", "")
                       .replace("-", " ")
                       .replace("✔", "")
                       .replace("•", "")
                       .replace("⇒", "")
                       .replace("¶", "")
                       .replace("↑", "")
                       .replace("/", "")
                       .replace("+", "")
                       .replace("🎉", "")
                       .replace("", "")
                       .replace("", "")
                       .replace("→", "")
                       .replace("~", ""))  # , lang='fr')

            tts.save(title)

    def test_convert_one_article_from_legifrance_into_a_speech(self):
        url_article = "https://www.legifrance.gouv.fr/affichCodeArticle.do;jsessionid=4B6A5BAC05E3FF5BA785867C5C1683E4.tplgfr26s_1?idArticle=LEGIARTI000006302200&cidTexte=LEGITEXT000006069577&dateTexte=20200405"

        # Request the content of a page from the url
        html = requests.get(url_article)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        text_to_speech = ""

        try:
            if soup.find("div", {"class": "titreArt"}) is not None:
                if soup.find("div", {"class": "histoArt"}) is not None:
                    if soup.find("div", {"class": "corpsArt"}) is not None:
                        text_to_speech += soup.find("div", {"class": "titreArt"}).text + " " \
                               + soup.find("div", {"class": "histoArt"}).text + " " \
                               + soup.find("div", {"class": "corpsArt"}).text
                else:
                    if soup.find("div", {"class": "corpsArt"}) is not None:
                        text_to_speech += soup.find("div", {"class": "titreArt"}).text + " " \
                               + soup.find("div", {"class": "corpsArt"}).text

            title = soup.find("div", {"class": "titreArt"}).text.replace(":", "_").replace(" ", "_") \
                        .replace("\n", "") \
                        .replace("?", "") \
                        .replace("/", "") \
                        .replace("-", "_") + '.mp3'

            tts = gTTS(text_to_speech.replace("", "")
                       .replace(".", "")
                       .replace("©", "")
                       .replace("*", "")
                       .replace("-", " ")
                       .replace("✔", "")
                       .replace("•", "")
                       .replace("⇒", "")
                       .replace("↑", "")
                       .replace("→", ""), lang='fr')

            tts.save(title)

        except Exception as e:
            print(str(e))

    def test_convert_each_article_of_one_block_of_article_of_one_code_in_force_from_legifrance_into_speech(self):
        url_block_of_article = "https://www.legifrance.gouv.fr/affichCode.do;jsessionid=1B4F2114E957C40B95C2EC654F63E084.tplgfr35s_3?idSectionTA=LEGISCTA000006117610&cidTexte=LEGITEXT000006070721&dateTexte=20200315"

        # Request the content of a page from the url
        html_block_of_article = requests.get(url_block_of_article)

        # Parse the content of html
        soup_block_of_article = BeautifulSoup(html_block_of_article.content, 'html.parser')

        if soup_block_of_article.find("div", {"class": "titreArt"}) is not None:
            all_titre_art = soup_block_of_article.find_all("div", {"class": "titreArt"})

            for titreArt in all_titre_art:
                print("https://www.legifrance.gouv.fr/" + titreArt.find("a").get('href'))

                url_article = "https://www.legifrance.gouv.fr/" + titreArt.find("a").get('href')

                # Request the content of a page from the url
                html_article = requests.get(url_article)

                # Parse the content of html
                soup_article = BeautifulSoup(html_article.content, 'html.parser')

                text_to_speech = ""

                try:
                    if soup_article.find("div", {"class": "titreArt"}) is not None:
                        if soup_article.find("div", {"class": "histoArt"}) is not None:
                            if soup_article.find("div", {"class": "corpsArt"}) is not None:
                                text_to_speech += soup_article.find("div", {"class": "titreArt"}).text + " " \
                                                  + soup_article.find("div", {"class": "histoArt"}).text + " " \
                                                  + soup_article.find("div", {"class": "corpsArt"}).text
                        else:
                            if soup_article.find("div", {"class": "corpsArt"}) is not None:
                                text_to_speech += soup_article.find("div", {"class": "titreArt"}).text + " " \
                                                  + soup_article.find("div", {"class": "corpsArt"}).text

                    title = soup_article.find("div", {"class": "titreArt"}).text.replace(":", "_").replace(" ", "_") \
                                .replace("\n", "") \
                                .replace("?", "") \
                                .replace("/", "") \
                                .replace("-", "_") + '.mp3'

                    tts = gTTS(text_to_speech.replace("", "")
                               .replace(".", "")
                               .replace("©", "")
                               .replace("*", "")
                               .replace("-", " ")
                               .replace("✔", "")
                               .replace("•", "")
                               .replace("⇒", "")
                               .replace("↑", "")
                               .replace("→", ""), lang='fr')

                    tts.save(title)

                except:
                    print('problem')

    def test_convert_one_code_in_force_from_legifrance_into_speech_folder(self):
        url_summary = "https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000006075116&dateTexte=20200315"

        # Request the content of a page from the url
        html_summary = requests.get(url_summary)

        # Parse the content of html
        soup_summary = BeautifulSoup(html_summary.content, 'html.parser')

        new_directory = ""

        if soup_summary.find(id="breadcrumb") is not None:
            titre = soup_summary.find(id="breadcrumb") \
                .find("strong") \
                .text \
                .replace(" ", "") \
                .replace("'", "") \
                .replace("\t", "")

            # detect the current working directory
            getcwd = os.getcwd()

            new_directory += getcwd + "\\" + titre[:len(titre)-5]

            try:
                os.mkdir(new_directory)
            except OSError:
                print("Creation of the directory %s failed" % new_directory)
            else:
                print("Successfully created the directory %s " % new_directory)

        else:
            # detect the current working directory
            getcwd = os.getcwd()

            new_directory += getcwd + "\\textes_de_lois"

            try:
                os.mkdir(new_directory)
            except OSError:
                print("Creation of the directory %s failed" % new_directory)
            else:
                print("Successfully created the directory %s " % new_directory)

        if soup_summary.find("span", {"class": "codeLienArt"}) is not None:
            all_code_lien_art = soup_summary.find_all("span", {"class": "codeLienArt"})

            for code_lien_art in all_code_lien_art:
                url_block_of_article = "https://www.legifrance.gouv.fr/" + code_lien_art.find("a").get('href')

                # Request the content of a page from the url
                html_block_of_article = requests.get(url_block_of_article)

                # Parse the content of html
                soup_block_of_article = BeautifulSoup(html_block_of_article.content, 'html.parser')

                if soup_block_of_article.find("div", {"class": "titreArt"}) is not None:
                    all_titre_art = soup_block_of_article.find_all("div", {"class": "titreArt"})

                    for titre_art in all_titre_art:
                        print("https://www.legifrance.gouv.fr/" + titre_art.find("a").get('href'))

                        url_article = "https://www.legifrance.gouv.fr/" + titre_art.find("a").get('href')

                        # Request the content of a page from the url
                        html_article = requests.get(url_article)

                        # Parse the content of html
                        soup_article = BeautifulSoup(html_article.content, 'html.parser')

                        text_to_speech = ""

                        try:
                            if soup_article.find("div", {"class": "titreArt"}) is not None:
                                if soup_article.find("div", {"class": "histoArt"}) is not None:
                                    if soup_article.find("div", {"class": "corpsArt"}) is not None:
                                        text_to_speech += soup_article.find("div", {"class": "titreArt"}).text + " " \
                                                          + soup_article.find("div", {"class": "histoArt"}).text + " " \
                                                          + soup_article.find("div", {"class": "corpsArt"}).text
                                else:
                                    if soup_article.find("div", {"class": "corpsArt"}) is not None:
                                        text_to_speech += soup_article.find("div", {"class": "titreArt"}).text + " " \
                                                          + soup_article.find("div", {"class": "corpsArt"}).text

                            print(soup_article.find("div", {"class": "titreArt"}).text)

                            title = new_directory + "\\" + soup_article.find("div", {"class": "titreArt"}).text\
                                        .replace(":", "_").replace(" ", "_") \
                                        .replace("\n", "") \
                                        .replace("?", "") \
                                        .replace("/", "") \
                                        .replace("-", "_") + '.mp3'

                            tts = gTTS(text_to_speech.replace("", "")
                                       .replace(".", "")
                                       .replace("©", "")
                                       .replace("*", "")
                                       .replace("-", " ")
                                       .replace("✔", "")
                                       .replace("•", "")
                                       .replace("⇒", "")
                                       .replace("↑", "")
                                       .replace("→", ""), lang='fr')

                            tts.save(title)

                        except:
                            print('problem')

    def test_print_current_directory(self):
        path = os.getcwd()
        print(path)

    def test_create_one_directory_into_the_current_directory(self):
        getcwd = os.getcwd()

        new_directory = getcwd + "\\" + "Jason"

        try:
            if not os.path.exists(getcwd + "\\" + "Jason"):
                os.mkdir(new_directory)

            else:
                print("the directory already exists.")

        except OSError:
            print("Creation of the directory %s failed" % new_directory)
        else:
            print("Successfully created the directory %s " % new_directory)

    def test_text_to_speech_from_urls(self):
        print("test_text_to_speech_from_urls")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        urls = [
            "https://net-entreprises.custhelp.com/app/answers/detail_nete/a_id/1487/p/348/session/L3RpbWUvMTU5MTQ2NTUxNi9zaWQvZlViUVZncEJ5UWRiU0U0a0w0VnpLdnQ3WDhrMkRoUGY2dmQzeUZTYVZLOVFieEZhQWdvcHZRWFhjclRSaHZpdmxGV2dvb3dtNWMwckFFQTdSM0xkbG1MTW9NdiU3RVN2TThEa01nbDdDdFVkdERGZ1lZNHJrNzZBVHclMjElMjE="
        ]

        for url in urls:
            time.sleep(3)

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            # title of the movie
            title = ""

            # To adapt
            if soup.find("div", {'class': 'title'}) is not None:
                title += str(soup.find("div", {'class': 'title'})
                             .find('span')
                             .text[:30]
                             .lower()
                             .replace(" ", "")
                             .replace("/", "")
                             .replace("-", "")
                             .replace(":", "")
                             .replace("\n", "")
                             .replace("?", "")
                             .replace('ã', '')
                             .replace('©', '')
                             .replace(":", "")
                             ) + '.mp3'

            text = ""

            # To adapt
            if soup.select_one("#rn_Container") is not None:
                text += str(soup.select_one("#rn_Container").text)

                tts = gTTS(text.replace("", "")
                           .replace(".", "")
                           .replace("©", "")
                           .replace("*", "")
                           .replace("-", " ")
                           .replace("✔", "")
                           .replace("•", "")
                           .replace("⇒", "")
                           .replace("↑", "")
                           .replace("→", ""), lang='fr')

                tts.save(title)
            else:
                print('no content')

    def test_count_the_number_of_caracters(self):
        print("test_count_the_number_of_caracters")

        count = 0

        my_string = """
        
        """

        for i in my_string:
            count += 1

        print(count)


if __name__ == '__main__':
    unittest.main()
