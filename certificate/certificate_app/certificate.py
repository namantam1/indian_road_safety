from PIL import Image,ImageDraw,ImageFont
from datetime import datetime

def generate_certificate(filespath,name,interntype,profile,startdate,enddate,logoname,registration,savepath,**kwargs):
    """
    Function to generate a certificate take parameters path to file,name of intern, type of work, profile,
    start date, end date, logoname to be used, registration number, path where file to be saved.
    """
    # print(filespath,name,type,profile,startdate,enddate,logoname,registration,savepath)
    imagepath = f"{filespath}/certificate.jpg"
    logopath = f"{filespath}/{logoname}.png"
    signpath = f"{filespath}/signature.png"

    # # Size of certificate to be generated
    cktsize = (1600,1200)
    logosize=(165,165)
    signsize=(224,78)

    # # font size
    namesize = 48 #px
    typesize = 26
    profilesize = 26
    datesize = 22

    # # content coordinates
    namecdt = (468,550)
    typecdt = (650,655-typesize)
    profilecdt = (450,760-profilesize)
    d1cdt = (662,706-datesize)
    d2cdt = (895,706-datesize)
    datecdt = (188,986-datesize)
    renocdt = (1133,130-datesize)
    logocdt = (718,920)
    signcdt = (1180,939)

    # # font faimily to be used 
    namefamily = f"{filespath}/fonts/Kalam-Regular.ttf"
    otherfamily = "segoe print"
    # defaultfamily = "arial.ttf"
    defaultfamily = f"{filespath}/fonts/Viga-Regular.ttf"

    text_color = (0,0,0)

    name = str(name)
    interntype = str(interntype)
    profile = str(profile)
    d1 = startdate.strftime('%m-%d-%Y')
    d2 = enddate.strftime('%m-%d-%Y')
    date = datetime.now().strftime('%m-%d-%Y')
    registration_no = str(registration)
    # # cerficate_no = 'certificate No. - c57f9298-d2c2-4b1a-a456-fd1b90668072'
    # # url = 'url - https://exmaple.com/certificate/c57f9298-d2c2-4b1a-a456-fd1b90668072'

    # print(imagepath,logopath,signpath,name,interntype,d1,d2,date,namefamily,savepath)
    # # opening images and making them proper
    cktim = Image.open(imagepath,'r').resize(cktsize).convert("RGBA")
    logoim = Image.open(logopath,'r').resize(logosize).convert("RGBA")
    signim = Image.open(signpath,'r').resize(signsize).convert("RGBA")

    # make the image drawable
    d = ImageDraw.Draw(cktim)

    namefont = ImageFont.truetype(namefamily,namesize)
    typefont = ImageFont.truetype(defaultfamily,typesize)
    profilefont = ImageFont.truetype(defaultfamily,profilesize)
    datefont = ImageFont.truetype(defaultfamily,datesize)
    refont = ImageFont.truetype(defaultfamily,datesize)

    d.text(namecdt,name,fill=text_color,font=namefont)
    d.text(typecdt,interntype,fill=text_color,font=typefont)
    d.text(profilecdt,profile,fill=text_color,font=profilefont)
    d.text(d1cdt,d1,fill=text_color,font=datefont)
    d.text(d2cdt,d2,fill=text_color,font=datefont)
    d.text(datecdt,date,fill=text_color,font=datefont)
    d.text(renocdt,registration_no,fill=text_color,font=datefont)

    transparent = Image.new('RGBA', cktsize, (0,0,0,0))
    transparent.paste(cktim,(0,0))
    transparent.paste(logoim,logocdt,logoim)
    transparent.paste(signim,signcdt,signim)

    # # print(cktim.size)
    # # print(logoim.size)
    # # print(signim.size)

    # transparent = Image.new("RGBA", cktsize)
    # transparent = Image.alpha_composite(transparent,cktim)
    # transparent = Image.alpha_composite(transparent, logoim)

    # registration_no = registration_no.split('/')[1]
    # saving as png
    png = f'{savepath}/tmp/certificate_{registration_no}.png'
    transparent.save(png)

    # converting to RGB mode to save as pdf
    transparent = transparent.convert("RGB")
    pdf = f'{savepath}/tmp/certificate_{registration_no}.pdf'
    transparent.save(pdf)
    return [png,pdf]