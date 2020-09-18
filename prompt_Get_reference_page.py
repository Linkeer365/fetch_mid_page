import os

ab_rf_path=r"D:\AllDowns\newbooks\page_mid_pic\pages_ab_rf.txt"
new_ab_rf_path=r"D:\AllDowns\newbooks\page_mid_pic\finished_pages_ab_rf.txt"

lines=[]
with open(ab_rf_path,"r",encoding="utf-8") as f:
    lines=f.readlines()

for each_idx,each_line in enumerate(lines):
    rf_zone,ab_zone,filename_zone=each_line.split("\t"*3)
    prompt=f"{filename_zone}\n{rf_zone}\t"
    rf_input=input(prompt)
    while True:
        if rf_input.isdigit():
            rf_zone+=rf_input
            new_line=f"{rf_zone}\t\t\t{ab_zone}\t\t\t{filename_zone}"
            lines[each_idx]=new_line
            break

lines_s="".join(lines)
with open(ab_rf_path,"w",encoding="utf-8") as f:
    f.write(lines_s)

os.rename(ab_rf_path,new_ab_rf_path)
print("done.")


