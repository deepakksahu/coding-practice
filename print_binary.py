#from https://rb.gy/mdb28n
#https://rb.gy/ksjhzd

#Problem: Given a real number between 0 and 1, print the binary representation.
# If the length of the representation is > 32, return 'ERROR'.

class Bits(object):
    MAX_BITS = 32

    def print_binary(self, num):
        if num is None or num >= 1 or num <= 0:
            return 'ERROR'
        result = ['0', '.']
        fraction = 0.5
        while num:
            if num >= fraction:
                result.append('1')
                num -= fraction
            else:
                result.append('0')
            if len(result) > self.MAX_BITS:
                return 'ERROR'
            fraction /= 2
        return ''.join(result)

def main():
    bits = Bits()
    result = bits.print_binary(0.625)
    print(result)


if __name__ == '__main__':
    main()

