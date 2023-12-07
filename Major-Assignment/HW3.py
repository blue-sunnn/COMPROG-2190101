# MOVIE_DICTIONARY (*** DO NOT DELETE this line or add line before this ***)
# Only add your code in the provided area.
# DO NOT delete or modified the given code in main().

# Function 1
def load_data_to_movie_dict(file_name):
    import json
    # use json.loads to turn string into dictionary
    # return the movies info in dictionary form
    mov = {}
    f = open(file_name, 'r')
    for line in f:
        i = json.loads(line)
        mov[i['_id']['$oid']] = { 'title': i['title'], 'year': int(i['year']['$numberInt']) }
        if 'genres' in i.keys(): mov[i['_id']['$oid']]['genres'] = i['genres']
        if 'tomatoes' in i.keys() and 'viewer' in i['tomatoes'] and 'meter' in i['tomatoes']['viewer']:
            mov[i['_id']['$oid']]['rating'] = int(i['tomatoes']['viewer']['meter']['$numberInt'])
    f.close()
    return mov

# Function 2
def yearly_summary_by_genre(year, movies):
    # return the dictionary of genre as the key and summary of length and min max rating as the value
    ysbg = {}
    for info in movies.values():
        if info['year'] == year and 'genres' in info:
            for genre in info['genres']:
                if genre not in ysbg.keys():
                    ysbg[genre] = { 'num': 1 }
                else:
                    ysbg[genre]['num'] += 1

                if 'rating' in info:
                    if 'rating' not in ysbg[genre]:
                        ysbg[genre]['rating'] = {
                            'avg': info['rating'],
                            'min': info['rating'],
                            'max': info['rating']}
                    else:
                        ysbg[genre]['rating']['avg'] += info['rating']
                        if info['rating'] < ysbg[genre]['rating']['min']:
                            ysbg[genre]['rating']['min'] = info['rating']
                        if info['rating'] > ysbg[genre]['rating']['max']:
                            ysbg[genre]['rating']['max'] = info['rating']

    for genre in ysbg: ysbg[genre]['rating']['avg'] = int(round(ysbg[genre]['rating']['avg'] / ysbg[genre]['num']))
    return ysbg

def search_g(sgenre, movies):
    mov_ids = []
    for ids, info in movies.items():
        if 'genres' in info:
            for i in info['genres']:
                if i.lower() == sgenre: mov_ids.append(ids)
    return mov_ids

def search_r(srating, movies):
    mov_ids = [ids for ids, info in movies.items() if 'rating' in info and info['rating'] == srating]
    return mov_ids

def search_y(syear, movies):
    mov_ids = [ids for ids, info in movies.items() if info['year'] == syear]
    return mov_ids

# Function 3
def search_movie_keys(query, movies):
    # return a list of ids
    sgenre, srating, syear = '', 0, 0
    mov_ids = []

    for k in query:
        if k == 'genres': sgenre = query['genres'].lower()
        elif k == 'rating': srating = query['rating']
        elif k == 'year': syear = query['year']
        else: return []

    if sgenre != '': g = set(search_g(sgenre, movies))
    if srating != 0: r = set(search_r(srating, movies))
    if syear != 0: y = set(search_y(syear, movies))

    if sgenre != '' and srating != 0 and syear != 0: mov_ids = list(r.intersection(y, g))
    elif sgenre == '' and srating == 0 and syear != 0: mov_ids = list(y)
    elif sgenre == '' and srating != 0 and syear == 0: mov_ids = list(r)
    elif sgenre != '' and srating == 0 and syear == 0: mov_ids = list(g)
    elif sgenre != '' and srating != 0 and syear == 0: mov_ids = list(g.intersection(r))
    elif sgenre != '' and srating == 0 and syear != 0: mov_ids = list(g.intersection(y))
    elif sgenre == '' and srating != 0 and syear != 0: mov_ids = list(r.intersection(y))

    temp = sorted([[movies[i]['title'], movies[i]['year']] for i in mov_ids])
    mov_ids = [ids for ii in temp for ids, info in movies.items() if info['title'] == ii[0]]
    return mov_ids

def word_deconstruct(query):
    deconstructed_words = [[query]]
    words = query.split()
    word_count = len(words)

    for _ in range(1, len(words) - 1):
        temp = []
        for end in range(len(words), -1, -1):
            for start in range(len(words), -1, -1):
                if end - start == word_count - 1:
                    temp.append(' '.join(words[start:end]))
        word_count -= 1
        deconstructed_words.append(temp)

    deconstructed_words.append(list(set(words)))
    return deconstructed_words

# Function 4
def search_movie_title(query, movies):
    # return a list of ids
    query = query.lower()
    temp, mov_ids, detected = [], [], []

    if len(query.split()) == 1:
        for ids, info in movies.items():
            c = len(set(query.split()).intersection(set([info['title'].lower().split()])))
            if c > 0: temp.append([-c, len(info['title'].split()), info['title'], info['year'], ids])

        mov_ids = [ii[4] for ii in sorted(temp)]

    else:
        for ii in word_deconstruct(query):
            for info in movies.values():
                for jj in word_deconstruct(info['title'].lower()):
                    if len(set(ii).intersection(set(jj))) > 0:
                        detected = ii
                        break
                if detected: break
            if detected: break

        if detected == []: return []

        for ids, info in movies.items():
            for words in word_deconstruct(info['title'].lower()):
                c = len(set(detected).intersection(set(words)))
                if c > 0: temp.append((ids, -c))

        temp1 = [[c, len(movies[ids]['title'].split()), movies[ids]['title'], movies[ids]['year'], ids] for ids, c in list(set(temp))]
        mov_ids = [ii[4] for ii in sorted(temp1)]

    return mov_ids

#------------------------------------------------------------#
# DO NOT DELETE OR MODIFIED THE CODE BELOW
#------------------------------------------------------------#

# This function will help you print out the movies' details from list of movie ids
def show_movie_info(ids, movies):
  for n,i in enumerate(ids):
    if 'title' in movies[i]:
      print('Title: {}'.format(movies[i]['title']))
    if 'year' in movies[i]:
      print('Year: {}'.format(movies[i]['year']))
    if 'genres' in movies[i]:
      print('Genres: {}'.format(', '.join(movies[i]['genres'])))
    if 'rating' in movies[i]:
      print('Rating: {}'.format(movies[i]['rating']))
    if n < len(ids) - 1:
      print('=============================================')

#------------------------------------------------------------#
# *** MAIN PART ****
movies = load_data_to_movie_dict('movies_2010_2013.json')