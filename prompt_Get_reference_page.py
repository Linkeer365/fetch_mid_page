import os

ab_rf_path=r"D:\AllDowns\newbooks\page_mid_pic\pages_ab_rf.txt"
new_ab_rf_path=r"D:\AllDowns\newbooks\page_mid_pic\finished_pages_ab_rf.txt"

lines=[]
with open(ab_rf_path,"r",encoding="utf-8") as f:
    lines=f.readlines()

for each_idx,each_line in enumerate(lines):
    rf_zone,ab_zone,filename_zone=each_line.split("\t"*3)
    ab_num=int(ab_zone.split(":")[1])
    prompt=f"{filename_zone}\n{rf_zone}\t"
    rf_input=input(prompt)
    while True:
        if rf_input.isdigit():
            rf_zone+=rf_input
            delta_num=ab_num-int(rf_input)
            delta_zone=f"DT_Page:{delta_num}"
            new_line=f"{delta_zone}\t\t\t{rf_zone}\t\t\t{ab_zone}\t\t\t{filename_zone}"
            lines[each_idx]=new_line
            break

lines_s="".join(lines)
with open(ab_rf_path,"w",encoding="utf-8") as f:
    f.write(lines_s)

os.rename(ab_rf_path,new_ab_rf_path)
print("done.")


