import csv
import requests
from PIL import Image
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool
import imghdr

lock = multiprocessing.Lock()

max = 1000000
size = 64 , 64
object = input("Enter the object to download:")
count = 1
input_list = list()

def process_caption(cption):
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	no_punct = ""
	for char in cption:
		if char not in punctuations:
			no_punct = no_punct + char
	if(len(cption.split(' ')) > 20):
		return False, no_punct
	return True, no_punct

def downloader(data):
	#download images from urls
	print("In downloader")
	caption = data['caption']
	link = data['link']
	try:
		r = requests.head(url = link)
		#print(r.headers)
		if r.status_code == 301:
			r.close()
			r = requests.head(url = r.headers.get('Location'))
		if r.headers.get('Content-Type') == 'image/jpeg' and r.status_code == 200:
			r.close()
			r = requests.get(url = link)
			lock.acquire()
			captions_file = open("captions.txt", "a+")
			global count
			image_file = open("imgs/"+str(count)+".jpg", "wb+")
			# image_file = open("imgs/temp.jpg", "wb+")
			image_file.write(r.content)
			'''im = Image.open("imgs/temp.jpg")
			im_resized = im.resize(size,Image.ANTIALIAS)
			im_resized.save("imgs/"+str(count)+".jpg", ppi=(64,64))'''
			captions_file.write(caption+"\n")
			r.close()
			captions_file.close()
			print("Downloaded Image No.:"+str(count)+"-"+caption+"----------"+link)
			count = count + 1
			lock.release()
	except:
		return

def handler():
	with open("Train_GCC-training.tsv", encoding="utf8") as fd:
		rd = csv.reader(fd, delimiter="\t", quotechar='"')
		global count
		for row in rd:
			#print(row[1])
			if count <= max:
				if object in row[0]:
					d = dict()
					status, caption = process_caption(row[0])
					if not status:
						continue
					d['caption'] = row[0]
					d['link'] = row[1]
					input_list.append(d)
					count += 1
			else:
				break

handler()
count = 1
print(len(input_list))
pool = ThreadPool(50)

pool.map(downloader, input_list)
pool.close()
pool.join()


#process_job(downloader, input_list, threads = 100)

print("Done!!!!!!")

# import word2id
