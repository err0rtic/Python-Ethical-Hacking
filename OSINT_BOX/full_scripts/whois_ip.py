import whois


def who(num, add):
    if num != 10:
        add = input('Enter domain: ')
    try:
        domain = whois.query(add)
        res = domain.__dict__
    except ZeroDivisionError as e:
        print('Input Error: ', e)
    except ValueError as e:
        print('Input Error: ', e)
    except SyntaxError as e:
        print('Input Error: ', e)
    except:
        print('Domain is not active')
    else:
        for i in res:
            print(i, res[i], sep=': ')


