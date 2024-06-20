import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as I

class ReverseNet(nn.Module):

    def _init_(self):

        super(ReverseNet, self)._init_()

        # Inverse of Fully Connected Layers
        self.fc3 = nn.Linear(in_features=2, out_features=1000)
        self.fc2 = nn.Linear(in_features=1000, out_features=1000)
        self.fc1 = nn.Linear(in_features=1000, out_features=230400)

        # Inverse of Dropout Layers
        self.drop6 = nn.Dropout(p=0.6)
        self.drop5 = nn.Dropout(p=0.5)
        self.drop4 = nn.Dropout(p=0.4)
        self.drop3 = nn.Dropout(p=0.3)
        self.drop2 = nn.Dropout(p=0.2)
        self.drop1 = nn.Dropout(p=0.1)

        # Inverse of MaxPooling Layer
        self.unpool = nn.Upsample(scale_factor=2, mode='nearest')

        # Inverse of Convolutional Layers
        self.deconv4 = nn.ConvTranspose2d(in_channels=256, out_channels=128, kernel_size=2)
        self.deconv3 = nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=3)
        self.deconv2 = nn.ConvTranspose2d(in_channels=64, out_channels=32, kernel_size=3)
        self.deconv1 = nn.ConvTranspose2d(in_channels=32, out_channels=3, kernel_size=5)

    def forward(self, x):

       # Inverse of Final Dense Layer
        x = F.relu(self.fc3(x))

        # Inverse of Second Dense Layer
        x = F.relu(self.fc2(x))
        x = self.drop6(x)

        # Inverse of First Dense Layer
        x = F.relu(self.fc1(x))
        x = self.drop5(x)

        # Reshape to the shape before flattening
        x = x.view(-1, 256, 15, 15)  # Assuming the shape before flattening

        # Inverse of Forth - Convolution + Activation + Pooling + Dropout
        x = F.relu(self.deconv4(x))
        x = self.drop4(x)

        # Inverse of Third - Convolution + Activation + Pooling + Dropout
        x = self.unpool(x)
        x = F.relu(self.deconv3(x))
        x = self.drop3(x)

        # Inverse of Second - Convolution + Activation + Pooling + Dropout
        x = self.unpool(x)
        x = F.relu(self.deconv2(x))
        x = self.drop2(x)

        # Inverse of First - Convolution + Activation + Pooling + Dropout
        x = self.unpool(x)
        x = F.relu(self.deconv1(x))
        x = self.drop1(x)

        return x