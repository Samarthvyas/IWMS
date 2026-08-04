from predict import predict_image

image_path = "ai_model/test_images/food.jpeg"

category, confidence = predict_image(image_path)

print("Prediction :", category)
print("Confidence:", confidence, "%")