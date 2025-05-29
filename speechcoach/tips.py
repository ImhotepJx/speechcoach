class PronunciationTips:
    def __init__(self):
        self.tips = {
            'en': "Focus on clear vowel sounds and stress patterns.",
            'es': "Pay attention to rolled R's and open vowels.",
            'fr': "Watch out for nasal sounds and silent letters.",
            'de': "Practice hard consonants and umlaut vowels (ä, ö, ü)."
        }

    def get_tip(self, text, lang):
        return self.tips.get(lang, "No specific tip available for this language.")
