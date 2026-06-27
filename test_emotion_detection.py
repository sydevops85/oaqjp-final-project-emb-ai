import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Unit tests for the emotion_detector function
    in the EmotionDetection package.
    """

    def test_emotion_pairs(self):
        """
        Test multiple statements against expected dominant emotions.
        """
        # Define test cases as (statement, expected_emotion)
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for statement, expected_emotion in test_cases:
            with self.subTest(statement=statement):
                result = emotion_detector(statement)
                self.assertEqual(
                    result["dominant_emotion"],
                    expected_emotion,
                    msg=f"Failed for statement: {statement}"
                )


if __name__ == "__main__":
    unittest.main()
