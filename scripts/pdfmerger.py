'''
 This script must be in the same ddirectory where your Syllabus folder: folder contains the pdfs
'''
# importing os module
import os

# folder where the pdfs are
path = 'Syllabus' 

# get the list of the files in the directory
pdfs = os.listdir(path)

lst = [os.path.join(path,i) for i in pdfs]
time_sorted_list = sorted(lst, key=os.path.getmtime)

for file in time_sorted_list:
    print(file)

# merging the pdfs
import fitz

result = fitz.open()

for pdf in time_sorted_list:
    with fitz.open(pdf) as mfile:
        result.insertPDF(mfile)
    
result.save("result.pdf")
print("Merged {} pdfs".format(len(time_sorted_list)))
