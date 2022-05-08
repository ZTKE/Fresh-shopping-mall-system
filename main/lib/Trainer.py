import os
import base64
import torch
from torchvision.models import resnet18
from torchvision.transforms import transforms
from main.lib.dataLoader import DL
from PIL import Image
import torch.nn.functional as F


class Traine:
    def __init__(self):
        self.device = torch.device('cpu')
        if torch.cuda.is_available():
            self.device = torch.device('cuda:0')
        self._init_data()
        self._init_net()

    def _init_data(self):
        dl = DL()
        self.traindl = dl.traindl
        self.testdl = dl.testdl
        self.classname = dl.classes
        self.text_name = dl.test_name

    def _init_net(self):
        self.net = resnet18(num_classes=33)
        self.net.to(self.device)
        self.opt = torch.optim.Adam(self.net.parameters(), )
        self.cri = torch.nn.CrossEntropyLoss()

    def train(self):
        epochs = 2
        patten = 'epochs: %s/%s   [===============]   loss: %.4f  acc: %.4f'
        for epoch in range(epochs):
            for batch, (inputs, targets) in enumerate(self.traindl):
                inputs = inputs.to(self.device)
                targets = targets.to(self.device)
                output = self.net(inputs)
                loss = self.cri(output, targets)
                self.opt.zero_grad()
                loss.backward()
                self.opt.step()

                acc = (targets.squeeze() == output.argmax(dim=1)).sum() / targets.shape[0]

                print(patten % (epoch, epochs, loss.item(), acc))
        self.save_model()

    def save_model(self):

        # torch.save(self.net.state_dict(), './results/model.pt')
        torch.save(self.net.state_dict(), './main/lib/results/model.pt')

    def load_model(self):
        # self.net.load_state_dict(torch.load('./results/model.pt', map_location=self.device))
        self.net.load_state_dict(torch.load('./main/lib/results/model.pt', map_location=self.device))

    def eval(self, basestr):
        self.load_model()
        transform = transforms.Compose([
            transforms.Resize((100, 100)),
            transforms.ToTensor(),
        ])
        imgdata = base64.b64decode(basestr)
        f = open('1.png', 'wb')
        f.write(imgdata)
        f.close()
        img = Image.open('1.png')
        img = img.convert("RGB")
        # os.remove('1.png')
        data = transform(img).unsqueeze(0).type(torch.float32).to(self.device)

        output = self.net(data).squeeze()
        output = F.softmax(output, dim=0).argmax(dim=0).cpu().detach().item()
        os.remove('1.png')
        return self.classname[output]




