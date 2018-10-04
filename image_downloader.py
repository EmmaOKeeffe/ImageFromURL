import requests
from requests.exceptions import ConnectionError

def main():
    i = 0 # to give each photo it's own id num
	urls = open("urls.txt", "r").readlines()

	for line in urls:

		line = line.strip("\n")
        image_name = 'images/' + str(i) + '.jpg' #file path and file name
		with open(image_name, 'wb') as handle:
			try:
				response = requests.get(line, stream=True)

				if not response.ok:
					print(response)

				for block in response.iter_content(1024):
					if not block:
						break

					handle.write(block)

			except ConnectionError:
                print('Failed to open url.') #deals with connection errors such as timeout
		i+=1

if __name__ == "__main__":
	main()
