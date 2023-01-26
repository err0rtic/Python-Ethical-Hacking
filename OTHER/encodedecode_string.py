import codecs
import base64
import urllib.parse
import binascii


def encode(text):
    encode_str = '\\'.join(hex(ord(c))[1:] for c in text)
    print('HEX:', '\\' + encode_str)
    encode_str = base64.b64encode(text.encode("UTF-8"))
    print('BASE64:', encode_str.decode("UTF-8"))
    encode_str = base64.b32encode(text.encode("UTF-8"))
    print('BASE32:', encode_str.decode("UTF-8"))
    encode_str = base64.b16encode(text.encode("UTF-8"))
    print('BASE16:', encode_str.decode("UTF-8"))
    encode_str = urllib.parse.quote(text)
    print('URLENCODE:', encode_str)
    encode_str = codecs.encode(text, 'rot_13')
    print('ROT-13:', encode_str)

def hex_decode(text):
    decode_str = text.replace('\\x', '')
    decode_str = codecs.decode(decode_str, 'hex')
    return decode_str


def rot_13_decode(text):
    return codecs.encode(text, 'rot_13')


def decode(text, type_encode):
    decode_dict = {'URLENCODE':urllib.parse.unquote, 'HEX': hex_decode, 'BASE64': base64.b64decode, 'BASE32': base64.b32decode, 'BASE16': base64.b16decode, 'ROT-13':rot_13_decode}
    if type_encode == 'URL' or type_encode == 'ROT-13':
        print(f'{type_encode}:', decode_dict[type_encode](text))
    elif type_encode == 'BASE64' or type_encode == 'BASE32' or type_encode == 'BASE16' or type_encode == 'HEX':
        print(f'{type_encode}:', decode_dict[type_encode](text).decode('utf-8'))
    else:
        print('Error, unsupported format specified')


if __name__ == "__main__":
    print('1 - encode\n2 - decode\n')
    try:
        action = int(input('Selected action: '))
    except ValueError:
        print("Error, you did not enter a number\n")
    finally:
        text = input('Enter text: ')
        if action == 1:
            encode(text)
        if action == 2:
            print('Selected the original format for decoding: HEX, URLENCODE, BASE64, BASE32, BASE16, ROT-13')
            type_encode = input('Enter format: ')
            try:
                decode(text, type_encode)
            except binascii.Error:
                print("Error, wrong text format entered")
