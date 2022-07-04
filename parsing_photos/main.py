import requests
url = "https://instagram.ffru2-1.fna.fbcdn.net/v/t51.2885-15/291335706_453272749508435_5107611148253264997_n.jpg?stp=dst-jpg_e15_fr_s1080x1080&_nc_ht=instagram.ffru2-1.fna.fbcdn.net&_nc_cat=111&_nc_ohc=iERKN-z1n-oAX9QpTig&edm=AJ9x6zYBAAAA&ccb=7-5&ig_cache_key=Mjg3MjY0OTkxNTAzNDMzMzA5OA%3D%3D.2-ccb7-5&oh=00_AT8rXDEEdcPBk78irPAijdpPUwMEv-jkh7fHYcTJCOSx2w&oe=62C53E66&_nc_sid=cff2a4"
res = requests.get(url)
print(res.content)
name = "photos/photo2.jpg"

with open(name, 'wb') as file :
    file.write(res.content)