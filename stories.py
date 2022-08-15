"""Madlibs Stories."""


from distutils.log import set_verbosity


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, title="untitled story"):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title
    
    # def __repr__(self):
    #     return str(self.title)
    
    # def __str__(self):
    #     return str(self.title)

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural noun}.""",
       "Past Story"
)

story2 = Story(
    ["proper noun", "occupation", "number", "currency", "emotion"],
    """{proper noun} was a successful {occupation} who earned {number} {currency} each year.
    They loved their job because it makes them feel {emotion}.""",
    "Present Story"
)

story3 = Story(
    ["personality trait", "occupation", "verb", "plural noun", "family relative", "emotion"],
    """In the near future there was a {personality trait} {occupation} who enjoyed {verb} {plural noun}.
    This caused his {family relative} to feel {emotion} about him.""",
    "Future Story"
)

story_list = {story1.title : story1,
story2.title : story2,
story3.title : story3}

#print(story_list)

#print(story.generate({'place': 'Las Vegas', 'noun' : 'dog', 'adjective' : 'furry', 'plural_noun' : 'kids', 'verb': 'eat'}))
# print(story2.generate({"proper_noun" : "Karl",
# "occupation": "serial killer",
# "number": "7 million",
# "currency": "Drachmae",
# "emotion": "glee"}))

# print(story3.generate({
#     "personality_trait" : "cynical",
#     "occupation" : "farmer",
#     "verb": "eating",
#     "plural_noun": "kids",
#     "family_relative" : "son",
#     "emotion" : "scornful"
# }))