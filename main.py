import pandas as pd
import requests
import json
from PIL import Image
counter = 0

missing_arr = []
path_names_set = []





file = open("people.json" , encoding="utf8")
data = json.load(file)
missing_data = data["data"]["table"]["rows"]
matching_photos = data["data"]["table"]["signedUserContentUrls"]


def getImage(url , counter):
    response = requests.get(url)
    if response.status_code:
        p = open(f'Images/Image{counter}.png', 'wb')
        p.write(response.content)
        p.close()
    return f'Images/Image{counter}.png'


for missing in missing_data:
    missing["cellValuesByColumnId"].setdefault("fldrT6C0v5EnP1cRV" , "none")
    missing["cellValuesByColumnId"].setdefault("fldgvhQGPkMBUWVLf" ,"none")
    missing["cellValuesByColumnId"].setdefault("fldcaFKPcs7pupkp9" , "none")
    missing["cellValuesByColumnId"].setdefault("fld33tJ7brN4d4ySl","none")
    missing["cellValuesByColumnId"].setdefault("fldKwNr89vZQ7MkOc","none")
    missing["cellValuesByColumnId"].setdefault("fldkSPhaML4WDhjx7","none")
    try:
        photos = missing["cellValuesByColumnId"]["flddsVBnWTKpIE36v"]
    except:
        pass
    try:
        for photo in photos:
                if photo["url"] in matching_photos:
                    if not matching_photos[photo["url"]] in path_names_set:
                        path_name = getImage(matching_photos[photo["url"]], counter)
                        path_names_set.append(matching_photos[photo["url"]])
                        counter += 1
                        missing_arr.append({
                                            "rowId" : missing["id"] ,
                                            "name": missing["cellValuesByColumnId"]["fldrT6C0v5EnP1cRV"],
                                            "additonal_info": missing["cellValuesByColumnId"]["fldgvhQGPkMBUWVLf"] ,
                                            "last_contact_made" : missing["cellValuesByColumnId"]["fldcaFKPcs7pupkp9"] ,
                                            "last_location" : missing["cellValuesByColumnId"]["fld33tJ7brN4d4ySl"] ,
                                            "image_path": path_name ,
                                            "phone_number" :  missing["cellValuesByColumnId"]["fldKwNr89vZQ7MkOc"] ,
                                            "email" : missing["cellValuesByColumnId"]["fldkSPhaML4WDhjx7"]})
                        continue
                    else:
                        continue
                if photo["fullThumbUrl"] in matching_photos:
                    if not matching_photos[photo["fullThumbUrl"]] in path_names_set:
                        path_name = getImage(matching_photos[photo["fullThumbUrl"]], counter)
                        path_names_set.append(matching_photos[photo["fullThumbUrl"]])
                        counter += 1
                        missing_arr.append({"rowId" : missing["id"] ,
                                            "name": missing["cellValuesByColumnId"]["fldrT6C0v5EnP1cRV"],
                                            "additonal_info": missing["cellValuesByColumnId"]["fldgvhQGPkMBUWVLf"] ,
                                            "last_contact_made" : missing["cellValuesByColumnId"]["fldcaFKPcs7pupkp9"] ,
                                            "last_location" : missing["cellValuesByColumnId"]["fld33tJ7brN4d4ySl"] ,
                                            "image_path": path_name , "phone_number" :  missing["cellValuesByColumnId"]["fldKwNr89vZQ7MkOc"] ,
                                            "email" : missing["cellValuesByColumnId"]["fldkSPhaML4WDhjx7"]})
                        continue
                    else:
                        continue
                if photo["smallThumbUrl"] in matching_photos:
                    if not matching_photos[photo["smallThumbUrl"]] in path_names_set:
                        path_name = getImage(matching_photos[photo["smallThumbUrl"]], counter)
                        path_names_set.append(matching_photos[photo["smallThumbUrl"]])
                        counter += 1
                        missing_arr.append({
                                            "rowId" : missing["id"] ,
                                            "name": missing["cellValuesByColumnId"]["fldrT6C0v5EnP1cRV"],
                                            "additonal_info": missing["cellValuesByColumnId"]["fldgvhQGPkMBUWVLf"] ,
                                            "last_contact_made" : missing["cellValuesByColumnId"]["fldcaFKPcs7pupkp9"] ,
                                            "last_location" : missing["cellValuesByColumnId"]["fld33tJ7brN4d4ySl"] ,
                                            "image_path": path_name ,
                                            "phone_number" :  missing["cellValuesByColumnId"]["fldKwNr89vZQ7MkOc"] ,
                                            "email" : missing["cellValuesByColumnId"]["fldkSPhaML4WDhjx7"]})
                        continue
                    else:
                        continue
                if photo["largeThumbUrl"] in matching_photos:
                    if not matching_photos[photo["largeThumbUrl"]] in path_names_set:
                        path_name = getImage(matching_photos[photo["largeThumbUrl"]], counter)
                        path_names_set.append(matching_photos[photo["largeThumbUrl"]])
                        counter += 1
                        missing_arr.append({
                                            "rowId" : missing["id"] ,
                                            "name": missing["cellValuesByColumnId"]["fldrT6C0v5EnP1cRV"],
                                            "additonal_info": missing["cellValuesByColumnId"]["fldgvhQGPkMBUWVLf"] ,
                                            "last_contact_made" : missing["cellValuesByColumnId"]["fldcaFKPcs7pupkp9"] ,
                                            "last_location" : missing["cellValuesByColumnId"]["fld33tJ7brN4d4ySl"] ,
                                            "image_path": path_name ,
                                            "phone_number" :  missing["cellValuesByColumnId"]["fldKwNr89vZQ7MkOc"] ,
                                            "email" : missing["cellValuesByColumnId"]["fldkSPhaML4WDhjx7"]})
                        continue
                    else:
                        continue
                else:
                    counter += 1
                    missing_arr.append({
                                        "rowId" : missing["id"] ,
                                        "name": missing["cellValuesByColumnId"]["fldrT6C0v5EnP1cRV"],
                                        "additonal_info": missing["cellValuesByColumnId"]["fldgvhQGPkMBUWVLf"] ,
                                        "last_contact_made" : missing["cellValuesByColumnId"]["fldcaFKPcs7pupkp9"] ,
                                        "last_location" : missing["cellValuesByColumnId"]["fld33tJ7brN4d4ySl"] ,
                                        "image_path": "none" ,
                                        "phone_number" :  missing["cellValuesByColumnId"]["fldKwNr89vZQ7MkOc"] ,
                                        "email" : missing["cellValuesByColumnId"]["fldkSPhaML4WDhjx7"]})
                    continue
    except:
        continue


df = pd.DataFrame(missing_arr)
df = df.drop_duplicates()
df.to_pickle('dataframe.pkl')
print(df.to_string(index=False))