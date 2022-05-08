import  re

def Renamer_TG(name):
    orgname = name.replace(".AlphaDL", "").replace("(","").replace(")","").replace(" ",".").replace("AD","",1).replace(".AM]","",).replace(".LT]","",)
    orgname = re.sub(r"(\.*\d{3,4}MB)","",orgname)
    orgname = re.sub(r"(\.*HQ)","",orgname)
    orgname = re.sub(r"\.*AAC\.*\d*\.*\d*","",orgname)
    orgname = orgname.replace("HEVC-", "").replace("H264-","").replace("x264-","").replace(".HEVC", "").replace(".H264","").replace(".x264","").replace("[","").replace(".MX]","").replace(".in","").replace(".ph","").replace(".li","").replace("HEVC", "").replace("H264","").replace("x264","").replace(".hevc","")
    orgname = orgname.replace("webdl","WEB-DL").replace("web-dl","WEB-DL").replace("webrip","WEBRip").replace("web","WEB").replace("bluray","BluRay").replace("hdtv","HDTV")
    orgname = orgname.replace("rmteam","RMT").replace("RMTeam","RMT")

    if re.findall(r"(\..{3,4})$", orgname):
        regex = re.search(r"(\..{3,4})$", orgname)
        orgname = orgname.replace(regex.group(1),".AlphaDL%s"%regex.group(1))

    if re.findall(r"[Ss]\d{1,2}.?[Ee]\d{1,2}",orgname):
        orgname = orgname.replace((re.search(r"([Ss]\d{1,2}.?[Ee]\d{1,2})", orgname)).group(1), (re.search(r"([Ss]\d{1,2}.?[Ee]\d{1,2})", orgname)).group(1).upper())

    if re.findall(r"[Ss]\d{1,2}.?[Ee]\d{1,2}(.*)\.\d{3,4}p", orgname):
        regex = re.search(r"[Ss]\d{1,2}.?[Ee]\d{1,2}(.*)\.\d{3,4}p", orgname)
        orgname = orgname.replace(regex.group(1),".Dual") if "dual"in regex.group(1).lower() else orgname.replace(regex.group(1),"")

    if re.findall(r"[Ss]\d{1,2}.?[Ee]\d{1,2}.*\.\d{3,4}p",orgname):
        orgname = orgname.replace((re.search(r"(.*)\.[Ss]\d{1,2}.?[Ee]\d{1,2}",orgname)).group(1), (re.search(r"(.*)\.[Ss]\d{1,2}.?[Ee]\d{1,2}",orgname)).group(1).title())
        if len(orgname) > 64:
            parts = (re.search(r"(.*)\.[Ss]\d{1,2}.?[Ee]\d{1,2}",orgname)).group(1).split(".")
            parts.reverse()
            for part in parts:
                if not re.findall(r"\d{4}",part):
                    if len(orgname) > 64:
                        orgname = orgname.replace(part, part[0].upper())

    if not re.findall(r"[Ss]\d{1,2}.?[Ee]\d{1,2}",orgname):
        if re.findall(r"\.\d{3,4}p",orgname):
            orgname = orgname.replace((re.search(r"(.*)\.\d{3,4}p",orgname)).group(1), (re.search(r"(.*)\.\d{3,4}p",orgname)).group(1).title())
            if len(orgname) > 64:
                parts = (re.search(r"(.*)\.\d{3,4}p",orgname)).group(1).split(".")
                parts.reverse()
                for part in parts:
                    if not re.findall(r"\d{4}",part):
                        if len(orgname) > 64:
                            orgname = orgname.replace(part, part[0].upper())
    
    if len(orgname) > 64:
        orgname = orgname.replace("AlphaDL", "AD")

    orgname = orgname.replace("..",".").replace(".-","-").replace("-.","-")

    return orgname





def Renamer_GD(name):
    orgname = name.replace(".AlphaDL", "").replace("AD","",1).replace("[","").replace(".MX]","").replace(".in","").replace(".ph","").replace(".li","").replace("(","").replace(")","").replace(" ",".").replace(".AM]","",).replace(".LT]","",).replace("hevc","HEVC")
    orgname = re.sub(r"(\.*\d{3,4}MB)","",orgname)
    orgname = orgname.replace("webdl","WEB-DL").replace("web-dl","WEB-DL").replace("webrip","WEBRip").replace("web","WEB").replace("bluray","BluRay").replace("hdtv","HDTV")

    if re.findall("(\..{3,4})$", orgname):
        regex = re.search("(\..{3,4})$", orgname)
        orgname = orgname.replace(regex.group(1),".AlphaDL%s"%regex.group(1))

    if re.findall(r"[Ss]\d{1,2}.?[Ee]\d{1,2}",orgname):
        orgname = orgname.replace((re.search(r"([Ss]\d{1,2}.?[Ee]\d{1,2})", orgname)).group(1), (re.search(r"([Ss]\d{1,2}.?[Ee]\d{1,2})", orgname)).group(1).upper())

    if re.findall(r"[Ss]\d{1,2}.?[Ee]\d{1,2}(.*)\.\d{3,4}p", orgname):
        regex = re.search(r"[Ss]\d{1,2}.?[Ee]\d{1,2}(.*)\.\d{3,4}p", orgname)
        orgname = orgname.replace(regex.group(1),".Dual") if "dual"in regex.group(1).lower() else orgname.replace(regex.group(1),"")

    if re.findall(r"[Ss]\d{1,2}.?[Ee]\d{1,2}.*\.\d{3,4}p",orgname):
        orgname = orgname.replace((re.search(r"(.*)\.[Ss]\d{1,2}.?[Ee]\d{1,2}",orgname)).group(1), (re.search(r"(.*)\.[Ss]\d{1,2}.?[Ee]\d{1,2}",orgname)).group(1).title())

    if not re.findall(r"[Ss]\d{1,2}.?[Ee]\d{1,2}",orgname):
        if re.findall(r"\.\d{3,4}p",orgname):
            orgname = orgname.replace((re.search(r"(.*)\.\d{3,4}p",orgname)).group(1), (re.search(r"(.*)\.\d{3,4}p",orgname)).group(1).title())
    
    return orgname
