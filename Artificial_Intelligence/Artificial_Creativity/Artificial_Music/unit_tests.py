import unittest
import sounddevice as sd
from scipy.io.wavfile import write


class UnitTestsMusic(unittest.TestCase):
    def test_record_a_sound_from_micro(self):
        print("test_play_one_sample_rate")

        # Minimal sample rate = 1000
        # Maximal sample rate = 384000

        # Sample rate
        fs = 45000

        # Duration of recording
        seconds = 10

        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

        # Wait until recording is finished
        sd.wait()

        # Save as WAV file
        write('output.wav', fs, myrecording)


if __name__ == '__main__':
    unittest.main()
