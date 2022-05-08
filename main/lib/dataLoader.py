from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision.transforms import transforms
import os


class DL:
    def __init__(self):

        transform = transforms.Compose([
            transforms.Resize((100,100)),
            transforms.ToTensor(),
        ])

        # train_data = ImageFolder('./dataset/train/train', transform=transform)
        # test_data = ImageFolder('./dataset/test', transform=transform)
        train_data = ImageFolder('./main/lib/dataset/train/train', transform=transform)
        test_data = ImageFolder('./main/lib/dataset/test', transform=transform)
        classname = train_data.classes
        self.classes = dict(zip(list(range(len(classname))), classname))
        self.test_name = [i[0].split('/')[-1] for i in test_data.imgs]

        self.traindl = DataLoader(train_data, batch_size=1000, shuffle=True)
        self.testdl = DataLoader(test_data, batch_size=300)


