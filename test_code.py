#file = input(sample_data1.txt)
file1 = open("sample_data1.txt", 'r')
file_content = file1.read()
file1.close()
print(file_content)

