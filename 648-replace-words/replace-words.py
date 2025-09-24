class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = list(sentence.split(" "))
        for i in range(len(dictionary)):
            n = len(dictionary[i])
            for j in range(len(sentence)):
                if dictionary[i] in sentence[j][:n]:
                    sentence[j] = dictionary[i]
        return (" ").join(sentence)