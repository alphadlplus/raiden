import  re

def Renamer_TG(name):
    orgname = name.replace("HEVC", "").replace("H264","").replace("x264","").replace("[","").replace("MX]","").replace(".in","").replace(".ph","").replace(".li","")
    regex = re.search(r"(\..{3,4})$", orgname)
    orgname = orgname.replace(regex.group(1),".AlphaDL%s"%regex.group(1))
    regex = re.search(r"[Ss]\d{1,2}.?[Ee]\d{1,2}(.+)\.\d{3,4}p", orgname)
    orgname = orgname.replace(regex.group(1),"")
    return orgname

def Renamer_GD(name):
    orgname = name
    regex = re.search("(\..{3,4})$", orgname)
    orgname = orgname.replace(regex.group(1),".AlphaDL%s"%regex.group(1))
    return orgname
