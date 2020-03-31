import os

def Dirprocess(pic_root= './斗罗大陆/'):
    dirlist = os.listdir(pic_root)
    i = 0
    for each in dirlist:
        if(i>=8):
            print("正在处理",each)
            jpg2pdf(pic_root + each)
        i += 1

def CompressImage(dir_name, image_name):
    # print(image_name)
    new_name = image_name
    
    os.system("magick convert -resize \"600x800\" %s %s" % (dir_name+'/'+image_name, dir_name+'/'+new_name.rjust(7,'0')))

def CompressAll(dir_name):
    ext_names = ['.jpg']
    for each_image in os.listdir(dir_name):
        for ext_name in ext_names:
            if each_image.endswith(ext_name):
                CompressImage(dir_name, each_image)
                # print(dir_name + '/' + each_image)
                os.system("rm %s"% (dir_name + '/' + each_image))
                break

def jpg2pdf(dir_name= './第1话_唐三穿越'):
    CompressAll(dir_name)
    os.system("magick convert %s/*.jpg %s.pdf"% (dir_name, './pdf/'+dir_name.split('/')[-1]))

Dirprocess()

# jpg2pdf()