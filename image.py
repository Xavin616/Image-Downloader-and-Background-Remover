import requests, json
import shutil 

def images(search):
    #search = 'leather+shoe'
    rq = requests.get(f"https://pixabay.com/api/?key=20415614-d0f2bda08ecbff4acc00b8926&q={search}&image_type=photo")
    data  = json.loads(rq.content)['hits']
    print(data)
    for i in data:
        image_url = i['largeImageURL']
        r = requests.get(image_url, stream = True)
        filename = image_url.split("/")[-1]
        r.raw.decode_content = True
         
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
                
        print('Image sucessfully Downloaded: ',filename)
        

def imagelister(search):
    rq = requests.get(f"https://pixabay.com/api/?key=20415614-d0f2bda08ecbff4acc00b8926&q={search}&image_type=photo")
    data  = json.loads(rq.content)['hits']

    imageList = []
    for i in data:
        imageList.append(i['largeImageURL'])
    return imageList

key = 'jq6pR2ndqYbcewcZumK9U56r'
def removebg(listr):
    for i in listr:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            data={
                'image_url': {i},
                'size': 'auto'
            },
            headers={'X-Api-Key': key},
        )
        if response.status_code == requests.codes.ok:
            with open('no-bg%s.png' % (i[50:55]), 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)
                
    
search = 'pair+of+shoes'
removebg(imagelister(search))