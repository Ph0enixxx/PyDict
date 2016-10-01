from Data import Data

def display(Data):
	print("type the word:",end="")
	print(Data(input()))

if __name__ == '__main__':
	while True:
		display(Data)