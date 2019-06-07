def split_file():
    counter = 0
    eng_lin = 3605
    lin_eng = 8681
    end = 12542

    with open('raw_text.txt', 'r') as data:
        for line in data:
            if counter >= eng_lin and counter < lin_eng:
                with open('eng_lin_dic.txt', 'a+') as o_file:
                    o_file.write(line)

            elif counter >= lin_eng and counter <= end:
                with open('lin_eng_dic.txt', 'a+') as o_file:
                    o_file.write(line)

            counter += 1

        o_file.close()

def clean():
    with open('eng_lin_dic.txt', 'r') as data:
        for line in data:
            if not line == '\n' and not line.strip().isdigit():
                with open('eng-lin.txt', 'a+') as f:
                    f.write(line.lower())

    f.close()

    with open('lin_eng_dic.txt', 'r') as data:
        for line in data:
            if not line == '\n' and not line.strip().isdigit():
                with open('lin-eng.txt', 'a+') as f:
                    f.write(line.lower())

    f.close()

def verbs_tagging():
    with open('unique_words.tagged.txt', 'r') as d:
        with open('verbs.tagged.txt', 'a+') as f:
            for line in d:
                if 'vblex' in line:
                    f.write(line)

def unique_words():
    alist = []
    with open('d.txt', 'r') as d:
        with open('unique_words.txt', 'w+') as f:
            for line in d:
              alist.append(line)

            alist = list(set(alist)) # removing duplicates
            alist.sort()

            for word in alist:
                f.write(word)

def verbs_final():
    c = 0
    t = 0
    with open('d_verbs.tagged.txt', 'r') as d:
        with open('lin_verbs.txt', 'w+') as f:
            with open('eng_lin_dic.txt', 'r') as o:
                verb_list = [v[1:v.find('/')] for v in d.readlines()] # eng nouns
                verb_list = list(set(verb_list)) # removing duplicates
                dic = [words.strip() for words in o.readlines()] # eng-lin dic
                for verb in verb_list:
                    for line in dic:
                        if verb in line:
                            lin_word = line.split(',')[1].strip()
                            out = lin_word + ":" + lin_word + " Verb-Suffix ; ! " + "\"To " + verb + "\"\n"
                            f.write(out)
                            c+=1
                            break

    print(c,'total words')


def verbs_final_dummy():
    c = 0
    with open('verbs.tagged.txt', 'r') as d:
        with open('lin_verbs.txt', 'w+') as f:
            with open('eng_lin_dic.txt', 'r') as o: # or dummy.txt for testing
                verb_list = [v[1:v.find('/')] for v in d.readlines()] # eng nouns
                verb_list = list(set(verb_list)) # removing duplicates
                dic = [words.strip() for words in o.readlines()] # eng-lin dic
                for verb in verb_list:
                    for line in dic:
                        if verb in line.split()[0]: # assuming that the first word from each entry is followed by a comma
                            for element in line.split():
                                element = element.replace(',', '').replace('.', '') # removing all comas and periods
                                if element not in [verb, 'vi', 'pl', 'n', 'vt', 'to', 'be', 'vt', 'v', ';', 'by', 'or', 'and', 'for', 'as', 'na', 'the', 'a'] and not element.startswith('(') and not element.endswith(')'):
                                    out = 'ko'+ element + ":" + element + " Verb-Suffix ; ! " + "\"To " + verb + "\"\n"
                                    f.write(out)
                                    #print(element, '->', verb)
                                    c+=1
                            break
    print(c, 'words added')

def verbs():
    with open('../lin_verbs_final.txt', 'r') as d:
        with open('restored_1.txt', 'r') as f:
            with open('verbs.txt', 'a+') as o:
                for line in d:
                    out = f.readline().strip()+ ' ' + ' '.join(line.split()[1:])+'\n'
                    o.write(out)

def dicritic_restoration():
    with open('restored.txt', 'r') as d:
        with open('restored_1.txt', 'a+') as f:
            for line in d:
                out = line.strip()+':'+line[2:len(line)-2]+'\n'
                f.write(out)

def nouns_1():
    c = 0
    mo_ba_class = []
    ba_class = []
    mo_mi_class = []
    li_ma_class = []
    e_bi_class = []
    lo_ma_class = []
    no_class = []

    with open('nouns_1.txt', 'r') as d:
        for line in d:
            line = line.split()

            i = 0
            while i < len(line):
                if 'pl' in line[i]:
                    # mo_ba
                    if line[i-1].startswith('mo') and line[i+1].startswith('ba'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        mo_ba_class.append(word)
                    #mo_mi
                    elif line[i-1].startswith('mo') and line[i+1].startswith('mi'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        mo_mi_class.append(word)
                    #li_ma
                    elif line[i-1].startswith('li') and line[i+1].startswith('ma'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        li_ma_class.append(word)
                    #e_bi
                    elif line[i-1].startswith('e') and line[i+1].startswith('bi'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        e_bi_class.append(word)
                    #lo_ma
                    elif line[i-1].startswith('lo') and line[i+1].startswith('ma'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        lo_ma_class.append(word)
                    #ba
                    elif line[i+1].startswith('ba'):
                        word = [line[i-1], line[i+1], line[0]]
                        #print(word)
                        ba_class.append(word)
                    else:
                        no_class.append(line)
                i += 1

    for word in li_ma_class:
        print(word)

def calculate_duplicates():
    with open('nouns_2.txt', 'r') as d:
        o_list = []
        for line in d:
            o_list.append(line.strip())
        print(len(o_list)-len(list(set(o_list))), 'duplicates')
        print(set([x for x in o_list if o_list.count(x) > 1]))

def nouns():
    with open('nouns_2.txt', 'r') as d:
        with open('nouns.txt', 'a+') as f :
            for word in d:
                out = word.strip() + ':' + word.strip().replace('mo', '') + ' III-IV5-Suffix ; ! ""' + '\n'
                f.write(out)
