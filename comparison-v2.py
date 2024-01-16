# csv-diff 2024-01-10_-_Worker_and_Temporary_Worker.csv 2024-01-11_-_Worker_and_Temporary_Worker.csv --key="Organisation Name"

import csv_diff

file1 = "2024-01-10_-_Worker_and_Temporary_Worker.csv"
file2 = "2024-01-11_-_Worker_and_Temporary_Worker.csv"

diff = csv_diff.diff_files(file1, file2, key="Organisation Name")
print(diff)