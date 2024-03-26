from skinlesion import YOLO
model = YOLO("/content/gdrive/MyDrive/SkinLession/train2/weights/last.pt")
model.train(data="/content/data",
            epochs=100,
            imgsz=512,
            batch=64,
            project="/content/gdrive/MyDrive/SkinLession",
            resume=True)