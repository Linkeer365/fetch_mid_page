import PyPDF2
import os
import io
from PIL import Image

# 必须要和PyMupdf一起安装才能用...

import fitz

target_dir=r"D:\AllDowns\newbooks"
target_dir2=r"D:\AllDowns\newbooks\page_mid"
target_dir3=r"D:\AllDowns\newbooks\page_mid_pic"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

if not os.path.exists(target_dir2):
    os.makedirs(target_dir2)

if not os.path.exists(target_dir3):
    os.makedirs(target_dir3)

pages=[]
names=[]
for each in os.listdir(target_dir):
    if each.endswith(".pdf"):
        pdf_fd=open(f"{target_dir}{os.sep}{each}","rb")
        pdf_rd = PyPDF2.PdfFileReader(pdf_fd)
        pdf_len=pdf_rd.getNumPages()
        # 简单地把它的中间几页抽出来，我们就能知道具体是第几页了
        # 注意下面的pick_page_idx要加2，原因不用我多说了...
        pick_page_idx=pdf_len//2
        page=pdf_rd.getPage(pick_page_idx)
        pdf_wt=PyPDF2.PdfFileWriter()
        pdf_wt.addPage(page)

        # 别问我原理，这个只能抄别人的才有活路的样子...
        # https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python/34116472#34116472

        # 保存成pdf文件
        with open(f"{target_dir2}{os.sep}page{pick_page_idx+1}_{each}","wb") as pdf_stream:
            pdf_wt.write(pdf_stream)
        pdf_fd.close()

        # 从pdf文件中下载png
        doc = fitz.open(f"{target_dir2}{os.sep}page{pick_page_idx+1}_{each}")
        for i in range(len(doc)):
            for img in doc.getPageImageList(i):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)

                # pix.writePNG(f"{target_dir3}{os.sep}page{pick_page_idx + 1}_{each.strip('.pdf')}.png")

                if pix.n < 5:  # this is GRAY or RGB
                    pix.writePNG(f"{target_dir3}{os.sep}page{pick_page_idx+1}_{each.strip('.pdf')}.png")
                else:  # CMYK: convert to RGB first
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.writePNG(f"{target_dir3}{os.sep}page{pick_page_idx+1}_{each.strip('.pdf')}.png")
                    pix1 = None
                pix = None
        print("one done.")

print("all done.")


