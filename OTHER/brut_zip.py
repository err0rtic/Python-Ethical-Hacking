from tqdm import tqdm
import zipfile


path_file = '/home/root/secure.zip'
wordlist = []

def wordlist_open():
    dirs_file = '/home/root/wordlists/100psswd.txt'
    with open(dirs_file, "rb") as reader:
        for line in reader.readlines():
            wordlist.append(line)


def zip_brut():
    zip_file = zipfile.ZipFile(path_file)
    words = len(wordlist)
    print('Total passwords to test:', words)
    for word in tqdm(wordlist, total=words, unit=" word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            pass
        else:
            print("\nPassword found:" + '\033[32m', word.decode().strip())
            exit(0)
    print("\nPassword not found", '\033[91m' + "try other wordlist.")


if __name__ == '__main__':
    wordlist_open()
    zip_brut()