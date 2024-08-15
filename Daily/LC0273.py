class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        # Words for numbers less than 20
        lt20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
            'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        # Tens place words
        tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
            'Seventy', 'Eighty', 'Ninety']

        # Units of thousand
        thousands = ['Billion', 'Million', 'Thousand', '']

        def translate(n):
            if n == 0:
                return ''
            elif n < 20:
                return lt20[n] + ' '
            elif n < 100:
                return tens[n//10] + ' ' + translate(n%10)
            else:
                return lt20[n//100] + ' Hundred ' + translate(n%100)
        
        result = []
        i, j = 1000000000, 0
        while i > 0:
            if num // i != 0:
                result.append(translate(num // i))
                result.append(thousands[j])
                result.append(' ')
                num %= i
            j += 1
            i //= 1000
        
        return ''.join(result).strip()
