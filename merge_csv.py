<<<<<<< HEAD
import os
import glob
import pandas as pd
os.chdir("./test4/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f,encoding='iso-8859-1') for f in all_filenames],sort=False)
# export to csv
#combined_csv = combined_csv[['STATION CODE','LOCATIONS','STATE']]
combined_csv = combined_csv[['STATION CODE','LOCATIONS','STATE','TEMPERATURE ºC  : Min','TEMPERATURE ºC  : Max','TEMPERATURE ºC  : Mean','D.O. (mg/l)  : Min  : > 4 mg/l','D.O. (mg/l)  : Max  : > 4 mg/l','D.O. (mg/l)  : Mean  : > 4 mg/l','pH  : Min  : 6.5-8.5','pH  : Max  : 6.5-8.5','pH  : Mean  : 6.5-8.5','CONDUCTIVITY (µmhos/cm)  : Min','CONDUCTIVITY (µmhos/cm)  : Max','CONDUCTIVITY (µmhos/cm)  : Mean','B.O.D. (mg/l)  : Min  : < 3 mg/l','B.O.D. (mg/l)  : Max  : < 3 mg/l','B.O.D. (mg/l)  : Mean  : < 3 mg/l','NITRATE- N+ NITRITE-N (mg/l)  : Min','NITRATE- N+ NITRITE-N (mg/l)  : Max','NITRATE- N+ NITRITE-N (mg/l)  : Mean','FECAL COLIFORM (MPN/100ml)  : Min  : < 2500 MPN/100ml','FECAL COLIFORM (MPN/100ml)  : Max  : < 2500 MPN/100ml','FECAL COLIFORM (MPN/100ml)  : Mean  : < 2500 MPN/100ml','TOTAL COLIFORM (MPN/100ml)  : Min  : < 5000 MPN/100ml','TOTAL COLIFORM (MPN/100ml)  : Max  : < 5000 MPN/100ml','TOTAL COLIFORM (MPN/100ml)  : Mean  : < 5000 MPN/100ml']]
=======
import os
import glob
import pandas as pd
os.chdir("./test4/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f,encoding='iso-8859-1') for f in all_filenames],sort=False)
# export to csv
#combined_csv = combined_csv[['STATION CODE','LOCATIONS','STATE']]
combined_csv = combined_csv[['STATION CODE','LOCATIONS','STATE','TEMPERATURE ºC  : Min','TEMPERATURE ºC  : Max','TEMPERATURE ºC  : Mean','D.O. (mg/l)  : Min  : > 4 mg/l','D.O. (mg/l)  : Max  : > 4 mg/l','D.O. (mg/l)  : Mean  : > 4 mg/l','pH  : Min  : 6.5-8.5','pH  : Max  : 6.5-8.5','pH  : Mean  : 6.5-8.5','CONDUCTIVITY (µmhos/cm)  : Min','CONDUCTIVITY (µmhos/cm)  : Max','CONDUCTIVITY (µmhos/cm)  : Mean','B.O.D. (mg/l)  : Min  : < 3 mg/l','B.O.D. (mg/l)  : Max  : < 3 mg/l','B.O.D. (mg/l)  : Mean  : < 3 mg/l','NITRATE- N+ NITRITE-N (mg/l)  : Min','NITRATE- N+ NITRITE-N (mg/l)  : Max','NITRATE- N+ NITRITE-N (mg/l)  : Mean','FECAL COLIFORM (MPN/100ml)  : Min  : < 2500 MPN/100ml','FECAL COLIFORM (MPN/100ml)  : Max  : < 2500 MPN/100ml','FECAL COLIFORM (MPN/100ml)  : Mean  : < 2500 MPN/100ml','TOTAL COLIFORM (MPN/100ml)  : Min  : < 5000 MPN/100ml','TOTAL COLIFORM (MPN/100ml)  : Max  : < 5000 MPN/100ml','TOTAL COLIFORM (MPN/100ml)  : Mean  : < 5000 MPN/100ml']]
>>>>>>> 0599a3dc0e041321b9ebb50f4e7fd223146eb358
combined_csv.to_csv("combined_csv_final.csv", index=False, encoding='iso-8859-1')