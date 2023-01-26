import dns.resolver


def mx_check(num, address):
    if num != 10:
        address = input('Enter domain: ')
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = ['8.8.8.8', '1.1.1.1']
    try:
        answers = my_resolver.resolve(address, 'MX')
    except dns.resolver.NXDOMAIN:
        print("No such domain %s" % address)
    except dns.resolver.Timeout:
        print("Timed out while resolving %s" % address)
    except dns.exception.DNSException:
        print("Unhandled exception")
    else:
        for rdata in answers:
            print('MX Record:', rdata.exchange)
