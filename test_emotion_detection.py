import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy_emotion(self):
        result = emotion_detector("我很高兴发生了这种事")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        result = emotion_detector("我对此非常生气")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        result = emotion_detector("仅仅听到这个我就感到厌恶")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        result = emotion_detector("我对此感到非常悲伤")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        result = emotion_detector("我真的很害怕这会发生")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main() 