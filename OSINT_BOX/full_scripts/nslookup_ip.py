from nslookup import Nslookup


def ns_look(num, domain):
    if num != 10:
        domain = input('Enter host: ')
    dns_query = Nslookup(dns_servers=["1.1.1.1"])
    ips_record = dns_query.dns_lookup(domain)
    soa_record = dns_query.dns_lookup(domain)
    if ips_record.response_full == [] and soa_record.response_full == []:
        print('No information or incorrectly entered domain')
    else:
        for i in ips_record.response_full:
            print(i)
        for i in soa_record.response_full:
            print('\n'.join(i.split('. ')))

