import base64

from Trainer import Traine

if __name__ == "__main__":
    trainer = Traine()
    # trainer.train()
    file = "img/2.jpg"
    with open(file, "rb") as f:
        # b64encode是编码，b64decode是解码
        img = base64.b64encode(f.read())
        s = trainer.eval(img)
        print(s)
