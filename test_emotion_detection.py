from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Note: These tests rely on the external API being available
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['emotion'], 'joy')

        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['emotion'], 'anger')

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['emotion'], 'disgust')

        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['emotion'], 'sadness')

        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()