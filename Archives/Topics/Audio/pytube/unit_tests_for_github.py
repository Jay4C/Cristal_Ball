import unittest
import pytube as pt


class UnitTestsAudioPytubeForGitHub(unittest.TestCase):
    # ok
    def test_download_one_video_into_mp3(self):
        print('test_download_one_video_into_mp3')

        url = 'https://www.youtube.com/watch?v=pxjsZK_fkO4'
        yt = pt.YouTube(url=url)
        t = yt.streams.filter(only_audio=True)
        t[0].download()


if __name__ == '__main__':
    unittest.main()
