file1 = open("sample_data1.txt", 'r')
file_content = file1.read()
file1.close()
print("File 1: \n", file_content)


#file 2
job_titles = ['Data Architect', 'Senior Business Analyst', 'Data Scientist', 'Machine Learning Engineer']

# initializing dictionaries to store the sum and count of salaries for each job title
salary_sums = {title: 0 for title in job_titles}
salary_counts = {title: 0 for title in job_titles}

# reading data from the CSV file
with open('job_data.csv', 'r') as file:
    lines = file.readlines()
    header = lines[0].strip().split(',')
    job_title_index = header.index('job_title')
    num_of_salaries_index = header.index('num_of_salaries')
    
    # iterating through data and updating the dictionaries
    for line in lines[1:]:
        values = line.strip().split(',')
        job_title = values[job_title_index]
        num_of_salaries = int(values[num_of_salaries_index])
        
        if job_title in job_titles:
            salary_sums[job_title] += num_of_salaries
            salary_counts[job_title] += 1

#  calculating the average salaries and then printing
print("\nFile2: ")
for job_title in job_titles:
    if salary_counts[job_title] > 0:
        average_salary = salary_sums[job_title] / salary_counts[job_title]
        print(f"Average salary for {job_title}: {average_salary:.2f}")
    else:
        print(f"No data found for {job_title}")
