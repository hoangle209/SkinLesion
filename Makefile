start_server:
	uvicorn main:app --reload --port 5555 --host 0.0.0.0

download_weight:
	gdown --id 1sRs8OeQqCya82ymEJtsArzXhMJqyWYtn -O ./weights/

install:
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install ffmpeg libsm6 libxext6  -y
	sudo apt install python3-pip
	sudo apt install python3.10-venv
	pip install -r requirements.txt
