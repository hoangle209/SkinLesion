start_server:
	uvicorn main:app --reload --port 5555 --host 192.168.6.85

download_weight:
	gdown --id 1sRs8OeQqCya82ymEJtsArzXhMJqyWYtn -O ./weights/