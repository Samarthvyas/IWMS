import os
import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split

# -----------------------------
# Configuration
# -----------------------------
DATASET_PATH = "ai_model/dataset"
MODEL_PATH = "ai_model/models/waste_model.pth"

IMAGE_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 5
LEARNING_RATE = 0.001

# -----------------------------
# Image Transform
# -----------------------------
transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
])

# -----------------------------
# Load Dataset
# -----------------------------
dataset = datasets.ImageFolder(DATASET_PATH, transform=transform)

print("Classes :", dataset.classes)
print("Total Images :", len(dataset))

# -----------------------------
# Split Dataset
# -----------------------------
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size

train_dataset, test_dataset = random_split(
    dataset,
    [train_size, test_size]
)

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# -----------------------------
# Load ResNet18
# -----------------------------
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

model.fc = nn.Linear(
    model.fc.in_features,
    len(dataset.classes)
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = model.to(device)

# -----------------------------
# Loss & Optimizer
# -----------------------------
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)

# -----------------------------
# Training
# -----------------------------
print("\nTraining Started...\n")

for epoch in range(EPOCHS):

    running_loss = 0

    model.train()

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        loss = criterion(outputs, labels)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    print(
        f"Epoch {epoch+1}/{EPOCHS} | Loss : {running_loss:.4f}"
    )

print("\nTraining Completed.")

# -----------------------------
# Save Model
# -----------------------------
os.makedirs("ai_model/models", exist_ok=True)

torch.save(model.state_dict(), MODEL_PATH)

print("\nModel Saved Successfully!")