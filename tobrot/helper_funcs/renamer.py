import  re

def Renamer_TG(name):
    orgname = name.replace(".AlphaDL", "").replace("(","").replace(")","").replace(" ",".").replace("AD","",1)
    orgname = orgname.replace("HEVC-", "").replace("H264-","").replace("x264-","").replace(".HEVC", "").replace(".H264","").replace(".x264","").replace("[","").replace(".MX]","").replace(".in","").replace(".ph","").replace(".li","").replace("HEVC", "").replace("H264","").replace("x264","")
    regex = re.search(r"(\..{3,4})$", orgname)
    orgname = orgname.replace(regex.group(1),".AlphaDL%s"%regex.group(1))
    regex = re.search(r"[Ss]\d{1,2}.?[Ee]\d{1,2}(.*)\.\d{3,4}p", orgname)
    if re.findall(r"[Ss]\d{1,2}.?[Ee]\d{1,2}(.*)\.\d{3,4}p", orgname):
        orgname = orgname.replace(regex.group(1),".Dual") if "dual"in regex.group(1).lower() else orgname.replace(regex.group(1),"")
    if len(orgname) > 64:
        orgname = orgname.replace("AlphaDL", "AD")
    return orgname

def Renamer_GD(name):
    orgname = name.replace(".AlphaDL", "").replace("AD","",1)
    regex = re.search("(\..{3,4})$", orgname)
    if re.findall("(\..{3,4})$", orgname):
        orgname = orgname.replace(regex.group(1),".AlphaDL%s"%regex.group(1))
    return orgname
