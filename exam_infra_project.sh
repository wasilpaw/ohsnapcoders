echo "*** Exam Infra startup script ***"
sudo apt-get update
mkdir exam_results
echo "Student_Name,Date,Course,Result" > exam_results/SchoolNameResults20231021.csv
echo "Nicola Tesla,2023-10-21,Science,62," >> exam_results/SchoolNameResults20231021.csv
