import sys
script, encoding, error =sys.argv
def main (language_file,encoding,errors):
    line = language_file.readline()
    if line :
        print_line(line,encoding,errors)
        # call main again inside main. jump back to the top and run again.
        # if will make this looping forever.
        return main(language_file,encoding,errors)

def print_line(line,encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors=errors)
    cooked_string = raw_bytes.decode(encoding,errors=errors)
    print(raw_bytes,"<====>",cooked_string)

languages = open("languages.txt",encoding ='UTF-8')
main(languages,encoding,error)