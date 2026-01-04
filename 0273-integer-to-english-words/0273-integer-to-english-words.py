class Solution:
    def numberToWords(self, num: int) -> str:
        # word mappings
        units = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        teens = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        scales = ["", "Thousand", "Million", "Billion"]

        def convertLessThanHundred(n):
            if n < 10:
                return units[n]
            elif 10 <= n < 20:
                return teens[n - 10]
            else:
                tensPart = tens[n//10]
                unitsPart = units[n % 10]

                if unitsPart != "":
                    return tensPart + " " + unitsPart #Twenty-One
                else:
                    return tensPart #Fifty
        
        def convertThreeDigits(n):
            if n == 0:
                return ""
            hundreds = n // 100
            remainders = n % 100

            result = []
            if hundreds > 0:
                result.append(units[hundreds] + " " + "Hundred")
            if remainders > 0:
                result.append(convertLessThanHundred(remainders))
            
            return " ".join(result) # "Two Hundred Forty-Five"
        

        if num == 0: return "Zero"
        # Chunks
        chunks = []
        while num > 0:
            chunks.append(num%1000)
            num = num // 1000
        result = []
        for i in range(len(chunks) -1, -1, -1):
            chunk = convertThreeDigits(chunks[i])
            if chunk != "":
                if i > 0:
                    chunk += " " + scales[i]
                result.append(chunk)
        return " ".join(result)

