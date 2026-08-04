from predict import predict_image

image_path = "ai_model/test_images/bottles.jpg"

result = predict_image(image_path)

print("Prediction:", result)