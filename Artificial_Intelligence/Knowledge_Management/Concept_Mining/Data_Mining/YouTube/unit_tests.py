import os
import time
import unittest
from pytube import YouTube
import re
import moviepy.editor as mp
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class UnitTestsDataMiningYouTube(unittest.TestCase):
    def test_download_youtube_videos(self):
        print("test_download_youtube_videos")

        youtube_link = "https://www.youtube.com/watch?v=hyTplvO4i9U"

        # download a file from youtube
        w = YouTube(youtube_link).streams.first()
        w.download(output_path='file',
                   filename=youtube_link.replace("https://www.youtube.com/watch?v=", "") + '.3gpp'
                   )

    def test_download_youtube_videos_for_only_mp4(self):
        print('test_download_youtube_videos_for_only_mp3')

        youtube_link = "https://www.youtube.com/watch?v=hyTplvO4i9U"

        # download a file with only audio, to save space
        # if the final goal is to convert to mp3
        y = YouTube(youtube_link)
        t = y.streams.filter(only_audio=True).all()
        t[0].download(output_path='mp4')

    def test_download_multiple_youtube_videos_for_stanley_meyer(self):
        print('test_download_multiple_youtube_videos_for_only_mp4')

        urls = [
            "https://www.youtube.com/watch?v=hyTplvO4i9U",
            "https://www.youtube.com/watch?v=Y1MaoxF3xM8",
            "https://www.youtube.com/watch?v=pKZ_67cReu0",
            "https://www.youtube.com/watch?v=j92FfWfWHLY",
            "https://www.youtube.com/watch?v=HHxK1VWrXcM",
            "https://www.youtube.com/watch?v=5YdsDbBJe-o",
            "https://www.youtube.com/watch?v=om6jN1A8Q70",
            "https://www.youtube.com/watch?v=Zf6GvCvcEDg",
            "https://www.youtube.com/watch?v=6eo72UKIae8",
            "https://www.youtube.com/watch?v=GsMOFHPjZpo",
            "https://www.youtube.com/watch?v=FAfAfzI8_rQ",
            "https://www.youtube.com/watch?v=xcF74Q_7kEI",
            "https://www.youtube.com/watch?v=OXctY1K4wko",
            "https://www.youtube.com/watch?v=aCV98ajnTA0",
            "https://www.youtube.com/watch?v=dFlkoQ6lkDQ",
            "https://www.youtube.com/watch?v=-T20Wmjce2E",
            "https://www.youtube.com/watch?v=_-hY09qYfhw",
            "https://www.youtube.com/watch?v=_PnVXbxHMkw",
            "https://www.youtube.com/watch?v=fxciCZHHAn4",
            "https://www.youtube.com/watch?v=ZSqPHSNrILM",
            "https://www.youtube.com/watch?v=jC4qSMH66kU",
            "https://www.youtube.com/watch?v=mVJV7rTyfp4",
            "https://www.youtube.com/watch?v=JYeI7r52Oyg",
            "https://www.youtube.com/watch?v=tRNCBiAn-lU",
            "https://www.youtube.com/watch?v=4nnvley2N4g",
            "https://www.youtube.com/watch?v=W-9PdVLU6zw",
            "https://www.youtube.com/watch?v=IhoYScyMMbc",
            "https://www.youtube.com/watch?v=hZ756IB8G2Q",
            "https://www.youtube.com/watch?v=ELkH3rXRQ1w",
            "https://www.youtube.com/watch?v=5X43sKFfRts",
            "https://www.youtube.com/watch?v=4_jCKBv_fxo",
            "https://www.youtube.com/watch?v=gigKSrDLtzM",
            "https://www.youtube.com/watch?v=0JN_4VxjUHA",
            "https://www.youtube.com/watch?v=q51igGQrZGE",
            "https://www.youtube.com/watch?v=F-FgsE7s4YY",
            "https://www.youtube.com/watch?v=YSmxliLwhT8",
            "https://www.youtube.com/watch?v=I5xsMryzxnA",
            "https://www.youtube.com/watch?v=NgEDL9XEN7Y",
            "https://www.youtube.com/watch?v=x4empHPqAxc",
            "https://www.youtube.com/watch?v=DcaSL0yQ6Kg",
            "https://www.youtube.com/watch?v=nCm4X7g6gq0",
            "https://www.youtube.com/watch?v=5pctHhgaJVw",
            "https://www.youtube.com/watch?v=DKtLhQ7tpZM"
        ]

        for url in urls:
            print(url)
            w = YouTube(url).streams.first()
            w.download(output_path='stanley_meyer',
                       filename=url.replace("https://www.youtube.com/watch?v=", "") + '.3gpp'
                       )
            time.sleep(5)

    def test_converting_from_mp4_to_mp3(self):
        print('test_converting_from_mp4_to_mp3')

        tgt_folder = "mp4"

        for file in [n for n in os.listdir(tgt_folder) if re.search('mp4', n)]:
            full_path = os.path.join(tgt_folder, file)
            output_path = os.path.join("mp3", os.path.splitext(file)[0] + '.mp3')
            clip = mp.AudioFileClip(full_path).subclip(10, )  # disable if do not want any clipping
            clip.write_audiofile(output_path)

    def test_extract_all_url_videos_from_one_channel(self):
        print("test_extract_all_url_videos_from_channel")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_channel = "https://www.youtube.com/user/TheEngpjk/videos"

        html = requests.get(url=url_channel, headers=headers)

        print(html.text)

        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find('a', {'class': 'yt-simple-endpoint'}) is not None:
            all_a = soup.find_all('a', {'class': 'yt-simple-endpoint'})

            for a in all_a:
                print('url : ' + a.get('href'))

    def test_extract_all_url_videos_from_one_channel_with_rpa_with_headless(self):
        print("test_extract_all_url_videos_from_one_channel_with_rpa_without_headless")

        url_channel = "https://www.youtube.com/user/TheEngpjk/videos"

        # with Firefox
        options = Options()
        options.headless = True
        # browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(20)

        # maximize window
        browser.maximize_window()

        time.sleep(10)

        # open
        browser.get(url_channel)
        print("page opened")

        time.sleep(15)

        j_accepte_button = browser.find_element_by_xpath(
            "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button"
        )
        j_accepte_button.click()

        time.sleep(15)

        all_a = browser.find_elements_by_id(
            "video-title"
        )

        for a in all_a:
            print("'" + a.get_attribute("href") + "',")

        time.sleep(10)

        browser.close()
        print("browser closed")


if __name__ == '__main__':
    unittest.main()
