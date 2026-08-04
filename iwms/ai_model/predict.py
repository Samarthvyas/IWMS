import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Class Names
classes = ["Dry", "Hazardous", "Wet"]

# Load Model
model = models.resnet18(weights=None)

model.fc = nn.Linear(model.fc.in_features, len(classes))

model.load_state_dict(
    torch.load(
        "ai_model/models/waste_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()

# Image Transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0).to(device)

    with torch.no_grad():

        output = model(image)

        probabilities = torch.softmax(output, dim=1)

        confidence, predicted = torch.max(probabilities, 1)

    predicted_class = classes[predicted.item()]

    confidence_score = round(confidence.item() * 100, 2)

    return predicted_class, confidence_score