import dns.exception
from dns import reversename, resolver


def rev_dns(num, ip):
    if num != 10:
        ip = input('Enter ip: ')
    try:
        rev_name = reversename.from_address(ip)
        reversed_dns = str(resolver.resolve(rev_name, "PTR")[0])
    except dns.exception.SyntaxError as e:
        print(e)
    except dns.exception.DNSException as e:
        print(e)
    else:
        print(reversed_dns)


