class Solution:

    def validIPAddress(self, IP: str) -> str:
        if validate_ipv4(IP):
            return 'IPv4'
        if validate_ipv6(IP):
            return 'IPv6'
        return 'Neither'


def validate_ipv4(IP: str) -> bool:
    if '.' not in IP:
        return False
    segments = IP.split('.')
    if len(segments) != 4:
        return False
    for segment in segments:
        try:
            if segment.startswith('-'):
                return False
            i = int(segment)
            if i < 0 or i > 255:
                return False
            if segment.startswith('0') and (i > 0 or len(segment) > 1):
                return False
        except ValueError:
            return False
    return True


def validate_ipv6(IP: str) -> bool:
    IP = IP.lower()
    if ':' not in IP:
        return False
    segments = IP.split(':')
    if len(segments) != 8:
        return False
    for segment in segments:
        try:
            if segment.startswith('-') or len(segment) > 4:
                return False
            i = int(segment, 16)
            if i < 0 or i > 0xFFFF:
                return False
        except ValueError:
            return False
    return True



def test_one(IP: str, expected: str):
    print(IP)
    actual = Solution().validIPAddress(IP)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one('172.16.254.1', 'IPv4')
    test_one('2001:0db8:85a3:0:0:8A2E:0370:7334', 'IPv6')
    test_one('2001:0db8:85a3:0000:0000:8a2e:0370:7334', 'IPv6')
    test_one('2001:0db8:85a3::8A2E:0370:7334', 'Neither')
    test_one('02001:0db8:85a3:0000:0000:8a2e:0370:7334', 'Neither')
    test_one('02001:0db8:85a3:0000:00000:8a2e:0370:7334', 'Neither')
    test_one('02001:0db8:85a3:0000:0000:zizi:0370:7334', 'Neither')
    test_one('haha.256.256.256', 'Neither')
    test_one('256.256.256.256', 'Neither')
    test_one('172.16.254.01', 'Neither')
    test_one('00.0.0.0', 'Neither')
    test_one('0.0.0.-0', 'Neither')


if __name__ == '__main__':
    test()
