import zipfile as z
# import pandas as pd

# help(zipfile)

# zip_package = 'ml-10m.zip'
zip_package = 'ml-1m.zip'
mov_in_zip = zip_package.strip('.zip') + '/movies.dat'
rat_in_zip = zip_package.strip('.zip') + '/ratings.dat'

# созания переменной file со всеми данным за день. NB: формат bytes\n",
with z.ZipFile(zip_package, 'r') as data_in:
    data_in.printdir()
    print(data_in.namelist())

    with data_in.open(mov_in_zip, 'r', encoding='utf-8') as m:
#         movies_list = m.readlines()
        # movies_list = ''.join([line_.replace("::", ";") for line_ in m.readlines()])
        # movies_list = [line_.replace(b'::', b';') for line_ in m.readlines()]
        movies_list = [line_.replace('::', ';') for line_ in m.readlines()]
        # [print(line_) for line_ in m.readlines()]
        
    # with data_in.open(rat_in_zip, 'r') as r:
#         ratings_list = r.readlines()
        # ratings_list = ''.join([line_.replace("::", ";") for line_ in r.readlines()])
        
print(len(movies_list))
# print(len(ratings_list))


#%%

import zipfile as z
import pandas as pd
import chardet

zip_package = 'ml-1m.zip'
mov_in_zip = zip_package.strip('.zip') + '/movies.dat'
rat_in_zip = zip_package.strip('.zip') + '/ratings.dat'

# созания переменной file со всеми данным за день. NB: формат bytes\n",
with z.ZipFile(zip_package, 'r') as data_in:
    # with open(data_in.open(mov_in_zip), 'rb') as rawdata:
        # result = chardet.detect(rawdata.read(100000))
    # print(result)
    
    # data_in.printdir()
    # print(data_in.namelist())
    dfm = pd.read_csv(data_in.open(mov_in_zip, 'r'), 'ISO-8859-1', sep='::')
    
print(dfm)

