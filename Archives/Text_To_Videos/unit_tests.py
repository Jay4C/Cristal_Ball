import os
import unittest
import time
from PIL import Image, ImageDraw
from gtts import gTTS
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio
from bs4 import BeautifulSoup
import requests
import cv2
from mutagen.mp3 import MP3
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class UnitTestsTextToVideos(unittest.TestCase):
    def test_create_video_from_one_existing_image_and_one_existing_audio(self):
        image_folder = os.getcwd() + '\\images'
        audio_file = os.getcwd() + '\\Article_4_A.mp3'
        video_name = 'movie_1.avi'
        output_movie = "movie_and_audio.avi"

        os.chdir(os.getcwd())

        images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

        frame = cv2.imread(os.path.join(image_folder, images[0]))

        # setting the frame width, height width the width, height of first image
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, 0, 1, (width, height))

        # Appending the images to the video one by one
        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        # Deallocating memories taken for window creation
        cv2.destroyAllWindows()

        # releasing the video generated
        video.release()

        try:
            ffmpeg_merge_video_audio(video_name, audio_file, output_movie, vcodec='copy', acodec='copy', ffmpeg_output=False, logger='bar')
        except Exception as e:
            print(str(e))

    def test_create_video_from_one_text(self):
        # Text to speech and images
        text = '''
Article 223 A En savoir plus sur cet article...
Modifié par LOI n°2015-990 du 6 août 2015 - art. 135 (V)

I. – Une société, ci-après désignée par les mots : " société mère ", peut se constituer seule redevable de l'impôt sur les sociétés dû sur l'ensemble des résultats du groupe formé par elle-même et les sociétés dont elle détient 95 % au moins du capital de manière continue au cours de l'exercice, directement ou indirectement par l'intermédiaire de sociétés ou d'établissements stables membres du groupe, ci-après désignés par les mots : " sociétés du groupe ", ou de sociétés ou d'établissements stables, ci-après désignés par les mots : " sociétés intermédiaires ", détenus à 95 % au moins par la société mère de manière continue au cours de l'exercice, directement ou indirectement par l'intermédiaire de sociétés du groupe ou de sociétés intermédiaires.

Une société, également désignée par les mots : " société mère ", dont le capital est détenu, de manière continue au cours de l'exercice, à 95 % au moins par une société ou un établissement stable soumis à un impôt équivalent à l'impôt sur les sociétés dans un Etat membre de l'Union européenne ou dans un autre Etat partie à l'accord sur l'Espace économique européen ayant conclu avec la France une convention d'assistance administrative en vue de lutter contre la fraude et l'évasion fiscales, ci-après désigné par les mots : " entité mère non résidente ", directement ou indirectement par l'intermédiaire de sociétés ou d'établissements stables détenus à 95 % au moins par l'entité mère non résidente et soumis à un impôt équivalent à l'impôt sur les sociétés dans les mêmes Etats, ci-après désignés par les mots : " sociétés étrangères ", peut aussi se constituer seule redevable de l'impôt sur les sociétés dû sur l'ensemble des résultats du groupe formé par elle-même et les sociétés détenues par l'entité mère non résidente dans les conditions prévues au premier alinéa du présent I, directement ou indirectement par l'intermédiaire de la société mère, de sociétés étrangères, de sociétés intermédiaires ou de sociétés membres du groupe.

Le capital de la société mère mentionnée au même premier alinéa ne doit pas être détenu à 95 % au moins, directement ou indirectement, par une autre personne morale soumise à l'impôt sur les sociétés dans les conditions de droit commun ou selon les modalités prévues à l'article 214. Le capital de l'entité mère non résidente ne doit pas être détenu à 95 % au moins, directement ou indirectement, par une autre personne morale soumise à l'impôt sur les sociétés dans les conditions de droit commun ou selon les modalités prévues au même article 214 ou par une autre personne morale soumise à un impôt équivalent à l'impôt sur les sociétés dans un Etat mentionné au deuxième alinéa du présent I. Le capital de la société mère mentionnée au même deuxième alinéa ne doit pas être détenu indirectement par l'entité mère non résidente par l'intermédiaire de sociétés ou d'établissements stables qui peuvent eux-mêmes se constituer seuls redevables de l'impôt sur les sociétés dans les conditions décrites audit deuxième alinéa. Toutefois, le capital de la société mère mentionnée au premier alinéa du présent I peut être détenu indirectement à 95 % ou plus par une autre personne morale soumise à l'impôt sur les sociétés dans les conditions de droit commun ou selon les modalités prévues à l'article 214, par l'intermédiaire d'une ou plusieurs personnes morales non soumises à cet impôt dans ces mêmes conditions ou par l'intermédiaire d'une ou plusieurs personnes morales qui y sont soumises dans ces mêmes conditions et dont le capital n'est pas détenu, directement ou indirectement, par cette autre personne morale à 95 % au moins. Le capital de l'entité mère non résidente peut être détenu indirectement à 95 % ou plus par une autre personne morale soumise à un impôt équivalent à l'impôt sur les sociétés dans un Etat mentionné au deuxième alinéa du présent I ou par une autre personne morale soumise à l'impôt sur les sociétés dans les conditions de droit commun ou selon les modalités prévues à l'article 214, par l'intermédiaire d'une ou plusieurs personnes morales qui ne sont soumises ni à cet impôt dans ces mêmes conditions, ni à un impôt équivalent dans un Etat mentionné au deuxième alinéa du présent I, ou par l'intermédiaire d'une ou plusieurs personnes morales qui y sont soumises dans ces mêmes conditions et dont le capital n'est pas détenu, directement ou indirectement, par cette autre personne morale à 95 % au moins.
        '''

        # Filename for audio
        audio_file = os.getcwd() + "\\audio\\" + text[:50]\
            .replace(":", "")\
            .replace(" ", "")\
            .replace("\n", "")\
            .replace("?", "")\
            .replace("/", "")\
            .replace("-", "") + '.mp3'

        # Convert text to audio
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

        # Save the audio
        tts.save(audio_file)

        # Duration of audio file in seconds
        duration_of_audio_file = round(MP3(audio_file).info.length)

        # Folder of images
        image_folder = os.getcwd() + '\\images'

        # Create images from the text
        number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
        number_of_caracters_per_line = 110

        number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
        number_of_lines = 0

        if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
            number_of_lines += round(number_of_lines_with_coma) + 1

        elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
            number_of_lines += round(number_of_lines_with_coma)

        number_of_lines_per_image = 10

        number_of_images_with_coma = number_of_lines / number_of_lines_per_image
        number_of_images = 0

        if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
            number_of_images += round(number_of_images_with_coma) + 1

        elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
            number_of_images += round(number_of_images_with_coma)

        l = 0

        for i in range(1, number_of_images + 1):
            img = Image.new('RGB', (700, 300), color=(255, 255, 255))
            d = ImageDraw.Draw(img)

            if l <= number_of_lines:
                for j in range(0, 10):
                    depart = 110 * l
                    arrivee = 110 + 110 * l
                    coordinate_y = 25 * j

                    if j < 9:
                        d.text((10, coordinate_y), text[depart:arrivee]
                               .replace('\t', ' ')
                               .replace('\n', ' ')
                               .replace(u"\u2018", "'")
                               .replace(u"\u2019", "'")
                               .replace(u"\u0153", "oe")
                               .replace(u"\u2013", "-")
                               , fill=(0, 0, 0))
                        l += 1

                    elif j == 9:
                        d.text((10, coordinate_y), text[depart:arrivee]
                               .replace('\t', ' ')
                               .replace('\n', ' ')
                               .replace(u"\u2018", "'")
                               .replace(u"\u2019", "'")
                               .replace(u"\u0153", "oe")
                               .replace(u"\u2013", "-")
                               , fill=(0, 0, 0))

                        l += 1

                        img.save(image_folder + "\\" + str(i) + ".png")

        os.chdir(os.getcwd())

        # Duration of each clip into the concatenation in seconds
        duration_of_each_clip = round(int(duration_of_audio_file/number_of_images)) + 5

        # Appending the images to the video one by one
        images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

        for i in range(1, number_of_images+1):
            frame = cv2.imread(os.path.join(image_folder, images[0]))

            # setting the frame width, height width the width, height of first image
            height, width, layers = frame.shape

            # video to create
            video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0, 1, (width, height))

            for j in range(duration_of_each_clip+12):
                video.write(cv2.imread(os.path.join(image_folder, image_folder + "\\" + str(i) + ".png")))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()

            # releasing the video generated
            video.release()

        # Delete all images
        for i in range(1, number_of_images + 1):
            os.remove(image_folder + "\\" + str(i) + ".png")

        clips = []

        for i in range(1, number_of_images+1):
            clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                         .set_start((duration_of_each_clip+12)*(i-1))
                         )

        CompositeVideoClip(clips).write_videofile(os.getcwd() + '\\videos\\my_concatenation.mp4')

        # Delete all clips
        for i in range(1, number_of_images + 1):
            os.remove(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')

        try:
            output_movie = os.getcwd() + "\\videos\\movie.avi"
            ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie, vcodec='copy', acodec='copy',
                                     ffmpeg_output=False, logger='bar')
            os.remove(os.getcwd() + '\\videos\\my_concatenation.mp4')
            os.remove(audio_file)
        except Exception as e:
            print("output movie exception : " + str(e))

    def test_get_duration_mp3_file(self):
        # Text to speech and images
        text = '''
La loi répute pareillement actes de commerce :

1° Toute entreprise de construction, et tous achats, ventes et reventes de bâtiments pour la navigation intérieure et extérieure ;

2° Toutes expéditions maritimes ;

3° Tout achat et vente d'agrès, apparaux et avitaillements ;

4° Tout affrètement ou nolisement, emprunt ou prêt à la grosse ;

5° Toutes assurances et autres contrats concernant le commerce de mer ;

6° Tous accords et conventions pour salaires et loyers d'équipages ;

7° Tous engagements de gens de mer pour le service de bâtiments de commerce.
        '''

        # Filename for audio
        audio_file = os.getcwd() + "\\audio\\" + text[:50] \
            .replace(":", "") \
            .replace(" ", "") \
            .replace("\n", "") \
            .replace("?", "") \
            .replace("/", "") \
            .replace("-", "") + '.mp3'

        # Convert text to audio
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

        # Save the audio
        tts.save(audio_file)

        # Display the duration of the mp3 file
        print("duration of audio file in seconds : " + str(MP3(audio_file).info.length))

        # Delete the mp3 file
        os.remove(audio_file)

    def test_create_video_from_one_article_of_code_in_force_from_legifrance(self):
        try:
            langue = 'fr'

            url_article = "https://www.legifrance.gouv.fr/affichCodeArticle.do;jsessionid=406511057CA1B390F2BB6AD364243707.tplgfr33s_2?idArticle=LEGIARTI000038610041&cidTexte=LEGITEXT000005634379&dateTexte=20200409"

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

                audio_file = os.getcwd() + "\\audio\\" + soup \
                    .find("div", {"class": "titreArt"}) \
                    .text.replace(":", "_") \
                    .replace(" ", "_") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "_") + '.mp3'

                movie_file = os.getcwd() + "\\videos_creees\\" + soup \
                    .find("div", {"class": "titreArt"}) \
                    .text.replace(":", "_") \
                    .replace(" ", "_") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "_") + '.avi'

                try:
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

                    tts.save(audio_file)
                except Exception as e:
                    print("error audio file : " + str(e))

                # Folder of images
                image_folder = os.getcwd() + '\\images'

                # Create images from the text
                number_of_caracters_of_text = len(text_to_speech.replace('\t', ' ').replace('\n', ' '))
                number_of_caracters_per_line = 110

                number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                number_of_lines = 0

                if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                    number_of_lines += round(number_of_lines_with_coma) + 1

                elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                    number_of_lines += round(number_of_lines_with_coma)

                number_of_lines_per_image = 10

                number_of_images_with_coma = number_of_lines / number_of_lines_per_image
                number_of_images = 0

                if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                    number_of_images += round(number_of_images_with_coma) + 1

                elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                    number_of_images += round(number_of_images_with_coma)

                # Array duration of each clip
                durations_of_each_clip = [0]

                l = 0

                duration = 0

                for i in range(1, number_of_images + 1):
                    img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                    d = ImageDraw.Draw(img)

                    if l <= number_of_lines:
                        for j in range(0, 10):
                            depart = 110 * l
                            arrivee = 110 + 110 * l
                            coordinate_y = 25 * j

                            if j < 9:
                                d.text((10, coordinate_y), text_to_speech[depart:arrivee]
                                       .replace('\t', ' ')
                                       .replace('\n', ' ')
                                       .replace(u"\u2018", "'")
                                       .replace(u"\u2019", "'")
                                       .replace(u"\u0153", "oe")
                                       .replace(u"\u2013", "-")
                                       , fill=(0, 0, 0))

                                if text_to_speech[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text_to_speech[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", "'")
                                                   .replace(u"\u2019", "'")
                                                   .replace(u"\u0153", "oe")
                                                   .replace(u"\u2013", "-")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""), lang=langue)

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = " + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                            elif j == 9:
                                d.text((10, coordinate_y), text_to_speech[depart:arrivee]
                                       .replace('\t', ' ')
                                       .replace('\n', ' ')
                                       .replace(u"\u2018", "'")
                                       .replace(u"\u2019", "'")
                                       .replace(u"\u0153", "oe")
                                       .replace(u"\u2013", "-")
                                       , fill=(0, 0, 0))

                                if text_to_speech[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text_to_speech[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", "'")
                                                   .replace(u"\u2019", "'")
                                                   .replace(u"\u0153", "oe")
                                                   .replace(u"\u2013", "-")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""), lang=langue)

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        img.save(image_folder + "\\" + str(i) + ".png")

                                        durations_of_each_clip.append(duration)

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = " + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                os.chdir(os.getcwd())

                # Appending the images to the video one by one
                images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                for i in range(1, number_of_images + 1):
                    frame = cv2.imread(os.path.join(image_folder, images[0]))

                    # setting the frame width, height width the width, height of first image
                    height, width, layers = frame.shape

                    # video to create
                    video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0, 1, (width, height))

                    try:
                        for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                            video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                    + "\\" + str(i) + ".png")))
                    except Exception as e:
                        print("error video write : " + str(e))

                    # Deallocating memories taken for window creation
                    cv2.destroyAllWindows()

                    # releasing the video generated
                    video.release()

                clips = []

                for i in range(1, number_of_images + 1):
                    clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                 .set_start(durations_of_each_clip[i - 1]))

                CompositeVideoClip(clips).write_videofile(os.getcwd() + '\\videos\\my_concatenation.mp4')

                try:
                    output_movie = movie_file
                    ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie,
                                             vcodec='copy', acodec='copy',
                                             ffmpeg_output=False, logger='bar')

                except Exception as e:
                    print("output movie exception : " + str(e))
            except Exception as e:
                print("error : " + str(e))
        finally:
            try:
                # Delete all audios
                for file in os.listdir(os.getcwd() + '\\audio'):
                    os.remove(os.getcwd() + '\\audio\\' + file)

                # Delete all clips
                for file in os.listdir(os.getcwd() + '\\videos'):
                    os.remove(os.getcwd() + '\\videos\\' + file)

                # Delete all images
                for file in os.listdir(os.getcwd() + '\\images'):
                    os.remove(os.getcwd() + '\\images\\' + file)

                print("done")
            except Exception as e:
                print("error delete all files : " + str(e))

    def test_create_video_from_one_article_of_code_in_force_from_legifrance_with_rpa(self):
        url = "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031210068"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        print('page open')

        time.sleep(20)

        try:
            langue = 'fr'

            text_to_speech = ""

            try:
                text_to_speech += browser.find_element_by_xpath(
                    "/html/body/div[1]/div/main/div/div[2]/div[4]/article"
                ).text \
                    .replace('Versions', '') \
                    .replace('Liens relatifs', '') \
                    .replace('\t', '') \
                    .replace('\r', '') \
                    .replace('\n', '')

                audio_file = os.getcwd() + "\\audio\\" + browser.find_element_by_xpath(
                    "/html/body/div[1]/div/main/div/div[2]/div[4]/article/div/div[1]/h2"
                ).text.replace(":", "_")\
                    .replace(" ", "_") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "_") + '.mp3'

                movie_file = os.getcwd() + "\\videos_creees\\" + browser.find_element_by_xpath(
                    "/html/body/div[1]/div/main/div/div[2]/div[4]/article/div/div[1]/h2"
                ).text.replace(":", "_")\
                    .replace(" ", "_") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "_") + '.avi'

                try:
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

                    tts.save(audio_file)
                except Exception as e:
                    print("error audio file : " + str(e))

                # Folder of images
                image_folder = os.getcwd() + '\\images'

                # Create images from the text
                number_of_caracters_of_text = len(text_to_speech.replace('\t', ' ').replace('\n', ' '))
                number_of_caracters_per_line = 110

                number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                number_of_lines = 0

                if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                    number_of_lines += round(number_of_lines_with_coma) + 1

                elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                    number_of_lines += round(number_of_lines_with_coma)

                number_of_lines_per_image = 10

                number_of_images_with_coma = number_of_lines / number_of_lines_per_image
                number_of_images = 0

                if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                    number_of_images += round(number_of_images_with_coma) + 1

                elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                    number_of_images += round(number_of_images_with_coma)

                # Array duration of each clip
                durations_of_each_clip = [0]

                l = 0

                duration = 0

                for i in range(1, number_of_images + 1):
                    img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                    d = ImageDraw.Draw(img)

                    if l <= number_of_lines:
                        for j in range(0, 10):
                            depart = 110 * l
                            arrivee = 110 + 110 * l
                            coordinate_y = 25 * j

                            if j < 9:
                                d.text((10, coordinate_y), text_to_speech[depart:arrivee]
                                       .replace('\t', ' ')
                                       .replace('\n', ' ')
                                       .replace(u"\u2018", "'")
                                       .replace(u"\u2019", "'")
                                       .replace(u"\u0153", "oe")
                                       .replace(u"\u2013", "-")
                                       , fill=(0, 0, 0))

                                if text_to_speech[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text_to_speech[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", "'")
                                                   .replace(u"\u2019", "'")
                                                   .replace(u"\u0153", "oe")
                                                   .replace(u"\u2013", "-")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""), lang=langue)

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = " + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                            elif j == 9:
                                d.text((10, coordinate_y), text_to_speech[depart:arrivee]
                                       .replace('\t', ' ')
                                       .replace('\n', ' ')
                                       .replace(u"\u2018", "'")
                                       .replace(u"\u2019", "'")
                                       .replace(u"\u0153", "oe")
                                       .replace(u"\u2013", "-")
                                       , fill=(0, 0, 0))

                                if text_to_speech[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text_to_speech[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", "'")
                                                   .replace(u"\u2019", "'")
                                                   .replace(u"\u0153", "oe")
                                                   .replace(u"\u2013", "-")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""), lang=langue)

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        img.save(image_folder + "\\" + str(i) + ".png")

                                        durations_of_each_clip.append(duration)

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = " + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                os.chdir(os.getcwd())

                # Appending the images to the video one by one
                images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                for i in range(1, number_of_images + 1):
                    frame = cv2.imread(os.path.join(image_folder, images[0]))

                    # setting the frame width, height width the width, height of first image
                    height, width, layers = frame.shape

                    # video to create
                    video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0, 1, (width, height))

                    try:
                        for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                            video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                    + "\\" + str(i) + ".png")))
                    except Exception as e:
                        print("error video write : " + str(e))

                    # Deallocating memories taken for window creation
                    cv2.destroyAllWindows()

                    # releasing the video generated
                    video.release()

                clips = []

                for i in range(1, number_of_images + 1):
                    clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                 .set_start(durations_of_each_clip[i - 1]))

                CompositeVideoClip(clips).write_videofile(os.getcwd() + '\\videos\\my_concatenation.mp4')

                try:
                    output_movie = movie_file
                    ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie,
                                             vcodec='copy', acodec='copy',
                                             ffmpeg_output=False, logger='bar')

                except Exception as e:
                    print("output movie exception : " + str(e))
            except Exception as e:
                print("error : " + str(e))

            browser.close()
        finally:
            try:
                # Delete all audios
                for file in os.listdir(os.getcwd() + '\\audio'):
                    os.remove(os.getcwd() + '\\audio\\' + file)

                # Delete all clips
                for file in os.listdir(os.getcwd() + '\\videos'):
                    os.remove(os.getcwd() + '\\videos\\' + file)

                # Delete all images
                for file in os.listdir(os.getcwd() + '\\images'):
                    os.remove(os.getcwd() + '\\images\\' + file)

                print("done")
            except Exception as e:
                print("error delete all files : " + str(e))

    def test_create_videos_from_one_code_in_force_from_legifrance(self):
        print("test_create_videos_from_one_code_in_force_from_legifrance")

        array_articles = []

        langue = 'fr'

        url_summary = "https://www.legifrance.gouv.fr/codes/id/LEGITEXT000006069577/"

        cookie = "visid_incap_1235873=WG9RDolTSuiNQNXcE8MooFoktmAAAAAAQUIPAAAAAAARmf9GTg0TRaqFrptlJZr5; incap_ses_390_1235873=2XttGZmRZihEr13cUI9pBVoktmAAAAAAIrBJvHKdDQnAk54LHOEABg==; tarteaucitron=!id=8f4f5306c163331d-84c37e86-fa28962c-df023d2d719d3a7694d5cb43!atinternet=true!hotjar=false; lf-demo-accueil=1; JSESSIONID=BF88CEC9830C7B6E7915C38B4ABDE973; LB_APP_ROUTE=.5; LB_FRONT_ROUTE=.1.1; nlbi_1235873=ethuMspDsSrgN/PSjJoYvAAAAABUnMkbBwV1TK/wxe67Z+0U"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
            'referer': 'https://www.google.fr/',
            'authority': 'www.legifrance.gouv.fr',
            'method': 'GET',
            'path': url_summary.replace("https://www.legifrance.gouv.fr", ""),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'dnt': '1',
            'if-none-match': '89dfa94b',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

        # Request the content of a page from the url
        html_summary = requests.get(url_summary, headers=headers)

        # Parse the content of html
        soup_summary = BeautifulSoup(html_summary.content, 'html.parser')

        new_directory = ""

        # Create the new directory
        # To adapt for changes
        if soup_summary.find("h1", {'class', 'main-title'}) is not None:
            titre = soup_summary.find("h1", {'class', 'main-title'}) \
                .text \
                .lower() \
                .replace(" ", "") \
                .replace('é', 'e') \
                .replace("'", "") \
                .replace("\t", "")

            # Folder for videos creees
            getcwd = os.getcwd() + "\\videos_creees\\"

            new_directory += getcwd + titre[:len(titre) - 5]

            try:
                if not os.path.exists(new_directory):
                    os.mkdir(new_directory)
            except OSError:
                print("Creation of the directory %s failed" % new_directory)
            else:
                print("The directory has been created %s " % new_directory)
        else:
            # detect the current working directory
            getcwd = os.getcwd() + "\\videos_creees"

            new_directory += getcwd + "\\textes_de_lois"

            try:
                if not os.path.exists(new_directory):
                    os.mkdir(new_directory)
            except OSError:
                print("Creation of the directory %s failed" % new_directory)
            else:
                print("The directory has been created %s " % new_directory)

        # To adapt for changes
        if soup_summary.find('a', {'class': 'articleLink'}) is not None:
            all_code_lien_art = soup_summary.find_all('a', {'class': 'articleLink'})

            for code_lien_art in all_code_lien_art:
                link = "https://www.legifrance.gouv.fr/codes/article_lc/" + code_lien_art.get('id').replace('art', '')
                array_articles.append(link)

            print("length array_articles : " + str(len(array_articles)))

            for x in range(12, len(array_articles)):
                url_article = str(array_articles[x])

                time.sleep(20)

                # Request the content of a page from the url
                html_article = requests.get(url_article, headers=headers)

                # Parse the content of html
                soup_article = BeautifulSoup(html_article.content, 'html.parser')

                text_to_speech = ""

                try:
                    # To adapt for changes
                    if soup_article.find('article') is not None:
                        text_to_speech += soup_article.find('article')\
                            .text\
                            .replace('Versions', '') \
                            .replace('Liens relatifs', '') \
                            .replace('\t', '') \
                            .replace('\n', '')
                    else:
                        print("no article")

                    # To adapt for changes
                    audio_file = ""
                    try:
                        audio_file += os.getcwd() + "\\audio\\audio_file.mp3"
                    except Exception as e:
                        print("error audio : " + str(e))

                    # To adapt for changes
                    movie_file = ""
                    try:
                        movie_file += new_directory + "\\" + str(x) + "_" + soup_article \
                            .find("h2", {"class": "name-article"}) \
                            .text.replace(":", "_") \
                            .replace(" ", "_") \
                            .replace('é', 'e') \
                            .replace('à', 'a') \
                            .replace("\n", "") \
                            .replace("?", "") \
                            .replace("/", "") \
                            .replace("-", "_") + ".avi"
                    except Exception as e:
                        print('error movie_file : ' + str(e))

                    try:
                        time.sleep(20)

                        tts = gTTS(text_to_speech.replace("", "")
                                   .replace('\t', ' ')
                                   .replace('\n', ' ')
                                   .replace(u"\u2018", "'")
                                   .replace(u"\u2019", "'")
                                   .replace(u"\u0153", "oe")
                                   .replace(u"\u2013", "-")
                                   .replace(u"\u2015", "―")
                                   .replace("", "")
                                   .replace(".", "")
                                   .replace("©", "")
                                   .replace("*", "")
                                   .replace("-", " ")
                                   .replace("✔", "")
                                   .replace("•", "")
                                   .replace("⇒", "")
                                   .replace("↑", "")
                                   .replace("→", ""), lang='fr')

                        tts.save(audio_file)
                    except Exception as e:
                        print("error audio file : " + str(e))

                    # Folder of images
                    image_folder = os.getcwd() + '\\images'

                    # Create images from the text
                    number_of_caracters_of_text = len(text_to_speech.replace('\t', ' ').replace('\n', ' '))
                    number_of_caracters_per_line = 110

                    number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                    number_of_lines = 0

                    if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                        number_of_lines += round(number_of_lines_with_coma) + 1
                    elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                        number_of_lines += round(number_of_lines_with_coma)

                    number_of_lines_per_image = 10

                    number_of_images_with_coma = number_of_lines / number_of_lines_per_image

                    number_of_images = 0

                    if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                        number_of_images += round(number_of_images_with_coma) + 1
                    elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                        number_of_images += round(number_of_images_with_coma)

                    # Array duration of each clip
                    durations_of_each_clip = [0]

                    l = 0

                    duration = 0

                    for i in range(1, number_of_images + 1):
                        img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                        d = ImageDraw.Draw(img)

                        if l <= number_of_lines:
                            for j in range(0, 10):
                                depart = 110 * l
                                arrivee = 110 + 110 * l
                                coordinate_y = 25 * j

                                if j < 9:
                                    try:
                                        d.text((10, coordinate_y), text_to_speech[depart:arrivee]
                                               .replace('\t', ' ')
                                               .replace('\n', ' ')
                                               .replace(u"\u2018", "'")
                                               .replace(u"\u2019", "'")
                                               .replace(u"\u0153", "oe")
                                               .replace(u"\u2013", "-")
                                               .replace(u"\u2015", "―")
                                               , fill=(0, 0, 0))
                                    except Exception as e:
                                        print("add text 1 : " + str(e))

                                    if text_to_speech[depart:arrivee] != "":
                                        try:
                                            time.sleep(20)

                                            tts = gTTS(text_to_speech[depart:arrivee]
                                                       .replace('\t', ' ')
                                                       .replace('\n', ' ')
                                                       .replace(u"\u2018", "'")
                                                       .replace(u"\u2019", "'")
                                                       .replace(u"\u0153", "oe")
                                                       .replace(u"\u2013", "-")
                                                       .replace(u"\u2015", "―")
                                                       .replace("", "")
                                                       .replace(".", "")
                                                       .replace("©", "")
                                                       .replace("*", "")
                                                       .replace("-", " ")
                                                       .replace("✔", "")
                                                       .replace("•", "")
                                                       .replace("⇒", "")
                                                       .replace("↑", "")
                                                       .replace("→", ""), lang=langue)

                                            tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                            duration += round(
                                                MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                            os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                            l += 1
                                        except Exception as e:
                                            print("error : l = " + str(l) + " et j = "
                                                  + str(j) + " " + str(e))
                                    else:
                                        print("break : l = " + str(l) + " et j = " + str(j))
                                        durations_of_each_clip.append(duration)
                                        img.save(image_folder + "\\" + str(i) + ".png")
                                        break

                                elif j == 9:
                                    try:
                                        d.text((10, coordinate_y), text_to_speech[depart:arrivee]
                                               .replace('\t', ' ')
                                               .replace('\n', ' ')
                                               .replace(u"\u2018", "'")
                                               .replace(u"\u2019", "'")
                                               .replace(u"\u0153", "oe")
                                               .replace(u"\u2013", "-")
                                               .replace(u"\u2015", "―")
                                               , fill=(0, 0, 0))
                                    except Exception as e:
                                        print("add text 2 : " + str(e))

                                    if text_to_speech[depart:arrivee] != "":
                                        try:
                                            time.sleep(20)

                                            tts = gTTS(text_to_speech[depart:arrivee]
                                                       .replace('\t', ' ')
                                                       .replace('\n', ' ')
                                                       .replace(u"\u2018", "'")
                                                       .replace(u"\u2019", "'")
                                                       .replace(u"\u0153", "oe")
                                                       .replace(u"\u2013", "-")
                                                       .replace(u"\u2015", "―")
                                                       .replace("", "")
                                                       .replace(".", "")
                                                       .replace("©", "")
                                                       .replace("*", "")
                                                       .replace("-", " ")
                                                       .replace("✔", "")
                                                       .replace("•", "")
                                                       .replace("⇒", "")
                                                       .replace("↑", "")
                                                       .replace("→", ""), lang=langue)

                                            tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                            duration += round(
                                                MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                            os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                            img.save(image_folder + "\\" + str(i) + ".png")

                                            durations_of_each_clip.append(duration)

                                            l += 1
                                        except Exception as e:
                                            print("error : l = " + str(l) + " et j = "
                                                  + str(j) + " " + str(e))
                                    else:
                                        print("break : l = " + str(l) + " et j = " + str(j))
                                        durations_of_each_clip.append(duration)
                                        img.save(image_folder + "\\" + str(i) + ".png")
                                        break

                    # Appending the images to the video one by one
                    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                    for i in range(1, number_of_images + 1):
                        try:
                            frame = cv2.imread(os.path.join(image_folder, images[0]))

                            # setting the frame width, height width the width, height of first image
                            height, width, layers = frame.shape

                            # video to create
                            video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0,
                                                    1,
                                                    (width, height))

                            for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                                video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                    + "\\" + str(i) + ".png")))

                            # Deallocating memories taken for window creation
                            cv2.destroyAllWindows()

                            # releasing the video generated
                            video.release()

                        except Exception as e:
                            print("error video write : " + str(e))

                    clips = []

                    for i in range(1, number_of_images + 1):
                        try:
                            clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                         .set_start(durations_of_each_clip[i - 1]))
                        except Exception as e:
                            print("Error to append videos : " + str(e))

                    try:
                        CompositeVideoClip(clips).write_videofile(
                            os.getcwd() + '\\videos\\my_concatenation.mp4')
                    except Exception as e:
                        print("Error CompositeVideoClip : " + str(e))

                    try:
                        output_movie = movie_file
                        ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file,
                                                 output_movie,
                                                 vcodec='copy', acodec='copy',
                                                 ffmpeg_output=False, logger='bar')
                    except Exception as e:
                        print("output movie exception : " + str(e))
                finally:
                    try:
                        print("Vidéo : " + str(x) + " créée")

                        # Delete all audios
                        for file in os.listdir(os.getcwd() + '\\audio'):
                            os.remove(os.getcwd() + '\\audio\\' + file)

                        # Delete all images
                        for file in os.listdir(os.getcwd() + '\\images'):
                            os.remove(os.getcwd() + '\\images\\' + file)

                        # Delete all clips
                        for file in os.listdir(os.getcwd() + '\\videos'):
                            os.remove(os.getcwd() + '\\videos\\' + file)

                        array_articles.pop(x)
                    except Exception as e:
                        print("Error delete all files : " + str(e))

    def test_create_videos_from_one_code_in_force_from_legifrance_with_rpa(self):
        print("test_create_videos_from_one_code_in_force_from_legifrance_with_rpa")

        array_articles = []

        langue = 'fr'

        url_summary = "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074075/2021-07-31/"

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_summary)

        print('page open')

        time.sleep(20)

        new_directory = ""

        # Create the new directory
        # To adapt for changes
        try:
            titre = browser.find_element_by_xpath(
                "/html/body/div[1]/div/main/div/div[2]/div[1]/h1"
            ).text\
                .lower()\
                .replace(" ", "") \
                .replace('é', 'e') \
                .replace("'", "") \
                .replace("\t", "")

            # Folder for videos creees
            getcwd = os.getcwd() + "\\videos_creees\\"

            new_directory += getcwd + titre[:len(titre) - 5]

            try:
                if not os.path.exists(new_directory):
                    os.mkdir(new_directory)
            except OSError:
                print("Creation of the directory %s failed" % new_directory)
            else:
                print("The directory has been created %s " % new_directory)
        except Exception as e:
            print('error title : ' + str(e))

            # detect the current working directory
            getcwd = os.getcwd() + "\\videos_creees"

            new_directory += getcwd + "\\textes_de_lois"

            try:
                if not os.path.exists(new_directory):
                    os.mkdir(new_directory)
            except OSError:
                print("Creation of the directory %s failed" % new_directory)
            else:
                print("The directory has been created %s " % new_directory)

        # To adapt for changes
        try:
            all_code_lien_art = browser.find_elements_by_class_name('articleLink')

            for code_lien_art in all_code_lien_art:
                link = "https://www.legifrance.gouv.fr/codes/article_lc/" + code_lien_art\
                    .get_attribute('id')\
                    .replace('art', '')
                array_articles.append(link)

            print("length array_articles : " + str(len(array_articles)))

            for x in range(0, len(array_articles)):
                print("vidéo : " + str(x) + " en cours")

                url_article = str(array_articles[x])

                warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

                # with Firefox
                options = Options()
                options.headless = True
                browser_1 = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

                time.sleep(10)

                # maximize window
                browser_1.maximize_window()

                time.sleep(5)

                browser_1.get(url_article)

                time.sleep(15)

                text_to_speech = ""

                try:
                    # To adapt for changes
                    try:
                        text_to_speech += browser_1.find_element_by_xpath(
                            "/html/body/div[1]/div/main/div/div[2]/div[4]/article"
                        ).text\
                            .replace('Versions', '') \
                            .replace('Liens relatifs', '') \
                            .replace('\t', '') \
                            .replace('\r', '') \
                            .replace('\n', '')
                    except Exception as e:
                        print("no article : " + str(e))

                    # To adapt for changes
                    audio_file = ""
                    try:
                        audio_file += os.getcwd() + "\\audio\\audio_file.mp3"
                    except Exception as e:
                        print("error audio : " + str(e))

                    # To adapt for changes
                    movie_file = ""
                    try:
                        movie_file += new_directory + "\\" + str(x) + "_" + browser_1.find_element_by_xpath(
                            "/html/body/div[1]/div/main/div/div[2]/div[4]/article/div/div[1]/h2"
                        ).text.replace(":", "_")\
                            .replace(" ", "_") \
                            .replace('é', 'e') \
                            .replace('à', 'a') \
                            .replace("\n", "") \
                            .replace("?", "") \
                            .replace("/", "") \
                            .replace("-", "_") + ".avi"
                    except Exception as e:
                        print('error movie_file : ' + str(e))

                    try:
                        time.sleep(20)

                        tts = gTTS(text_to_speech.replace("", "")
                                   .replace('\t', ' ')
                                   .replace('\n', ' ')
                                   .replace(u"\u2018", "'")
                                   .replace(u"\u2019", "'")
                                   .replace(u"\u0153", "oe")
                                   .replace(u"\u2013", "-")
                                   .replace(u"\u2015", "―")
                                   .replace("", "")
                                   .replace(".", "")
                                   .replace("©", "")
                                   .replace("*", "")
                                   .replace("-", " ")
                                   .replace("✔", "")
                                   .replace("•", "")
                                   .replace("⇒", "")
                                   .replace("↑", "")
                                   .replace("→", ""), lang='fr')

                        tts.save(audio_file)
                    except Exception as e:
                        print("error audio file : " + str(e))

                    # Folder of images
                    image_folder = os.getcwd() + '\\images'

                    # Create images from the text
                    number_of_caracters_of_text = len(text_to_speech.replace('\t', ' ').replace('\n', ' '))
                    number_of_caracters_per_line = 110

                    number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                    number_of_lines = 0

                    if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                        number_of_lines += round(number_of_lines_with_coma) + 1
                    elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                        number_of_lines += round(number_of_lines_with_coma)

                    number_of_lines_per_image = 10

                    number_of_images_with_coma = number_of_lines / number_of_lines_per_image

                    number_of_images = 0

                    if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                        number_of_images += round(number_of_images_with_coma) + 1
                    elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                        number_of_images += round(number_of_images_with_coma)

                    # Array duration of each clip
                    durations_of_each_clip = [0]

                    l = 0

                    duration = 0

                    for i in range(1, number_of_images + 1):
                        img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                        d = ImageDraw.Draw(img)

                        if l <= number_of_lines:
                            for j in range(0, 10):
                                depart = 110 * l
                                arrivee = 110 + 110 * l
                                coordinate_y = 25 * j

                                if j < 9:
                                    try:
                                        d.text((10, coordinate_y), text_to_speech[depart:arrivee]
                                               .replace('\t', ' ')
                                               .replace('\n', ' ')
                                               .replace(u"\u2018", "'")
                                               .replace(u"\u2019", "'")
                                               .replace(u"\u0153", "oe")
                                               .replace(u"\u2013", "-")
                                               .replace(u"\u2015", "―")
                                               , fill=(0, 0, 0))
                                    except Exception as e:
                                        print("add text 1 : " + str(e))

                                    if text_to_speech[depart:arrivee] != "":
                                        try:
                                            time.sleep(20)

                                            tts = gTTS(text_to_speech[depart:arrivee]
                                                       .replace('\t', ' ')
                                                       .replace('\n', ' ')
                                                       .replace(u"\u2018", "'")
                                                       .replace(u"\u2019", "'")
                                                       .replace(u"\u0153", "oe")
                                                       .replace(u"\u2013", "-")
                                                       .replace(u"\u2015", "―")
                                                       .replace("", "")
                                                       .replace(".", "")
                                                       .replace("©", "")
                                                       .replace("*", "")
                                                       .replace("-", " ")
                                                       .replace("✔", "")
                                                       .replace("•", "")
                                                       .replace("⇒", "")
                                                       .replace("↑", "")
                                                       .replace("→", ""), lang=langue)

                                            tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                            duration += round(
                                                MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                            os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                            l += 1
                                        except Exception as e:
                                            print("error : l = " + str(l) + " et j = "
                                                  + str(j) + " " + str(e))
                                    else:
                                        print("break : l = " + str(l) + " et j = " + str(j))
                                        durations_of_each_clip.append(duration)
                                        img.save(image_folder + "\\" + str(i) + ".png")
                                        break

                                elif j == 9:
                                    try:
                                        d.text((10, coordinate_y), text_to_speech[depart:arrivee]
                                               .replace('\t', ' ')
                                               .replace('\n', ' ')
                                               .replace(u"\u2018", "'")
                                               .replace(u"\u2019", "'")
                                               .replace(u"\u0153", "oe")
                                               .replace(u"\u2013", "-")
                                               .replace(u"\u2015", "―")
                                               , fill=(0, 0, 0))
                                    except Exception as e:
                                        print("add text 2 : " + str(e))

                                    if text_to_speech[depart:arrivee] != "":
                                        try:
                                            time.sleep(20)

                                            tts = gTTS(text_to_speech[depart:arrivee]
                                                       .replace('\t', ' ')
                                                       .replace('\n', ' ')
                                                       .replace(u"\u2018", "'")
                                                       .replace(u"\u2019", "'")
                                                       .replace(u"\u0153", "oe")
                                                       .replace(u"\u2013", "-")
                                                       .replace(u"\u2015", "―")
                                                       .replace("", "")
                                                       .replace(".", "")
                                                       .replace("©", "")
                                                       .replace("*", "")
                                                       .replace("-", " ")
                                                       .replace("✔", "")
                                                       .replace("•", "")
                                                       .replace("⇒", "")
                                                       .replace("↑", "")
                                                       .replace("→", ""), lang=langue)

                                            tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                            duration += round(
                                                MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                            os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                            img.save(image_folder + "\\" + str(i) + ".png")

                                            durations_of_each_clip.append(duration)

                                            l += 1
                                        except Exception as e:
                                            print("error : l = " + str(l) + " et j = "
                                                  + str(j) + " " + str(e))
                                    else:
                                        print("break : l = " + str(l) + " et j = " + str(j))
                                        durations_of_each_clip.append(duration)
                                        img.save(image_folder + "\\" + str(i) + ".png")
                                        break

                    # Appending the images to the video one by one
                    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                    for i in range(1, number_of_images + 1):
                        try:
                            frame = cv2.imread(os.path.join(image_folder, images[0]))

                            # setting the frame width, height width the width, height of first image
                            height, width, layers = frame.shape

                            # video to create
                            video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0,
                                                    1,
                                                    (width, height))

                            for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                                video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                    + "\\" + str(i) + ".png")))

                            # Deallocating memories taken for window creation
                            cv2.destroyAllWindows()

                            # releasing the video generated
                            video.release()

                        except Exception as e:
                            print("error video write : " + str(e))

                    clips = []

                    for i in range(1, number_of_images + 1):
                        try:
                            clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                         .set_start(durations_of_each_clip[i - 1]))
                        except Exception as e:
                            print("Error to append videos : " + str(e))

                    try:
                        CompositeVideoClip(clips).write_videofile(
                            os.getcwd() + '\\videos\\my_concatenation.mp4')
                    except Exception as e:
                        print("Error CompositeVideoClip : " + str(e))

                    try:
                        output_movie = movie_file
                        ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file,
                                                 output_movie,
                                                 vcodec='copy', acodec='copy',
                                                 ffmpeg_output=False, logger='bar')
                    except Exception as e:
                        print("output movie exception : " + str(e))
                finally:
                    try:
                        print("Vidéo : " + str(x) + " créée")

                        # Delete all audios
                        for file in os.listdir(os.getcwd() + '\\audio'):
                            os.remove(os.getcwd() + '\\audio\\' + file)

                        # Delete all images
                        for file in os.listdir(os.getcwd() + '\\images'):
                            os.remove(os.getcwd() + '\\images\\' + file)

                        # Delete all clips
                        for file in os.listdir(os.getcwd() + '\\videos'):
                            os.remove(os.getcwd() + '\\videos\\' + file)

                        array_articles.pop(x)
                    except Exception as e:
                        print("Error delete all files : " + str(e))

                browser_1.close()

            browser.close()
        except Exception as e:
            print('main error : ' + str(e))

    def test_create_videos_from_a_list_of_urls_from_wikipedia_topic(self):
        print("test_create_videos_from_a_list_of_urls_from_wikipedia_topic")

        audio_file = ""
        image_folder = ""
        number_of_images = ""

        try:
            urls = [
                "https://en.wikipedia.org/wiki/Intelligence"
            ]

            for url in urls:
                # Request the content of a page from the url
                html = requests.get(url)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                # title of the movie
                title = ""

                if soup.select_one("#firstHeading") is not None:
                    title += str(soup.select_one("#firstHeading")
                                 .text
                                 .lower()
                                 .replace(" ", "_")
                                 .replace("/", "_")
                                 .replace("-", "_")
                                 .replace(":", "_")
                                 .replace("\n", "")
                                 .replace("?", "")
                                 ) + ".avi"

                # Text to speech and images
                text = ""

                if soup.select_one("#bodyContent") is not None:
                    text += str(soup.select_one("#bodyContent").text)

                # Filename for audio
                audio_file = os.getcwd() + "\\audio\\" + text[:50] \
                    .replace(":", "") \
                    .replace(" ", "") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "") + '.mp3'

                # Convert text to audio
                tts = gTTS(text.replace("", "")
                           .replace(".", "")
                           .replace("©", "")
                           .replace("*", "")
                           .replace("-", " ")
                           .replace("✔", "")
                           .replace("•", "")
                           .replace("⇒", "")
                           .replace("↑", "")
                           .replace("→", ""))

                # Save the audio
                tts.save(audio_file)

                # Folder of images
                image_folder = os.getcwd() + '\\images'

                # Create images from the text
                number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
                number_of_caracters_per_line = 110

                number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                number_of_lines = 0

                if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                    number_of_lines += round(number_of_lines_with_coma) + 1

                elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                    number_of_lines += round(number_of_lines_with_coma)

                number_of_lines_per_image = 10

                number_of_images_with_coma = number_of_lines / number_of_lines_per_image
                number_of_images = 0

                if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                    number_of_images += round(number_of_images_with_coma) + 1

                elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                    number_of_images += round(number_of_images_with_coma)

                # Array duration of each clip
                durations_of_each_clip = [0]

                l = 0

                duration = 0

                for i in range(1, number_of_images + 1):
                    img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                    d = ImageDraw.Draw(img)

                    if l <= number_of_lines:
                        for j in range(0, 10):
                            depart = 110 * l
                            arrivee = 110 + 110 * l
                            coordinate_y = 25 * j

                            if j < 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 1 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(
                                            MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                            elif j == 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 2 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        img.save(image_folder + "\\" + str(i) + ".png")

                                        durations_of_each_clip.append(duration)

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                # Appending the images to the video one by one
                images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                for i in range(1, number_of_images + 1):
                    try:
                        frame = cv2.imread(os.path.join(image_folder, images[0]))

                        # setting the frame width, height width the width, height of first image
                        height, width, layers = frame.shape

                        # video to create
                        video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0,
                                                1,
                                                (width, height))

                        for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                            video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                + "\\" + str(i) + ".png")))

                        # Deallocating memories taken for window creation
                        cv2.destroyAllWindows()

                        # releasing the video generated
                        video.release()

                    except Exception as e:
                        print("error video write : " + str(e))

                clips = []

                for i in range(1, number_of_images + 1):
                    try:
                        clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                     .set_start(durations_of_each_clip[i - 1]))
                    except Exception as e:
                        print("Error to append videos : " + str(e))

                try:
                    CompositeVideoClip(clips).write_videofile(
                        os.getcwd() + '\\videos\\my_concatenation.mp4')
                except Exception as e:
                    print("Error CompositeVideoClip : " + str(e))

                try:
                    output_movie = os.getcwd() + "\\videos_creees\\" + title
                    ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie,
                                             vcodec='copy', acodec='copy',
                                             ffmpeg_output=False, logger='bar')
                except Exception as e:
                    print("output movie exception : " + str(e))
        finally:
            # Delete all images
            for i in range(1, number_of_images + 1):
                os.remove(image_folder + "\\" + str(i) + ".png")

            # Delete all clips
            for i in range(1, number_of_images + 1):
                os.remove(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')

            os.remove(os.getcwd() + '\\videos\\my_concatenation.mp4')
            os.remove(audio_file)

    def test_create_videos_from_a_list_of_urls_from_net_entreprises_lectures(self):
        print("test_create_videos_from_a_list_of_urls_from_net_entreprises_lectures")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        audio_file = ""
        image_folder = ""
        number_of_images = ""

        try:
            urls = [
                "https://net-entreprises.custhelp.com/app/answers/detail_nete/a_id/1487/p/348/session/L3RpbWUvMTU5MTQ2NTUxNi9zaWQvZlViUVZncEJ5UWRiU0U0a0w0VnpLdnQ3WDhrMkRoUGY2dmQzeUZTYVZLOVFieEZhQWdvcHZRWFhjclRSaHZpdmxGV2dvb3dtNWMwckFFQTdSM0xkbG1MTW9NdiU3RVN2TThEa01nbDdDdFVkdERGZ1lZNHJrNzZBVHclMjElMjE=",
                "https://dsn-info.custhelp.com/app/answers/detail_nete/a_id/1488/p/348/session/L3RpbWUvMTU5MTQ2NTUxNi9zaWQvZlViUVZncEJ5UWRiU0U0a0w0VnpLdnQ3WDhrMkRoUGY2dmQzeUZTYVZLOVFieEZhQWdvcHZRWFhjclRSaHZpdmxGV2dvb3dtNWMwckFFQTdSM0xkbG1MTW9NdiU3RVN2TThEa01nbDdDdFVkdERGZ1lZNHJrNzZBVHclMjElMjE="
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
                                 .text[:20]
                                 .lower()
                                 .replace(" ", "")
                                 .replace("/", "")
                                 .replace("-", "")
                                 .replace(":", "")
                                 .replace("\n", "")
                                 .replace("?", "")
                                 .replace('ã', '')
                                 .replace('©', '')
                                 ) + ".avi"

                # Text to speech and images
                text = ""

                # To adapt
                if soup.find("body") is not None:
                    text += str(soup.find("body").text)

                # Filename for audio
                audio_file = os.getcwd() + "\\audio\\" + text[:10] \
                    .replace(":", "") \
                    .replace(" ", "") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "") + '.mp3'

                # Convert text to audio
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

                # Save the audio
                tts.save(audio_file)

                # Folder of images
                image_folder = os.getcwd() + '\\images'

                # Create images from the text
                number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
                number_of_caracters_per_line = 110

                number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                number_of_lines = 0

                if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                    number_of_lines += round(number_of_lines_with_coma) + 1

                elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                    number_of_lines += round(number_of_lines_with_coma)

                number_of_lines_per_image = 10

                number_of_images_with_coma = number_of_lines / number_of_lines_per_image
                number_of_images = 0

                if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                    number_of_images += round(number_of_images_with_coma) + 1

                elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                    number_of_images += round(number_of_images_with_coma)

                # Array duration of each clip
                durations_of_each_clip = [0]

                l = 0

                duration = 0

                for i in range(1, number_of_images + 1):
                    img = Image.new('RGB', (700, 300), color=(255, 255, 255))

                    d = ImageDraw.Draw(img)

                    if l <= number_of_lines:
                        for j in range(0, 10):
                            depart = 110 * l
                            arrivee = 110 + 110 * l
                            coordinate_y = 25 * j

                            if j < 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 1 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(
                                            MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break
                            elif j == 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 2 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        img.save(image_folder + "\\" + str(i) + ".png")

                                        durations_of_each_clip.append(duration)

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                # Appending the images to the video one by one
                images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                for i in range(1, number_of_images + 1):
                    try:
                        frame = cv2.imread(os.path.join(image_folder, images[0]))

                        # setting the frame width, height width the width, height of first image
                        height, width, layers = frame.shape

                        # video to create
                        video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0,
                                                1,
                                                (width, height))

                        for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                            video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                + "\\" + str(i) + ".png")))

                        # Deallocating memories taken for window creation
                        cv2.destroyAllWindows()

                        # releasing the video generated
                        video.release()

                    except Exception as e:
                        print("error video write : " + str(e))

                clips = []

                for i in range(1, number_of_images + 1):
                    try:
                        clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                     .set_start(durations_of_each_clip[i - 1]))
                    except Exception as e:
                        print("Error to append videos : " + str(e))

                try:
                    CompositeVideoClip(clips).write_videofile(
                        os.getcwd() + '\\videos\\my_concatenation.mp4')
                except Exception as e:
                    print("Error CompositeVideoClip : " + str(e))

                try:
                    output_movie = os.getcwd() + "\\videos_creees\\" + title
                    ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie,
                                             vcodec='copy', acodec='copy',
                                             ffmpeg_output=False, logger='bar')
                except Exception as e:
                    print("output movie exception : " + str(e))
        finally:
            # Delete all images
            for i in range(1, number_of_images + 1):
                os.remove(image_folder + "\\" + str(i) + ".png")

            # Delete all clips
            for i in range(1, number_of_images + 1):
                os.remove(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')

            os.remove(os.getcwd() + '\\videos\\my_concatenation.mp4')
            os.remove(audio_file)

    def test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_artificial_intelligence(self):
        print("test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_artificial_intelligence")

        audio_file = ""
        image_folder = ""
        number_of_images = ""
        directory = "artificial_intelligence"

        try:
            '''
            "https://en.wikipedia.org/wiki/Weak_AI",
            "https://en.wikipedia.org/wiki/Artificial_general_intelligence",
            '''

            urls = [
                "https://en.wikipedia.org/wiki/Superintelligence",
                "https://en.wikipedia.org/wiki/Artificial_intelligence",
                "https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Behavior-based_robotics",
                "https://en.wikipedia.org/wiki/Subsumption_architecture",
                "https://en.wikipedia.org/wiki/Nouvelle_AI",
                "https://en.wikipedia.org/wiki/Computational_creativity",
                "https://en.wikipedia.org/wiki/Machine_learning",
                "https://en.wikipedia.org/wiki/Neural_network",
                "https://en.wikipedia.org/wiki/Hybrid_neural_network",
                "https://en.wikipedia.org/wiki/Recurrent_neural_network",
                "https://en.wikipedia.org/wiki/Perceptron",
                "https://en.wikipedia.org/wiki/Support_vector_machine",
                "https://en.wikipedia.org/wiki/Fuzzy_control_system",
                "https://en.wikipedia.org/wiki/Evolutionary_computation",
                "https://en.wikipedia.org/wiki/Evolutionary_algorithm",
                "https://en.wikipedia.org/wiki/Genetic_algorithm",
                "https://en.wikipedia.org/wiki/Differential_evolution",
                "https://en.wikipedia.org/wiki/Metaheuristic",
                "https://en.wikipedia.org/wiki/Swarm_intelligence",
                "https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms",
                "https://en.wikipedia.org/wiki/Particle_swarm_optimization",
                "https://en.wikipedia.org/wiki/BELBIC",
                "https://en.wikipedia.org/wiki/Probability",
                "https://en.wikipedia.org/wiki/Bayesian_network",
                "https://en.wikipedia.org/wiki/Bayesian_network",
                "https://en.wikipedia.org/wiki/Hidden_Markov_model",
                "https://en.wikipedia.org/wiki/Kalman_filter",
                "https://en.wikipedia.org/wiki/Chaos_theory",
                "https://en.wikipedia.org/wiki/Applications_of_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Computational_creativity",
                "https://en.wikipedia.org/wiki/Artificial_life",
                "https://en.wikipedia.org/wiki/Automated_planning_and_scheduling",
                "https://en.wikipedia.org/wiki/Automated_reasoning",
                "https://en.wikipedia.org/wiki/Automation",
                "https://en.wikipedia.org/wiki/Automatic_target_recognition",
                "https://en.wikipedia.org/wiki/Bio-inspired_computing",
                "https://en.wikipedia.org/wiki/Computer_audition",
                "https://en.wikipedia.org/wiki/Speech_recognition",
                "https://en.wikipedia.org/wiki/Speaker_recognition",
                "https://en.wikipedia.org/wiki/Computer_vision",
                "https://en.wikipedia.org/wiki/Digital_image_processing",
                "https://en.wikipedia.org/wiki/Intelligent_word_recognition",
                "https://en.wikipedia.org/wiki/Outline_of_object_recognition",
                "https://en.wikipedia.org/wiki/Optical_mark_recognition",
                "https://en.wikipedia.org/wiki/Handwriting_recognition",
                "https://en.wikipedia.org/wiki/Optical_character_recognition",
                "https://en.wikipedia.org/wiki/Automatic_number-plate_recognition",
                "https://en.wikipedia.org/wiki/Facial_recognition_system",
                "https://en.wikipedia.org/wiki/Silent_speech_interface",
                "https://en.wikipedia.org/wiki/Diagnosis_(artificial_intelligence)",
                "https://en.wikipedia.org/wiki/Expert_system",
                "https://en.wikipedia.org/wiki/Decision_support_system",
                "https://en.wikipedia.org/wiki/Clinical_decision_support_system",
                "https://en.wikipedia.org/wiki/Artificial_intelligence_in_video_games",
                "https://en.wikipedia.org/wiki/Video_game_bot",
                "https://en.wikipedia.org/wiki/Computer_chess",
                "https://en.wikipedia.org/wiki/Computer_Go",
                "https://en.wikipedia.org/wiki/General_game_playing",
                "https://en.wikipedia.org/wiki/Game_theory",
                "https://en.wikipedia.org/wiki/Hybrid_intelligent_system",
                "https://en.wikipedia.org/wiki/Intelligent_agent",
                "https://en.wikipedia.org/wiki/Agent_architecture",
                "https://en.wikipedia.org/wiki/Cognitive_architecture",
                "https://en.wikipedia.org/wiki/Intelligent_control",
                "https://en.wikipedia.org/wiki/Knowledge_management",
                "https://en.wikipedia.org/wiki/Concept_mining",
                "https://en.wikipedia.org/wiki/Data_mining",
                "https://en.wikipedia.org/wiki/Text_mining",
                "https://en.wikipedia.org/wiki/Process_mining",
                "https://en.wikipedia.org/wiki/Email_spam",
                "https://en.wikipedia.org/wiki/Information_extraction",
                "https://en.wikipedia.org/wiki/Activity_recognition",
                "https://en.wikipedia.org/wiki/Image_retrieval",
                "https://en.wikipedia.org/wiki/Automatic_image_annotation",
                "https://en.wikipedia.org/wiki/Named-entity_recognition",
                "https://en.wikipedia.org/wiki/Relationship_extraction",
                "https://en.wikipedia.org/wiki/Terminology_extraction",
                "https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning",
                "https://en.wikipedia.org/wiki/Semantic_Web",
                "https://en.wikipedia.org/wiki/Constrained_conditional_model",
                "https://en.wikipedia.org/wiki/Deep_learning",
                "https://en.wikipedia.org/wiki/Neural_modeling_fields",
                "https://en.wikipedia.org/wiki/Natural_language_processing",
                "https://en.wikipedia.org/wiki/Chatbot",
                "https://en.wikipedia.org/wiki/Language_identification",
                "https://en.wikipedia.org/wiki/Natural-language_user_interface",
                "https://en.wikipedia.org/wiki/Natural-language_understanding",
                "https://en.wikipedia.org/wiki/Machine_translation",
                "https://en.wikipedia.org/wiki/Statistical_semantics",
                "https://en.wikipedia.org/wiki/Question_answering",
                "https://en.wikipedia.org/wiki/Semantic_translation",
                "https://en.wikipedia.org/wiki/Nonlinear_control",
                "https://en.wikipedia.org/wiki/Pattern_recognition",
                "https://en.wikipedia.org/wiki/Robotics",
                "https://en.wikipedia.org/wiki/Cognition",
                "https://en.wikipedia.org/wiki/Cybernetics",
                "https://en.wikipedia.org/wiki/Developmental_robotics",
                "https://en.wikipedia.org/wiki/Evolutionary_robotics",
                "https://en.wikipedia.org/wiki/Speech-generating_device",
                "https://en.wikipedia.org/wiki/Strategic_planning",
                "https://en.wikipedia.org/wiki/Vehicle_infrastructure_integration",
                "https://en.wikipedia.org/wiki/Virtual_intelligence",
                "https://en.wikipedia.org/wiki/Virtual_reality",
                "https://en.wikipedia.org/wiki/Action_selection",
                "https://en.wikipedia.org/wiki/Affective_computing",
                "https://en.wikipedia.org/wiki/AI_box",
                "https://en.wikipedia.org/wiki/AI-complete",
                "https://en.wikipedia.org/wiki/Algorithmic_probability",
                "https://en.wikipedia.org/wiki/Artificial_intelligence_systems_integration",
                "https://en.wikipedia.org/wiki/Autonomic_computing",
                "https://en.wikipedia.org/wiki/Autonomic_networking",
                "https://en.wikipedia.org/wiki/Backward_chaining",
                "https://en.wikipedia.org/wiki/Artificial_immune_system",
                "https://en.wikipedia.org/wiki/Blackboard_system",
                "https://en.wikipedia.org/wiki/Combs_method",
                "https://en.wikipedia.org/wiki/Commonsense_reasoning",
                "https://en.wikipedia.org/wiki/Computational_humor",
                "https://en.wikipedia.org/wiki/Computer-assisted_proof",
                "https://en.wikipedia.org/wiki/Conceptual_dependency_theory",
                "https://en.wikipedia.org/wiki/Darwin_machine",
                "https://en.wikipedia.org/wiki/Description_logic",
                "https://en.wikipedia.org/wiki/Frame_problem",
                "https://en.wikipedia.org/wiki/Grammar_systems_theory",
                "https://en.wikipedia.org/wiki/Informatics",
                "https://en.wikipedia.org/wiki/Kinect",
                "https://en.wikipedia.org/wiki/LIDA_(cognitive_architecture)",
                "https://en.wikipedia.org/wiki/Means%E2%80%93ends_analysis",
                "https://en.wikipedia.org/wiki/Moravec%27s_paradox",
                "https://en.wikipedia.org/wiki/Music_and_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Ordered_weighted_averaging_aggregation_operator",
                "https://en.wikipedia.org/wiki/Percept_(artificial_intelligence)",
                "https://en.wikipedia.org/wiki/Perceptual_computing",
                "https://en.wikipedia.org/wiki/Rule-based_system",
                "https://en.wikipedia.org/wiki/Self-management_(computer_science)",
                "https://en.wikipedia.org/wiki/Software_agent",
                "https://en.wikipedia.org/wiki/Autonomous_agent",
                "https://en.wikipedia.org/wiki/Rational_agent",
                "https://en.wikipedia.org/wiki/Control_system",
                "https://en.wikipedia.org/wiki/Hierarchical_control_system",
                "https://en.wikipedia.org/wiki/Networked_control_system",
                "https://en.wikipedia.org/wiki/Distributed_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Multi-agent_system",
                "https://en.wikipedia.org/wiki/Monitoring_and_surveillance_agents",
                "https://en.wikipedia.org/wiki/Embodied_agent",
                "https://en.wikipedia.org/wiki/Situated",
                "https://en.wikipedia.org/wiki/Sussman_anomaly",
                "https://en.wikipedia.org/wiki/Wetware_(brain)",
                "https://en.wikipedia.org/wiki/List_of_artificial_intelligence_projects",
                "https://en.wikipedia.org/wiki/Automated_Mathematician",
                "https://en.wikipedia.org/wiki/Allen_(robot)",
                "https://en.wikipedia.org/wiki/Open_Mind_Common_Sense",
                "https://en.wikipedia.org/wiki/Mindpixel",
                "https://en.wikipedia.org/wiki/CALO",
                "https://en.wikipedia.org/wiki/Blue_Brain_Project",
                "https://en.wikipedia.org/wiki/DeepMind",
                "https://en.wikipedia.org/wiki/Human_Brain_Project",
                "https://en.wikipedia.org/wiki/Watson_(computer)",
                "https://en.wikipedia.org/wiki/AIBO",
                "https://en.wikipedia.org/wiki/ASIMO",
                "https://en.wikipedia.org/wiki/Cog_(project)",
                "https://en.wikipedia.org/wiki/QRIO",
                "https://en.wikipedia.org/wiki/TOPIO",
                "https://en.wikipedia.org/wiki/Question_answering",
                "https://en.wikipedia.org/wiki/Information_retrieval",
                "https://en.wikipedia.org/wiki/Project_Debater",
                "https://en.wikipedia.org/wiki/Virtual_assistant",
                "https://en.wikipedia.org/wiki/Amazon_Alexa",
                "https://en.wikipedia.org/wiki/Assistant_(by_Speaktoit)",
                "https://en.wikipedia.org/wiki/Braina",
                "https://en.wikipedia.org/wiki/Cortana",
                "https://en.wikipedia.org/wiki/Google_Assistant",
                "https://en.wikipedia.org/wiki/Google_Now",
                "https://en.wikipedia.org/wiki/Mycroft_(software)",
                "https://en.wikipedia.org/wiki/Siri",
                "https://en.wikipedia.org/wiki/Viv_(software)",
                "https://en.wikipedia.org/wiki/OpenAIR",
                "https://en.wikipedia.org/wiki/OpenCog",
                "https://en.wikipedia.org/wiki/OpenIRIS",
                "https://en.wikipedia.org/wiki/RapidMiner",
                "https://en.wikipedia.org/wiki/TensorFlow",
                "https://en.wikipedia.org/wiki/Artificial_psychology",
                "https://en.wikipedia.org/wiki/AI_effect",
                "https://en.wikipedia.org/wiki/Uncanny_valley",
                "https://en.wikipedia.org/wiki/History_of_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Asilomar_Conference_on_Beneficial_AI",
                "https://en.wikipedia.org/wiki/AI_winter",
                "https://en.wikipedia.org/wiki/History_of_machine_translation",
                "https://en.wikipedia.org/wiki/Moore%27s_law",
                "https://en.wikipedia.org/wiki/History_of_natural_language_processing",
                "https://en.wikipedia.org/wiki/Existential_risk_from_artificial_general_intelligence",
                "https://en.wikipedia.org/wiki/AI_takeover",
                "https://en.wikipedia.org/wiki/Technological_singularity",
                "https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Artificial_intelligence_arms_race",
                "https://en.wikipedia.org/wiki/Lethal_autonomous_weapon",
                "https://en.wikipedia.org/wiki/Military_robot",
                "https://en.wikipedia.org/wiki/Unmanned_combat_aerial_vehicle",
                "https://en.wikipedia.org/wiki/Friendly_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Self-replicating_machine",
                "https://en.wikipedia.org/wiki/Group_mind_(science_fiction)",
                "https://en.wikipedia.org/wiki/Swarm_intelligence",
                "https://en.wikipedia.org/wiki/Singularitarianism",
                "https://en.wikipedia.org/wiki/Human_enhancement",
                "https://en.wikipedia.org/wiki/Transhumanism",
                "https://en.wikipedia.org/wiki/Posthumanism",
                "https://en.wikipedia.org/wiki/Cyborg",
                "https://en.wikipedia.org/wiki/Mind_uploading",
                "https://en.wikipedia.org/wiki/Philosophy_of_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Artificial_brain",
                "https://en.wikipedia.org/wiki/Artificial_consciousness",
                "https://en.wikipedia.org/wiki/User_illusion",
                "https://en.wikipedia.org/wiki/Legal_informatics",
                "https://en.wikipedia.org/wiki/Chinese_room",
                "https://en.wikipedia.org/wiki/Cognitive_science",
                "https://en.wikipedia.org/wiki/Artificial_consciousness",
                "https://en.wikipedia.org/wiki/Embodied_cognitive_science",
                "https://en.wikipedia.org/wiki/Embodied_cognition",
                "https://en.wikipedia.org/wiki/Philosophy_of_mind",
                "https://en.wikipedia.org/wiki/Computational_theory_of_mind",
                "https://en.wikipedia.org/wiki/Functionalism_(philosophy_of_mind)",
                "https://en.wikipedia.org/wiki/Physical_symbol_system",
                "https://en.wikipedia.org/wiki/Turing_test",
                "https://en.wikipedia.org/wiki/Artificial_intelligence_in_fiction",
                "https://en.wikipedia.org/wiki/Agent_(The_Matrix)",
                "https://en.wikipedia.org/wiki/Agent_Smith",
                "https://en.wikipedia.org/wiki/The_Matrix",
                "https://en.wikipedia.org/wiki/Sprawl_trilogy",
                "https://en.wikipedia.org/wiki/I_Have_No_Mouth,_and_I_Must_Scream",
                "https://en.wikipedia.org/wiki/Westworld_(film)",
                "https://en.wikipedia.org/wiki/Futureworld",
                "https://en.wikipedia.org/wiki/Angel_F",
                "https://en.wikipedia.org/wiki/Arnold_Rimmer",
                "https://en.wikipedia.org/wiki/Red_Dwarf",
                "https://en.wikipedia.org/wiki/Alien_(film)",
                "https://en.wikipedia.org/wiki/Ash_(Alien)",
                "https://en.wikipedia.org/wiki/C-3PO",
                "https://en.wikipedia.org/wiki/Star_Wars",
                "https://en.wikipedia.org/wiki/Chappie_(film)",
                "https://en.wikipedia.org/wiki/Colossus_(novel)",
                "https://en.wikipedia.org/wiki/Colossus:_The_Forbin_Project",
                "https://en.wikipedia.org/wiki/Data_(Star_Trek)",
                "https://en.wikipedia.org/wiki/Star_Trek:_The_Next_Generation",
                "https://en.wikipedia.org/wiki/Cortana_(Halo)",
                "https://en.wikipedia.org/wiki/Halo_(franchise)",
                "https://en.wikipedia.org/wiki/Cylon_(Battlestar_Galactica)",
                "https://en.wikipedia.org/wiki/Battlestar_Galactica_(2004_TV_series)",
                "https://en.wikipedia.org/wiki/Dune:_The_Butlerian_Jihad#Dune:_The_Butlerian_JihadPrequels",
                "https://en.wikipedia.org/wiki/HAL_9000",
                "https://en.wikipedia.org/wiki/Holly_(Red_Dwarf)",
                "https://en.wikipedia.org/wiki/Permutation_City",
                "https://en.wikipedia.org/wiki/Children_of_the_Mind",
                "https://en.wikipedia.org/wiki/First_Meetings",
                "https://en.wikipedia.org/wiki/Short_Circuit_(1986_film)",
                "https://en.wikipedia.org/wiki/WarGames",
                "https://en.wikipedia.org/wiki/Keymaker",
                "https://en.wikipedia.org/wiki/The_Machine_(film)",
                "https://en.wikipedia.org/wiki/Real_Humans",
                "https://en.wikipedia.org/wiki/Organizations_of_the_Dune_universe",
                "https://en.wikipedia.org/wiki/List_of_Ghost_in_the_Shell_characters",
                "https://en.wikipedia.org/wiki/Ghost_in_the_Shell",
                "https://en.wikipedia.org/wiki/R2-D2",
                "https://en.wikipedia.org/wiki/Ex_Machina_(film)",
                "https://en.wikipedia.org/wiki/Aliens_(film)",
                "https://en.wikipedia.org/wiki/Replicant",
                "https://en.wikipedia.org/wiki/Do_Androids_Dream_of_Electric_Sheep%3F",
                "https://en.wikipedia.org/wiki/Blade_Runner",
                "https://en.wikipedia.org/wiki/Roboduck",
                "https://en.wikipedia.org/wiki/NEW-GEN",
                "https://en.wikipedia.org/wiki/Robot_series",
                "https://en.wikipedia.org/wiki/The_Animatrix",
                "https://en.wikipedia.org/wiki/Skynet_(Terminator)",
                "https://en.wikipedia.org/wiki/Terminator_(franchise)",
                "https://en.wikipedia.org/wiki/Android_(robot)",
                "https://en.wikipedia.org/wiki/Fallout_4",
                "https://en.wikipedia.org/wiki/TARDIS",
                "https://en.wikipedia.org/wiki/Doctor_Who",
                "https://en.wikipedia.org/wiki/Terminator_(character)",
                "https://en.wikipedia.org/wiki/The_Bicentennial_Man",
                "https://en.wikipedia.org/wiki/Foundation_(Asimov_novel)",
                "https://en.wikipedia.org/wiki/Mass_Effect",
                "https://en.wikipedia.org/wiki/Person_of_Interest_(TV_series)",
                "https://en.wikipedia.org/wiki/The_Culture",
                "https://en.wikipedia.org/wiki/The_Oracle_(The_Matrix)",
                "https://en.wikipedia.org/wiki/Ship_in_a_Bottle_(Star_Trek:_The_Next_Generation)",
                "https://en.wikipedia.org/wiki/Destination:_Void",
                "https://en.wikipedia.org/wiki/Transcendence_(2014_film)",
                "https://en.wikipedia.org/wiki/Transformers",
                "https://en.wikipedia.org/wiki/Three_Laws_of_Robotics",
                "https://en.wikipedia.org/wiki/The_City_and_the_Stars",
                "https://en.wikipedia.org/wiki/WALL-E",
                "https://en.wikipedia.org/wiki/Competitions_and_prizes_in_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Loebner_Prize",
                "https://en.wikipedia.org/wiki/List_of_important_publications_in_computer_science",
                "https://en.wikipedia.org/wiki/Adaptive_Behavior_(journal)",
                "https://en.wikipedia.org/wiki/AI_Memo",
                "https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach",
                "https://en.wikipedia.org/wiki/Artificial_Minds",
                "https://en.wikipedia.org/wiki/Computational_Intelligence_(journal)",
                "https://en.wikipedia.org/wiki/Computing_Machinery_and_Intelligence",
                "https://en.wikipedia.org/wiki/Royal_Swedish_Academy_of_Sciences",
                "https://en.wikipedia.org/wiki/IEEE_Intelligent_Systems",
                "https://en.wikipedia.org/wiki/IEEE_Transactions_on_Pattern_Analysis_and_Machine_Intelligence",
                "https://en.wikipedia.org/wiki/List_of_emerging_technologies",
                "https://en.wikipedia.org/wiki/Neural_Networks_(journal)",
                "https://en.wikipedia.org/wiki/On_Intelligence",
                "https://en.wikipedia.org/wiki/Paradigms_of_AI_Programming",
                "https://en.wikipedia.org/wiki/Hubert_Dreyfus%27s_views_on_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Allen_Institute_for_AI",
                "https://en.wikipedia.org/wiki/Artificial_General_Intelligence_Research_Institute",
                "https://en.wikipedia.org/wiki/Artificial_Intelligence_Applications_Institute",
                "https://en.wikipedia.org/wiki/Association_for_the_Advancement_of_Artificial_Intelligence",
                "https://en.wikipedia.org/wiki/European_Association_for_Artificial_Intelligence",
                "https://en.wikipedia.org/wiki/European_Neural_Network_Society",
                "https://en.wikipedia.org/wiki/Future_of_Humanity_Institute",
                "https://en.wikipedia.org/wiki/Future_of_Life_Institute",
                "https://en.wikipedia.org/wiki/ILabs",
                "https://en.wikipedia.org/wiki/International_Joint_Conference_on_Artificial_Intelligence",
                "https://en.wikipedia.org/wiki/Knowledge_Engineering_and_Machine_Learning_Group",
                "https://en.wikipedia.org/wiki/Machine_Intelligence_Research_Institute",
                "https://en.wikipedia.org/wiki/Partnership_on_AI",
                "https://en.wikipedia.org/wiki/Society_for_the_Study_of_Artificial_Intelligence_and_the_Simulation_of_Behaviour",
                "https://en.wikipedia.org/wiki/AI_Companies_of_India",
                "https://en.wikipedia.org/wiki/Alphabet_Inc.",
                "https://en.wikipedia.org/wiki/X_(company)",
                "https://en.wikipedia.org/wiki/Meka_Robotics",
                "https://en.wikipedia.org/wiki/Redwood_Robotics",
                "https://en.wikipedia.org/wiki/Boston_Dynamics",
                "https://en.wikipedia.org/wiki/Baidu",
                "https://en.wikipedia.org/wiki/IBM",
                "https://en.wikipedia.org/wiki/Universal_Robotics",
                "https://en.wikipedia.org/wiki/Abductive_logic_programming",
                "https://en.wikipedia.org/wiki/Abductive_reasoning",
                "https://en.wikipedia.org/wiki/Abstract_data_type",
                "https://en.wikipedia.org/wiki/Abstraction_(computer_science)",
                "https://en.wikipedia.org/wiki/Accelerating_change",
                "https://en.wikipedia.org/wiki/Action_language",
                "https://en.wikipedia.org/wiki/Action_model_learning",
                "https://en.wikipedia.org/wiki/Activation_function",
                "https://en.wikipedia.org/wiki/Adaptive_algorithm",
                "https://en.wikipedia.org/wiki/Adaptive_neuro_fuzzy_inference_system",
                "https://en.wikipedia.org/wiki/Admissible_heuristic",
                "https://en.wikipedia.org/wiki/AI_accelerator",
                "https://en.wikipedia.org/wiki/Algorithm",
                "https://en.wikipedia.org/wiki/Algorithmic_efficiency",
                "https://en.wikipedia.org/wiki/AlphaGo",
                "https://en.wikipedia.org/wiki/Ambient_intelligence",
                "https://en.wikipedia.org/wiki/Analysis_of_algorithms",
                "https://en.wikipedia.org/wiki/Analytics",
                "https://en.wikipedia.org/wiki/Answer_set_programming",
                "https://en.wikipedia.org/wiki/Anytime_algorithm",
                "https://en.wikipedia.org/wiki/API",
                "https://en.wikipedia.org/wiki/Approximate_string_matching",
                "https://en.wikipedia.org/wiki/Approximation_error",
                "https://en.wikipedia.org/wiki/Argumentation_framework",
                "https://en.wikipedia.org/wiki/AIML",
                "https://en.wikipedia.org/wiki/Artificial_neural_network",
                "https://en.wikipedia.org/wiki/Asymptotic_computational_complexity",
                "https://en.wikipedia.org/wiki/Attributional_calculus",
                "https://en.wikipedia.org/wiki/Augmented_reality",
                "https://en.wikipedia.org/wiki/Automata_theory",
                "https://en.wikipedia.org/wiki/Self-driving_car",
                "https://en.wikipedia.org/wiki/Autonomous_robot",
                "https://en.wikipedia.org/wiki/Backpropagation",
                "https://en.wikipedia.org/wiki/Backpropagation_through_time",
                "https://en.wikipedia.org/wiki/Bag-of-words_model",
                "https://en.wikipedia.org/wiki/Bag-of-words_model_in_computer_vision",
                "https://en.wikipedia.org/wiki/Batch_normalization",
                "https://en.wikipedia.org/wiki/Bayesian_programming",
                "https://en.wikipedia.org/wiki/Bees_algorithm",
                "https://en.wikipedia.org/wiki/Behavior_informatics",
                "https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)",
                "https://en.wikipedia.org/wiki/Belief%E2%80%93desire%E2%80%93intention_software_model",
                "https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff",
                "https://en.wikipedia.org/wiki/Big_data",
                "https://en.wikipedia.org/wiki/Big_O_notation",
                "https://en.wikipedia.org/wiki/Binary_tree",
                "https://en.wikipedia.org/wiki/Boltzmann_machine",
                "https://en.wikipedia.org/wiki/Boolean_satisfiability_problem",
                "https://en.wikipedia.org/wiki/Brain_technology",
                "https://en.wikipedia.org/wiki/Branching_factor",
                "https://en.wikipedia.org/wiki/Brute-force_search",
                "https://en.wikipedia.org/wiki/Capsule_neural_network",
                "https://en.wikipedia.org/wiki/Case-based_reasoning",
                "https://en.wikipedia.org/wiki/Cloud_robotics",
                "https://en.wikipedia.org/wiki/Cluster_analysis",
                "https://en.wikipedia.org/wiki/Cobweb_(clustering)",
                "https://en.wikipedia.org/wiki/Cognitive_computing",
                "https://en.wikipedia.org/wiki/Combinatorial_optimization",
                "https://en.wikipedia.org/wiki/Committee_machine",
                "https://en.wikipedia.org/wiki/Commonsense_knowledge_(artificial_intelligence)",
                "https://en.wikipedia.org/wiki/Computational_chemistry",
                "https://en.wikipedia.org/wiki/Computational_complexity_theory",
                "https://en.wikipedia.org/wiki/Computational_cybernetics",
                "https://en.wikipedia.org/wiki/Computational_intelligence",
                "https://en.wikipedia.org/wiki/Computational_learning_theory",
                "https://en.wikipedia.org/wiki/Computational_linguistics",
                "https://en.wikipedia.org/wiki/Computational_mathematics",
                "https://en.wikipedia.org/wiki/Computational_neuroscience",
                "https://en.wikipedia.org/wiki/Computational_number_theory",
                "https://en.wikipedia.org/wiki/Computational_problem",
                "https://en.wikipedia.org/wiki/Computational_statistics",
                "https://en.wikipedia.org/wiki/Computer-automated_design",
                "https://en.wikipedia.org/wiki/Computer_audition",
                "https://en.wikipedia.org/wiki/Computer_science",
                "https://en.wikipedia.org/wiki/Concept_drift",
                "https://en.wikipedia.org/wiki/Connectionism",
                "https://en.wikipedia.org/wiki/Consistent_heuristic",
                "https://en.wikipedia.org/wiki/Constraint_logic_programming",
                "https://en.wikipedia.org/wiki/Constraint_programming",
                "https://en.wikipedia.org/wiki/Constructed_language",
                "https://en.wikipedia.org/wiki/Control_theory",
                "https://en.wikipedia.org/wiki/Convolutional_neural_network",
                "https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)",
                "https://en.wikipedia.org/wiki/Name_binding",
                "https://en.wikipedia.org/wiki/Darkforest",
                "https://en.wikipedia.org/wiki/Dartmouth_workshop",
                "https://en.wikipedia.org/wiki/Data_fusion",
                "https://en.wikipedia.org/wiki/Data_integration",
                "https://en.wikipedia.org/wiki/Data_science",
                "https://en.wikipedia.org/wiki/Data_set",
                "https://en.wikipedia.org/wiki/Data_warehouse",
                "https://en.wikipedia.org/wiki/Datalog",
                "https://en.wikipedia.org/wiki/Decision_boundary",
                "https://en.wikipedia.org/wiki/Decision_theory",
                "https://en.wikipedia.org/wiki/Decision_tree_learning",
                "https://en.wikipedia.org/wiki/Declarative_programming",
                "https://en.wikipedia.org/wiki/Deductive_classifier",
                "https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)",
                "https://en.wikipedia.org/wiki/DeepMind",
                "https://en.wikipedia.org/wiki/Default_logic",
                "https://en.wikipedia.org/wiki/Dialogue_system",
                "https://en.wikipedia.org/wiki/Dimensionality_reduction",
                "https://en.wikipedia.org/wiki/Discrete_system",
                "https://en.wikipedia.org/wiki/Dynamic_epistemic_logic",
                "https://en.wikipedia.org/wiki/Eager_learning",
                "https://en.wikipedia.org/wiki/Ebert_test",
                "https://en.wikipedia.org/wiki/Echo_state_network",
                "https://en.wikipedia.org/wiki/Error-driven_learning",
                "https://en.wikipedia.org/wiki/Ensemble_averaging_(machine_learning)",
                "https://en.wikipedia.org/wiki/Evolving_classification_function",
                "https://en.wikipedia.org/wiki/Fast-and-frugal_trees",
                "https://en.wikipedia.org/wiki/Feature_extraction",
                "https://en.wikipedia.org/wiki/Feature_learning",
                "https://en.wikipedia.org/wiki/Feature_selection",
                "https://en.wikipedia.org/wiki/Federated_learning",
                "https://en.wikipedia.org/wiki/First-order_logic",
                "https://en.wikipedia.org/wiki/Fluent_(artificial_intelligence)",
                "https://en.wikipedia.org/wiki/Formal_language",
                "https://en.wikipedia.org/wiki/Forward_chaining",
                "https://en.wikipedia.org/wiki/Frame_(artificial_intelligence)",
                "https://en.wikipedia.org/wiki/Futures_studies",
                "https://en.wikipedia.org/wiki/Fuzzy_logic",
                "https://en.wikipedia.org/wiki/Fuzzy_rule",
                "https://en.wikipedia.org/wiki/Fuzzy_set",
                "https://en.wikipedia.org/wiki/Generative_adversarial_network",
                "https://en.wikipedia.org/wiki/Genetic_operator",
                "https://en.wikipedia.org/wiki/List_of_metaphor-based_metaheuristics",
                "https://en.wikipedia.org/wiki/Graph_(abstract_data_type)",
                "https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)",
                "https://en.wikipedia.org/wiki/Graph_database",
                "https://en.wikipedia.org/wiki/Graph_theory",
                "https://en.wikipedia.org/wiki/Graph_traversal",
                "https://en.wikipedia.org/wiki/Halting_problem",
                "https://en.wikipedia.org/wiki/Heuristic_(computer_science)",
                "https://en.wikipedia.org/wiki/Hyper-heuristic",
                "https://en.wikipedia.org/wiki/IEEE_Computational_Intelligence_Society",
                "https://en.wikipedia.org/wiki/Incremental_learning",
                "https://en.wikipedia.org/wiki/Inference_engine",
                "https://en.wikipedia.org/wiki/Information_integration",
                "https://en.wikipedia.org/wiki/Information_Processing_Language",
                "https://en.wikipedia.org/wiki/Intelligence_amplification",
                "https://en.wikipedia.org/wiki/Interpretation_(logic)",
                "https://en.wikipedia.org/wiki/Intrinsic_motivation_(artificial_intelligence)",
                "https://en.wikipedia.org/wiki/Issue_tree",
                "https://en.wikipedia.org/wiki/Junction_tree_algorithm",
                "https://en.wikipedia.org/wiki/Kernel_method",
                "https://en.wikipedia.org/wiki/KL-ONE",
                "https://en.wikipedia.org/wiki/Knowledge_acquisition",
                "https://en.wikipedia.org/wiki/Knowledge-based_systems",
                "https://en.wikipedia.org/wiki/Knowledge_engineering",
                "https://en.wikipedia.org/wiki/Knowledge_extraction",
                "https://en.wikipedia.org/wiki/Knowledge_Interchange_Format",
                "https://en.wikipedia.org/wiki/Lazy_learning",
                "https://en.wikipedia.org/wiki/Lisp_(programming_language)",
                "https://en.wikipedia.org/wiki/Logic_programming",
                "https://en.wikipedia.org/wiki/Long_short-term_memory",
                "https://en.wikipedia.org/wiki/Machine_vision",
                "https://en.wikipedia.org/wiki/Markov_chain",
                "https://en.wikipedia.org/wiki/Markov_decision_process",
                "https://en.wikipedia.org/wiki/Mathematical_optimization",
                "https://en.wikipedia.org/wiki/Machine_perception",
                "https://en.wikipedia.org/wiki/Mechanism_design",
                "https://en.wikipedia.org/wiki/Mechatronics",
                "https://en.wikipedia.org/wiki/Metabolic_network_modelling",
                "https://en.wikipedia.org/wiki/Model_checking",
                "https://en.wikipedia.org/wiki/Modus_ponens",
                "https://en.wikipedia.org/wiki/Modus_tollens",
                "https://en.wikipedia.org/wiki/Monte_Carlo_tree_search",
                "https://en.wikipedia.org/wiki/Multi-swarm_optimization",
                "https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm)",
                "https://en.wikipedia.org/wiki/Mycin",
                "https://en.wikipedia.org/wiki/Naive_Bayes_classifier",
                "https://en.wikipedia.org/wiki/Naive_semantics",
                "https://en.wikipedia.org/wiki/Named_graph",
                "https://en.wikipedia.org/wiki/Natural-language_generation",
                "https://en.wikipedia.org/wiki/Natural-language_programming",
                "https://en.wikipedia.org/wiki/Network_motif",
                "https://en.wikipedia.org/wiki/Neural_machine_translation",
                "https://en.wikipedia.org/wiki/Neural_Turing_machine",
                "https://en.wikipedia.org/wiki/Neuro-fuzzy",
                "https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface",
                "https://en.wikipedia.org/wiki/Neuromorphic_engineering",
                "https://en.wikipedia.org/wiki/Node_(computer_science)",
                "https://en.wikipedia.org/wiki/Nondeterministic_algorithm",
                "https://en.wikipedia.org/wiki/NP_(complexity)",
                "https://en.wikipedia.org/wiki/NP-completeness",
                "https://en.wikipedia.org/wiki/NP-hardness",
                "https://en.wikipedia.org/wiki/Occam%27s_razor",
                "https://en.wikipedia.org/wiki/Offline_learning",
                "https://en.wikipedia.org/wiki/Online_machine_learning",
                "https://en.wikipedia.org/wiki/Ontology_learning",
                "https://en.wikipedia.org/wiki/OpenAI",
                "https://en.wikipedia.org/wiki/Open-source_software",
                "https://en.wikipedia.org/wiki/Partial_order_reduction",
                "https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process",
                "https://en.wikipedia.org/wiki/Pathfinding",
                "https://en.wikipedia.org/wiki/First-order_logic",
                "https://en.wikipedia.org/wiki/Predictive_analytics",
                "https://en.wikipedia.org/wiki/Principal_component_analysis",
                "https://en.wikipedia.org/wiki/Principle_of_rationality",
                "https://en.wikipedia.org/wiki/Probabilistic_programming",
                "https://en.wikipedia.org/wiki/Production_system_(computer_science)",
                "https://en.wikipedia.org/wiki/Programming_language",
                "https://en.wikipedia.org/wiki/Prolog",
                "https://en.wikipedia.org/wiki/Propositional_calculus",
                "https://en.wikipedia.org/wiki/Python_(programming_language)",
                "https://en.wikipedia.org/wiki/Qualification_problem",
                "https://en.wikipedia.org/wiki/Quantifier_(logic)",
                "https://en.wikipedia.org/wiki/Quantum_computing",
                "https://en.wikipedia.org/wiki/Query_language",
                "https://en.wikipedia.org/wiki/R_(programming_language)",
                "https://en.wikipedia.org/wiki/Radial_basis_function_network",
                "https://en.wikipedia.org/wiki/Random_forest",
                "https://en.wikipedia.org/wiki/Reasoning_system",
                "https://en.wikipedia.org/wiki/Recurrent_neural_network",
                "https://en.wikipedia.org/wiki/Region_connection_calculus",
                "https://en.wikipedia.org/wiki/Reinforcement_learning",
                "https://en.wikipedia.org/wiki/Reservoir_computing",
                "https://en.wikipedia.org/wiki/Resource_Description_Framework",
                "https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine",
                "https://en.wikipedia.org/wiki/Rete_algorithm",
                "https://en.wikipedia.org/wiki/Robotics",
                "https://en.wikipedia.org/wiki/Rule-based_system",
                "https://en.wikipedia.org/wiki/Satisfiability",
                "https://en.wikipedia.org/wiki/Search_algorithm",
                "https://en.wikipedia.org/wiki/Selection_(genetic_algorithm)",
                "https://en.wikipedia.org/wiki/Self-management_(computer_science)",
                "https://en.wikipedia.org/wiki/Semantic_network",
                "https://en.wikipedia.org/wiki/Semantic_reasoner",
                "https://en.wikipedia.org/wiki/Semantic_query",
                "https://en.wikipedia.org/wiki/Semantics_(computer_science)",
                "https://en.wikipedia.org/wiki/Sensor_fusion",
                "https://en.wikipedia.org/wiki/Separation_logic",
                "https://en.wikipedia.org/wiki/Similarity_learning",
                "https://en.wikipedia.org/wiki/Simulated_annealing",
                "https://en.wikipedia.org/wiki/Artificial_intelligence,_situated_approach",
                "https://en.wikipedia.org/wiki/Situation_calculus",
                "https://en.wikipedia.org/wiki/SLD_resolution",
                "https://en.wikipedia.org/wiki/Software",
                "https://en.wikipedia.org/wiki/Software_engineering",
                "https://en.wikipedia.org/wiki/Spatial%E2%80%93temporal_reasoning",
                "https://en.wikipedia.org/wiki/SPARQL",
                "https://en.wikipedia.org/wiki/Speech_recognition",
                "https://en.wikipedia.org/wiki/Spiking_neural_network",
                "https://en.wikipedia.org/wiki/State_(computer_science)",
                "https://en.wikipedia.org/wiki/Statistical_classification",
                "https://en.wikipedia.org/wiki/Statistical_relational_learning",
                "https://en.wikipedia.org/wiki/Stochastic_optimization",
                "https://en.wikipedia.org/wiki/Stochastic_semantic_analysis",
                "https://en.wikipedia.org/wiki/Stanford_Research_Institute_Problem_Solver",
                "https://en.wikipedia.org/wiki/Subject-matter_expert",
                "https://en.wikipedia.org/wiki/Superintelligence",
                "https://en.wikipedia.org/wiki/Supervised_learning",
                "https://en.wikipedia.org/wiki/Support_vector_machine",
                "https://en.wikipedia.org/wiki/Swarm_intelligence",
                "https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence",
                "https://en.wikipedia.org/wiki/Synthetic_intelligence",
                "https://en.wikipedia.org/wiki/Systems_neuroscience",
                "https://en.wikipedia.org/wiki/Technological_singularity",
                "https://en.wikipedia.org/wiki/Temporal_difference_learning",
                "https://en.wikipedia.org/wiki/Tensor_network_theory",
                "https://en.wikipedia.org/wiki/Theoretical_computer_science",
                "https://en.wikipedia.org/wiki/Theory_of_computation",
                "https://en.wikipedia.org/wiki/Time_complexity",
                "https://en.wikipedia.org/wiki/Transhumanism",
                "https://en.wikipedia.org/wiki/Transition_system",
                "https://en.wikipedia.org/wiki/Tree_traversal",
                "https://en.wikipedia.org/wiki/True_quantified_Boolean_formula",
                "https://en.wikipedia.org/wiki/Turing_machine",
                "https://en.wikipedia.org/wiki/Turing_test",
                "https://en.wikipedia.org/wiki/Type_system",
                "https://en.wikipedia.org/wiki/Unsupervised_learning",
                "https://en.wikipedia.org/wiki/Vision_processing_unit",
                "https://en.wikipedia.org/wiki/Watson_(computer)",
                "https://en.wikipedia.org/wiki/Weak_AI",
                "https://en.wikipedia.org/wiki/World_Wide_Web_Consortium",
                "https://en.wikipedia.org/wiki/Infinitary_combinatorics",
                "https://en.wikipedia.org/wiki/Actuarial_science",
                "https://en.wikipedia.org/wiki/Additive_combinatorics",
                "https://en.wikipedia.org/wiki/Additive_number_theory",
                "https://en.wikipedia.org/wiki/Affine_geometry",
                "https://en.wikipedia.org/wiki/Affine_geometry_of_curves",
                "https://en.wikipedia.org/wiki/Affine_differential_geometry",
                "https://en.wikipedia.org/wiki/Ahlfors_theory",
                "https://en.wikipedia.org/wiki/Gauge_theory",
                "https://en.wikipedia.org/wiki/General_topology",
                "https://en.wikipedia.org/wiki/Generalized_trigonometry",
                "https://en.wikipedia.org/wiki/Geometric_algebra",
                "https://en.wikipedia.org/wiki/Geometric_analysis",
                "https://en.wikipedia.org/wiki/Geometric_calculus",
                "https://en.wikipedia.org/wiki/Geometric_combinatorics",
                "https://en.wikipedia.org/wiki/Geometric_function_theory",
                "https://en.wikipedia.org/wiki/Geometric_invariant_theory",
                "https://en.wikipedia.org/wiki/Geometric_graph_theory",
                "https://en.wikipedia.org/wiki/Geometric_group_theory",
                "https://en.wikipedia.org/wiki/Geometric_measure_theory",
                "https://en.wikipedia.org/wiki/Geometric_topology",
                "https://en.wikipedia.org/wiki/Geometry",
                "https://en.wikipedia.org/wiki/Geometry_of_numbers",
                "https://en.wikipedia.org/wiki/Global_analysis",
                ""
            ]

            for url in urls:
                # Request the content of a page from the url
                html = requests.get(url)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                # title of the movie
                title = ""

                if soup.select_one("#firstHeading") is not None:
                    title += str(soup.select_one("#firstHeading")
                                 .text
                                 .lower()
                                 .replace(" ", "_")
                                 .replace("/", "_")
                                 .replace("-", "_")
                                 .replace(":", "_")
                                 .replace("\n", "")
                                 .replace("?", "")
                                 ) + ".avi"

                    print("title : " + title)

                # Text to speech and images
                text = ""

                if soup.select_one("#bodyContent") is not None:
                    text += str(soup.select_one("#bodyContent").text)

                # Filename for audio
                audio_file = os.getcwd() + "\\audio\\" + text[:50] \
                    .replace(":", "") \
                    .replace(" ", "") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "") + '.mp3'

                try:
                    # Convert text to audio
                    tts = gTTS(text.replace("", "")
                               .replace(".", "")
                               .replace("©", "")
                               .replace("*", "")
                               .replace("-", " ")
                               .replace("✔", "")
                               .replace("•", "")
                               .replace("⇒", "")
                               .replace("↑", "")
                               .replace("→", ""))

                    # Save the audio
                    tts.save(audio_file)

                except Exception as e:
                    print("exit tts 1 : " + str(e))

                # Folder of images
                image_folder = os.getcwd() + '\\images'

                # Create images from the text
                number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
                number_of_caracters_per_line = 110

                number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                number_of_lines = 0

                if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                    number_of_lines += round(number_of_lines_with_coma) + 1

                elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                    number_of_lines += round(number_of_lines_with_coma)

                number_of_lines_per_image = 10

                number_of_images_with_coma = number_of_lines / number_of_lines_per_image
                number_of_images = 0

                if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                    number_of_images += round(number_of_images_with_coma) + 1

                elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                    number_of_images += round(number_of_images_with_coma)

                # Array duration of each clip
                durations_of_each_clip = [0]

                l = 0

                duration = 0

                for i in range(1, number_of_images + 1):
                    img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                    d = ImageDraw.Draw(img)

                    if l <= number_of_lines:
                        for j in range(0, 10):
                            depart = 110 * l
                            arrivee = 110 + 110 * l
                            coordinate_y = 25 * j

                            if j < 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 1 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(
                                            MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                            elif j == 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 2 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        img.save(image_folder + "\\" + str(i) + ".png")

                                        durations_of_each_clip.append(duration)

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                # Appending the images to the video one by one
                images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                for i in range(1, number_of_images + 1):
                    try:
                        frame = cv2.imread(os.path.join(image_folder, images[0]))

                        # setting the frame width, height width the width, height of first image
                        height, width, layers = frame.shape

                        # video to create
                        video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0,
                                                1,
                                                (width, height))

                        for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                            video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                + "\\" + str(i) + ".png")))

                        # Deallocating memories taken for window creation
                        cv2.destroyAllWindows()

                        # releasing the video generated
                        video.release()

                    except Exception as e:
                        print("error video write : " + str(e))

                clips = []

                for i in range(1, number_of_images + 1):
                    try:
                        clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                     .set_start(durations_of_each_clip[i - 1]))
                    except Exception as e:
                        print("Error to append videos : " + str(e))

                try:
                    CompositeVideoClip(clips).write_videofile(
                        os.getcwd() + '\\videos\\my_concatenation.mp4')
                except Exception as e:
                    print("Error CompositeVideoClip : " + str(e))

                try:
                    output_movie = os.getcwd() + "\\videos_creees\\" + directory + "\\" + title
                    ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie,
                                             vcodec='copy', acodec='copy',
                                             ffmpeg_output=False, logger='bar')
                except Exception as e:
                    print("output movie exception : " + str(e))
        finally:
            # Delete all images
            for i in range(1, number_of_images + 1):
                os.remove(image_folder + "\\" + str(i) + ".png")

            # Delete all clips
            for i in range(1, number_of_images + 1):
                os.remove(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')

            os.remove(os.getcwd() + '\\videos\\my_concatenation.mp4')
            os.remove(audio_file)

    def test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_glossary_of_areas_of_mathematics(self):
        print("test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_glossary_of_areas_of_mathematics")

        audio_file = ""
        image_folder = ""
        number_of_images = ""
        directory = "mathematics"

        '''
        "https://en.wikipedia.org/wiki/Computational_mathematics",
        "https://en.wikipedia.org/wiki/Computational_number_theory",
        "https://en.wikipedia.org/wiki/Computational_statistics",
        "https://en.wikipedia.org/wiki/Synthetic_geometry",
        "https://en.wikipedia.org/wiki/Computational_topology",
        "https://en.wikipedia.org/wiki/Computer_algebra",
        "https://en.wikipedia.org/wiki/Conformal_geometry",
        "https://en.wikipedia.org/wiki/Constructive_analysis",
        "https://en.wikipedia.org/wiki/Constructive_function_theory",
        "https://en.wikipedia.org/wiki/Constructivism_(philosophy_of_mathematics)",
        "https://en.wikipedia.org/wiki/Constructive_quantum_field_theory",
        "https://en.wikipedia.org/wiki/Constructive_set_theory",
        "https://en.wikipedia.org/wiki/Contact_geometry",
        "https://en.wikipedia.org/wiki/Convex_analysis",
        "https://en.wikipedia.org/wiki/Convex_geometry",
        '''

        try:
            urls = [
                "https://en.wikipedia.org/wiki/Analytic_geometry",
                "https://en.wikipedia.org/wiki/CR_manifold",
                "https://en.wikipedia.org/wiki/Cryptography",
                "https://en.wikipedia.org/wiki/Decision_analysis",
                "https://en.wikipedia.org/wiki/Decision_theory",
                "https://en.wikipedia.org/wiki/Noncommutative_algebraic_geometry",
                "https://en.wikipedia.org/wiki/Descriptive_set_theory",
                "https://en.wikipedia.org/wiki/Differential_algebraic_geometry",
                "https://en.wikipedia.org/wiki/Differential_calculus",
                "https://en.wikipedia.org/wiki/Differential_Galois_theory",
                "https://en.wikipedia.org/wiki/Differential_geometry",
                "https://en.wikipedia.org/wiki/Differentiable_curve",
                "https://en.wikipedia.org/wiki/Differential_geometry_of_surfaces",
                "https://en.wikipedia.org/wiki/Differential_topology",
                "https://en.wikipedia.org/wiki/Diffiety",
                "https://en.wikipedia.org/wiki/Diophantine_geometry",
                "https://en.wikipedia.org/wiki/Discrepancy_theory",
                "https://en.wikipedia.org/wiki/Discrete_differential_geometry",
                "https://en.wikipedia.org/wiki/Discrete_exterior_calculus",
                "https://en.wikipedia.org/wiki/Discrete_geometry",
                "https://en.wikipedia.org/wiki/Discrete_mathematics",
                "https://en.wikipedia.org/wiki/Discrete_Morse_theory",
                "https://en.wikipedia.org/wiki/Distance_geometry",
                "https://en.wikipedia.org/wiki/Domain_theory",
                "https://en.wikipedia.org/wiki/Donaldson_theory",
                "https://en.wikipedia.org/wiki/Dynamical_systems_theory",
                "https://en.wikipedia.org/wiki/Econometrics",
                "https://en.wikipedia.org/wiki/Effective_descriptive_set_theory",
                "https://en.wikipedia.org/wiki/Elementary_algebra",
                "https://en.wikipedia.org/wiki/Elementary_arithmetic",
                "https://en.wikipedia.org/wiki/Elementary_mathematics",
                "https://en.wikipedia.org/wiki/Group_(mathematics)",
                "https://en.wikipedia.org/wiki/Elimination_theory",
                "https://en.wikipedia.org/wiki/Elliptic_geometry",
                "https://en.wikipedia.org/wiki/Enumerative_combinatorics",
                "https://en.wikipedia.org/wiki/Enumerative_geometry",
                "https://en.wikipedia.org/wiki/Epidemiology",
                "https://en.wikipedia.org/wiki/Noncommutative_algebraic_geometry",
                "https://en.wikipedia.org/wiki/Ergodic_Ramsey_theory",
                "https://en.wikipedia.org/wiki/Ergodic_theory",
                "https://en.wikipedia.org/wiki/Euclidean_geometry",
                "https://en.wikipedia.org/wiki/Euler_calculus",
                "https://en.wikipedia.org/wiki/Experimental_mathematics",
                "https://en.wikipedia.org/wiki/Cohomology",
                "https://en.wikipedia.org/wiki/Extremal_combinatorics",
                "https://en.wikipedia.org/wiki/Extremal_graph_theory",
                "https://en.wikipedia.org/wiki/Anabelian_geometry",
                "https://en.wikipedia.org/wiki/Mathematical_analysis",
                "https://en.wikipedia.org/wiki/Symbolic_method_(combinatorics)",
                "https://en.wikipedia.org/wiki/Analytic_geometry",
                "https://en.wikipedia.org/wiki/Analytic_number_theory",
                "https://en.wikipedia.org/wiki/Applied_mathematics",
                "https://en.wikipedia.org/wiki/Approximation_theory",
                "https://en.wikipedia.org/wiki/Arakelov_theory",
                "https://en.wikipedia.org/wiki/Arithmetic",
                "https://en.wikipedia.org/wiki/Arithmetic_geometry",
                "https://en.wikipedia.org/wiki/Arithmetic_combinatorics",
                "https://en.wikipedia.org/wiki/Arithmetic_dynamics",
                "https://en.wikipedia.org/wiki/Arithmetic_topology",
                "https://en.wikipedia.org/wiki/Assignment_problem",
                "https://en.wikipedia.org/wiki/Asymptotic_analysis",
                "https://en.wikipedia.org/wiki/Auslander%E2%80%93Reiten_theory",
                "https://en.wikipedia.org/wiki/Set_theory",
                "https://en.wikipedia.org/wiki/Bifurcation_theory",
                "https://en.wikipedia.org/wiki/Biostatistics",
                "https://en.wikipedia.org/wiki/Birational_geometry",
                "https://en.wikipedia.org/wiki/C*-algebra",
                "https://en.wikipedia.org/wiki/Analytic_geometry",
                "https://en.wikipedia.org/wiki/Calculus",
                "https://en.wikipedia.org/wiki/Calculus_of_moving_surfaces",
                "https://en.wikipedia.org/wiki/Calculus_of_variations",
                "https://en.wikipedia.org/wiki/Catastrophe_theory",
                "https://en.wikipedia.org/wiki/Categorical_logic",
                "https://en.wikipedia.org/wiki/Category_theory",
                "https://en.wikipedia.org/wiki/Character_theory",
                "https://en.wikipedia.org/wiki/Class_field_theory",
                "https://en.wikipedia.org/wiki/Algebraic_topology",
                "https://en.wikipedia.org/wiki/Mathematical_analysis",
                "https://en.wikipedia.org/wiki/Invariant_theory",
                "https://en.wikipedia.org/wiki/Classical_mathematics",
                "https://en.wikipedia.org/wiki/Projective_geometry",
                "https://en.wikipedia.org/wiki/Tensor",
                "https://en.wikipedia.org/wiki/Clifford_analysis",
                "https://en.wikipedia.org/wiki/Clifford_theory",
                "https://en.wikipedia.org/wiki/Cobordism",
                "https://en.wikipedia.org/wiki/Coding_theory",
                "https://en.wikipedia.org/wiki/Cohomology",
                "https://en.wikipedia.org/wiki/Combinatorial_commutative_algebra",
                "https://en.wikipedia.org/wiki/Combinatorial_design",
                "https://en.wikipedia.org/wiki/Combinatorial_game_theory",
                "https://en.wikipedia.org/wiki/Combinatorial_group_theory",
                "https://en.wikipedia.org/wiki/Combinatorics",
                "https://en.wikipedia.org/wiki/Number_theory",
                "https://en.wikipedia.org/wiki/Combinatorial_topology",
                "https://en.wikipedia.org/wiki/Commutative_algebra",
                "https://en.wikipedia.org/wiki/Field_of_sets",
                "https://en.wikipedia.org/wiki/Algebraic_geometry",
                "https://en.wikipedia.org/wiki/Complex_analysis",
                "https://en.wikipedia.org/wiki/Complex_dynamics",
                "https://en.wikipedia.org/wiki/Complex_geometry",
                "https://en.wikipedia.org/wiki/Complexity_theory",
                "https://en.wikipedia.org/wiki/Computable_analysis",
                "https://en.wikipedia.org/wiki/Computable_model_theory",
                "https://en.wikipedia.org/wiki/Computability_theory",
                "https://en.wikipedia.org/wiki/Computational_geometry",
                "https://en.wikipedia.org/wiki/Computational_group_theory",
                "https://en.wikipedia.org/wiki/Algebraic_number_theory",
                "https://en.wikipedia.org/wiki/Algebraic_statistics",
                "https://en.wikipedia.org/wiki/Algebra",
                "https://en.wikipedia.org/wiki/Algebraic_analysis",
                "https://en.wikipedia.org/wiki/Algebraic_combinatorics",
                "https://en.wikipedia.org/wiki/Computer_algebra",
                "https://en.wikipedia.org/wiki/Algebraic_graph_theory",
                "https://en.wikipedia.org/wiki/Algebraic_K-theory",
                "https://en.wikipedia.org/wiki/Abstract_algebra",
                "https://en.wikipedia.org/wiki/Abstract_analytic_number_theory",
                "https://en.wikipedia.org/wiki/Abstract_differential_geometry",
                "https://en.wikipedia.org/wiki/Homotopy_theory",
                "https://en.wikipedia.org/wiki/Absolute_geometry",
                "https://en.wikipedia.org/wiki/Field_(mathematics)",
                "https://en.wikipedia.org/wiki/Finite_geometry",
                "https://en.wikipedia.org/wiki/Finite_model_theory",
                "https://en.wikipedia.org/wiki/Finsler_manifold",
                "https://en.wikipedia.org/wiki/Fourier_analysis",
                "https://en.wikipedia.org/wiki/Fractal",
                "https://en.wikipedia.org/wiki/Fractional_calculus",
                "https://en.wikipedia.org/wiki/Fractional-order_system",
                "https://en.wikipedia.org/wiki/Fredholm_theory",
                "https://en.wikipedia.org/wiki/Functional_analysis",
                "https://en.wikipedia.org/wiki/Functional_calculus",
                "https://en.wikipedia.org/wiki/Fuzzy_mathematics",
                "https://en.wikipedia.org/wiki/Fuzzy_measure_theory",
                "https://en.wikipedia.org/wiki/Fuzzy_set",
                "https://en.wikipedia.org/wiki/Galois_cohomology",
                "https://en.wikipedia.org/wiki/Galois_theory",
                "https://en.wikipedia.org/wiki/Galois_geometry",
                "https://en.wikipedia.org/wiki/Group_representation",
                "https://en.wikipedia.org/wiki/Group_theory",
                "https://en.wikipedia.org/wiki/Gyrovector_space",
                "https://en.wikipedia.org/wiki/Harmonic_analysis",
                "https://en.wikipedia.org/wiki/Higher_category_theory",
                "https://en.wikipedia.org/wiki/Higher-dimensional_algebra",
                "https://en.wikipedia.org/wiki/Hodge_theory",
                "https://en.wikipedia.org/wiki/Holomorphic_functional_calculus",
                "https://en.wikipedia.org/wiki/Homological_algebra",
                "https://en.wikipedia.org/wiki/Homology_(mathematics)",
                "https://en.wikipedia.org/wiki/Hyperbolic_geometry",
                "https://en.wikipedia.org/wiki/Hypercomplex_analysis",
                "https://en.wikipedia.org/wiki/Hyperfunction",
                "https://en.wikipedia.org/wiki/Ideal_theory",
                "https://en.wikipedia.org/wiki/Idempotent_analysis",
                "https://en.wikipedia.org/wiki/Incidence_geometry",
                "https://en.wikipedia.org/wiki/Paraconsistent_mathematics",
                "https://en.wikipedia.org/wiki/Infinitary_combinatorics",
                "https://en.wikipedia.org/wiki/Calculus",
                "https://en.wikipedia.org/wiki/Information_geometry",
                "https://en.wikipedia.org/wiki/Integral",
                "https://en.wikipedia.org/wiki/Integral_geometry",
                "https://en.wikipedia.org/wiki/Intersection_theory",
                "https://en.wikipedia.org/wiki/Intuitionistic_type_theory",
                "https://en.wikipedia.org/wiki/Invariant_theory",
                "https://en.wikipedia.org/wiki/Inventory_theory",
                "https://en.wikipedia.org/wiki/Inversive_geometry",
                "https://en.wikipedia.org/wiki/Projective_line_over_a_ring",
                "https://en.wikipedia.org/wiki/It%C3%B4_calculus",
                "https://en.wikipedia.org/wiki/Iwasawa_theory",
                "https://en.wikipedia.org/wiki/Job_shop_scheduling",
                "https://en.wikipedia.org/wiki/K-theory",
                "https://en.wikipedia.org/wiki/K-homology",
                "https://en.wikipedia.org/wiki/K%C3%A4hler_manifold",
                "https://en.wikipedia.org/wiki/KK-theory",
                "https://en.wikipedia.org/wiki/Klein_geometry",
                "https://en.wikipedia.org/wiki/Knot_theory",
                "https://en.wikipedia.org/wiki/Kummer_theory",
                "https://en.wikipedia.org/wiki/L-theory",
                "https://en.wikipedia.org/wiki/Large_deviations_theory",
                "https://en.wikipedia.org/wiki/Asymptotic_theory_(statistics)",
                "https://en.wikipedia.org/wiki/Lattice_(order)",
                "https://en.wikipedia.org/wiki/Lie_group",
                "https://en.wikipedia.org/wiki/Lie_sphere_geometry",
                "https://en.wikipedia.org/wiki/Lie_theory",
                "https://en.wikipedia.org/wiki/Line_coordinates",
                "https://en.wikipedia.org/wiki/Linear_algebra",
                "https://en.wikipedia.org/wiki/Functional_analysis",
                "https://en.wikipedia.org/wiki/Linear_programming",
                "https://en.wikipedia.org/wiki/List_of_graphical_methods",
                "https://en.wikipedia.org/wiki/Local_ring",
                "https://en.wikipedia.org/wiki/Local_class_field_theory",
                "https://en.wikipedia.org/wiki/Low-dimensional_topology",
                "https://en.wikipedia.org/wiki/Malliavin_calculus",
                "https://en.wikipedia.org/wiki/Mathematical_and_theoretical_biology",
                "https://en.wikipedia.org/wiki/Mathematical_chemistry",
                "https://en.wikipedia.org/wiki/Mathematical_economics",
                "https://en.wikipedia.org/wiki/Mathematical_finance",
                "https://en.wikipedia.org/wiki/Mathematical_logic",
                "https://en.wikipedia.org/wiki/Mathematical_optimization",
                "https://en.wikipedia.org/wiki/Mathematical_physics",
                "https://en.wikipedia.org/wiki/Mathematical_psychology",
                "https://en.wikipedia.org/wiki/Mathematical_sciences",
                "https://en.wikipedia.org/wiki/Mathematical_sociology",
                "https://en.wikipedia.org/wiki/Mathematical_statistics",
                "https://en.wikipedia.org/wiki/Dynamical_systems_theory",
                "https://en.wikipedia.org/wiki/Matrix_ring",
                "https://en.wikipedia.org/wiki/Matrix_calculus",
                "https://en.wikipedia.org/wiki/Matrix_(mathematics)",
                "https://en.wikipedia.org/wiki/Matroid",
                "https://en.wikipedia.org/wiki/Measure_(mathematics)",
                "https://en.wikipedia.org/wiki/Metric_space",
                "https://en.wikipedia.org/wiki/Microlocal_analysis",
                "https://en.wikipedia.org/wiki/Model_theory",
                "https://en.wikipedia.org/wiki/Abstract_algebra",
                "https://en.wikipedia.org/wiki/Scheme_(mathematics)",
                "https://en.wikipedia.org/wiki/Invariant_theory",
                "https://en.wikipedia.org/wiki/Modular_representation_theory",
                "https://en.wikipedia.org/wiki/Module_(mathematics)",
                "https://en.wikipedia.org/wiki/Molecular_geometry",
                "https://en.wikipedia.org/wiki/Morse_theory",
                "https://en.wikipedia.org/wiki/Motivic_cohomology",
                "https://en.wikipedia.org/wiki/Multilinear_algebra",
                "https://en.wikipedia.org/wiki/Multiplicative_number_theory",
                "https://en.wikipedia.org/wiki/Multivariable_calculus",
                "https://en.wikipedia.org/wiki/Multiple-scale_analysis",
                "https://en.wikipedia.org/wiki/Absolute_geometry",
                "https://en.wikipedia.org/wiki/Nevanlinna_theory",
                "https://en.wikipedia.org/wiki/Nielsen_theory",
                "https://en.wikipedia.org/wiki/Non-abelian_class_field_theory",
                "https://en.wikipedia.org/wiki/Non-classical_analysis",
                "https://en.wikipedia.org/wiki/Non-Euclidean_geometry",
                "https://en.wikipedia.org/wiki/Nonstandard_analysis",
                "https://en.wikipedia.org/wiki/Nonstandard_calculus",
                "https://en.wikipedia.org/wiki/Arithmetic_dynamics",
                "https://en.wikipedia.org/wiki/Noncommutative_algebraic_geometry",
                "https://en.wikipedia.org/wiki/Noncommutative_geometry",
                "https://en.wikipedia.org/wiki/Noncommutative_harmonic_analysis",
                "https://en.wikipedia.org/wiki/Noncommutative_topology",
                "https://en.wikipedia.org/wiki/Nonlinear_functional_analysis",
                "https://en.wikipedia.org/wiki/Number_theory",
                "https://en.wikipedia.org/wiki/Numerical_analysis",
                "https://en.wikipedia.org/wiki/Numerical_linear_algebra",
                "https://en.wikipedia.org/wiki/Operad",
                "https://en.wikipedia.org/wiki/Operations_research",
                "https://en.wikipedia.org/wiki/Operator_K-theory",
                "https://en.wikipedia.org/wiki/Operator_theory",
                "https://en.wikipedia.org/wiki/Optimal_control",
                "https://en.wikipedia.org/wiki/Optimal_maintenance",
                "https://en.wikipedia.org/wiki/Order_theory",
                "https://en.wikipedia.org/wiki/Ordered_geometry",
                "https://en.wikipedia.org/wiki/Oscillation_theory",
                "https://en.wikipedia.org/wiki/P-adic_analysis",
                "https://en.wikipedia.org/wiki/P-adic_Hodge_theory",
                "https://en.wikipedia.org/wiki/Parabolic_geometry",
                "https://en.wikipedia.org/wiki/Paraconsistent_mathematics",
                "https://en.wikipedia.org/wiki/Partition_(number_theory)",
                "https://en.wikipedia.org/wiki/Perturbation_theory",
                "https://en.wikipedia.org/wiki/Picard%E2%80%93Vessiot_theory",
                "https://en.wikipedia.org/wiki/Euclidean_geometry",
                "https://en.wikipedia.org/wiki/General_topology",
                "https://en.wikipedia.org/wiki/Pointless_topology",
                "https://en.wikipedia.org/wiki/Poisson_manifold",
                "https://en.wikipedia.org/wiki/Polyhedral_combinatorics",
                "https://en.wikipedia.org/wiki/Possibility_theory",
                "https://en.wikipedia.org/wiki/Potential_theory",
                "https://en.wikipedia.org/wiki/Precalculus",
                "https://en.wikipedia.org/wiki/Impredicativity",
                "https://en.wikipedia.org/wiki/Probability_theory",
                "https://en.wikipedia.org/wiki/Probabilistic_method",
                "https://en.wikipedia.org/wiki/Random_graph",
                "https://en.wikipedia.org/wiki/Probabilistic_number_theory",
                "https://en.wikipedia.org/wiki/Projective_geometry",
                "https://en.wikipedia.org/wiki/Projective_differential_geometry",
                "https://en.wikipedia.org/wiki/Proof_theory",
                "https://en.wikipedia.org/wiki/Pseudo-Riemannian_manifold",
                "https://en.wikipedia.org/wiki/Pure_mathematics",
                "https://en.wikipedia.org/wiki/Quantum_calculus",
                "https://en.wikipedia.org/wiki/Quantum_geometry",
                "https://en.wikipedia.org/wiki/Quaternion",
                "https://en.wikipedia.org/wiki/Ramsey_theory",
                "https://en.wikipedia.org/wiki/Rational_trigonometry",
                "https://en.wikipedia.org/wiki/Real_algebraic_geometry",
                "https://en.wikipedia.org/wiki/Real_analysis",
                "https://en.wikipedia.org/wiki/K-theory",
                "https://en.wikipedia.org/wiki/Recreational_mathematics",
                "https://en.wikipedia.org/wiki/Computability_theory",
                "https://en.wikipedia.org/wiki/Representation_theory",
                "https://en.wikipedia.org/wiki/Algebra_representation",
                "https://en.wikipedia.org/wiki/Representation_theory_of_diffeomorphism_groups",
                "https://en.wikipedia.org/wiki/Representation_theory_of_finite_groups",
                "https://en.wikipedia.org/wiki/Group_representation",
                "https://en.wikipedia.org/wiki/Representation_theory_of_Hopf_algebras",
                "https://en.wikipedia.org/wiki/Lie_algebra_representation",
                "https://en.wikipedia.org/wiki/Representation_of_a_Lie_group",
                "https://en.wikipedia.org/wiki/Representation_theory_of_the_Galilean_group",
                "https://en.wikipedia.org/wiki/Representation_theory_of_the_Lorentz_group",
                "https://en.wikipedia.org/wiki/Representation_theory_of_the_Poincar%C3%A9_group",
                "https://en.wikipedia.org/wiki/Representation_theory_of_the_symmetric_group",
                "https://en.wikipedia.org/wiki/Ribbon_theory",
                "https://en.wikipedia.org/wiki/Riemannian_geometry",
                "https://en.wikipedia.org/wiki/Rough_set",
                "https://en.wikipedia.org/wiki/Sampling_(statistics)",
                "https://en.wikipedia.org/wiki/Scheme_(mathematics)",
                "https://en.wikipedia.org/wiki/Secondary_calculus_and_cohomological_physics",
                "https://en.wikipedia.org/wiki/Self-similarity",
                "https://en.wikipedia.org/wiki/Set-theoretic_topology",
                "https://en.wikipedia.org/wiki/Set_theory",
                "https://en.wikipedia.org/wiki/Sheaf_(mathematics)",
                "https://en.wikipedia.org/wiki/Sheaf_cohomology",
                "https://en.wikipedia.org/wiki/Sieve_theory",
                "https://en.wikipedia.org/wiki/Operator_theory",
                "https://en.wikipedia.org/wiki/Singularity_theory",
                "https://en.wikipedia.org/wiki/Smooth_infinitesimal_analysis",
                "https://en.wikipedia.org/wiki/Solid_geometry",
                "https://en.wikipedia.org/wiki/Three-dimensional_space",
                "https://en.wikipedia.org/wiki/Spectral_geometry",
                "https://en.wikipedia.org/wiki/Spectral_graph_theory",
                "https://en.wikipedia.org/wiki/Spectral_theory",
                "https://en.wikipedia.org/wiki/Spectral_theory_of_ordinary_differential_equations",
                "https://en.wikipedia.org/wiki/Spectrum_continuation_analysis",
                "https://en.wikipedia.org/wiki/Spherical_geometry",
                "https://en.wikipedia.org/wiki/Spherical_trigonometry",
                "https://en.wikipedia.org/wiki/Statistical_mechanics",
                "https://en.wikipedia.org/wiki/Statistical_model",
                "https://en.wikipedia.org/wiki/Statistical_theory",
                "https://en.wikipedia.org/wiki/Mathematical_statistics",
                "https://en.wikipedia.org/wiki/Steganography",
                "https://en.wikipedia.org/wiki/Stochastic_calculus",
                "https://en.wikipedia.org/wiki/Malliavin_calculus",
                "https://en.wikipedia.org/wiki/Stochastic_geometry",
                "https://en.wikipedia.org/wiki/Stochastic_process",
                "https://en.wikipedia.org/wiki/Stratified_Morse_theory",
                "https://en.wikipedia.org/wiki/Super_vector_space",
                "https://en.wikipedia.org/wiki/Surgery_theory",
                "https://en.wikipedia.org/wiki/Survey_sampling",
                "https://en.wikipedia.org/wiki/Survey_methodology",
                "https://en.wikipedia.org/wiki/Computer_algebra",
                "https://en.wikipedia.org/wiki/Symbolic_dynamics",
                "https://en.wikipedia.org/wiki/Symplectic_geometry",
                "https://en.wikipedia.org/wiki/Synthetic_differential_geometry",
                "https://en.wikipedia.org/wiki/Synthetic_geometry",
                "https://en.wikipedia.org/wiki/Systolic_geometry",
                "https://en.wikipedia.org/wiki/Tensor_field",
                "https://en.wikipedia.org/wiki/Tensor_calculus",
                "https://en.wikipedia.org/wiki/Tessellation",
                "https://en.wikipedia.org/wiki/Theoretical_physics",
                "https://en.wikipedia.org/wiki/Theory_of_computation",
                "https://en.wikipedia.org/wiki/Time-scale_calculus",
                "https://en.wikipedia.org/wiki/Topology",
                "https://en.wikipedia.org/wiki/Topological_combinatorics",
                "https://en.wikipedia.org/wiki/Topological_degree_theory",
                "https://en.wikipedia.org/wiki/Topological_graph_theory",
                "https://en.wikipedia.org/wiki/Topological_K-theory",
                "https://en.wikipedia.org/wiki/Topos",
                "https://en.wikipedia.org/wiki/Toric_variety",
                "https://en.wikipedia.org/wiki/Transcendental_number_theory",
                "https://en.wikipedia.org/wiki/Transformation_geometry",
                "https://en.wikipedia.org/wiki/Trigonometry",
                "https://en.wikipedia.org/wiki/Tropical_analysis",
                "https://en.wikipedia.org/wiki/Tropical_geometry",
                "https://en.wikipedia.org/wiki/Twisted_K-theory",
                "https://en.wikipedia.org/wiki/Type_theory",
                "https://en.wikipedia.org/wiki/Umbral_calculus",
                "https://en.wikipedia.org/wiki/Uncertainty_theory",
                "https://en.wikipedia.org/wiki/Universal_algebra",
                "https://en.wikipedia.org/wiki/Rational_trigonometry",
                "https://en.wikipedia.org/wiki/Valuation_(algebra)",
                "https://en.wikipedia.org/wiki/Variational_analysis",
                "https://en.wikipedia.org/wiki/Vector_calculus",
                "https://en.wikipedia.org/wiki/Wavelet",
                "https://en.wikipedia.org/wiki/Short-time_Fourier_transform",
                "https://en.wikipedia.org/wiki/Window_function"
            ]

            for url in urls:
                # Request the content of a page from the url
                html = requests.get(url)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                # title of the movie
                title = ""

                if soup.select_one("#firstHeading") is not None:
                    title += str(soup.select_one("#firstHeading")
                                 .text
                                 .lower()
                                 .replace(" ", "_")
                                 .replace("/", "_")
                                 .replace("-", "_")
                                 .replace(":", "_")
                                 .replace("\n", "")
                                 .replace("?", "")
                                 ) + ".avi"

                    print("title : " + title)

                # Text to speech and images
                text = ""

                if soup.select_one("#bodyContent") is not None:
                    text += str(soup.select_one("#bodyContent").text)

                # Filename for audio
                audio_file = os.getcwd() + "\\audio\\" + text[:50] \
                    .replace(":", "") \
                    .replace(" ", "") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "") + '.mp3'

                try:
                    # Convert text to audio
                    tts = gTTS(text.replace("", "")
                               .replace(".", "")
                               .replace("©", "")
                               .replace("*", "")
                               .replace("-", " ")
                               .replace("✔", "")
                               .replace("•", "")
                               .replace("⇒", "")
                               .replace("↑", "")
                               .replace("→", ""))

                    # Save the audio
                    tts.save(audio_file)
                except Exception as e:
                    print("error convert text to audio")

                # Folder of images
                image_folder = os.getcwd() + '\\images'

                # Create images from the text
                number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
                number_of_caracters_per_line = 110

                number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                number_of_lines = 0

                if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                    number_of_lines += round(number_of_lines_with_coma) + 1

                elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                    number_of_lines += round(number_of_lines_with_coma)

                number_of_lines_per_image = 10

                number_of_images_with_coma = number_of_lines / number_of_lines_per_image
                number_of_images = 0

                if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                    number_of_images += round(number_of_images_with_coma) + 1

                elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                    number_of_images += round(number_of_images_with_coma)

                # Array duration of each clip
                durations_of_each_clip = [0]

                l = 0

                duration = 0

                for i in range(1, number_of_images + 1):
                    img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                    d = ImageDraw.Draw(img)

                    if l <= number_of_lines:
                        for j in range(0, 10):
                            depart = 110 * l
                            arrivee = 110 + 110 * l
                            coordinate_y = 25 * j

                            if j < 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 1 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(
                                            MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                            elif j == 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 2 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        img.save(image_folder + "\\" + str(i) + ".png")

                                        durations_of_each_clip.append(duration)

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                # Appending the images to the video one by one
                images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                for i in range(1, number_of_images + 1):
                    try:
                        frame = cv2.imread(os.path.join(image_folder, images[0]))

                        # setting the frame width, height width the width, height of first image
                        height, width, layers = frame.shape

                        # video to create
                        video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0,
                                                1,
                                                (width, height))

                        for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                            video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                + "\\" + str(i) + ".png")))

                        # Deallocating memories taken for window creation
                        cv2.destroyAllWindows()

                        # releasing the video generated
                        video.release()

                    except Exception as e:
                        print("error video write : " + str(e))

                clips = []

                for i in range(1, number_of_images + 1):
                    try:
                        clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                     .set_start(durations_of_each_clip[i - 1]))
                    except Exception as e:
                        print("Error to append videos : " + str(e))

                try:
                    CompositeVideoClip(clips).write_videofile(
                        os.getcwd() + '\\videos\\my_concatenation.mp4')
                except Exception as e:
                    print("Error CompositeVideoClip : " + str(e))

                try:
                    output_movie = os.getcwd() + "\\videos_creees\\" + directory + "\\" + title
                    ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie,
                                             vcodec='copy', acodec='copy',
                                             ffmpeg_output=False, logger='bar')
                except Exception as e:
                    print("output movie exception : " + str(e))
        finally:
            # Delete all images
            for i in range(1, number_of_images + 1):
                os.remove(image_folder + "\\" + str(i) + ".png")

            # Delete all clips
            for i in range(1, number_of_images + 1):
                os.remove(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')

            os.remove(os.getcwd() + '\\videos\\my_concatenation.mp4')
            os.remove(audio_file)

    def test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_glossary_of_astronomy(self):
        print("test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_glossary_of_astronomy")

        audio_file = ""
        image_folder = ""
        number_of_images = ""
        directory = "astronomy"

        try:
            urls = [
                "https://en.wikipedia.org/wiki/Asteroid",
                "https://en.wikipedia.org/wiki/Asteroid_belt",
                "https://en.wikipedia.org/wiki/Astrobiology",
                "https://en.wikipedia.org/wiki/Orbital_mechanics",
                "https://en.wikipedia.org/wiki/Planetary_geology",
                "https://en.wikipedia.org/wiki/Stellar_classification",
                "https://en.wikipedia.org/wiki/Absolute_magnitude",
                "https://en.wikipedia.org/wiki/Accretion_disk",
                "https://en.wikipedia.org/wiki/Active_galactic_nucleus",
                "https://en.wikipedia.org/wiki/Albedo",
                "https://en.wikipedia.org/wiki/Albedo_feature",
                "https://en.wikipedia.org/wiki/Am_star",
                "https://en.wikipedia.org/wiki/Apsis",
                "https://en.wikipedia.org/wiki/Apparent_magnitude",
                "https://en.wikipedia.org/wiki/Appulse",
                "https://en.wikipedia.org/wiki/Argument_of_periapsis",
                "https://en.wikipedia.org/wiki/Satellite",
                "https://en.wikipedia.org/wiki/Orbital_node",
                "https://en.wikipedia.org/wiki/Asterism_(astronomy)",
                "https://en.wikipedia.org/wiki/Binary_star",
                "https://en.wikipedia.org/wiki/Astrometry",
                "https://en.wikipedia.org/wiki/Astronomical_object",
                "https://en.wikipedia.org/wiki/Astronomical_catalog",
                "https://en.wikipedia.org/wiki/Astronomical_symbols",
                "https://en.wikipedia.org/wiki/Astronomical_unit",
                "https://en.wikipedia.org/wiki/Astronomy",
                "https://en.wikipedia.org/wiki/Astrophotography",
                "https://en.wikipedia.org/wiki/Astrophysics",
                "https://en.wikipedia.org/wiki/Atmosphere",
                "https://en.wikipedia.org/wiki/Axial_precession",
                "https://en.wikipedia.org/wiki/Axial_tilt",
                "https://en.wikipedia.org/wiki/Rotation_around_a_fixed_axis",
                "https://en.wikipedia.org/wiki/Azimuth",
                "https://en.wikipedia.org/wiki/Barycenter",
                "https://en.wikipedia.org/wiki/Baryogenesis",
                "https://en.wikipedia.org/wiki/Big_Bang",
                "https://en.wikipedia.org/wiki/Binary_star",
                "https://en.wikipedia.org/wiki/Black_hole",
                "https://en.wikipedia.org/wiki/Blazar",
                "https://en.wikipedia.org/wiki/Brown_dwarf",
                "https://en.wikipedia.org/wiki/Bulge_(astronomy)",
                "https://en.wikipedia.org/wiki/Celestial_equator",
                "https://en.wikipedia.org/wiki/Celestial_mechanics",
                "https://en.wikipedia.org/wiki/Celestial_pole",
                "https://en.wikipedia.org/wiki/Celestial_sphere",
                "https://en.wikipedia.org/wiki/Centaur_(small_Solar_System_body)",
                "https://en.wikipedia.org/wiki/Central_massive_object",
                "https://en.wikipedia.org/wiki/Chromosphere",
                "https://en.wikipedia.org/wiki/Circumstellar_disc",
                "https://en.wikipedia.org/wiki/Cis-Neptunian_object",
                "https://en.wikipedia.org/wiki/Clearing_the_neighbourhood",
                "https://en.wikipedia.org/wiki/Color_index",
                "https://en.wikipedia.org/wiki/Comet",
                "https://en.wikipedia.org/wiki/Commensurability_(astronomy)",
                "https://en.wikipedia.org/wiki/Compact_star",
                "https://en.wikipedia.org/wiki/Nuclear_star_cluster",
                "https://en.wikipedia.org/wiki/Conjunction_(astronomy)",
                "https://en.wikipedia.org/wiki/Constellation",
                "https://en.wikipedia.org/wiki/Stellar_corona",
                "https://en.wikipedia.org/wiki/Coronal_mass_ejection",
                "https://en.wikipedia.org/wiki/Cosmic_distance_ladder",
                "https://en.wikipedia.org/wiki/Cosmic_dust",
                "https://en.wikipedia.org/wiki/Cosmic_microwave_background",
                "https://en.wikipedia.org/wiki/Cosmic_ray",
                "https://en.wikipedia.org/wiki/Cosmogony",
                "https://en.wikipedia.org/wiki/Cosmology",
                "https://en.wikipedia.org/wiki/Culmination",
                "https://en.wikipedia.org/wiki/Debris_disk",
                "https://en.wikipedia.org/wiki/Declination",
                "https://en.wikipedia.org/wiki/Be_star",
                "https://en.wikipedia.org/wiki/Deep-sky_object",
                "https://en.wikipedia.org/wiki/Orbital_node",
                "https://en.wikipedia.org/wiki/Detached_object",
                "https://en.wikipedia.org/wiki/Retrograde_and_prograde_motion",
                "https://en.wikipedia.org/wiki/Diurnal_motion",
                "https://en.wikipedia.org/wiki/Double_star",
                "https://en.wikipedia.org/wiki/Dwarf_planet",
                "https://en.wikipedia.org/wiki/Dwarf_star",
                "https://en.wikipedia.org/wiki/Orbital_eccentricity",
                "https://en.wikipedia.org/wiki/Ecliptic_coordinate_system",
                "https://en.wikipedia.org/wiki/Ecliptic",
                "https://en.wikipedia.org/wiki/Effective_temperature",
                "https://en.wikipedia.org/wiki/Elliptical_galaxy",
                "https://en.wikipedia.org/wiki/Elliptic_orbit",
                "https://en.wikipedia.org/wiki/Elongation_(astronomy)",
                "https://en.wikipedia.org/wiki/Ephemeris",
                "https://en.wikipedia.org/wiki/Epoch_(astronomy)",
                "https://en.wikipedia.org/wiki/Equator",
                "https://en.wikipedia.org/wiki/Equatorial_coordinate_system",
                "https://en.wikipedia.org/wiki/Equinox",
                "https://en.wikipedia.org/wiki/Escape_velocity",
                "https://en.wikipedia.org/wiki/Main_sequence",
                "https://en.wikipedia.org/wiki/Extinction_(astronomy)",
                "https://en.wikipedia.org/wiki/Extragalactic_astronomy",
                "https://en.wikipedia.org/wiki/Extrasolar_object",
                "https://en.wikipedia.org/wiki/Exoplanet",
                "https://en.wikipedia.org/wiki/Facula",
                "https://en.wikipedia.org/wiki/Field_galaxy",
                "https://en.wikipedia.org/wiki/First_light_(astronomy)",
                "https://en.wikipedia.org/wiki/First_Point_of_Aries",
                "https://en.wikipedia.org/wiki/Fixed_stars",
                "https://en.wikipedia.org/wiki/Flare_star",
                "https://en.wikipedia.org/wiki/Small_planet_radius_gap",
                "https://en.wikipedia.org/wiki/Galactic_astronomy",
                "https://en.wikipedia.org/wiki/Galactic_anticenter",
                "https://en.wikipedia.org/wiki/Galactic_Center",
                "https://en.wikipedia.org/wiki/Galactic_coordinate_system",
                "https://en.wikipedia.org/wiki/Galactic_corona",
                "https://en.wikipedia.org/wiki/Active_galactic_nucleus",
                "https://en.wikipedia.org/wiki/Galactic_year",
                "https://en.wikipedia.org/wiki/Galactic_tide",
                "https://en.wikipedia.org/wiki/Galaxy",
                "https://en.wikipedia.org/wiki/Galaxy_cluster",
                "https://en.wikipedia.org/wiki/Phase_angle_(astronomy)",
                "https://en.wikipedia.org/wiki/Photometric_system",
                "https://en.wikipedia.org/wiki/Photosphere",
                "https://en.wikipedia.org/wiki/Plane_of_reference",
                "https://en.wikipedia.org/wiki/Planet",
                "https://en.wikipedia.org/wiki/Planetary_body",
                "https://en.wikipedia.org/wiki/Planetary_differentiation",
                "https://en.wikipedia.org/wiki/Planetary_nebula",
                "https://en.wikipedia.org/wiki/Planetary_science",
                "https://en.wikipedia.org/wiki/Planetary_system",
                "https://en.wikipedia.org/wiki/Planetesimal",
                "https://en.wikipedia.org/wiki/Minor_planet",
                "https://en.wikipedia.org/wiki/Polar_orbit",
                "https://en.wikipedia.org/wiki/Axial_precession",
                "https://en.wikipedia.org/wiki/Primary_(astronomy)",
                "https://en.wikipedia.org/wiki/Retrograde_and_prograde_motion",
                "https://en.wikipedia.org/wiki/Proper_motion",
                "https://en.wikipedia.org/wiki/Protoplanet",
                "https://en.wikipedia.org/wiki/Protoplanetary_disk",
                "https://en.wikipedia.org/wiki/Protostar",
                "https://en.wikipedia.org/wiki/Pulsar",
                "https://en.wikipedia.org/wiki/Quasar",
                "https://en.wikipedia.org/wiki/Radial_velocity",
                "https://en.wikipedia.org/wiki/Radio_astronomy",
                "https://en.wikipedia.org/wiki/Astronomical_radio_source",
                "https://en.wikipedia.org/wiki/Red-giant_branch",
                "https://en.wikipedia.org/wiki/Redshift",
                "https://en.wikipedia.org/wiki/Regular_moon",
                "https://en.wikipedia.org/wiki/Right_ascension",
                "https://en.wikipedia.org/wiki/Ring_system",
                "https://en.wikipedia.org/wiki/Roche_limit",
                "https://en.wikipedia.org/wiki/Rogue_planet",
                "https://en.wikipedia.org/wiki/Opacity_(optics)",
                "https://en.wikipedia.org/wiki/Rotation_period",
                "https://en.wikipedia.org/wiki/Satellite_galaxy",
                "https://en.wikipedia.org/wiki/Scattered_disc",
                "https://en.wikipedia.org/wiki/Secular_variation",
                "https://en.wikipedia.org/wiki/Semi-major_and_semi-minor_axes",
                "https://en.wikipedia.org/wiki/September_equinox",
                "https://en.wikipedia.org/wiki/Sidereal_time",
                "https://en.wikipedia.org/wiki/Orbital_period",
                "https://en.wikipedia.org/wiki/Sidereal_time",
                "https://en.wikipedia.org/wiki/Sidereal_year",
                "https://en.wikipedia.org/wiki/Sky",
                "https://en.wikipedia.org/wiki/Small_Solar_System_body",
                "https://en.wikipedia.org/wiki/Solar_eclipse",
                "https://en.wikipedia.org/wiki/Solar_flare",
                "https://en.wikipedia.org/wiki/Solar_mass",
                "https://en.wikipedia.org/wiki/Solar_prominence",
                "https://en.wikipedia.org/wiki/Solar_radius",
                "https://en.wikipedia.org/wiki/Solar_System",
                "https://en.wikipedia.org/wiki/Solar_time",
                "https://en.wikipedia.org/wiki/Solar_wind",
                "https://en.wikipedia.org/wiki/Solstice",
                "https://en.wikipedia.org/wiki/Astronomical_spectroscopy",
                "https://en.wikipedia.org/wiki/Speed_of_light",
                "https://en.wikipedia.org/wiki/Spherical_astronomy",
                "https://en.wikipedia.org/wiki/Spiral_galaxy",
                "https://en.wikipedia.org/wiki/Standard_gravity",
                "https://en.wikipedia.org/wiki/Star",
                "https://en.wikipedia.org/wiki/Star_catalogue",
                "https://en.wikipedia.org/wiki/Star_cluster",
                "https://en.wikipedia.org/wiki/Star_system",
                "https://en.wikipedia.org/wiki/Starburst_galaxy",
                "https://en.wikipedia.org/wiki/Stellar_atmosphere",
                "https://en.wikipedia.org/wiki/Stellar_designations_and_names",
                "https://en.wikipedia.org/wiki/Stellar_dynamics",
                "https://en.wikipedia.org/wiki/Stellar_evolution",
                "https://en.wikipedia.org/wiki/Stellar_magnetic_field",
                "https://en.wikipedia.org/wiki/Stellar_parallax",
                "https://en.wikipedia.org/wiki/Compact_star",
                "https://en.wikipedia.org/wiki/Submillimetre_astronomy",
                "https://en.wikipedia.org/wiki/Subsatellite",
                "https://en.wikipedia.org/wiki/Galaxy_group",
                "https://en.wikipedia.org/wiki/Galilean_moons",
                "https://en.wikipedia.org/wiki/Gamma-ray_astronomy",
                "https://en.wikipedia.org/wiki/Gamma-ray_burst",
                "https://en.wikipedia.org/wiki/Gas_giant",
                "https://en.wikipedia.org/wiki/Geometric_albedo",
                "https://en.wikipedia.org/wiki/Geostationary_orbit",
                "https://en.wikipedia.org/wiki/Geosynchronous_orbit",
                "https://en.wikipedia.org/wiki/Giant_planet",
                "https://en.wikipedia.org/wiki/Globular_cluster",
                "https://en.wikipedia.org/wiki/Gravitational_collapse",
                "https://en.wikipedia.org/wiki/Gravitational_lens",
                "https://en.wikipedia.org/wiki/Gravitational-wave_astronomy",
                "https://en.wikipedia.org/wiki/H_II_region",
                "https://en.wikipedia.org/wiki/Heliosphere",
                "https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram",
                "https://en.wikipedia.org/wiki/Hill_sphere",
                "https://en.wikipedia.org/wiki/Ice_giant",
                "https://en.wikipedia.org/wiki/Orbital_inclination",
                "https://en.wikipedia.org/wiki/Inferior_and_superior_planets",
                "https://en.wikipedia.org/wiki/Infrared_astronomy",
                "https://en.wikipedia.org/wiki/International_Astronomical_Union",
                "https://en.wikipedia.org/wiki/Interstellar_medium",
                "https://en.wikipedia.org/wiki/Extinction_(astronomy)",
                "https://en.wikipedia.org/wiki/Invariable_plane",
                "https://en.wikipedia.org/wiki/Ionosphere",
                "https://en.wikipedia.org/wiki/Irregular_galaxy",
                "https://en.wikipedia.org/wiki/Irregular_moon",
                "https://en.wikipedia.org/wiki/Tautochrone_curve",
                "https://en.wikipedia.org/wiki/Jeans_instability",
                "https://en.wikipedia.org/wiki/Julian_year_(astronomy)",
                "https://en.wikipedia.org/wiki/Kelvin%E2%80%93Helmholtz_mechanism",
                "https://en.wikipedia.org/wiki/Kepler_orbit",
                "https://en.wikipedia.org/wiki/Kuiper_belt",
                "https://en.wikipedia.org/wiki/Lagrangian_point",
                "https://en.wikipedia.org/wiki/Laniakea_Supercluster",
                "https://en.wikipedia.org/wiki/Libration",
                "https://en.wikipedia.org/wiki/Light-year",
                "https://en.wikipedia.org/wiki/Limb_darkening",
                "https://en.wikipedia.org/wiki/Local_Group",
                "https://en.wikipedia.org/wiki/Longitude_of_the_ascending_node",
                "https://en.wikipedia.org/wiki/Luminosity",
                "https://en.wikipedia.org/wiki/Lunar_phase",
                "https://en.wikipedia.org/wiki/Magnetosphere",
                "https://en.wikipedia.org/wiki/Magnitude_(astronomy)",
                "https://en.wikipedia.org/wiki/Main_sequence",
                "https://en.wikipedia.org/wiki/March_equinox",
                "https://en.wikipedia.org/wiki/Mean_anomaly",
                "https://en.wikipedia.org/wiki/Meridian_(astronomy)",
                "https://en.wikipedia.org/wiki/Messier_object",
                "https://en.wikipedia.org/wiki/Meteoroid",
                "https://en.wikipedia.org/wiki/Meteorite",
                "https://en.wikipedia.org/wiki/Meteor_shower",
                "https://en.wikipedia.org/wiki/Metallicity",
                "https://en.wikipedia.org/wiki/Micrometeorite",
                "https://en.wikipedia.org/wiki/Micrometeoroid",
                "https://en.wikipedia.org/wiki/Milky_Way",
                "https://en.wikipedia.org/wiki/Minor_planet",
                "https://en.wikipedia.org/wiki/Molecular_cloud",
                "https://en.wikipedia.org/wiki/Moment_of_inertia_factor",
                "https://en.wikipedia.org/wiki/Natural_satellite",
                "https://en.wikipedia.org/wiki/Moon",
                "https://en.wikipedia.org/wiki/Moonlet",
                "https://en.wikipedia.org/wiki/Stellar_kinematics",
                "https://en.wikipedia.org/wiki/Multi-messenger_astronomy",
                "https://en.wikipedia.org/wiki/Multiverse",
                "https://en.wikipedia.org/wiki/Natural_satellite",
                "https://en.wikipedia.org/wiki/Near-Earth_object",
                "https://en.wikipedia.org/wiki/Nebula",
                "https://en.wikipedia.org/wiki/Neutrino",
                "https://en.wikipedia.org/wiki/Neutron_star",
                "https://en.wikipedia.org/wiki/New_General_Catalogue",
                "https://en.wikipedia.org/wiki/Night_sky",
                "https://en.wikipedia.org/wiki/Non-inclined_orbit",
                "https://en.wikipedia.org/wiki/Nuclear_star_cluster",
                "https://en.wikipedia.org/wiki/Number_density",
                "https://en.wikipedia.org/wiki/Astronomical_nutation",
                "https://en.wikipedia.org/wiki/Observable_universe",
                "https://en.wikipedia.org/wiki/Observational_astronomy",
                "https://en.wikipedia.org/wiki/Occultation",
                "https://en.wikipedia.org/wiki/Oort_cloud",
                "https://en.wikipedia.org/wiki/Opacity_(optics)",
                "https://en.wikipedia.org/wiki/Open_cluster",
                "https://en.wikipedia.org/wiki/Opposition_(astronomy)",
                "https://en.wikipedia.org/wiki/Orbit",
                "https://en.wikipedia.org/wiki/Orbital_eccentricity",
                "https://en.wikipedia.org/wiki/Orbital_elements",
                "https://en.wikipedia.org/wiki/Orbital_inclination",
                "https://en.wikipedia.org/wiki/Orbital_mechanics",
                "https://en.wikipedia.org/wiki/Orbital_node",
                "https://en.wikipedia.org/wiki/Orbital_plane_(astronomy)",
                "https://en.wikipedia.org/wiki/Orbital_resonance",
                "https://en.wikipedia.org/wiki/Orbital_speed",
                "https://en.wikipedia.org/wiki/Osculating_orbit",
                "https://en.wikipedia.org/wiki/Outer_space",
                "https://en.wikipedia.org/wiki/Parsec",
                "https://en.wikipedia.org/wiki/Perturbation_(astronomy)",
                "https://en.wikipedia.org/wiki/Substellar_object",
                "https://en.wikipedia.org/wiki/Sun",
                "https://en.wikipedia.org/wiki/Supercluster",
                "https://en.wikipedia.org/wiki/Supermassive_black_hole",
                "https://en.wikipedia.org/wiki/Supernova",
                "https://en.wikipedia.org/wiki/Surface_gravity",
                "https://en.wikipedia.org/wiki/Synchronous_orbit",
                "https://en.wikipedia.org/wiki/Synodic_day",
                "https://en.wikipedia.org/wiki/Syzygy_(astronomy)",
                "https://en.wikipedia.org/wiki/Telescope",
                "https://en.wikipedia.org/wiki/Terminator_(solar)",
                "https://en.wikipedia.org/wiki/Theoretical_astronomy",
                "https://en.wikipedia.org/wiki/Tidal_acceleration",
                "https://en.wikipedia.org/wiki/Tidal_force",
                "https://en.wikipedia.org/wiki/Tidal_locking",
                "https://en.wikipedia.org/wiki/Trans-Neptunian_object",
                "https://en.wikipedia.org/wiki/Transit_(astronomy)",
                "https://en.wikipedia.org/wiki/Trojan_(celestial_body)",
                "https://en.wikipedia.org/wiki/Tropical_year",
                "https://en.wikipedia.org/wiki/True_anomaly",
                "https://en.wikipedia.org/wiki/Tully%E2%80%93Fisher_relation",
                "https://en.wikipedia.org/wiki/Two-body_problem",
                "https://en.wikipedia.org/wiki/UBV_photometric_system",
                "https://en.wikipedia.org/wiki/Universe",
                "https://en.wikipedia.org/wiki/Variable_star",
                "https://en.wikipedia.org/wiki/Velocity_dispersion",
                "https://en.wikipedia.org/wiki/Virgo_Supercluster",
                "https://en.wikipedia.org/wiki/White_dwarf",
                "https://en.wikipedia.org/wiki/Wilson%E2%80%93Bappu_effect",
                "https://en.wikipedia.org/wiki/Zenith",
                "https://en.wikipedia.org/wiki/Main_sequence",
                "https://en.wikipedia.org/wiki/Zodiac",
                "https://en.wikipedia.org/wiki/Zodiacal_light"
            ]

            for url in urls:
                # Request the content of a page from the url
                html = requests.get(url)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                # title of the movie
                title = ""

                if soup.select_one("#firstHeading") is not None:
                    title += str(soup.select_one("#firstHeading")
                                 .text
                                 .lower()
                                 .replace(" ", "_")
                                 .replace("/", "_")
                                 .replace("-", "_")
                                 .replace(":", "_")
                                 .replace("\n", "")
                                 .replace("?", "")
                                 ) + ".avi"

                    print("title : " + title)

                # Text to speech and images
                text = ""

                if soup.select_one("#bodyContent") is not None:
                    text += str(soup.select_one("#bodyContent").text)

                # Filename for audio
                audio_file = os.getcwd() + "\\audio\\" + text[:50] \
                    .replace(":", "") \
                    .replace(" ", "") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "") + '.mp3'

                try:
                    # Convert text to audio
                    tts = gTTS(text.replace("", "")
                               .replace(".", "")
                               .replace("©", "")
                               .replace("*", "")
                               .replace("-", " ")
                               .replace("✔", "")
                               .replace("•", "")
                               .replace("⇒", "")
                               .replace("↑", "")
                               .replace("→", ""))

                    # Save the audio
                    tts.save(audio_file)
                except Exception as e:
                    print("error convert text to audio")

                # Folder of images
                image_folder = os.getcwd() + '\\images'

                # Create images from the text
                number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
                number_of_caracters_per_line = 110

                number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                number_of_lines = 0

                if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                    number_of_lines += round(number_of_lines_with_coma) + 1

                elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                    number_of_lines += round(number_of_lines_with_coma)

                number_of_lines_per_image = 10

                number_of_images_with_coma = number_of_lines / number_of_lines_per_image
                number_of_images = 0

                if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                    number_of_images += round(number_of_images_with_coma) + 1

                elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                    number_of_images += round(number_of_images_with_coma)

                # Array duration of each clip
                durations_of_each_clip = [0]

                l = 0

                duration = 0

                for i in range(1, number_of_images + 1):
                    img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                    d = ImageDraw.Draw(img)

                    if l <= number_of_lines:
                        for j in range(0, 10):
                            depart = 110 * l
                            arrivee = 110 + 110 * l
                            coordinate_y = 25 * j

                            if j < 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 1 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(
                                            MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                            elif j == 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 2 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        img.save(image_folder + "\\" + str(i) + ".png")

                                        durations_of_each_clip.append(duration)

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                # Appending the images to the video one by one
                images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                for i in range(1, number_of_images + 1):
                    try:
                        frame = cv2.imread(os.path.join(image_folder, images[0]))

                        # setting the frame width, height width the width, height of first image
                        height, width, layers = frame.shape

                        # video to create
                        video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0,
                                                1,
                                                (width, height))

                        for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                            video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                + "\\" + str(i) + ".png")))

                        # Deallocating memories taken for window creation
                        cv2.destroyAllWindows()

                        # releasing the video generated
                        video.release()

                    except Exception as e:
                        print("error video write : " + str(e))

                clips = []

                for i in range(1, number_of_images + 1):
                    try:
                        clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                     .set_start(durations_of_each_clip[i - 1]))
                    except Exception as e:
                        print("Error to append videos : " + str(e))

                try:
                    CompositeVideoClip(clips).write_videofile(
                        os.getcwd() + '\\videos\\my_concatenation.mp4')
                except Exception as e:
                    print("Error CompositeVideoClip : " + str(e))

                try:
                    output_movie = os.getcwd() + "\\videos_creees\\" + directory + "\\" + title
                    ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie,
                                             vcodec='copy', acodec='copy',
                                             ffmpeg_output=False, logger='bar')
                except Exception as e:
                    print("output movie exception : " + str(e))
        finally:
            # Delete all images
            for i in range(1, number_of_images + 1):
                os.remove(image_folder + "\\" + str(i) + ".png")

            # Delete all clips
            for i in range(1, number_of_images + 1):
                os.remove(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')

            os.remove(os.getcwd() + '\\videos\\my_concatenation.mp4')
            os.remove(audio_file)

    def test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_glossary_of_chemistry_terms(self):
        print("test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_glossary_of_chemistry_terms")

        audio_file = ""
        image_folder = ""
        number_of_images = ""
        directory = "chemistry"

        try:
            urls = [
                "https://en.wikipedia.org/wiki/Torr",
                "https://en.wikipedia.org/wiki/Transition_metal",
                "https://en.wikipedia.org/wiki/Transuranium_element",
                "https://en.wikipedia.org/wiki/Bond_order",
                "https://en.wikipedia.org/wiki/Triple_point",
                "https://en.wikipedia.org/wiki/Tyndall_effect",
                "https://en.wikipedia.org/wiki/UN_number",
                "https://en.wikipedia.org/wiki/Uncertainty",
                "https://en.wikipedia.org/wiki/Uncertainty_principle",
                "https://en.wikipedia.org/wiki/Dalton_(unit)",
                "https://en.wikipedia.org/wiki/Crystal_structure",
                "https://en.wikipedia.org/wiki/Dimensional_analysis",
                "https://en.wikipedia.org/wiki/Unpaired_electron",
                "https://en.wikipedia.org/wiki/Vacuum_flask",
                "https://en.wikipedia.org/wiki/Valence_electron",
                "https://en.wikipedia.org/wiki/Valence_bond_theory",
                "https://en.wikipedia.org/wiki/Valence_(chemistry)",
                "https://en.wikipedia.org/wiki/Van_der_Waals_force",
                "https://en.wikipedia.org/wiki/Van_%27t_Hoff_factor",
                "https://en.wikipedia.org/wiki/Vapor",
                "https://en.wikipedia.org/wiki/Vapor_pressure",
                "https://en.wikipedia.org/wiki/Vaporization",
                "https://en.wikipedia.org/wiki/Viscosity",
                "https://en.wikipedia.org/wiki/Volatility_(chemistry)",
                "https://en.wikipedia.org/wiki/Volt",
                "https://en.wikipedia.org/wiki/Voltmeter",
                "https://en.wikipedia.org/wiki/Volume",
                "https://en.wikipedia.org/wiki/Volumetric_flask",
                "https://en.wikipedia.org/wiki/Watch_glass",
                "https://en.wikipedia.org/wiki/Properties_of_water",
                "https://en.wikipedia.org/wiki/Wave_function",
                "https://en.wikipedia.org/wiki/Acid_strength",
                "https://en.wikipedia.org/wiki/Weak_base",
                "https://en.wikipedia.org/wiki/Wet_chemistry",
                "https://en.wikipedia.org/wiki/Work_(physics)",
                "https://en.wikipedia.org/wiki/Work-up_(chemistry)",
                "https://en.wikipedia.org/wiki/X-ray",
                "https://en.wikipedia.org/wiki/X-ray_scattering_techniques",
                "https://en.wikipedia.org/wiki/X-ray_photoelectron_spectroscopy",
                "https://en.wikipedia.org/wiki/Yield_(chemistry)",
                "https://en.wikipedia.org/wiki/Zone_melting",
                "https://en.wikipedia.org/wiki/Zwitterion",
                "https://en.wikipedia.org/wiki/Zinc",
                "https://en.wikipedia.org/wiki/Redox",
                "https://en.wikipedia.org/wiki/Reducing_agent",
                "https://en.wikipedia.org/wiki/Reduction_potential",
                "https://en.wikipedia.org/wiki/Resonance_(chemistry)",
                "https://en.wikipedia.org/wiki/Retort",
                "https://en.wikipedia.org/wiki/Round-bottom_flask",
                "https://en.wikipedia.org/wiki/Rust",
                "https://en.wikipedia.org/wiki/Block_(periodic_table)",
                "https://en.wikipedia.org/wiki/Salt_(chemistry)",
                "https://en.wikipedia.org/wiki/Salt_bridge",
                "https://en.wikipedia.org/wiki/Saline_(medicine)",
                "https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation",
                "https://en.wikipedia.org/wiki/Rate_equation",
                "https://en.wikipedia.org/wiki/Semiconductor",
                "https://en.wikipedia.org/wiki/Serial_dilution",
                "https://en.wikipedia.org/wiki/Side_chain",
                "https://en.wikipedia.org/wiki/Bond_order",
                "https://en.wikipedia.org/wiki/Skeletal_formula",
                "https://en.wikipedia.org/wiki/Sol_(colloid)",
                "https://en.wikipedia.org/wiki/Solid",
                "https://en.wikipedia.org/wiki/Solubility",
                "https://en.wikipedia.org/wiki/Solution",
                "https://en.wikipedia.org/wiki/Solvated_electron",
                "https://en.wikipedia.org/wiki/Solvation",
                "https://en.wikipedia.org/wiki/Solvation_shell",
                "https://en.wikipedia.org/wiki/Solvent",
                "https://en.wikipedia.org/wiki/Spectrochemistry",
                "https://en.wikipedia.org/wiki/Spectroscopy",
                "https://en.wikipedia.org/wiki/Standard_solution",
                "https://en.wikipedia.org/wiki/Standard_conditions_for_temperature_and_pressure",
                "https://en.wikipedia.org/wiki/State_of_matter",
                "https://en.wikipedia.org/wiki/Stepwise_reaction",
                "https://en.wikipedia.org/wiki/Stereochemistry",
                "https://en.wikipedia.org/wiki/Stereoisomerism",
                "https://en.wikipedia.org/wiki/Stoichiometry",
                "https://en.wikipedia.org/wiki/Acid_strength",
                "https://en.wikipedia.org/wiki/Structural_formula",
                "https://en.wikipedia.org/wiki/Structural_isomer",
                "https://en.wikipedia.org/wiki/Subatomic_particle",
                "https://en.wikipedia.org/wiki/Sublimation_(phase_transition)",
                "https://en.wikipedia.org/wiki/Chemical_substance",
                "https://en.wikipedia.org/wiki/Substituent",
                "https://en.wikipedia.org/wiki/Suspension_(chemistry)",
                "https://en.wikipedia.org/wiki/Tarnish",
                "https://en.wikipedia.org/wiki/Temperature",
                "https://en.wikipedia.org/wiki/Yield_(chemistry)",
                "https://en.wikipedia.org/wiki/Thermal_conductivity",
                "https://en.wikipedia.org/wiki/Thermochemistry",
                "https://en.wikipedia.org/wiki/Thermodynamics",
                "https://en.wikipedia.org/wiki/Chemical_stability",
                "https://en.wikipedia.org/wiki/Thermometer",
                "https://en.wikipedia.org/wiki/Titration",
                "https://en.wikipedia.org/wiki/Period_(periodic_table)",
                "https://en.wikipedia.org/wiki/Periodic_table",
                "https://en.wikipedia.org/wiki/Chemical_polarity",
                "https://en.wikipedia.org/wiki/Potential_energy",
                "https://en.wikipedia.org/wiki/Pressure",
                "https://en.wikipedia.org/wiki/Photon",
                "https://en.wikipedia.org/wiki/Polyatomic_ion",
                "https://en.wikipedia.org/wiki/Protecting_group",
                "https://en.wikipedia.org/wiki/Proton",
                "https://en.wikipedia.org/wiki/Protonation",
                "https://en.wikipedia.org/wiki/Pyrolysis",
                "https://en.wikipedia.org/wiki/Quantum_mechanics",
                "https://en.wikipedia.org/wiki/Quark",
                "https://en.wikipedia.org/wiki/Quantum",
                "https://en.wikipedia.org/wiki/Racemic_mixture",
                "https://en.wikipedia.org/wiki/Radiation",
                "https://en.wikipedia.org/wiki/Radical_(chemistry)",
                "https://en.wikipedia.org/wiki/Radioactive_decay",
                "https://en.wikipedia.org/wiki/Raoult%27s_law",
                "https://en.wikipedia.org/wiki/Rare-earth_element",
                "https://en.wikipedia.org/wiki/Rate_equation",
                "https://en.wikipedia.org/wiki/Reagent",
                "https://en.wikipedia.org/wiki/Reaction_mechanism",
                "https://en.wikipedia.org/wiki/Reaction_rate",
                "https://en.wikipedia.org/wiki/Reaction_rate_constant",
                "https://en.wikipedia.org/wiki/Reactive_intermediate",
                "https://en.wikipedia.org/wiki/Reactivity_(chemistry)",
                "https://en.wikipedia.org/wiki/Reactivity_series",
                "https://en.wikipedia.org/wiki/Molar_concentration",
                "https://en.wikipedia.org/wiki/Mole_fraction",
                "https://en.wikipedia.org/wiki/Molar_mass",
                "https://en.wikipedia.org/wiki/Mole_(unit)",
                "https://en.wikipedia.org/wiki/Chemical_formula",
                "https://en.wikipedia.org/wiki/Molecular_orbital",
                "https://en.wikipedia.org/wiki/Molecular_orbital_diagram",
                "https://en.wikipedia.org/wiki/Molecule",
                "https://en.wikipedia.org/wiki/Monatomic_gas",
                "https://en.wikipedia.org/wiki/Natural_abundance",
                "https://en.wikipedia.org/wiki/Neutron",
                "https://en.wikipedia.org/wiki/Nitrogen",
                "https://en.wikipedia.org/wiki/Nucleon",
                "https://en.wikipedia.org/wiki/Nucleophile",
                "https://en.wikipedia.org/wiki/Atomic_nucleus",
                "https://en.wikipedia.org/wiki/Noble_gas",
                "https://en.wikipedia.org/wiki/Nonmetal",
                "https://en.wikipedia.org/wiki/Equivalent_concentration",
                "https://en.wikipedia.org/wiki/Atomic_nucleus",
                "https://en.wikipedia.org/wiki/Nuclear_chemistry",
                "https://en.wikipedia.org/wiki/Nuclear_magnetic_resonance_spectroscopy",
                "https://en.wikipedia.org/wiki/Nuclear_transmutation",
                "https://en.wikipedia.org/wiki/Nuclide",
                "https://en.wikipedia.org/wiki/Number_density",
                "https://en.wikipedia.org/wiki/Octet_rule",
                "https://en.wikipedia.org/wiki/Alkene",
                "https://en.wikipedia.org/wiki/Optical_rotation",
                "https://en.wikipedia.org/wiki/Orbital_hybridisation",
                "https://en.wikipedia.org/wiki/Rate_equation",
                "https://en.wikipedia.org/wiki/Organic_acid",
                "https://en.wikipedia.org/wiki/Organic_base",
                "https://en.wikipedia.org/wiki/Organic_compound",
                "https://en.wikipedia.org/wiki/Organic_chemistry",
                "https://en.wikipedia.org/wiki/Organic_redox_reaction",
                "https://en.wikipedia.org/wiki/Osmotic_pressure",
                "https://en.wikipedia.org/wiki/Redox",
                "https://en.wikipedia.org/wiki/Oxidation_state",
                "https://en.wikipedia.org/wiki/Oxidizing_agent",
                "https://en.wikipedia.org/wiki/Oxyacid",
                "https://en.wikipedia.org/wiki/Oxygen",
                "https://en.wikipedia.org/wiki/Paraffin",
                "https://en.wikipedia.org/wiki/Partial_pressure",
                "https://en.wikipedia.org/wiki/Pascal_(unit)",
                "https://en.wikipedia.org/wiki/Passivation_(chemistry)",
                "https://en.wikipedia.org/wiki/PH",
                "https://en.wikipedia.org/wiki/Phase_(matter)",
                "https://en.wikipedia.org/wiki/Phase_transition",
                "https://en.wikipedia.org/wiki/Phi_bond",
                "https://en.wikipedia.org/wiki/Physical_chemistry",
                "https://en.wikipedia.org/wiki/Pi_bond",
                "https://en.wikipedia.org/wiki/Pipette",
                "https://en.wikipedia.org/wiki/Plasma_(physics)",
                "https://en.wikipedia.org/wiki/Mass_fraction_(chemistry)",
                "https://en.wikipedia.org/wiki/Mass_number",
                "https://en.wikipedia.org/wiki/Mass_spectrometry",
                "https://en.wikipedia.org/wiki/Matter",
                "https://en.wikipedia.org/wiki/Metal",
                "https://en.wikipedia.org/wiki/Melting",
                "https://en.wikipedia.org/wiki/Melting_point",
                "https://en.wikipedia.org/wiki/Metalloid",
                "https://en.wikipedia.org/wiki/Methylene_blue",
                "https://en.wikipedia.org/wiki/Laboratory_centrifuge",
                "https://en.wikipedia.org/wiki/Mineral",
                "https://en.wikipedia.org/wiki/Miscibility",
                "https://en.wikipedia.org/wiki/Mixture",
                "https://en.wikipedia.org/wiki/Moiety_(chemistry)",
                "https://en.wikipedia.org/wiki/Molality",
                "https://en.wikipedia.org/wiki/Molar_attenuation_coefficient",
                "https://en.wikipedia.org/wiki/Ductility",
                "https://en.wikipedia.org/wiki/Pressure_measurement",
                "https://en.wikipedia.org/wiki/Mass",
                "https://en.wikipedia.org/wiki/Mass_concentration_(chemistry)",
                "https://en.wikipedia.org/wiki/Corrosion",
                "https://en.wikipedia.org/wiki/Coulomb",
                "https://en.wikipedia.org/wiki/Covalent_bond",
                "https://en.wikipedia.org/wiki/Critical_point_(thermodynamics)",
                "https://en.wikipedia.org/wiki/Crystal",
                "https://en.wikipedia.org/wiki/Crystallography",
                "https://en.wikipedia.org/wiki/Cuvette",
                "https://en.wikipedia.org/wiki/Dalton%27s_law",
                "https://en.wikipedia.org/wiki/Purified_water",
                "https://en.wikipedia.org/wiki/Hygroscopy",
                "https://en.wikipedia.org/wiki/Delocalized_electron",
                "https://en.wikipedia.org/wiki/Density",
                "https://en.wikipedia.org/wiki/Denticity",
                "https://en.wikipedia.org/wiki/Dependent_and_independent_variables",
                "https://en.wikipedia.org/wiki/Deposition_(chemistry)",
                "https://en.wikipedia.org/wiki/Vacuum_flask",
                "https://en.wikipedia.org/wiki/Diatomic_molecule",
                "https://en.wikipedia.org/wiki/Diffusion",
                "https://en.wikipedia.org/wiki/Dimer_(chemistry)",
                "https://en.wikipedia.org/wiki/Coordinate_covalent_bond",
                "https://en.wikipedia.org/wiki/Dipole",
                "https://en.wikipedia.org/wiki/Bond_dipole_moment",
                "https://en.wikipedia.org/wiki/Dispersion_(chemistry)",
                "https://en.wikipedia.org/wiki/Dissociation_(chemistry)",
                "https://en.wikipedia.org/wiki/Solvation",
                "https://en.wikipedia.org/wiki/Distillation",
                "https://en.wikipedia.org/wiki/Double_bond",
                "https://en.wikipedia.org/wiki/Salt_metathesis_reaction",
                "https://en.wikipedia.org/wiki/Electric_charge",
                "https://en.wikipedia.org/wiki/Electrolyte",
                "https://en.wikipedia.org/wiki/Electrochemical_cell",
                "https://en.wikipedia.org/wiki/Electromagnetic_radiation",
                "https://en.wikipedia.org/wiki/Electromagnetic_spectrum",
                "https://en.wikipedia.org/wiki/Electromagnetism",
                "https://en.wikipedia.org/wiki/Electromotive_force",
                "https://en.wikipedia.org/wiki/Electron",
                "https://en.wikipedia.org/wiki/Electron_configuration",
                "https://en.wikipedia.org/wiki/Electron_deficiency",
                "https://en.wikipedia.org/wiki/Electron_pair",
                "https://en.wikipedia.org/wiki/Electron_shell",
                "https://en.wikipedia.org/wiki/Electronegativity",
                "https://en.wikipedia.org/wiki/Electrophile",
                "https://en.wikipedia.org/wiki/Electrosynthesis",
                "https://en.wikipedia.org/wiki/Chemical_element",
                "https://en.wikipedia.org/wiki/Elementary_reaction",
                "https://en.wikipedia.org/wiki/Enantiomer",
                "https://en.wikipedia.org/wiki/Chirality_(mathematics)",
                "https://en.wikipedia.org/wiki/Endothermic_process",
                "https://en.wikipedia.org/wiki/Energy",
                "https://en.wikipedia.org/wiki/Amount_of_substance",
                "https://en.wikipedia.org/wiki/Enthalpy",
                "https://en.wikipedia.org/wiki/Enthalpy_of_fusion",
                "https://en.wikipedia.org/wiki/Entropy",
                "https://en.wikipedia.org/wiki/Environmental_chemistry",
                "https://en.wikipedia.org/wiki/Enzyme",
                "https://en.wikipedia.org/wiki/Empirical_formula",
                "https://en.wikipedia.org/wiki/List_of_types_of_equilibrium",
                "https://en.wikipedia.org/wiki/Erlenmeyer_flask",
                "https://en.wikipedia.org/wiki/Exothermic_process",
                "https://en.wikipedia.org/wiki/Intensive_and_extensive_properties",
                "https://en.wikipedia.org/wiki/Extraction_(chemistry)",
                "https://en.wikipedia.org/wiki/Intrinsic_and_extrinsic_properties",
                "https://en.wikipedia.org/wiki/Freezing",
                "https://en.wikipedia.org/wiki/Faraday_constant",
                "https://en.wikipedia.org/wiki/Faraday%27s_laws_of_electrolysis",
                "https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion",
                "https://en.wikipedia.org/wiki/Filtration",
                "https://en.wikipedia.org/wiki/Laboratory_flask",
                "https://en.wikipedia.org/wiki/Formal_charge",
                "https://en.wikipedia.org/wiki/Fractional_distillation",
                "https://en.wikipedia.org/wiki/Radical_(chemistry)",
                "https://en.wikipedia.org/wiki/Freezing-point_depression",
                "https://en.wikipedia.org/wiki/Melting_point",
                "https://en.wikipedia.org/wiki/Frequency",
                "https://en.wikipedia.org/wiki/Functional_group",
                "https://en.wikipedia.org/wiki/Galvanic_cell",
                "https://en.wikipedia.org/wiki/Gas",
                "https://en.wikipedia.org/wiki/Gas_chromatography",
                "https://en.wikipedia.org/wiki/Gay-Lussac%27s_law",
                "https://en.wikipedia.org/wiki/Geochemistry",
                "https://en.wikipedia.org/wiki/Gibbs_free_energy",
                "https://en.wikipedia.org/wiki/Glass",
                "https://en.wikipedia.org/wiki/Grignard_reaction",
                "https://en.wikipedia.org/wiki/Ground_glass_joint",
                "https://en.wikipedia.org/wiki/Group_(periodic_table)",
                "https://en.wikipedia.org/wiki/Halogen",
                "https://en.wikipedia.org/wiki/Hadron",
                "https://en.wikipedia.org/wiki/Heat",
                "https://en.wikipedia.org/wiki/Enthalpy_of_fusion",
                "https://en.wikipedia.org/wiki/Henry%27s_law",
                "https://en.wikipedia.org/wiki/Hess%27s_law",
                "https://en.wikipedia.org/wiki/Hund%27s_rules",
                "https://en.wikipedia.org/wiki/Hydrate",
                "https://en.wikipedia.org/wiki/Hydration_reaction",
                "https://en.wikipedia.org/wiki/Hydrogen",
                "https://en.wikipedia.org/wiki/Hydrogen_bond",
                "https://en.wikipedia.org/wiki/Hydrogenation",
                "https://en.wikipedia.org/wiki/Hydrolysis",
                "https://en.wikipedia.org/wiki/Hygroscopy",
                "https://en.wikipedia.org/wiki/Ideal_gas",
                "https://en.wikipedia.org/wiki/Gas_constant",
                "https://en.wikipedia.org/wiki/Ideal_gas_law",
                "https://en.wikipedia.org/wiki/Ideal_solution",
                "https://en.wikipedia.org/wiki/Dependent_and_independent_variables",
                "https://en.wikipedia.org/wiki/PH_indicator",
                "https://en.wikipedia.org/wiki/Induced_radioactivity",
                "https://en.wikipedia.org/wiki/Chemically_inert",
                "https://en.wikipedia.org/wiki/Inorganic_compound",
                "https://en.wikipedia.org/wiki/Inorganic_chemistry",
                "https://en.wikipedia.org/wiki/Insulator_(electricity)",
                "https://en.wikipedia.org/wiki/Intermolecular_force",
                "https://en.wikipedia.org/wiki/International_System_of_Units",
                "https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry",
                "https://en.wikipedia.org/wiki/Intramolecular_force",
                "https://en.wikipedia.org/wiki/Ion",
                "https://en.wikipedia.org/wiki/Ionic_bonding",
                "https://en.wikipedia.org/wiki/Ionization",
                "https://en.wikipedia.org/wiki/Isoelectronicity",
                "https://en.wikipedia.org/wiki/Isomerization",
                "https://en.wikipedia.org/wiki/Isomer",
                "https://en.wikipedia.org/wiki/Isotope",
                "https://en.wikipedia.org/wiki/Joule",
                "https://en.wikipedia.org/wiki/Kelvin",
                "https://en.wikipedia.org/wiki/Ketone",
                "https://en.wikipedia.org/wiki/Chemical_kinetics",
                "https://en.wikipedia.org/wiki/Kinetic_energy",
                "https://en.wikipedia.org/wiki/Lability",
                "https://en.wikipedia.org/wiki/Lanthanide",
                "https://en.wikipedia.org/wiki/Crystal_structure",
                "https://en.wikipedia.org/wiki/Lattice_energy",
                "https://en.wikipedia.org/wiki/Conservation_of_energy",
                "https://en.wikipedia.org/wiki/Conservation_of_mass",
                "https://en.wikipedia.org/wiki/Law_of_multiple_proportions",
                "https://en.wikipedia.org/wiki/Laws_of_thermodynamics",
                "https://en.wikipedia.org/wiki/Leveling_effect",
                "https://en.wikipedia.org/wiki/Lewis_acids_and_bases",
                "https://en.wikipedia.org/wiki/Lewis_structure",
                "https://en.wikipedia.org/wiki/Ligand",
                "https://en.wikipedia.org/wiki/Liquefaction",
                "https://en.wikipedia.org/wiki/Liquid",
                "https://en.wikipedia.org/wiki/Locant",
                "https://en.wikipedia.org/wiki/London_dispersion_force",
                "https://en.wikipedia.org/wiki/Absorbance",
                "https://en.wikipedia.org/wiki/Absorption_(chemistry)",
                "https://en.wikipedia.org/wiki/Abundance_(chemistry)",
                "https://en.wikipedia.org/wiki/Accuracy_and_precision",
                "https://en.wikipedia.org/wiki/Acid",
                "https://en.wikipedia.org/wiki/Acid_anhydride",
                "https://en.wikipedia.org/wiki/Acid_dissociation_constant",
                "https://en.wikipedia.org/wiki/Actinide",
                "https://en.wikipedia.org/wiki/Activated_complex",
                "https://en.wikipedia.org/wiki/Activation_energy",
                "https://en.wikipedia.org/wiki/Reactivity_series",
                "https://en.wikipedia.org/wiki/Yield_(chemistry)",
                "https://en.wikipedia.org/wiki/Open-chain_compound",
                "https://en.wikipedia.org/wiki/Addition_reaction",
                "https://en.wikipedia.org/wiki/Adhesion",
                "https://en.wikipedia.org/wiki/Adsorption",
                "https://en.wikipedia.org/wiki/Aeration",
                "https://en.wikipedia.org/wiki/Alcohol",
                "https://en.wikipedia.org/wiki/Aldehyde",
                "https://en.wikipedia.org/wiki/Alkali_metal",
                "https://en.wikipedia.org/wiki/Alkaline_earth_metal",
                "https://en.wikipedia.org/wiki/Alkane",
                "https://en.wikipedia.org/wiki/Alkene",
                "https://en.wikipedia.org/wiki/Alkyl",
                "https://en.wikipedia.org/wiki/Alkyne",
                "https://en.wikipedia.org/wiki/Allomerism",
                "https://en.wikipedia.org/wiki/Allotropy",
                "https://en.wikipedia.org/wiki/Alloy",
                "https://en.wikipedia.org/wiki/Amalgam_(chemistry)",
                "https://en.wikipedia.org/wiki/Amount_of_substance",
                "https://en.wikipedia.org/wiki/Analyte",
                "https://en.wikipedia.org/wiki/Analytical_chemistry",
                "https://en.wikipedia.org/wiki/Anode",
                "https://en.wikipedia.org/wiki/Aqueous_solution",
                "https://en.wikipedia.org/wiki/Aromaticity",
                "https://en.wikipedia.org/wiki/Arrow_pushing",
                "https://en.wikipedia.org/wiki/Aryl",
                "https://en.wikipedia.org/wiki/Atom",
                "https://en.wikipedia.org/wiki/Atomic_mass",
                "https://en.wikipedia.org/wiki/Dalton_(unit)",
                "https://en.wikipedia.org/wiki/Atomic_number",
                "https://en.wikipedia.org/wiki/Atomic_orbital",
                "https://en.wikipedia.org/wiki/Atomic_radius",
                "https://en.wikipedia.org/wiki/Relative_atomic_mass",
                "https://en.wikipedia.org/wiki/Avogadro%27s_law",
                "https://en.wikipedia.org/wiki/Avogadro_constant",
                "https://en.wikipedia.org/wiki/Azeotrope",
                "https://en.wikipedia.org/wiki/Barometer",
                "https://en.wikipedia.org/wiki/Base_(chemistry)",
                "https://en.wikipedia.org/wiki/Base_anhydride",
                "https://en.wikipedia.org/wiki/Beaker_(laboratory_equipment)",
                "https://en.wikipedia.org/wiki/Beer%E2%80%93Lambert_law",
                "https://en.wikipedia.org/wiki/Biochemistry",
                "https://en.wikipedia.org/wiki/Bohr_model",
                "https://en.wikipedia.org/wiki/Boiling",
                "https://en.wikipedia.org/wiki/Boiling_point",
                "https://en.wikipedia.org/wiki/Boiling-point_elevation",
                "https://en.wikipedia.org/wiki/Chemical_bond",
                "https://en.wikipedia.org/wiki/Boyle%27s_law",
                "https://en.wikipedia.org/wiki/Bragg%27s_law",
                "https://en.wikipedia.org/wiki/Brownian_motion",
                "https://en.wikipedia.org/wiki/Br%C3%B8nsted%E2%80%93Lowry_acid%E2%80%93base_theory",
                "https://en.wikipedia.org/wiki/B%C3%BCchner_flask",
                "https://en.wikipedia.org/wiki/Buffer_solution",
                "https://en.wikipedia.org/wiki/Bumping_(chemistry)",
                "https://en.wikipedia.org/wiki/Bung",
                "https://en.wikipedia.org/wiki/Burette",
                "https://en.wikipedia.org/wiki/Calorimeter",
                "https://en.wikipedia.org/wiki/Carbanion",
                "https://en.wikipedia.org/wiki/Carbocation",
                "https://en.wikipedia.org/wiki/Catalysis",
                "https://en.wikipedia.org/wiki/Cathode",
                "https://en.wikipedia.org/wiki/Centrifugation",
                "https://en.wikipedia.org/wiki/Centrifuge",
                "https://en.wikipedia.org/wiki/Resting_potential",
                "https://en.wikipedia.org/wiki/Chain_reaction",
                "https://en.wikipedia.org/wiki/Charge_number",
                "https://en.wikipedia.org/wiki/Charles%27s_law",
                "https://en.wikipedia.org/wiki/Chelation",
                "https://en.wikipedia.org/wiki/Chemical_composition",
                "https://en.wikipedia.org/wiki/Chemical_formula",
                "https://en.wikipedia.org/wiki/Chemical_law",
                "https://en.wikipedia.org/wiki/Chemical_nomenclature",
                "https://en.wikipedia.org/wiki/Chemical_process",
                "https://en.wikipedia.org/wiki/Chemical_reaction",
                "https://en.wikipedia.org/wiki/Chemical_species",
                "https://en.wikipedia.org/wiki/Chemical_substance",
                "https://en.wikipedia.org/wiki/Chemical_synthesis",
                "https://en.wikipedia.org/wiki/Chemistry",
                "https://en.wikipedia.org/wiki/Chirality",
                "https://en.wikipedia.org/wiki/Chromatography",
                "https://en.wikipedia.org/wiki/Cis%E2%80%93trans_isomerism",
                "https://en.wikipedia.org/wiki/Closed_system",
                "https://en.wikipedia.org/wiki/Atom_cluster",
                "https://en.wikipedia.org/wiki/Cohesion_(chemistry)",
                "https://en.wikipedia.org/wiki/Colligative_properties",
                "https://en.wikipedia.org/wiki/Colloid",
                "https://en.wikipedia.org/wiki/Combustion",
                "https://en.wikipedia.org/wiki/Commission_on_Isotopic_Abundances_and_Atomic_Weights",
                "https://en.wikipedia.org/wiki/Compression_(physics)",
                "https://en.wikipedia.org/wiki/Chemical_compound",
                "https://en.wikipedia.org/wiki/Concentration",
                "https://en.wikipedia.org/wiki/Condensation",
                "https://en.wikipedia.org/wiki/Condosity",
                "https://en.wikipedia.org/wiki/Electrical_conductor",
                "https://en.wikipedia.org/wiki/Conformational_isomerism",
                "https://en.wikipedia.org/wiki/Conjugate_acid",
                "https://en.wikipedia.org/wiki/Conjugated_system",
                "https://en.wikipedia.org/wiki/Cooling_curve",
                "https://en.wikipedia.org/wiki/Coordinate_covalent_bond",
                "https://en.wikipedia.org/wiki/Coordination_complex",
                "https://en.wikipedia.org/wiki/Absolute_zero"
            ]

            for url in urls:
                # Request the content of a page from the url
                html = requests.get(url)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                # title of the movie
                title = ""

                if soup.select_one("#firstHeading") is not None:
                    title += str(soup.select_one("#firstHeading")
                                 .text
                                 .lower()
                                 .replace(" ", "_")
                                 .replace("/", "_")
                                 .replace("-", "_")
                                 .replace(":", "_")
                                 .replace("\n", "")
                                 .replace("?", "_")
                                 .replace("'", "_")
                                 .replace("(", "_")
                                 .replace(")", "_")
                                 ) + ".avi"

                    print("title : " + title)

                # Text to speech and images
                text = ""

                if soup.select_one("#bodyContent") is not None:
                    text += str(soup.select_one("#bodyContent").text)

                # Filename for audio
                audio_file = os.getcwd() + "\\audio\\" + text[:50] \
                    .replace(":", "") \
                    .replace(" ", "") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "") + '.mp3'

                try:
                    # Convert text to audio
                    tts = gTTS(text.replace("", "")
                               .replace(".", "")
                               .replace("©", "")
                               .replace("*", "")
                               .replace("-", " ")
                               .replace("✔", "")
                               .replace("•", "")
                               .replace("⇒", "")
                               .replace("↑", "")
                               .replace("→", ""))

                    # Save the audio
                    tts.save(audio_file)
                except Exception as e:
                    print("error convert text to audio")

                # Folder of images
                image_folder = os.getcwd() + '\\images'

                # Create images from the text
                number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
                number_of_caracters_per_line = 110

                number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                number_of_lines = 0

                if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                    number_of_lines += round(number_of_lines_with_coma) + 1

                elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                    number_of_lines += round(number_of_lines_with_coma)

                number_of_lines_per_image = 10

                number_of_images_with_coma = number_of_lines / number_of_lines_per_image
                number_of_images = 0

                if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                    number_of_images += round(number_of_images_with_coma) + 1

                elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                    number_of_images += round(number_of_images_with_coma)

                # Array duration of each clip
                durations_of_each_clip = [0]

                l = 0

                duration = 0

                for i in range(1, number_of_images + 1):
                    img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                    d = ImageDraw.Draw(img)

                    if l <= number_of_lines:
                        for j in range(0, 10):
                            depart = 110 * l
                            arrivee = 110 + 110 * l
                            coordinate_y = 25 * j

                            if j < 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 1 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(
                                            MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                            elif j == 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 2 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        img.save(image_folder + "\\" + str(i) + ".png")

                                        durations_of_each_clip.append(duration)

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                # Appending the images to the video one by one
                images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                for i in range(1, number_of_images + 1):
                    try:
                        frame = cv2.imread(os.path.join(image_folder, images[0]))

                        # setting the frame width, height width the width, height of first image
                        height, width, layers = frame.shape

                        # video to create
                        video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0,
                                                1,
                                                (width, height))

                        for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                            video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                + "\\" + str(i) + ".png")))

                        # Deallocating memories taken for window creation
                        cv2.destroyAllWindows()

                        # releasing the video generated
                        video.release()

                    except Exception as e:
                        print("error video write : " + str(e))

                clips = []

                for i in range(1, number_of_images + 1):
                    try:
                        clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                     .set_start(durations_of_each_clip[i - 1]))
                    except Exception as e:
                        print("Error to append videos : " + str(e))

                try:
                    CompositeVideoClip(clips).write_videofile(
                        os.getcwd() + '\\videos\\my_concatenation.mp4')
                except Exception as e:
                    print("Error CompositeVideoClip : " + str(e))

                try:
                    output_movie = os.getcwd() + "\\videos_creees\\" + directory + "\\" + title
                    ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie,
                                             vcodec='copy', acodec='copy',
                                             ffmpeg_output=False, logger='bar')
                except Exception as e:
                    print("output movie exception : " + str(e))
        finally:
            # Delete all images
            for i in range(1, number_of_images + 1):
                os.remove(image_folder + "\\" + str(i) + ".png")

            # Delete all clips
            for i in range(1, number_of_images + 1):
                os.remove(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')

            os.remove(os.getcwd() + '\\videos\\my_concatenation.mp4')
            os.remove(audio_file)

    def test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_glossary_of_biology(self):
        print("test_create_videos_from_a_list_of_urls_from_wikipedia_topic_for_glossary_of_biology")

        audio_file = ""
        image_folder = ""
        number_of_images = ""
        directory = "biology"

        try:
            urls = [
                "https://en.wikipedia.org/wiki/Abiotic_component",
                "https://en.wikipedia.org/wiki/Abscission",
                "https://en.wikipedia.org/wiki/Absorption_(skin)",
                "https://en.wikipedia.org/wiki/Absorption_spectroscopy",
                "https://en.wikipedia.org/wiki/Acclimatization",
                "https://en.wikipedia.org/wiki/Acetyl-CoA",
                "https://en.wikipedia.org/wiki/Coelom",
                "https://en.wikipedia.org/wiki/Action_potential",
                "https://en.wikipedia.org/wiki/Activation_energy",
                "https://en.wikipedia.org/wiki/Active_site",
                "https://en.wikipedia.org/wiki/Active_transport",
                "https://en.wikipedia.org/wiki/Adaptation",
                "https://en.wikipedia.org/wiki/Adaptive_radiation",
                "https://en.wikipedia.org/wiki/Adenine",
                "https://en.wikipedia.org/wiki/Adenosine_triphosphate",
                "https://en.wikipedia.org/wiki/Adipose_tissue",
                "https://en.wikipedia.org/wiki/Estrogen",
                "https://en.wikipedia.org/wiki/Ethology",
                "https://en.wikipedia.org/wiki/Eukaryote",
                "https://en.wikipedia.org/wiki/Evolution",
                "https://en.wikipedia.org/wiki/Evolutionary_biology",
                "https://en.wikipedia.org/wiki/Exocytosis",
                "https://en.wikipedia.org/wiki/Exogeny",
                "https://en.wikipedia.org/wiki/Exponential_growth",
                "https://en.wikipedia.org/wiki/External_fertilization",
                "https://en.wikipedia.org/wiki/Extinction",
                "https://en.wikipedia.org/wiki/Extranuclear_inheritance",
                "https://en.wikipedia.org/wiki/Entomology",
                "https://en.wikipedia.org/wiki/Environmental_science",
                "https://en.wikipedia.org/wiki/Enzyme",
                "https://en.wikipedia.org/wiki/Epidemiology",
                "https://en.wikipedia.org/wiki/Epigenetics",
                "https://en.wikipedia.org/wiki/Epiphyte",
                "https://en.wikipedia.org/wiki/Nutrient",
                "https://en.wikipedia.org/wiki/Chemical_reaction",
                "https://en.wikipedia.org/wiki/Chemistry",
                "https://en.wikipedia.org/wiki/Chemosynthesis",
                "https://en.wikipedia.org/wiki/Chlorophyll",
                "https://en.wikipedia.org/wiki/Chloroplast",
                "https://en.wikipedia.org/wiki/Cholesterol",
                "https://en.wikipedia.org/wiki/Chromosome",
                "https://en.wikipedia.org/wiki/Cilium",
                "https://en.wikipedia.org/wiki/Circadian_rhythm",
                "https://en.wikipedia.org/wiki/Citric_acid_cycle",
                "https://en.wikipedia.org/wiki/Clade",
                "https://en.wikipedia.org/wiki/Class_(biology)",
                "https://en.wikipedia.org/wiki/Clonal_selection",
                "https://en.wikipedia.org/wiki/Cloning",
                "https://en.wikipedia.org/wiki/Colony_(biology)",
                "https://en.wikipedia.org/wiki/Comparative_biology",
                "https://en.wikipedia.org/wiki/Conservation_biology",
                "https://en.wikipedia.org/wiki/Convergent_evolution",
                "https://en.wikipedia.org/wiki/Countercurrent_exchange",
                "https://en.wikipedia.org/wiki/Crista",
                "https://en.wikipedia.org/wiki/Cryobiology",
                "https://en.wikipedia.org/wiki/Cell_biology",
                "https://en.wikipedia.org/wiki/Cytoplasm",
                "https://en.wikipedia.org/wiki/Cytosine",
                "https://en.wikipedia.org/wiki/Cytoskeleton",
                "https://en.wikipedia.org/wiki/Fitness_(biology)",
                "https://en.wikipedia.org/wiki/Deciduous",
                "https://en.wikipedia.org/wiki/Decomposition",
                "https://en.wikipedia.org/wiki/Dehydration_reaction",
                "https://en.wikipedia.org/wiki/Denaturation_(biochemistry)",
                "https://en.wikipedia.org/wiki/Dendrite",
                "https://en.wikipedia.org/wiki/Denitrification",
                "https://en.wikipedia.org/wiki/DNA",
                "https://en.wikipedia.org/wiki/Depolarization",
                "https://en.wikipedia.org/wiki/Desmosome",
                "https://en.wikipedia.org/wiki/Developmental_biology",
                "https://en.wikipedia.org/wiki/Disease",
                "https://en.wikipedia.org/wiki/DNA_replication",
                "https://en.wikipedia.org/wiki/DNA_sequencing",
                "https://en.wikipedia.org/wiki/Drug",
                "https://en.wikipedia.org/wiki/Dynein",
                "https://en.wikipedia.org/wiki/Ecological_efficiency",
                "https://en.wikipedia.org/wiki/Ecological_pyramid",
                "https://en.wikipedia.org/wiki/Ecological_succession",
                "https://en.wikipedia.org/wiki/Ecology",
                "https://en.wikipedia.org/wiki/Ecophysiology",
                "https://en.wikipedia.org/wiki/Ecosystem",
                "https://en.wikipedia.org/wiki/Ecotype",
                "https://en.wikipedia.org/wiki/Ectoderm",
                "https://en.wikipedia.org/wiki/Ectotherm",
                "https://en.wikipedia.org/wiki/Effector_(biology)",
                "https://en.wikipedia.org/wiki/Egg",
                "https://en.wikipedia.org/wiki/Electrochemical_gradient",
                "https://en.wikipedia.org/wiki/Electron_acceptor",
                "https://en.wikipedia.org/wiki/Electron_transport_chain",
                "https://en.wikipedia.org/wiki/Electron_donor",
                "https://en.wikipedia.org/wiki/Electron_microscope",
                "https://en.wikipedia.org/wiki/Embryo",
                "https://en.wikipedia.org/wiki/Embryology",
                "https://en.wikipedia.org/wiki/Endangered_species",
                "https://en.wikipedia.org/wiki/Endemism",
                "https://en.wikipedia.org/wiki/Endergonic_reaction",
                "https://en.wikipedia.org/wiki/Endocrine_gland",
                "https://en.wikipedia.org/wiki/Endocrine_system",
                "https://en.wikipedia.org/wiki/Endocytosis",
                "https://en.wikipedia.org/wiki/Endoderm",
                "https://en.wikipedia.org/wiki/Endogeny_(biology)",
                "https://en.wikipedia.org/wiki/Endoplasmic_reticulum",
                "https://en.wikipedia.org/wiki/Endosperm",
                "https://en.wikipedia.org/wiki/Symbiogenesis",
                "https://en.wikipedia.org/wiki/Endotherm",
                "https://en.wikipedia.org/wiki/Aerobic_organism",
                "https://en.wikipedia.org/wiki/Aerobiology",
                "https://en.wikipedia.org/wiki/Agriculture",
                "https://en.wikipedia.org/wiki/Agrobiology",
                "https://en.wikipedia.org/wiki/Algae",
                "https://en.wikipedia.org/wiki/Allopatric_speciation",
                "https://en.wikipedia.org/wiki/Amino_acid",
                "https://en.wikipedia.org/wiki/Amniote",
                "https://en.wikipedia.org/wiki/Anaerobic_organism",
                "https://en.wikipedia.org/wiki/Convergent_evolution",
                "https://en.wikipedia.org/wiki/Anatomy",
                "https://en.wikipedia.org/wiki/Animal",
                "https://en.wikipedia.org/wiki/Antibiotic",
                "https://en.wikipedia.org/wiki/Apoptosis",
                "https://en.wikipedia.org/wiki/Arachnology",
                "https://en.wikipedia.org/wiki/Archaea",
                "https://en.wikipedia.org/wiki/Selective_breeding",
                "https://en.wikipedia.org/wiki/Asexual_reproduction",
                "https://en.wikipedia.org/wiki/Astrobiology",
                "https://en.wikipedia.org/wiki/Autoimmunity",
                "https://en.wikipedia.org/wiki/Autotroph",
                "https://en.wikipedia.org/wiki/B_cell",
                "https://en.wikipedia.org/wiki/Bacteria",
                "https://en.wikipedia.org/wiki/Bacteriophage",
                "https://en.wikipedia.org/wiki/Barr_body",
                "https://en.wikipedia.org/wiki/Basal_body",
                "https://en.wikipedia.org/wiki/Behavioral_ecology",
                "https://en.wikipedia.org/wiki/Bile",
                "https://en.wikipedia.org/wiki/Fission_(biology)",
                "https://en.wikipedia.org/wiki/Binomial_nomenclature",
                "https://en.wikipedia.org/wiki/Biocatalysis",
                "https://en.wikipedia.org/wiki/Biochemistry",
                "https://en.wikipedia.org/wiki/Biodiversity",
                "https://en.wikipedia.org/wiki/Biological_engineering",
                "https://en.wikipedia.org/wiki/Bioenergetics",
                "https://en.wikipedia.org/wiki/Biogeography",
                "https://en.wikipedia.org/wiki/Bioinformatics",
                "https://en.wikipedia.org/wiki/Biological_organisation",
                "https://en.wikipedia.org/wiki/Biology",
                "https://en.wikipedia.org/wiki/Biomass",
                "https://en.wikipedia.org/wiki/Mathematical_and_theoretical_biology",
                "https://en.wikipedia.org/wiki/Biome",
                "https://en.wikipedia.org/wiki/Biomechanics",
                "https://en.wikipedia.org/wiki/Biomedical_engineering",
                "https://en.wikipedia.org/wiki/Medical_research",
                "https://en.wikipedia.org/wiki/Biomolecule",
                "https://en.wikipedia.org/wiki/Biophysics",
                "https://en.wikipedia.org/wiki/Biosynthesis",
                "https://en.wikipedia.org/wiki/Biotechnology",
                "https://en.wikipedia.org/wiki/Bipedalism",
                "https://en.wikipedia.org/wiki/Birth",
                "https://en.wikipedia.org/wiki/Blastocyst",
                "https://en.wikipedia.org/wiki/Blood",
                "https://en.wikipedia.org/wiki/Blood%E2%80%93brain_barrier",
                "https://en.wikipedia.org/wiki/Botany",
                "https://en.wikipedia.org/wiki/Building_biology",
                "https://en.wikipedia.org/wiki/Calvin_cycle",
                "https://en.wikipedia.org/wiki/Carbon_fixation",
                "https://en.wikipedia.org/wiki/Carbonate",
                "https://en.wikipedia.org/wiki/Carotenoid",
                "https://en.wikipedia.org/wiki/Catalase",
                "https://en.wikipedia.org/wiki/Cell_(biology)",
                "https://en.wikipedia.org/wiki/Cell_biology",
                "https://en.wikipedia.org/wiki/Cell_cycle",
                "https://en.wikipedia.org/wiki/Cell_division",
                "https://en.wikipedia.org/wiki/Cell_membrane",
                "https://en.wikipedia.org/wiki/Cell_nucleus",
                "https://en.wikipedia.org/wiki/Cell_plate",
                "https://en.wikipedia.org/wiki/Cell_theory",
                "https://en.wikipedia.org/wiki/Cell_wall",
                "https://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology",
                "https://en.wikipedia.org/wiki/Centriole",
                "https://en.wikipedia.org/wiki/Centrosome",
                "https://en.wikipedia.org/wiki/Chemical_compound",
                "https://en.wikipedia.org/wiki/Chemical_equilibrium",
                "https://en.wikipedia.org/wiki/Population_biology",
                "https://en.wikipedia.org/wiki/Population_ecology",
                "https://en.wikipedia.org/wiki/Predation",
                "https://en.wikipedia.org/wiki/Primer_(molecular_biology)",
                "https://en.wikipedia.org/wiki/Progesterone",
                "https://en.wikipedia.org/wiki/Prokaryote",
                "https://en.wikipedia.org/wiki/Protein",
                "https://en.wikipedia.org/wiki/Protist",
                "https://en.wikipedia.org/wiki/Behavioral_neuroscience",
                "https://en.wikipedia.org/wiki/Regeneration_(biology)",
                "https://en.wikipedia.org/wiki/Reproduction",
                "https://en.wikipedia.org/wiki/Reproductive_biology",
                "https://en.wikipedia.org/wiki/RNA",
                "https://en.wikipedia.org/wiki/Ribosome",
                "https://en.wikipedia.org/wiki/RNA_polymerase",
                "https://en.wikipedia.org/wiki/Ground_tissue",
                "https://en.wikipedia.org/wiki/Seed",
                "https://en.wikipedia.org/wiki/Selective_breeding",
                "https://en.wikipedia.org/wiki/Sessility_(motility)",
                "https://en.wikipedia.org/wiki/Sex",
                "https://en.wikipedia.org/wiki/Sexual_reproduction",
                "https://en.wikipedia.org/wiki/Sociality",
                "https://en.wikipedia.org/wiki/Sociobiology",
                "https://en.wikipedia.org/wiki/Soil_biology",
                "https://en.wikipedia.org/wiki/Species",
                "https://en.wikipedia.org/wiki/Speciation",
                "https://en.wikipedia.org/wiki/Sperm",
                "https://en.wikipedia.org/wiki/Spore",
                "https://en.wikipedia.org/wiki/Stem_cell",
                "https://en.wikipedia.org/wiki/Steroid",
                "https://en.wikipedia.org/wiki/Strain_(biology)",
                "https://en.wikipedia.org/wiki/Structural_biology",
                "https://en.wikipedia.org/wiki/Symbiogenesis",
                "https://en.wikipedia.org/wiki/Symbiosis",
                "https://en.wikipedia.org/wiki/Synthetic_biology",
                "https://en.wikipedia.org/wiki/Systematics",
                "https://en.wikipedia.org/wiki/Systems_biology",
                "https://en.wikipedia.org/wiki/T_cell",
                "https://en.wikipedia.org/wiki/Taxon",
                "https://en.wikipedia.org/wiki/Taxonomy_(biology)",
                "https://en.wikipedia.org/wiki/Telophase",
                "https://en.wikipedia.org/wiki/Testosterone",
                "https://en.wikipedia.org/wiki/Thymine",
                "https://en.wikipedia.org/wiki/Tissue_(biology)",
                "https://en.wikipedia.org/wiki/Phenotypic_trait",
                "https://en.wikipedia.org/wiki/Transcription_(biology)",
                "https://en.wikipedia.org/wiki/Translation_(biology)",
                "https://en.wikipedia.org/wiki/Trophic_level",
                "https://en.wikipedia.org/wiki/Neoplasm",
                "https://en.wikipedia.org/wiki/Unicellular_organism",
                "https://en.wikipedia.org/wiki/Uracil",
                "https://en.wikipedia.org/wiki/Urea",
                "https://en.wikipedia.org/wiki/Urine",
                "https://en.wikipedia.org/wiki/Uterus",
                "https://en.wikipedia.org/wiki/Vacuole",
                "https://en.wikipedia.org/wiki/Vasodilation",
                "https://en.wikipedia.org/wiki/Vector_(epidemiology)",
                "https://en.wikipedia.org/wiki/Vegetative_reproduction",
                "https://en.wikipedia.org/wiki/Vertebrate",
                "https://en.wikipedia.org/wiki/Vesicle_(biology_and_chemistry)",
                "https://en.wikipedia.org/wiki/Vestigiality",
                "https://en.wikipedia.org/wiki/Virology",
                "https://en.wikipedia.org/wiki/Virus",
                "https://en.wikipedia.org/wiki/White_blood_cell",
                "https://en.wikipedia.org/wiki/Whole_genome_sequencing",
                "https://en.wikipedia.org/wiki/Wood",
                "https://en.wikipedia.org/wiki/Xanthophyll",
                "https://en.wikipedia.org/wiki/Xylem",
                "https://en.wikipedia.org/wiki/Yolk",
                "https://en.wikipedia.org/wiki/Zoology",
                "https://en.wikipedia.org/wiki/Zooplankton",
                "https://en.wikipedia.org/wiki/Zygospore",
                "https://en.wikipedia.org/wiki/Zygote",
                "https://en.wikipedia.org/wiki/Mast_cell",
                "https://en.wikipedia.org/wiki/Mating",
                "https://en.wikipedia.org/wiki/Medulla_oblongata",
                "https://en.wikipedia.org/wiki/Meiosis",
                "https://en.wikipedia.org/wiki/Membrane_potential",
                "https://en.wikipedia.org/wiki/Messenger_RNA",
                "https://en.wikipedia.org/wiki/Metabolism",
                "https://en.wikipedia.org/wiki/Metamorphosis",
                "https://en.wikipedia.org/wiki/Metaphase",
                "https://en.wikipedia.org/wiki/Microbiology",
                "https://en.wikipedia.org/wiki/Microevolution",
                "https://en.wikipedia.org/wiki/Mitochondrion",
                "https://en.wikipedia.org/wiki/Mitosis",
                "https://en.wikipedia.org/wiki/Molecule",
                "https://en.wikipedia.org/wiki/Molecular_biology",
                "https://en.wikipedia.org/wiki/Molecular_switch",
                "https://en.wikipedia.org/wiki/Monomer",
                "https://en.wikipedia.org/wiki/Morphology_(biology)",
                "https://en.wikipedia.org/wiki/Motility",
                "https://en.wikipedia.org/wiki/Motor_neuron",
                "https://en.wikipedia.org/wiki/Mucous_membrane",
                "https://en.wikipedia.org/wiki/Multicellular_organism",
                "https://en.wikipedia.org/wiki/Mycology",
                "https://en.wikipedia.org/wiki/Myofibril",
                "https://en.wikipedia.org/wiki/Myosin",
                "https://en.wikipedia.org/wiki/Natural_selection",
                "https://en.wikipedia.org/wiki/Neuroscience",
                "https://en.wikipedia.org/wiki/Neuron",
                "https://en.wikipedia.org/wiki/Neurotransmitter",
                "https://en.wikipedia.org/wiki/Ecological_niche",
                "https://en.wikipedia.org/wiki/Nucleic_acid",
                "https://en.wikipedia.org/wiki/Nucleic_acid_sequence",
                "https://en.wikipedia.org/wiki/Nucleobase",
                "https://en.wikipedia.org/wiki/Nucleoid",
                "https://en.wikipedia.org/wiki/Nucleolus",
                "https://en.wikipedia.org/wiki/Nucleotide",
                "https://en.wikipedia.org/wiki/Offspring",
                "https://en.wikipedia.org/wiki/Order_(biology)",
                "https://en.wikipedia.org/wiki/Organ_(anatomy)",
                "https://en.wikipedia.org/wiki/Organism",
                "https://en.wikipedia.org/wiki/Ornithology",
                "https://en.wikipedia.org/wiki/Osmosis",
                "https://en.wikipedia.org/wiki/Paleontology",
                "https://en.wikipedia.org/wiki/Parallel_evolution",
                "https://en.wikipedia.org/wiki/Parasitism",
                "https://en.wikipedia.org/wiki/Parasitology",
                "https://en.wikipedia.org/wiki/Pathology",
                "https://en.wikipedia.org/wiki/Pathogen",
                "https://en.wikipedia.org/wiki/PH",
                "https://en.wikipedia.org/wiki/Pharmacology",
                "https://en.wikipedia.org/wiki/Phenotype",
                "https://en.wikipedia.org/wiki/Pheromone",
                "https://en.wikipedia.org/wiki/Phloem",
                "https://en.wikipedia.org/wiki/Photosynthesis",
                "https://en.wikipedia.org/wiki/Phylogenetic_tree",
                "https://en.wikipedia.org/wiki/Phylum",
                "https://en.wikipedia.org/wiki/Physiology",
                "https://en.wikipedia.org/wiki/Phytochemistry",
                "https://en.wikipedia.org/wiki/Plant_pathology",
                "https://en.wikipedia.org/wiki/Placebo",
                "https://en.wikipedia.org/wiki/Plant",
                "https://en.wikipedia.org/wiki/Plasmolysis",
                "https://en.wikipedia.org/wiki/Pollination",
                "https://en.wikipedia.org/wiki/Polymer",
                "https://en.wikipedia.org/wiki/Polymerase_chain_reaction",
                "https://en.wikipedia.org/wiki/Polyploidy",
                "https://en.wikipedia.org/wiki/Population",
                "https://en.wikipedia.org/wiki/Lichen",
                "https://en.wikipedia.org/wiki/Life",
                "https://en.wikipedia.org/wiki/Biological_life_cycle",
                "https://en.wikipedia.org/wiki/Ligament",
                "https://en.wikipedia.org/wiki/Calvin_cycle",
                "https://en.wikipedia.org/wiki/Genetic_linkage",
                "https://en.wikipedia.org/wiki/Lipid",
                "https://en.wikipedia.org/wiki/Lipoprotein",
                "https://en.wikipedia.org/wiki/Cell_cycle",
                "https://en.wikipedia.org/wiki/Macroevolution",
                "https://en.wikipedia.org/wiki/Macromolecule",
                "https://en.wikipedia.org/wiki/Macrophage",
                "https://en.wikipedia.org/wiki/Mammalogy",
                "https://en.wikipedia.org/wiki/Marine_biology",
                "https://en.wikipedia.org/wiki/Herpetology",
                "https://en.wikipedia.org/wiki/Heterosis",
                "https://en.wikipedia.org/wiki/Heterotroph",
                "https://en.wikipedia.org/wiki/Histology",
                "https://en.wikipedia.org/wiki/Hormone",
                "https://en.wikipedia.org/wiki/Host_(biology)",
                "https://en.wikipedia.org/wiki/Hybrid_(biology)",
                "https://en.wikipedia.org/wiki/Hydrocarbon",
                "https://en.wikipedia.org/wiki/Ichthyology",
                "https://en.wikipedia.org/wiki/Immune_response",
                "https://en.wikipedia.org/wiki/Immunity_(medical)",
                "https://en.wikipedia.org/wiki/Antibody",
                "https://en.wikipedia.org/wiki/Infection",
                "https://en.wikipedia.org/wiki/Insulin",
                "https://en.wikipedia.org/wiki/Integrative_Biology",
                "https://en.wikipedia.org/wiki/Interferon",
                "https://en.wikipedia.org/wiki/Internal_fertilization",
                "https://en.wikipedia.org/wiki/International_System_of_Units",
                "https://en.wikipedia.org/wiki/Interphase",
                "https://en.wikipedia.org/wiki/Introduced_species",
                "https://en.wikipedia.org/wiki/Invertebrate",
                "https://en.wikipedia.org/wiki/Ion",
                "https://en.wikipedia.org/wiki/Ionic_bonding",
                "https://en.wikipedia.org/wiki/Isomer",
                "https://en.wikipedia.org/wiki/Tonicity",
                "https://en.wikipedia.org/wiki/Jejunum",
                "https://en.wikipedia.org/wiki/Kinase",
                "https://en.wikipedia.org/wiki/Kingdom_(biology)",
                "https://en.wikipedia.org/wiki/Citric_acid_cycle",
                "https://en.wikipedia.org/wiki/Larva",
                "https://en.wikipedia.org/wiki/Mendelian_inheritance",
                "https://en.wikipedia.org/wiki/White_blood_cell",
                "https://en.wikipedia.org/wiki/Facultative_anaerobic_organism",
                "https://en.wikipedia.org/wiki/Family_(biology)",
                "https://en.wikipedia.org/wiki/Fermentation",
                "https://en.wikipedia.org/wiki/Fitness_(biology)",
                "https://en.wikipedia.org/wiki/Fitness_landscape",
                "https://en.wikipedia.org/wiki/Fertilisation",
                "https://en.wikipedia.org/wiki/Fetus",
                "https://en.wikipedia.org/wiki/Flagellum",
                "https://en.wikipedia.org/wiki/Flavin_adenine_dinucleotide",
                "https://en.wikipedia.org/wiki/Food_chain",
                "https://en.wikipedia.org/wiki/Founder_effect",
                "https://en.wikipedia.org/wiki/Fungus",
                "https://en.wikipedia.org/wiki/G_protein",
                "https://en.wikipedia.org/wiki/Gamete",
                "https://en.wikipedia.org/wiki/Gene",
                "https://en.wikipedia.org/wiki/Gene_pool",
                "https://en.wikipedia.org/wiki/Genetic_code",
                "https://en.wikipedia.org/wiki/Genetic_drift",
                "https://en.wikipedia.org/wiki/Genetic_variation",
                "https://en.wikipedia.org/wiki/Genetics",
                "https://en.wikipedia.org/wiki/Genome",
                "https://en.wikipedia.org/wiki/Genotype",
                "https://en.wikipedia.org/wiki/Genus",
                "https://en.wikipedia.org/wiki/Gizzard",
                "https://en.wikipedia.org/wiki/Guanine",
                "https://en.wikipedia.org/wiki/Habitat",
                "https://en.wikipedia.org/wiki/Habituation",
                "https://en.wikipedia.org/wiki/Heredity",
                "https://en.wikipedia.org/wiki/Hermaphrodite"
            ]

            for url in urls:
                # Request the content of a page from the url
                html = requests.get(url)

                time.sleep(3)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                # title of the movie
                title = ""

                if soup.select_one("#firstHeading") is not None:
                    title += str(soup.select_one("#firstHeading")
                                 .text
                                 .lower()
                                 .replace(" ", "_")
                                 .replace("/", "_")
                                 .replace("-", "_")
                                 .replace(":", "_")
                                 .replace("\n", "")
                                 .replace("?", "_")
                                 .replace("'", "_")
                                 .replace("(", "_")
                                 .replace(")", "_")
                                 ) + ".avi"

                    print("title : " + title)

                # Text to speech and images
                text = ""

                if soup.select_one("#bodyContent") is not None:
                    text += str(soup.select_one("#bodyContent").text)

                # Filename for audio
                audio_file = os.getcwd() + "\\audio\\" + text[:50] \
                    .replace(":", "") \
                    .replace(" ", "") \
                    .replace("\n", "") \
                    .replace("?", "") \
                    .replace("/", "") \
                    .replace("-", "") + '.mp3'

                try:
                    # Convert text to audio
                    tts = gTTS(text.replace("", "")
                               .replace(".", "")
                               .replace("©", "")
                               .replace("*", "")
                               .replace("-", " ")
                               .replace("✔", "")
                               .replace("•", "")
                               .replace("⇒", "")
                               .replace("↑", "")
                               .replace("→", ""))

                    # Save the audio
                    tts.save(audio_file)
                except Exception as e:
                    print("error convert text to audio")

                # Folder of images
                image_folder = os.getcwd() + '\\images'

                # Create images from the text
                number_of_caracters_of_text = len(text.replace('\t', ' ').replace('\n', ' '))
                number_of_caracters_per_line = 110

                number_of_lines_with_coma = number_of_caracters_of_text / number_of_caracters_per_line
                number_of_lines = 0

                if int(str(number_of_lines_with_coma).split(".")[1][:1]) < 5:
                    number_of_lines += round(number_of_lines_with_coma) + 1

                elif int(str(number_of_lines_with_coma).split(".")[1][:1]) >= 5:
                    number_of_lines += round(number_of_lines_with_coma)

                number_of_lines_per_image = 10

                number_of_images_with_coma = number_of_lines / number_of_lines_per_image
                number_of_images = 0

                if int(str(number_of_images_with_coma).split('.')[1][:1]) < 5:
                    number_of_images += round(number_of_images_with_coma) + 1

                elif int(str(number_of_images_with_coma).split(".")[1][:1]) >= 5:
                    number_of_images += round(number_of_images_with_coma)

                # Array duration of each clip
                durations_of_each_clip = [0]

                l = 0

                duration = 0

                for i in range(1, number_of_images + 1):
                    img = Image.new('RGB', (700, 300), color=(255, 255, 255))
                    d = ImageDraw.Draw(img)

                    if l <= number_of_lines:
                        for j in range(0, 10):
                            depart = 110 * l
                            arrivee = 110 + 110 * l
                            coordinate_y = 25 * j

                            if j < 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 1 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(
                                            MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                            elif j == 9:
                                try:
                                    d.text((10, coordinate_y), text[depart:arrivee]
                                           .replace('\t', ' ')
                                           .replace('\n', ' ')
                                           .replace(u"\u2018", " ")
                                           .replace(u"\u2019", " ")
                                           .replace(u"\u0153", " ")
                                           .replace(u"\u2013", " ")
                                           .replace(u"\u2015", " ")
                                           .replace(u"\u2014", " ")
                                           .replace(u"\u2207", " ")
                                           .replace(u"\u03c4", " ")
                                           .replace(u"\u201c", " ")
                                           .replace(u"\u201d", " ")
                                           .replace(u"\u0113", " ")
                                           , fill=(0, 0, 0))
                                except Exception as e:
                                    print("add text 2 : " + str(e))

                                if text[depart:arrivee] != "":
                                    try:
                                        tts = gTTS(text[depart:arrivee]
                                                   .replace('\t', ' ')
                                                   .replace('\n', ' ')
                                                   .replace(u"\u2018", " ")
                                                   .replace(u"\u2019", " ")
                                                   .replace(u"\u0153", " ")
                                                   .replace(u"\u2013", " ")
                                                   .replace(u"\u2015", " ")
                                                   .replace(u"\u2014", " ")
                                                   .replace(u"\u2207", " ")
                                                   .replace(u"\u03c4", " ")
                                                   .replace(u"\u201c", " ")
                                                   .replace(u"\u201d", " ")
                                                   .replace(u"\u0113", " ")
                                                   .replace("", "")
                                                   .replace(".", "")
                                                   .replace("©", "")
                                                   .replace("*", "")
                                                   .replace("-", " ")
                                                   .replace("✔", "")
                                                   .replace("•", "")
                                                   .replace("⇒", "")
                                                   .replace("↑", "")
                                                   .replace("→", ""))

                                        tts.save(os.getcwd() + "\\audio\\audio_line.mp3")

                                        duration += round(MP3(os.getcwd() + "\\audio\\audio_line.mp3").info.length)

                                        os.remove(os.getcwd() + "\\audio\\audio_line.mp3")

                                        img.save(image_folder + "\\" + str(i) + ".png")

                                        durations_of_each_clip.append(duration)

                                        l += 1
                                    except Exception as e:
                                        print("error : l = " + str(l) + " et j = "
                                              + str(j) + " " + str(e))
                                else:
                                    print("break : l = " + str(l) + " et j = " + str(j))
                                    durations_of_each_clip.append(duration)
                                    img.save(image_folder + "\\" + str(i) + ".png")
                                    break

                # Appending the images to the video one by one
                images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

                for i in range(1, number_of_images + 1):
                    try:
                        frame = cv2.imread(os.path.join(image_folder, images[0]))

                        # setting the frame width, height width the width, height of first image
                        height, width, layers = frame.shape

                        # video to create
                        video = cv2.VideoWriter(os.getcwd() + '\\videos\\video_' + str(i) + '.avi', 0,
                                                1,
                                                (width, height))

                        for j in range((durations_of_each_clip[i] - durations_of_each_clip[i - 1])):
                            video.write(cv2.imread(os.path.join(image_folder, image_folder
                                                                + "\\" + str(i) + ".png")))

                        # Deallocating memories taken for window creation
                        cv2.destroyAllWindows()

                        # releasing the video generated
                        video.release()

                    except Exception as e:
                        print("error video write : " + str(e))

                clips = []

                for i in range(1, number_of_images + 1):
                    try:
                        clips.append(VideoFileClip(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')
                                     .set_start(durations_of_each_clip[i - 1]))
                    except Exception as e:
                        print("Error to append videos : " + str(e))

                try:
                    CompositeVideoClip(clips).write_videofile(
                        os.getcwd() + '\\videos\\my_concatenation.mp4')
                except Exception as e:
                    print("Error CompositeVideoClip : " + str(e))

                try:
                    output_movie = os.getcwd() + "\\videos_creees\\" + directory + "\\" + title
                    ffmpeg_merge_video_audio(os.getcwd() + '\\videos\\my_concatenation.mp4', audio_file, output_movie,
                                             vcodec='copy', acodec='copy',
                                             ffmpeg_output=False, logger='bar')
                except Exception as e:
                    print("output movie exception : " + str(e))
        finally:
            # Delete all images
            for i in range(1, number_of_images + 1):
                os.remove(image_folder + "\\" + str(i) + ".png")

            # Delete all clips
            for i in range(1, number_of_images + 1):
                os.remove(os.getcwd() + '\\videos\\video_' + str(i) + '.avi')

            os.remove(os.getcwd() + '\\videos\\my_concatenation.mp4')
            os.remove(audio_file)


if __name__ == '__main__':
    unittest.main()
