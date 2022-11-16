import unittest
from pydub import AudioSegment
import speech_recognition as sr


class UnitTestsSpeechRecognition(unittest.TestCase):
    def test_convert_mp3_into_wav(self):
        print('test_convert_mp3_into_wav')

        # files
        src = "mp3\\file.mp3"
        dst = "wav\\test.wav"

        # convert wav to mp3
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")

    def test_convert_speech_into_text_from_one_wav_file(self):
        print('test_convert_speech_into_text_from_one_wav_file')

        filename = "wav\\test.wav"

        # initialize the recognizer
        r = sr.Recognizer()

        # open the file
        with sr.AudioFile(filename) as source:
            audio_text = r.listen(source)

            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:
                # using google speech recognition
                # text = r.recognize_google(audio_text)
                text = r.recognize_sphinx(audio_text)
                print('Converting audio transcripts into text ... \n')
                print(text)

            except Exception as e:
                print('Sorry.. run again... : ' + str(e))


if __name__ == '__main__':
    unittest.main()
